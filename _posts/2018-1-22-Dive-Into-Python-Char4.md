---
layout: post
teaser:
title: Dive into python 3 chapter 4
category: coding
tags: [python, note-taking]
---
+ first some knowledge (kinda boring stuff) about <def>Unicode</def>. UTF-8 is a _variable-length_ encoding system for Unicode. That is, different characters take up a different number of bytes.
It's an efficient way of encoding comparing to UTF-32 or UTF-16, and it doesn't cause byte-ordering issues when the byte stream is transferred.

formatting can be a powerful tool for you can pass on list and acces its item, pass on dictionaries and access the values with the keys, or even pass on modules and access its variables and functions
~~~python
>>> import humansize
>>> import sys
>>> '1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys)
'1MB = 1000KB'
~~~
