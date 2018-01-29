---
layout: post
teaser: Regular Expression, or so-called 're' module
title: Dive into python 3 chapter 5
category: coding
tags: [python, note-taking]
---
### Dive into the field of Regular Expression
>Regular expressions are a powerful and (mostly) standardized way of searching, replacing, and parsing text
with complex patterns of characters.

Regular expressions might be learnt and understood using some cases, like the following one
~~~python
>>> s = '100 NORTH MAIN ROAD'
>>> import re
>>> re.sub('ROAD$', 'RD.', s)
'100 NORTH BROAD RD.'
~~~
the dollar sign(`$`) means “end of the string.” (There is a corresponding character,the caret `^`, which means “beginning of the string.”)

~~~python
>>> s = '100 BROAD ROAD APT. 3'
>>> re.sub(r'\bROAD\b', 'RD.', s)
'100 BROAD RD. APT 3'
~~~
`\b` stands for word boundary, and we use `r''` to avoid backslash plague

another example is use it to match _Roman Numerals_, one way is to use the {n,m} syntax:
~~~python
 >>> pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
~~~
but it should be more readable if you use **Verbose Regular Expression**, note the extra argument `re.VERBOSE`
~~~python
>>> pattern = '''
^                 # beginning of string
M{0,3}            # thousands - 0 to 3 Ms
(CM|CD|D?C{0,3})  # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3Cs),
                  # or 500-800 (D, followed by 0 to 3 Cs)
(omitting tens and ones)
$                 # end of string

'''
>>> re.search(pattern, 'M', re.VERBOSE)
<_sre.SRE_Match object at 0x008EEB48>
~~~
matching phone numbers is another challenge, when you have to deal with a variety of styles, with or without '-' (sometimes other connectors) and extensions.
after long struggles, one possible solution might be:
~~~python
>>> phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
>>> phonePattern.search('80055512121234').groups()
('800', '555', '1212', '1234')
>>> phonePattern.search('800.555.1212 x1234').groups()
('800', '555', '1212', '1234')
>>> phonePattern.search('800-555-1212').groups()
('800', '555', '1212', '')
>>> phonePattern.search('(800)5551212 ext. 1234').groups()
('800', '555', '1212', '1234')
~~~
`\d{3}` means matching exactly 3 numeric digits, and putting it all in `()` will remember them as a group for later use [^1]. similarly `\D` stands for any character except a numeric digit, `*` is '0 or more'(BTW `+` is '1 or more'), so this should mathch the majority of the numbers.       
**But** to prevent an extra '(1)' and its interference, we finally resort to remove the beginning `^`...

As I discovered, it was a great mess, so finally we shall put it using VERBOSE Regular Expression, the `re.VERBOSE` can be put as an argument of `compile()`

--------
### Resources #
for more help, see [here][re] and [here][manual]

--------

### Postscript
+ ^ matches the beginning of a string.
+ $ matches the end of a string.
+ \b matches a word boundary.
+ \d matches any numeric digit.
+ \D matches any non-numeric character.
+ x? matches an optional x character (in other words, it matches an x zero or one times).
+ x* matches x zero or more times.
+ x+ matches x one or more times.
+ x{n,m} matches an x character at least n times, but not more than m times.
+ `'(a|b|c)'` matches exactly one of a, b or c.
+ (x) in general is a remembered group. You can get the value of what matched by using the groups() method
of the object returned by re.search.
----

[^1]:     
    after grouping, you can refer to the grouped items using `\1` etc.    
  ———  *which means “hey, that first group you remembered? put it right here.”*


[re]:https://docs.python.org/3/howto/regex.html
[manual]:https://docs.python.org/3/library/re.html
