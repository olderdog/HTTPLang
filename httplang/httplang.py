import parse
import sys

def run(file_):
    with open(file_, 'rb') as file:
        for line in file.readlines():
            parse.parse(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: ./httplang <file.http>")
    inputFile = sys.argv[1]
    run(inputFile)
