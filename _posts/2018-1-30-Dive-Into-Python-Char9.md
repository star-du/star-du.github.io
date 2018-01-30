---
layout: post
teaser: unit testing is a software testing method to test individual units. By getting familiar with unittest module, we also understand the procedure of modern day programming better.
title: Dive into python 3 chapter 9
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
see **source code** of [unit_testing][ut] and [Roman Numeral utility][roman].

For more, go to https://docs.python.org/3/library/unittest.html

[ut]:https://github.com/star-du/star-du.github.io/blob/master/sourcefile/unit_testing.py
[roman]:https://github.com/star-du/star-du.github.io/blob/master/sourcefile/roman2.py
