#!/usr/bin/python3

from sys import argv

argc = len(argv)

if __name__ == "__main__":
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif argc > 2:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))
