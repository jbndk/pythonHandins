import requests
import os
from tqdm import tqdm
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor
import operator
import matplotlib.pyplot as plt
import numpy as np


def make_plot(sorted_dict):
    plt.bar(sorted_dict.keys(), sorted_dict.values())
    plt.xticks(rotation=20, horizontalalignment='right', fontweight='light', fontsize='x-small')
    plt.xlabel('Text name')
    plt.ylabel('Vowels per word')
    plt.show()


class TextComparer:

    filenames = []
    i = 0

    def __init__(self, url_list):
        self.url_list = url_list

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.filenames) > self.i:
            this_filename = self.filenames[self.i]
            self.i += 1
            return this_filename
        raise StopIteration

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def download(self, url, filename):
        with requests.get(url, stream=True) as r:
            # Raises exception if server responses with error (4XX or 5XX)
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in tqdm(r.iter_content(chunk_size=8192)):
                    f.write(chunk)

    def multi_download(self):
        for url in self.url_list:
            self.filenames.append(url[-8:])
        # multiprocessing should be used here, but it doesn't work, so I have hard-coded the number:
        workers = 8
        with ProcessPoolExecutor(workers) as ex:
            res = list(ex.map(self.download, self.url_list, self.filenames))
            return res

    def avg_vowels(self, text):
        vowels = set("AEIOUaeiou")
        total_words = 0
        total_vowels = 0

        for line in text:
            words = line.split(" ")
            for word in words:
                total_words += 1
                for char in word:
                    if char in vowels:
                        total_vowels += 1

        avg_vowels = total_vowels / total_words
        return avg_vowels

    def hardest_read(self):
        hardest_read_dict = {}
        # Iterate through filenames[]:
        for f in self.filenames:
            # Open each file:
            file = open(f, "r", encoding='utf-8')
            # Append filename (key) and avg. vowels (value) to the 'texts' dictionary:
            hardest_read_dict[f] = self.avg_vowels(file)

        # 'texts' dictionary is sorted to be used to the make_plot() method:
        sorted_list = sorted(hardest_read_dict.items(), key=lambda x: x[1])
        sorted_dict = {k: v for k, v in sorted_list}
        print(sorted_dict)
        make_plot(sorted_dict)

        # We use the max() method to find the maximum value in the 'texts' dictionary.
        # The operator.itemgetter method is used, to make sure that we compare using the value in the dictionary:
        return max(hardest_read_dict.items(), key=operator.itemgetter(1))


if __name__ == '__main__':

    url_list = [
        "https://www.gutenberg.org/files/1342/1342-0.txt",
        "https://www.gutenberg.org/files/84/84-0.txt",
        "https://www.gutenberg.org/files/11/11-0.txt",
        "https://www.gutenberg.org/files/1661/1661-0.txt",
        "https://www.gutenberg.org/files/2701/2701-0.txt",
        "https://www.gutenberg.org/files/98/98-0.txt",
        "https://www.gutenberg.org/files/219/219-0.txt",
        "https://www.gutenberg.org/files/1260/1260-0.txt",
        "https://www.gutenberg.org/files/64317/64317-0.txt",
        "https://www.gutenberg.org/files/174/174-0.txt"
    ]

    # New instance of TextComparer with url_list
    tc = TextComparer(url_list)

    # Tests urllist_generator method
    url_gen = tc.urllist_generator()
    print("Program is running urllist_generator():")
    for url in url_list:
        print(url_gen.__next__())
    print("\n\n")

    # Tests multi_download method
    print("Program is running multi_download():")
    tc.multi_download()
    print("\n\n")

    # Tests __next__ method:
    print("Program is running  __next__():")
    for f in tc.filenames:
        print(next(tc))
    print("\n\n")

    # Tests hardest_read method:
    print("Program is running  hardest_read():")
    print(tc.hardest_read())
    print("\n\n")



