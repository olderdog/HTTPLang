import parse
import sys

def run(file_):
    with open(file_, 'rb') as file:
        for line in file.readlines():
            parse.parse(line)

if __name__ == "__main__":
    inputFile = sys.argv[1]
    run(inputFile)
