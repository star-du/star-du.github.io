---
layout: post
teaser: Class and Iterators in python, possibly be called as sources of charm
title: Dive into python 3 chapter 7
category: coding
tags: [python, note-taking]
---
#### What is an iterator?
>An iterator is just a class that defines an ` __iter__()`
method.

It might be best to start the note with codes that built an iterator for FIBONACCI sequence:
~~~python
class Fib:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
~~~
And how we use it?
~~~python
>>> from fibonacci2 import Fib
>>> for n in Fib(1000):
... print(n, end=' ')
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
~~~
To understand this is no easy thing, first let's look at the `Fib(1000)` that the for loop calls, it returns an instance of Fib, and by using `for` loop, we actually call the `__iter__(instance)` as well.

After performing beginning-of-iteration initialization (in this case, resetting self.a and self.b, our two counters), the `__iter__()` method can return any object that implements a `__next__()` method. In this case (and in most cases), `__iter__()` simply returns self. The object that is returned by this function is an iterator, let's call it a *fib_iter*.

The `__next__(fib_iter)` method returns the value, for loop assign it to `n`, than `for` loop goes on calling `__next__(fib_iter)`, when and only when  `__next__(fib_iter)` raise an `StopIteration` exception, the loop stops, in a _graceful_ manner!

This time let's rewrite the previous [rules function][rf] again, with an iterator to pursue a greater performance.
~~~python
class LazyRules:
    rules_filename = 'plural6-rules.txt'
    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []
    def __iter__(self):
        self.cache_index = 0
        return self
    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]
        if self.pattern_file.closed:
            raise StopIteration
        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration
        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(
          pattern, search, replace)
        self.cache.append(funcs)
        return funcs
rules = LazyRules()
~~~
This time, we shall use the plural function as before, with a `for` loop:
~~~python
def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))
~~~
The better part of this iterator of your own is that, if you want to _pluralize_ multiple nouns, you only have to build all those `funcs` out of the pattern files for once at worst. By using the for loop, we only call the `__iter__` (to clear up `cache_index`) and `__next__` for different nouns, so the cache still remains there, so the functions in that cache list remain untouched.

When evoking the `__next__` function, only words that can not fit in the existing rules in cache and need more rule shall move all the way to the end (`return funcs`) and require further loops.

More efforts shall be made to understand iterators better, and I will take a record of them *asap*.

[rf]:https://star-du.github.io/posts/2018-1-24-Dive-Into-Python-Char6
