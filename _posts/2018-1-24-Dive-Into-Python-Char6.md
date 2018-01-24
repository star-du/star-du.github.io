---
layout: post
teaser: things start to get more complicated now, when we start some tricks with closures and generators, but WE CAN HANDLE IT!
title: Dive into python 3 chapter 6
category: coding
tags: [python, note-taking]
---
**Challenge accepted:** we're encountered with the _pluralize problem_ (i.e. how to pluralize English nouns), first thing to do, we add some more practices of [Regular Expression][re], like the following:
~~~python
if re.search('[sxz]$', noun):
    return re.sub('$', 'es', noun)
elif re.search('[^aeioudgkprt]h$', noun):
    return re.sub('$', 'es', noun)
elif re.search('[^aeiou]y$', noun):
    return re.sub('y$', 'ies', noun)
else:
    return noun + 's'
~~~
[sxz] means “s, or x, or z”, but only one of them, and [^abc] means “any single character except a, b, or c”.

## closures and other stuff #
first dive in some code :

~~~Python
import re
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)


patterns = \
  (
    ('[sxz]$',            '$',  'es'),
    ('[^aeioudgkprt]h$',  '$',  'es'),
    ('(qu|[^aeiou])y$',   'y$', 'ies'),
    ('$',                 '$',  's')
  )
rules = [build_match_and_apply_functions(pattern, search, replace)
        for (pattern, search, replace) in patterns]

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
~~~
It's noticeable that `build_match_and_apply_functions(pattern, search, replace)` builds other functions (in this case `matches_rule` and `apply_rule`) using three arguments that are defined using the `for` sentence.     
The entry point here is the `plural()`, when it jumps to the first cycle(_iteration_) of `for`, it builds `rules` first, using `patterns` to provide arguments.           
Patterns here is a tuple of tuples of strings, the first string is used to perform as a match-tester, to see if the noun matches current rule, the judge is executed using the `matches_rule` function that is build. If ever it returns True, the plural function will call `apply_rule()` function and return its value as the final resual.    
**Ahh!**    
I believe it will make things a little better, if we put the rules in a seperate file rather than a list in the code, and that just needs some knowledge in concerning files:     

in a txt named `plural4-rules.txt`, we simply writes the rules like:
~~~
[sxz]$            $     es
[^aeioudgkprt]h$  $     es
[^aeiou]y$        y$    ies
$                 $     s
~~~
and we have :
~~~python
import re
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
return (matches_rule, apply_rule)

rules = []

with open('plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_and_apply_functions(
                pattern, search, replace))
~~~
_(note the trick of the split function)_    
than we have the rules, which ends up storing the
list of match and apply functions that the `plural()` function expects.
>Code is code, data is data, and life is good.

To go on enhance it, we shall use <def>generators</def>.

## generators#
Generators use `next()` to return next value. Repeatedly calling next() with the same generator object resumes exactly where it left off and continues until it hits the next yield statement.          
But it can be more productive when we use _for_ loop and listing, see the case of _FIBONACCI GENERATOR_
~~~python
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


>>> for n in fib(1000):
...     print(n, end=' ')
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> list(fib(1000))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
~~~
so we know that-- pass a generator to the list() function, and it will iterate through the entire generator   
with that in mind, the following code is a bit easier to understand
~~~python
def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)
        yield build_match_and_apply_functions(pattern, search, replace)


def plural(noun, rules_filename='plural5-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))
~~~
In each iteration of the for loop in `plural()`, we call the `rules()` which is in essence a generator, the `rules()` yield dynamically built functions (match and apply), and the functions are used in the if sentence.
Every time it calls the rules(), it just goes on with a new line in the file.

So now, we use the generator to build a function, it overall reduces some costs of time, for you don't have to load a complete list before you even start using `plural()`. But, it always build some same functions if you use the plural() for multiple times. That problems shall remain to be solve.    
IF YOU HAVE TIME: [Dig more about closures][clos]

[re]:https://star-du.github.io/posts/2018-1-23-Dive-Into-Python-Char5

[clos]:http://ynniv.com/blog/2007/08/closures-in-python.html
