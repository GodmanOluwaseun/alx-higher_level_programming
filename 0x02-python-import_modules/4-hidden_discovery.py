#!/usr/bin/python3

import hidden_4

hidden = dir(hidden_4)
hidden.sort(key=str.lower)

if __name__ == "__main__":
    for strings in hidden:
        if strings[0] != "_":
            print(strings)
