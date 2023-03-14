import sys


def add(a, b):
    x = a+ " " + b
    return x

a = sys.argv[1]
b = sys.argv[2]

print(f'Final Message = {add(a, b)}')