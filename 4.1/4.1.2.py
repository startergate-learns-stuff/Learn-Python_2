import random
for i in iter(lambda : random.randint(0, 5), 2):
    print(i, end=' ')
print()

def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step;


for i in count(2, 2):
    if i < 10:
        break
    print(i)

from itertools import *


def takewhile(predicate, iterable):
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break


def condition(n):
    return n < 10


a = [ x for x in takewhile(condition, [1, 4, 6, 7, 10 ,2, 3]) ]


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


from functools import reduce


def sum(x, y):
    return x + y

print(reduce(sum, [1, 2, 3, 4, 5]))

print(reduce(lambda x, y : x + y, [1, 2, 3, 4, 5], 10))
print(reduce(lambda x, y : x * y, range(1, 6)))
print(reduce(lambda x, y : x * y, range(1, 7)))