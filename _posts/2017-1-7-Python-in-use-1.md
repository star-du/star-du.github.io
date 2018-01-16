---
layout: post
title: Python in use-math
teaser: How to build a Integral calculator?
category: coding
tags: [python, note-taking]
---
1. the use of `matplotlib.pyplot` is not hard to learn, which can be find on its [official website](https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py). One of the common practices is
```
import matplotlib as plt
x = np.linspace(start,end,50)
plt.plot(x,fun(x),ro)
plt.show
```
and this returns a graph of the function
2. any class that has a __call__ method can be called with `instance_name()` just like a function
3. after importing the built-in module `logging`, the log-level can be altered to determine which kinds of messages shall be shown and which shall not.
E.g.:`logging.getLogger().setLevel(0)`