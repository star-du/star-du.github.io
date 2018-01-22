---
layout: post
teaser: a peek into strings, and how they differ from and connect with bytes
title: Dive into python 3 chapter 4
category: coding
tags: [python, note-taking]
---
 first some knowledge (kinda boring stuff) about <def>Unicode</def>. UTF-8 is a _variable-length_ encoding system for Unicode. That is, different characters take up a different number of bytes.
It's an efficient way of encoding comparing to UTF-32 or UTF-16, and it doesn't cause byte-ordering issues when the byte stream is transferred.
>note that all strings are sequences of Unicode characters, and UTF-8 is a way of encoding characters as a sequences of bytes.

*Formatting* can be a powerful tool for you can pass on list and access its item, pass on dictionaries and access the values with the keys, or even pass on modules and access its variables and functions
~~~python
>>> import humansize
>>> import sys
>>> '1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys)
'1MB = 1000KB'
~~~
also just like **c**, we can use `{index:.3f}` to specify decimal precision and adjust space padding. Advanced useage like ` '{:>30}'.format('right aligned')` can be consulted [here][fm].

---
speaking of useful methods, we have `count()`, `str.split(sep=None, maxsplit=-1)`(which returns a list), look up the [Official Doc][strm] is always welcomed.

bytes are somehow similar to strings, with a look of `b''`, and its items are integer 0-256. It's immutable (unable to change), but you workaround ways are using _bytearray_ object, you may convert string to bytes using `encode()`, and vice versa with(`decode()`).

[fm]: https://docs.python.org/3.1/library/string.html#format-specification-mini-language
[strm]:https://docs.python.org/3/library/stdtypes.html#string-methods
