---
layout: default
title: Dive into python 3 chapter 2
---

## {{ page.title }}

1. operators that are somewhat different: `//` provides integer division, and will return an integer that is closest to it _yet lower_ (it's different when one of the numbers is float );   
`**`acts as 'raise to the power of';
```examples
>>> 11 // 2   
5    
>>> −11 // 2   
−6   
>>> 11.0 // 2   
5.0    
>>> 11 ** 2   
121
```
2. `fractions module.` can be import to calculate with fraction, To define a fraction, create a Fraction object and pass in the numerator and denominator;   
  eg:`x = fractions.Fraction(1, 3)`
  `math module`is also a helpful one to use constnts like **pi**;

3. in a list a_list[-n] == a_list[len(a_list) - n];  
4. four ways to add items in a list:  
`a_list = a_list + [2.0, 3]`:creates a second list in memory and assigned to the existing variable `a_list`; `append()` adds one new item and `extend()` method takes a list as the argument, and adds each one of the item to the original list;`insert( , )`insert an item into a indexed position.      
_note that_
```   
>>> a_list.append(['g', 'h', 'i'])    
>>> a_list    
['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i']]
>>> len(a_list)
7
```
5. useful list methods include `count()`,`in list_name` and `index()`,the last one returns the index of first occurence and will raise an exception (`ValueError`) if there is no such item;
`remove()` is available, while `pop()` removes the item and returns it. 

[back](./)
