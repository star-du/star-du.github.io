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
One more thing to notice is that the first letter of each word cannot match digit 0.      
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
Next, let's take a look at the `itertools` module, it provides [a variety of][itertools] fun stuff, such as `permutations()`, `combinations` and `product()` (returns iterator containing Cartesian product of two sequences)
~~~python
>>> import itertools
>>> list(itertools.permutations('ABC', 3))
[('A', 'B', 'C'), ('A', 'C', 'B'),
 ('B', 'A', 'C'), ('B', 'C', 'A'),
 ('C', 'A', 'B'), ('C', 'B', 'A')]
~~~
And there'is `groupby()` to take a sequence and a key function to return an iterator that generates pairs. (_but first you need to sort the input sequence by the grouping function_)   
Also, we have `chain()` to return an iterator that contains all the item from the given iterators, also the `zip()` one to return an iterator of the tuples of items of each two iterators.
~~~python
>>> characters = ('S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y')
>>> guess = ('1', '2', '0', '3', '4', '5', '6', '7')
>>> dict(zip(characters, guess))
{'E': '0', 'D': '3', 'M': '2', 'O': '4',
 'N': '5', 'S': '1', 'R': '6', 'Y': '7'}
~~~
We need help from a string method calls `translate()` as well, example is as follows:
~~~python
>>> translation_table = {ord('A'): ord('O')}
>>> translation_table
{65: 79}
>>> 'MARK'.translate(translation_table)
'MORK'
~~~
Simply speaking, you creat a translation_table first, which is a dictionary maps one *byte* to another, then you translate and get a new string using that table.     
Finally, what we need is `eval()`, which evaluates the value of the content of a string, interesting enough, the author stress again and again the potential danger of using `eval()`, like using code
```
>>> eval("__import__('subprocess').getoutput('rm  -rf ~)")
```
even if you add extra two arguments explicitly set the global and local namespaces, you might also face other kind of great risk, like:`>>> eval("2 ** 2147483647",{"__builtins__":None}, {})`    
So as I now understands, **there is no such thing named Absolute Safety**.

Besides that, we shall go on with our alphametics problem.
for each of the possible permutations, we use `eval()` mentioned above to test if it fits what we want:
~~~python
for guess in itertools.permutations(digits, len(characters)):
    if zero not in guess[:n]:
        equation = puzzle.translate(dict(zip(characters, guess)))
        if eval(equation):
            return equation
~~~
Just like what is examplified above, we use `dict(zip())` to create a translation_table, _if_ guess of each first letter is not '0'. To achieve this, a little trick is used, we give a forming pattern of the characters so that the first letters always locate at the start of the `characters` string.
~~~python
first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
    ''.join(unique_characters - first_letters)
~~~
and the two sequence is built with following code:
~~~python
characters = tuple(ord(c) for c in sorted_characters)
digits = tuple(ord(c) for c in '0123456789')
~~~
so the `zero` mentioned above is actually `digits[0]`   

raw code available here

-----
[^1]:       
  using generator expression is a bit more complex:
```python
  def ord_map(a_string):
    for c in a_string:
        yield ord(c)    
  gen = ord_map(unique_characters)
```


[dabeaz]:http://www.dabeaz.com/
[itertools]:https://docs.python.org/3/library/itertools.html
