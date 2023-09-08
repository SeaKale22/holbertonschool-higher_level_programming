#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    int_arguments = []
    for arg in arguments:
        int_value = int(arg)
        int_arguments.append(int_value)
    total_sum = 0
    for num in int_arguments:
        total_sum += num
    print("{}".format(total_sum))
