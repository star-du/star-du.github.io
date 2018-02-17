---
layout: post
teaser: Unsystemetical notes about python and its practical usage -- which now has part 2!
title: Updates about python 3 part2
category: coding
tags: [python, note-taking]
---
#### errors and exceptions
Let's start with a standard error message:
~~~python
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
~~~
The last line of this little piece of info states the type of the error, and the rest of the line provides the details. `TypeError` here is a built-in exception class.

The preceding part of the error message shows the context where the exception happened, in the form of a _stack traceback_. In general it contains a stack traceback listing source lines; however, it will not display lines read from standard input.

The piece above shows a 'normal' error message we might often face. When we handle these errors by our own, we should notice that
>A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class).

that means, if you raises an error of the derived class, an 'except clause' with a base class error will be triggered. And.. the first matching one is invoked. See [examples here.][handling_exc]

Use `except` only to perform a wildcard-like task, but it should be used with extreme caution, at times it is used to print error message and re-raise the exception (to allow a caller to handle the exception as well).

If an exception has arguments, they are printed as the last part (‘detail’) of the message for unhandled exceptions.

The `try` ... `except` has an optional `else` cause so that it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

Usually, the `finally` statement serves as a clean-up action, but we also have those pre-defined one using `with` statement.

[handling_exc]:https://docs.python.org/3/tutorial/errors.html#handling-exceptions
