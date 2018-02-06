---
layout: post
title: Python in use-math (updated Feb 6, 2018)
teaser: How to build a Integral calculator?
category: coding
tags: [python, note-taking]
---
1. the use of `matplotlib.pyplot` is not hard to learn, which can be find on its [official website](https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py). One of the common practices is
```python
import matplotlib as plt
x = np.linspace(start,end,50)
plt.plot(x,fun(x),ro)
plt.show
```
and this returns a graph of the function

2. any class that has a __call__ method can be called with `instance_name()` just like a function

3. after importing the built-in module `logging`, the log-level can be altered to determine which kinds of messages shall be shown and which shall not.
E.g.:`logging.getLogger().setLevel(0)`
Another way is just print it out in a _log-style_, like
~~~python
print("[LOG] under current iteration: {}".format(summation))
~~~

4. do not start calculating until it's called, so-called _lazy mode_

Source file avaliable at my github [repo][myrepo] and _'dalao' smdsbz_'s [repo][smdsbz]

[myrepo]:https://github.com/star-du/sicun-assignments/blob/master/Integral.py
[smdsbz]:https://github.com/star-du/Lecture/blob/master/Test01/mysolution_integral.py
