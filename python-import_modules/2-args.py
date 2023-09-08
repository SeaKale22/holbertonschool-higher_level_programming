#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
    arguments = sys.argv[1:]
    if num_args == 0:
        print("{} arguments.".format(num_args))
    else:
        if num_args == 1:
            print("{} argument:".format(num_args))
        else:
            print("{} arguments:".format(num_args))
        for i, arg in enumerate(arguments, 1):
            print(f"{i}: {arg}")
