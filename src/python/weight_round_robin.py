# -*- coding: utf-8 -*-

import random
from bisect import bisect

"""
bisect is a python sort module.

>>> import bisect
>>> dir(bisect)
['__builtins__',
 '__doc__',
  '__file__',
  '__name__',
  '__package__',
  'bisect',
  'bisect_left',
 'bisect_right',
 'insort',
 'insort_left',
 'insort_right']
"""


def weightedChoice(choices):
    """Like random.choice, but each element can have a different chance of
    being selected.

    choices can be any iterable containing iterables with two items each.
    Technically, they can have more than two items, the rest will just be
    ignored.  The first item is the thing being chosen, the second item is
    its weight.  The weights can be any numeric values, what matters is the
    relative differences between them.
    """
    space = {}
    current = 0
    for choice, weight in choices:
        if weight > 0:
            space[current] = choice
            current += weight
    rand = random.uniform(0, current)
    for key in sorted(space.keys() + [current]):
        if rand < key:
            return choice
        choice = space[key]
    return None


def _weight_round_robin(choices):
    """pick server depending on weight

    :return: `(key, weight)`
    """
    total = sum(int(w) for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for key, weight in choices:
        weight = int(weight)
        upto += weight
        if upto >= r:
            return (key, weight)
    return random.choice(choices)


def _weight_round_robin2(choices):
    weight_list = []
    for key, weight in choices:
        [weight_list.append(key) for _ in xrange(weight)]
    return weight_list


def test(s):
    print s


def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.random() * total
    index = bisect(cum_weights, x)
    return values[index], weights[index]


l = [('test1', 1), ('test2', 50), ('test3', 1), ('test4', 100)]
print weighted_choice(l)
print '======================'
print _weight_round_robin(l)
