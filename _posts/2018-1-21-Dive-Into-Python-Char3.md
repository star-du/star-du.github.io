---
layout: post
teaser: A bit more understanding of list, dictionaries...
title: Dive into python 3 chapter 3
category: coding
tags: [python, note-taking]
---

1. `os` module has `os.getcwd()` and `os.chdir()`[^1] functions, note that When calling the `os.chdir()` function, use a Linux-style pathname (forward slashes, no drive letter) even on Windows.     
eg:   
os.chdir('/Users/pilgrim/diveintopython3/examples')
2. `os.path.join()` will take any number of arguments and `os.path.expanduser()` function will expand a pathname that uses ~ to represent the current user’s home directory.
3. `os.path.split()` return a tuple of two variables (the directory name and the filename), and `splitext()` will return name and extension.
4. the <dfn>glob</dfn> function can be used to get the contents of a directory using wildcards. consult glob reference [here][gr1] or [here][gr2].
5. get metadata of a file using `os.stat()`[^2]:
```
>>> metadata = os.stat('feed.xml')
>>> metadata.st_size
3070
```
6. list and dictionary comprehnsions are easy ways to construct new lists and dictionaries based on given ones.

### A comprehensive usage example
~~~python
>>> import os, glob
>>> glob.glob('*.xml')
['feed-broken.xml', 'feed-ns0.xml', 'feed.xml']
>>> [os.path.realpath(f) for f in glob.glob('*.xml') if os.stat(f).st_size > 1000]
['c:\\Users\\pilgrim\\diveintopython3\\examples\\feed-broken.xml',
'c:\\Users\\pilgrim\\diveintopython3\\examples\\feed-ns0.xml',
'c:\\Users\\pilgrim\\diveintopython3\\examples\\feed.xml']
~~~

[^1]:   
    The function `os.chdir()` changes the current working directory.

[^2]:     
    os.stat() return a `stat_result` object (an instance of the class), and st_size stuffs are the attributes of the class.

[gr1]: https://docs.python.org/3/library/glob.html?highlight=glob#glob.glob
[gr2]:https://pymotw.com/3/glob/
