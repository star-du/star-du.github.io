---
layout: default
teaser: What can you do with Python's native data types?
title: Dive into python 3 chapter 2
category: coding
tags: [python, note-taking]
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
>>>a_list+['g','h']
>>>a_list
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']   
>>> a_list.append(['g', 'h', 'i'])    
>>> a_list    
['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i']]
>>> len(a_list)
7
```
5. useful list methods include `count()`,`in list_name` and `index()`,the last one returns the index of first occurence and will raise an exception (`ValueError`) if there is no such item;`del` (takes the _index_) and `remove()` (takes the _index_) is available, while `pop()` removes the item and returns it.
6. tuple in use:  
in `sqlite`, if you want to use values from Python variables,Python request that
>
 Put `?` as a placeholder wherever you want to use a value, and then provide a tuple of values as the second argument to the cursor’s execute() method.

 example here:
 ```
 purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
             ]       
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
```
7. to create a tuple with one item, we need a comma after that item.    
```asign name to a number range of values:   
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)  
```
8. an empty set should be `>>> a_set = set() `, rather than a pair of `{}`.
9. The `update()` method takes one argument, a set (also list and tuple), and adds all its members to the original set. And a tuple has no duplicates.  
10. If you call the `discard()` method with a value that doesn’t exist in the set, it does nothing. No error; it’s
just a no-op. But for the `remove()`, such operation would raise a `KeyError` exception.
11. The `union()` method returns a new set containing all the elements that are in either set.    
 The `intersection()` method returns a new set containing all the elements that are in both sets.   
 The `difference()` method returns a new set containing all the elements that are in a_set but not b_set.
