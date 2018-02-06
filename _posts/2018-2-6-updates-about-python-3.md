---
layout: post
teaser: Unsystemetical notes about python and its practical usage
title: Updates about python 3
category: coding
tags: [python, note-taking]
---
#### Lambda expressions
The [lamda expression][lamda]
~~~python
lambda [parameter_list]: expression
~~~
yields an anonymous function, which behaves in the same way as
~~~python
def <lambda>(arguments):
    return expression
~~~
useage example:
+ uses a lambda expression to return a function

~~~python
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
~~~
  is equal to
~~~python
L = list(filter(lambda n: n % 2 == 1, range(1,20)))
~~~

+ pass a small function as an argument
~~~python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
~~~
(see manual of [list.sort()][sort])

#### decorators, the use of `@property`
<b>decorator</b>: A function returning another function, usually applied as a function transformation using the `@wrapper` syntax.

for example: adding `@classmethod` before defining a method in class will transform that method into a classmethod
~~~python
class C:
    @classmethod
    def f(cls, arg1, arg2, ...): ...
~~~
It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class.

It is equal to
~~~python
def f(self, arg1, arg2):...
f = classmethod(f)
~~~
<b>More help [here][bop] and [here][man].</b>


[lamda]:https://docs.python.org/3/reference/expressions.html#lambda
[sort]:https://docs.python.org/3/library/stdtypes.html?#list.sort
[bop]:https://bop.mol.uno/18.more.html#decorator
[man]:https://docs.python.org/3/library/functions.html?highlight=property#property
