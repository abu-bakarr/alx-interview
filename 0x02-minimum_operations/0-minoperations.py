#!/usr/bin/python3
''' count mini operations
'''


def minOperations(n):
    ''' count min operations
    '''
    iterable = 1
    sum = 0
    while n > 1:
        if n % iterable == 0 and iterable != 1:
            n //= iterable
            sum += iterable
            iterable = 1
        iterable += 1
    return (sum)
