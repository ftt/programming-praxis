#!/usr/bin/env python


import operator
import sys
from numbers import Number


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div
}

class ParseException(Exception):
    pass

def to_number(string):
    '''Accepts a string or and returns a number represented by that string.
    If a number is passed, that number is returned intact.'''
    if isinstance(string, Number):
        return string
    try:
        return int(string)
    except ValueError:
        return float(string)


def calculate(stack):
    '''Takes a list representing an expression stack and solves the first expression found.
    Changes the list in place.'''
    op = None
    for op_index in xrange(len(stack)):
        if stack[op_index] in _OPERATORS.keys():
            op = stack[op_index]
            break
    if op is None or op_index < 2:
        return
    left_operand, right_operand = stack[op_index - 2:op_index]
    try:
        left_operand = _to_number(left_operand)
        right_operand = _to_number(right_operand)
    except ValueError:
        raise ParseException('Unknown numbers')
    stack[op_index - 2] = _OPERATORS[op](left_operand, right_operand)
    stack[op_index - 1:] = stack[op_index + 1:]


def main():
    stack = []
    print 'RPN calculator. Enter an empty line to quit.'
    while True:
        user_input = sys.stdin.readline().split()
        if not user_input:
            return
        stack.extend(user_input)
        old_len = len(stack)
        while True:
            try:
                _calculate(stack)
            except ParseException as e:
                print '{0}\nStack is cleared.'.format(e.message)
                stack = []
                break
            if len(stack) == old_len:
                break
            old_len = len(stack)
        print '> {0}'.format(' '.join(str(n) for n in stack))


if __name__ == '__main__':
    main()
