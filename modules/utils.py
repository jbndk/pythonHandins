import argparse
import os


def get_file_names(folderpath,out):
    file_names = os.listdir(folderpath)
    with open(out, 'w') as file_object:
        for f in file_names:
            file_object.write(f + '\n')
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""


# Out param removed, so it just prints to console:
def get_all_file_names(folderpath):
    for roots, dirs, file in os.walk(folderpath):
        for f in file:
            print("File: " + f)
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""


#get_all_file_names("C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks")


def print_line_one(file_names):
    for f in file_names:
        with open(f, 'r') as file_object:
            print(file_object.readline())
    """takes a list of filenames and print the first line of each"""


#print_line_one(["C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\txt\\File1.txt", "C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\txt\\fasf.txt"])


def print_emails(file_names):
    for f in file_names:
        with open(f, 'r') as file_object:
            lines = file_object.readlines()
            for line in lines:
                if "@" in line:
                    print(line)
    """takes a list of filenames and print each line that contains an email (just look for @)"""


#print_emails(["C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\txt\\File1.txt", "C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\txt\\fasf.txt"])


def write_headlines(md_files):
    for f in md_files:
        with open(f, 'r') as file_object:
            lines = file_object.readlines()
            for line in lines:
                if line.startswith('#'):
                    print(line)
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""

#write_headlines(["C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\txt\\mdfile1.md", "C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\txt\\mdfile2.md"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that can print various file names and content to console')
    parser.add_argument('program', help='Path of the folder that the program reads from')
    parser.add_argument('-f', '--folderpath', help='Path of the folder that the program reads from')

    args = parser.parse_args()

    if 'get_file_names' in args.program:
        get_file_names(args.folderpath)
    if 'get_all_file_names' in args.program:
        get_all_file_names(args.folderpath)