from ./Week_6.py import *

if __name__ == '__main__':
    def url_list_generator():
        urls = []
        i = 10
        while i < 21:
            url = "https://www.gutenberg.org/files/{}/{}-0.txt".format(i, i)
            print(url)
            urls.append(url)
            i += 1
        return urls


    urllist = url_list_generator()
    files = TextComparer(urllist)
    # files = TextComparer(["https://www.gutenberg.org/files/60/60-0.txt"])

    #files.download('https://www.gutenberg.org/files/60/60-0.txt', 'book65.txt')

    files.multi_download()