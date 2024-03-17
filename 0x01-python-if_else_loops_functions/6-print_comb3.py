#!/usr/bin/python3

for i in range(0, 10):
    for x in range(0, 10):
        if i != x:
            if int(str(i) + str(x)) > int(str(x) + str(i)):
                continue;
            elif (str(i) + str(x)) != "89":
                print("{:}, ".format(str(i) + str(x)), end='')
print("89")
