import argparse


def print_file_content(file_path):
    file = open(file_path)
    for line in file:
        print(line)


def write_list_to_file(output_file, *args):
    with open(output_file, 'w') as file_object:
        for arg in args:
            file_object.write(arg + '\n')
    with open(output_file, 'r') as file_object:
        for f in file_object:
            print(f)


def read_csv(input_file):
    output = []
    with open(input_file, 'r') as file_object:
        for item in file_object:
            output.append(item)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that can write to a CSV file or print to console')
    parser.add_argument('path', help='The path to the CSV file')
    # I was not sure what you meant with 'file_name' in the exercise, so I decided to replace this with 'content' as it made more sense for me:
    parser.add_argument('-c', '--content', help='Write content to file', action='store_true')

    args = parser.parse_args()

    if args.content:
        write_list_to_file(args.path, args.content)

    print_file_content(args.path)

