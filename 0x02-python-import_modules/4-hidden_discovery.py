#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as h
    for name in dir(h):
        if name[:2] != "__":
            print("{}".format(name))
