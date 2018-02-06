---
layout: post
teaser: The book comes nearer to its end, and I hope to dig more things useful by this little charpter.
title: Dive into python 3 stuffs and appendix
category: coding
tags: [python, note-taking]
---
We've gone through much of the book _Dive into python3_ by **Mark Pilgrim**. The remaining parts combine some more lessons, a guide for transporting codes from python 2 to python 3, and some useful stuff about packaging library, plus some helpful appendixes.

It's currently hard for me to get all of them in use, which means that this note will hopefully be updated once further progress is reached. Up until then, I will take a note as much as I can.

when calling repr(), str(), bytes() of an instance, Python is actually calling `__repr__()`, `__str__()`, `__bytes__()` of the class.

When you refer to some attributes of an instance, by writing x.property, there is actually two functions possibly been called. _Unconditionally_, if your class defines a `__getattribute__()` method, Python will call it on every reference to any attribute or
method name (except special method names). Then, if no results is found, it will call `x.__getattr__('my_property')`, this is called a _fallback_.
~~~python
class Dynamo:
    def __getattr__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError
~~~
as a example, when we define such a class, and instantialize it with `dyn = Dynamo()`, we then ask for the value of `dyn.color`, The dyn instance does not have an attribute named color, so the `__getattr__()` method is called to provide a computed value. But if we explicitly set the `color` attribute with a value, the next time we ask for it, it will find out the existing attribute, without calling `__getattr__()`.
~~~python
if __name__ == '__main__':
    dyn = Dynamo()
    print(dyn.color)
    dyn.color = 'LemonChiffon'
    print(dyn.color)
~~~
and the result is
~~~python
PapayaWhip
LemonChiffon
~~~

Likewise, there are so many _special methods_ existing, when you treat classes as functions, you define their `__call__` method; if they are treated like sets, dictionaries and numbers, methods like `__contains__(x)` and `x.__add__(y)` are called.

<b>Thanks again for [the brilliant book][dip] presented by Mark Pilgrim!</b>

[dip]:http://www.diveintopython3.net/
