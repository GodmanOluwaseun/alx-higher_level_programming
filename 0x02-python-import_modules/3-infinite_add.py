#!/usr/bin/python3

from sys import argv

result = 0
argc = len(argv)

if __name__ == "__main__":
    for i in range(1, argc):
        result += int(argv[i])
    print(result)
