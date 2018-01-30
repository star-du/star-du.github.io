import re

roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

class OutOfRangeError(ValueError):
    pass

class NotIntegerError(ValueError):
    pass

class InvalidRomanNumeralError(ValueError):
    pass


def to_roman(n):
    '''convert integer to Roman numeral'''
    if not (0 < n < 4000):
        raise OutOfRangeError("the number must be 1...3999\n"
                              "get {} instead".format(n))
    if not isinstance(n,int):
        raise NotIntegerError("the number must be integers!")
    result = ''
    for roman, integer in roman_numeral_map:
        while n >= integer:
            result += roman
            n -= integer
            # print('subtracting {0} from input, adding {1} to output'.format(integer, roman))
    return result

def from_roman(s):
    '''convert Roman numeral to integer'''
    if not re.search(pattern,s):
        raise InvalidRomanNumeralError("It's not a valid Roman Numeral")
    result = 0
    index = 0
    for roman, integer in roman_numeral_map:
        while s[index:index+len(roman)] == roman:
            result += integer
            index += len(roman)
            # print('subtracting {0} from input, adding {1} to output'.format(integer, roman))
    return result