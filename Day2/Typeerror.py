# len('123567') + len(123567)
# This will raise a TypeError because len() expects a sequence (like a string, list, etc.)
# but 123567 is an integer, which does not have a length.
# To fix the error, we can convert the integer to a string first
print(len('123567') + len(str(123567)))

#Type checking examples
print(type('Hello')) # This will return <class 'str'>
print(type(12345))   # This will return <class 'int'>
print(type(12.34))   # This will return <class 'float'>
print(type(True))    # This will return <class 'bool'> 

#Type conversion examples
print(int('123'))    # This will convert the string '123' to the integer 123
print(float('12.34')) # This will convert the string '12.34' to the float 12.34
print(str(12345))    # This will convert the integer 12345 to the string '12345'
print(bool(1))       # This will convert the integer 1 to the boolean True
print(bool(0))       # This will convert the integer 0 to the boolean False
print('123' + str(456)) # This will concatenate the string '123' with the string '456' to get '123456'
print(123 + int('456')) # This will add the integer 123 to the integer 456 to get 579
                       #but there is a TypeError if we try to add a string and an integer directly
                       # we should also be very careful while converting types to avoid unexpected results.
                       # For example, converting a non-numeric string to an integer will raise a ValueError:
# print(int('abc'))  # This will raise a ValueError because 'abc' cannot be converted to an integer.

            