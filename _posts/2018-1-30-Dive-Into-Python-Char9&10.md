---
layout: post
teaser: unit testing is a software testing method to test individual units. By getting familiar with unittest module, we also understand the procedure of modern day programming better.
title: Dive into python 3 chapter 9&10
category: coding
tags: [python, note-taking]
---
This chapter deals with unit testing, which is more like a _philosophy_ of python rather than a certain part of grammar. It's part of the so-called **TDD**, test-driven development.   
It certainly needs multiple practices to put it right, so I may just record some example here.
### unit-testing for a roman-integer conversion utility
The thing is, you create class with one or more tests as methods (those methods are required to start with `test` as a key word), and all the class have to be the subclass of `unittest.TestCase`, then using assert methods that's provided by `TestCase`, you can make out whether the tests you're running _pass_ or _fail_ (which is different from _error_!)     
after `import unittest`, first using 'good' input to test whether it can work
~~~python
class KnownValues(unittest.TestCase):
  known_values = ((1, 'I'),
                  ... ...
                  (3888, 'MMMDCCCLXXXVIII'),
                  (3940, 'MMMCMXL'),
                  (3999, 'MMMCMXCIX'))

  def test_to_roman_known_values(self):
      '''to_roman should give known result with known input'''
      for integer, numeral in self.known_values:
          result = roman2.to_roman(integer)
          self.assertEqual(numeral, result)

  def test_from_roman_known_values(self):
      '''from_roman should give known result with known input'''
      for integer, numeral in self.known_values:
          result = roman2.from_roman(numeral)
          self.assertEqual(integer, result)
~~~
`assertEqual` is one of the provided method to verify the result is identical to what we expect.

But also we have *bad* input from nearly every corner, to test if the program could handle those invalid input and raise error, we use `assertRaises`, take to_roman as an example:
~~~python
class to_roman_bad_input (unittest.TestCase):
    def test_too_large(self):
        '''to_roman should raise exception with large input'''
        self.assertRaises(roman2.OutOfRangeError,roman2.to_roman,4000)
    def test_too_small(self):
        '''to_roman should raise exception with input smaller than 1'''
        self.assertRaises(roman2.OutOfRangeError,roman2.to_roman,0)

    def test_non_integer(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(roman2.NotIntegerError, roman2.to_roman, 0.5)
~~~
Of course, the program needs to have this kind of error at first place to pass the unittest, and here we need to know more about error and exception.

first define the error you wish to raise, let it inherit from the built-in ValueError:
~~~python
class OutOfRangeError(ValueError):
    pass
~~~
than we add some `if` or `if not` sentence to raise this error with readable message
~~~python
if not (0 < n < 4000):
    raise OutOfRangeError("the number must be 1...3999\n"
                          "get {} instead".format(n))
~~~
And besides test above, we may have 'roundtrip' to test once more to verify the correctness.
~~~python
class RoundtripCheck(unittest.TestCase):
    def test_roundtrip(self):
        '''from_roman(to_roman(n))==n for all n'''
        for integer in range(1, 4000):
            numeral = roman2.to_roman(integer)
            result = roman2.from_roman(numeral)
            self.assertEqual(integer, result)
~~~
And when we have the following code
~~~python
if __name__ == '__main__':
    unittest.main()
~~~
...and run it, we can now get if the code pass or fail, with ease.
```
Ran 9 tests in 0.052s

OK
```


For more, go to <https://docs.python.org/3/library/unittest.html>
### Refactoring
This chapter is generally about testing and refactoring (i.e. how to enhance your code to make it _better_).

The procedures we now have are that you have your test cases first, and the codes are always behind, so you have to fix. Once your code catches uo to the test cases, you stop coding.
>The best thing about unit testing is that it gives you the freedom to refactor mercilessly.

Yor always have your complete set of unit tests, so you can change your code completely yet the unit tests will stay the same. So that you can always prove that your new code works just as well as the original ones.

In the example above, you can boldly refactor your code with a totally different method - like, building a map for these 4000 pairs.
~~~python
to_roman_table = [None]
from_roman_table = {}

def build_lookup_tables():
    def to_roman(n):
        result = ''
        for numeral, integer in roman_numeral_map:
            if n >= integer:
                result = numeral
                n -= integer
                break
        if n > 0:
            result += to_roman_table[n]
        return result

    for integer in range(1, 4000):
        roman_numeral = to_roman(integer)
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer
~~~  
the code above uses a clever bit of programming, you defines a function in the local scope of `build_lookup_tables` function, and as I see it, recursively get a table of numeral-integer pairs

then the original `to_roman` and `from_roman` function only needs to find the corresponding values, and deal with those exceptions now!
~~~python
def to_roman(n):
    '''convert integer to Roman numeral'''
    if not (0 < n < 4000):
        raise OutOfRangeError('number out of range (must be 1..3999)')
    if int(n) != n:
        raise NotIntegerError('non-integers can not be converted')
    return to_roman_table[n]
~~~
And every time you use `to_roman` and `from_roman`, you will need those two tables, so remember to add a calling sentence of `build_lookup_tables()`.

see **source code** of [unit_testing][ut] and Roman Numeral utility [example1][roman1] and [example2][roman2]

[ut]:https://github.com/star-du/star-du.github.io/blob/master/sourcefile/unit_testing.py
[roman1]:https://github.com/star-du/star-du.github.io/blob/master/sourcefile/roman2.py
[roman2]:https://github.com/star-du/star-du.github.io/blob/master/sourcefile/roman3.py
