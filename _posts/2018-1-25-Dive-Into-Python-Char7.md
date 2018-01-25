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
