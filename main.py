# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import sys
# sys.path.append("module python file location")

import importModules.math_function as f
import argparse

print(f.sum(10, 13))
print(f.multiply(10, 13))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    parser = argparse.ArgumentParser(description='Process some integers.')

    # postional arguments
    # parser.add_argument("number1", help="first number")
    # parser.add_argument("number2", help="second number")
    # parser.add_argument("operation", help="operation")

    # optional arguments
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="operation", \
                        choices=["add", "subtract", "multiply"])

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
