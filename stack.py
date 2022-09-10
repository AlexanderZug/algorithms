# id 70249471

import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self, array=None):
        self._stack = [] if array is None else array

    def pop(self):
        return self._stack.pop()

    def push(self, value):
        self._stack.append(value)
        return self._stack


def is_number(value):
    return value.lstrip('+-').isnumeric()


def main():
    try:
        sequence = input().split()
    except EOFError:
        sequence = []

    stack = Stack()
    for item in sequence:
        if is_number(item):
            stack.push(int(item))
            continue
        second = stack.pop()
        first = stack.pop()
        if item in OPERATORS:
            stack.push(OPERATORS[item](first, second))
    print(0 if len(stack._stack) == 0 else stack.pop())


if __name__ == '__main__':
    main()
