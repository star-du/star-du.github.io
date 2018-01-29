---
layout: post
teaser: dig more about advanced iterators
title: Dive into python 3 chapter 8
category: coding
tags: [python, note-taking]
---
## Advanced iterators #
The problem we're trying to solve is called <def>alphametics</def>, to put it simple, it requires you to find the matching digits for letters in an equations, so that the matching numbers 'spell' an arithmetic equation. For example, the following problem:
~~~
HAWAII + IDAHO + IOWA + OHIO == STATES
~~~
has its answer:
```
510199 + 98153 + 9301 + 3593 == 621246
```
To find a simple solution to this problem, we shall take it step-by-step, with some extra stuff about python.
### solution: step-by-step #
~~~python
words = re.findall('[A-Z]+', puzzle.upper())
unique_characters = set(''.join(words))
assert len(unique_characters) <= 10, 'Too many letters'
~~~
first use the `re` module to find all of the letters appeared in the equation, using `join()` in string method, and put them in a set to get a list of unique_characters (i.e. different letters).
Assert here equals to
~~~python
if len(unique_characters) > 10:
    raise AssertionError('Too many letters')
~~~
before we go on the next parts, we shall review generators and hopefully have some deeper understanding.
As David Beazley [puts][dabeaz] it
>A generator function is mainly a more convenient way of writing an iterator. You don't have to worry about the iterator protocol (.next, .`__iter__`, etc.).   
>It just works.

Generators have two types generator expressions and functions. Just taking about expressions this time:   
• General syntax
~~~python
(expression for i in s if condition)
~~~
• What it means
~~~python
for i in s:
    if condition:
        yield expression
~~~
then we get an object that generates values (which are typically consumed in a for loop).   
And we can pass the generator expression to `tuple()`, `list()` or `set` (no need for extra parenthese!)
~~~python
>>>unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
>>> tuple(ord(c) for c in unique_characters)
(69, 68, 77, 79, 78, 83, 82, 89)
~~~
Besides its simplicity [^1], what's good about using a generator?     
Using a generator expression instead of a list comprehension can save both C P U and R A M .

[^1]:     
using generator expression is a bit more complex
~~~python
def ord_map(a_string):
  for c in a_string:
      yield ord(c)    
gen = ord_map(unique_characters)
~~~


[dabeaz]:http://www.dabeaz.com/
