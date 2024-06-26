# -*- coding: utf-8 -*-
"""HIgh functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i_rDjs0Y2GhlljcCbUz6KtSrspm7SwdT

High Functions

lambda
"""

add = lambda x:x+10
print(add(67))

"""Map"""

# map(func,iterable)
lst = [12,23,45]
add = list(map(lambda x:x+190 ,lst))
print(add)

lst = [12,12,233]
sqr = list(map(lambda x:x**4,lst))
print(sqr)

"""Filter

"""

# filter(condition, iterable)
even = list(filter(lambda x:x%2==0, range(1,21)))
print(even)

odd = list(filter(lambda x:x%2==1, range(1,21)))
print(odd)

""" reduce"""

from functools import reduce
a = reduce(lambda a,b:a+b,range(1,23))
print(a)