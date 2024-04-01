#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argn = len(sys.argv) - 1

    if argn == 0:
        print("{} arguments.".format(argn))
    elif argn == 1:
        print("{} argument:".format(argn))
    else:
        print("{} arguments:".format(argn))

    for i in range(argn):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
