---
layout: post
teaser: files, files, files!
title: Dive into python 3 chapter 11
category: coding
tags: [python, note-taking]
---
<span style = "font-family:Candara; font-size:40px; color:grey"> Files </span>, files have been something we are dealing with every so ofen, as an example, we might have come across such code:
~~~python
file = open('examples/rules.txt', encoding='utf-8')
~~~
two things to notice for this concise code:
1. use forward slash to denote subdirectories even on Windows
2. encoding is used to indicate the proper decoding system, because the default one is platform-dependent

So, what does the `open()` function return? It is a _stream_ object, which has methods and attributes for getting information about and manipulating a stream of characters, like `.name`, `.encoding`, `.mode`, by default, the mode is read.
~~~python
>>> a_file = open('examples/chinese.txt', encoding='utf-8')
>>> a_file.read()
'Dive Into Python 是为有经验的程序员编写的一本 Python 书。\n'
>>> a_file.seek(17)
17
>>> a_file.read(1)
'是'
>>> a_file.tell()
20
~~~
`seek` method moves to a specific *byte* position, `read` takes the number of *characters* to read, so when you `tell` the byte position now, it has moved another 3 position rather than one. And since Chinese characters requires multiple bytes to encode, you should be aware that you cannot read from the middle of a set of  constituting bytes of one character.

finally close it by using `.close()`, the stream object then still exists with only a `closed` attribute. But the more preferred manner should be using **with** statement:
~~~python
with open('examples/chinese.txt', encoding='utf-8') as a_file:
~~~
It's more secure to use with code block, it guarantees that your file will be closed however your program halts. That's because the with statement creates a so-called _runtime context_, and the stream object calls its own `close()` method once Python exits that context.

The stream object is an iterator itself, you can use a for loop to read one line at a time:
~~~python
line_number = 0
with open('name.txt', encoding='utf-8') as a_file:
    for a_line in a_file:
        line_number += 1
        print('{:>4} {}'.format(line_number, a_line.rstrip()))
~~~
just in case it's unfamiliar: `{:>4}` means “print this argument right-justified within 4 spaces.

\*of course, you can use the method `readline()` as well as `readlines()`

reading and appending is achieved through the mode parameter 'w' and 'a'.
### Read things beyond text files #
What if we want to read something like a picture? The same old tricks shall work, except that the mode parameter should now be `rb`, `wb`, or `ab`;

But we can even read things beyond files. By using `StringIo` class in `io` module, we create an instance of theclass and pass it the string you want to use as your “file” data.
~~~Python
>>> a_string = 'PapayaWhip is the new black.'
>>> import io
>>> a_file = io.StringIO(a_string)
~~~
The stream object you now have get all those methods and attributes as well.
### Standard Input, output and error #
>Standard output and standard error (commonly
abbreviated stdout and stderr) are pipes that are built
into every U N I X -like system, including Mac OS X and
Linux. When you call the print() function, the thing
you’re printing is sent to the stdout pipe. When your
program crashes and prints out a traceback, it goes to
the stderr pipe.

If that is understood, which is to say the nature of `print()` is adding a carriage return and calling `sys.stdout.write`[^1], we can direct a different output place, with a custom _context manager_.

A class is a context-manager as long as it has `__enter__()` and `__exit__()` methods.
~~~Python
class RedirectStdoutTo:
    def __init__(self,out_new):
        self.out_new = out_new

    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.out_old
~~~
Then we can use with statement to automatically call `__enter__()` and `__exit__()`. A bit tricky though, is that we can use with statement to take _a comma-separated list of contexts_.
~~~Python
with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
print('B')
~~~
The first context listed is the “outer” block; the last one listed is the “inner” block. Rewrite it would be like
~~~Python
with open('out.log', mode='w', encoding='utf-8') as a_file:
    with RedirectStdoutTo(a_file):
        print('B')
~~~

[^1]:
`sys.stdout` and `sys.stderr` are stream objects, but they are write-only. Attempting to call their `read()` method will always raise an IOError.
