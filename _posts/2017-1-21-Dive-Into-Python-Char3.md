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
4. the `glob` function can be used to get the contents of a directory using wildcards, eg:
```
>>> import glob
>>> glob.glob('examples/*.xml')
['examples\\feed-broken.xml',
'examples\\feed-ns0.xml',
'examples\\feed.xml']
```
5. get metadata of a file:
```
>>> metadata = os.stat('feed.xml')
>>> metadata.st_size 
3070
```
[^1]:
    The function `os.chdir()` changes the current working directory.
