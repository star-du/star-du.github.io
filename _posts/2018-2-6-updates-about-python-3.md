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


#### higher-order function
In python, function can be be taken as arguments for other functions, and can also return as a result of other functions. That's something I've met before, but the structure _closure_ is something unfamiliar to me.

A closure is a way of keeping alive a variable even when the function has returned.  In Python, this is done by nesting a function inside other function and then returning the underlying function.
~~~python
def lazy_sum(*args):
    def sum():
        a = 0
        for n in args:
            a += n
        return a
    return sum
~~~
The good part about using closure here is that you need not to evaluate the sum immediately after providing your argument, see below
~~~python
>>>f = lazy_sum(1, 3, 5, 7)
>>>f
<function closure_test.lazy_sum.<locals>.sum>
>>>f()
16
~~~
the `f` references the variables of lazy_sum() even after it returns.
another useage:
~~~python
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
~~~
According to [learnpython.org][learn]
>ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.(Eg. When there are few methods in a class, use closures instead)

It's very important to note that in python, the variables in the enclosing scopes are only readonly by nested functions. However, one can use the `nonlocal` keyword explicitly with these variables in order to modify them. Refer to examples of [liaoxuefeng's][lxf] exercises if you please.

The nested functions also leads to the use of _decorators_.

#### decorators
<b>decorator</b>: A function returning another function, usually applied as a function transformation using the `@wrapper` syntax.

generally, a decorator use syntax like
~~~python
@decorator
def functions(arg):
  ...
~~~
and it is equivalent to:
~~~python
def function(arg):
  ...
function=decorator(function)
~~~
<i>Usage example 1:</i>

adding `@classmethod` before defining a method in class will transform that method into a classmethod
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

<i>Usage example 2:</i>

 a decorator is just another function which takes a functions and returns one, and you can use it to modify an old function and return a new one:
 ~~~python
 def Check(old_function):
     def new_function(arg):
         if arg<0: raise ValueError("Negative Argument")
         old_function(arg)
     return new_function

 @Check
 def r(n):
     print(n**3)     
 ~~~
 and it will raise `ValueError` then if you give r() a negative argument.

 <i>Usage example 3:</i>
 ~~~python
 def type_check(correct_type):
     def check(old_func):
         def new_func(arg):
             if not isinstance(arg, correct_type):
                 raise TypeError("Bad Type")
             return old_func(arg)
         return new_func
     return check


 @type_check(int)
 def times2(num):
     return num*2

 @type_check(str)
 def first_letter(word):
     return word[0]
~~~
then when you test it, you can get expected results
~~~python     
 print(times2(2)) # returns 4
 times2('Not A Number') # raises TypeError
 print(first_letter('Hello World')) # returns 'H'
 first_letter(['Not', 'A', 'String']) # raises TypeError
 ~~~

<b>More help available [here][bop] and [here][man], also the [learnpython.org][l2] is quite helpful.</b>

#### the use of `@property`
It's also part of the decorator techniques, but relatively more complex.
~~~python     
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
 ~~~
According to [Mr.Liao][lxf2], when using `@property`, we transfer a method to an attribute, and when we wrapped it up with this decorator, this descript object has extra methods: `getter`, `setter`, `deleter`. Amazingly, these decorator act as decorators too. They return a new property object:
~~~python
>>> property().getter(None)
<property object at 0x10ff079f0>
~~~
When we use `@score.setter`, what we are doing is call that `property().setter` method, so we are replacing the original setter function with the new one, and keep everything else.
For in-depth explanation, see answers in [stackoverflow][stack].

If we don't designate that `setter()` method, we'll make the attribute readonly, which is, in some cases, what we desired.
~~~python
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value    

    @property
    def resolution(self):
        return self._width * self._height
~~~
#### more about list
we can use lists as _stacks_ as well as _queue_, which makes it possible both “last-in, first-out” and “first-in, first-out”, although the latter is less efficient.
~~~python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
~~~
To implement a queue, use `collections.deque` which was designed to have fast appends and pops from both ends.
~~~python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
~~~
list comprehension is definitely flexible:
~~~python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
~~~
The sequence of `for` in the second example should not be reversed, for the elem needs to be defined first by `for elem in vec`.

In case I might forget, to **unpack** argument list, we use the `*` operator, likewise, use `**`-operator for dictionaries. See [here][unpack]

_Looping_ through a sequence is easy wiht `for` statements,  and if we want the position index as well, we can use the `enumerate()` function
~~~python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
~~~
to loop over two or more sequences, use `zip` to pair, `zip` yields an iterator
~~~python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
~~~
For more about `zip`, see <b>[here][zip]</b>

for the difference between list and tuple, the [docs][tuple_seq] give us some hints:
>Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

[lamda]:https://docs.python.org/3/reference/expressions.html#lambda
[sort]:https://docs.python.org/3/library/stdtypes.html?#list.sort
[bop]:https://bop.mol.uno/18.more.html#decorator
[man]:https://docs.python.org/3/library/functions.html?highlight=property#property
[learn]:https://www.learnpython.org/en/Closures
[lxf]:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000
[l2]:https://www.learnpython.org/en/Decorators
[lxf2]:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000
[stack]:https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work
[tuple_seq]:https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
[unpack]:https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
[zip]:https://docs.python.org/3/library/functions.html#zip
