#!/usr/bin/python3

for i in range(0,100):
    print("{:02}, ".format(i), end="")
    if i in (22, 45, 68, 91, 99):
        print()
