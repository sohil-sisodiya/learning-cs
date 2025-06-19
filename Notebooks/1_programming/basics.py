import keyword
import sys

# Keywords 
print(keyword.kwlist) # list of the all the keyword


# Identifiers 
var2 = 20


# Comments
# single line comment
'''
Multiple
line
comments
'''


# Statements - Instructions that a python interpreter can execute
p1 = 20 + 30


# Multiple line statements
p1 = 20 + 30 \
    + 40 + 50 + \
    + 70 + 80

p2 = ['a' ,
    'b' ,
    'c' ,
    'd'
    ]

# print(p1)
# print(p2)


# Indentation - Space matters in python


# Docstring
def square(num):
    '''Square Function:- This function will return the square of a number'''
    return num**2

square.__doc__ # We can access the Docstring using __doc__ method


# Variables
p = 30
id(p) # it returns the "indentity" of the object.
hex(id(p)) # Memory adress of the variable

type(p) # return the type of the variable

p = p + 10 # variable overwriting

# Variable Assignment
intvar = 10 
floatvar = 2.302
strvar = "Hello World!" 

# Multiple Assignment
intvar, floatvar, strvar = 20, 2.34, "Python Language" # use commas to separates

p1 = p2 = p3 = p4 = 44 # all variable pointing to same value


# Data Types 
# Numeric
val1 = 10 # integer
print(val1)
print(type(val1))
print(sys.getsizeof(val1)) # size of integer in bytes
# print(val1, "is Integer?", isinstance(val1, int))

val2 = 14.78 # float
val3 = 25 + 10j # complex data types, size = 32

sys.getsizeof(int()) # 24 
sys.getsizeof(float()) # 24

# Boolean
bool1 = True
bool2 = False

# String
str1 = "hello python!"
print(str1)

mystr = 'Hello' # single quotes
mystr = "Hello World!" # double quotes
mystr = '''Hello
            World''' # Triple quotes

print(mystr)

mystr = ('Happy'
         'Birthday'
         'to'
         'Me')
print(mystr)

mystr2 = "happy "
mystr2 = mystr2*10
print(mystr2)

len(mystr2) # check the length of string

# String Indexing
str1[0] # first character in str1 - 'h'
str1[len(str1) - 1] # last character in str1 - '!'

str1[-1] # last character in str1
str1[6] # fetcht he 7th element of the string

# String Slicing
str1[0:5] # fetch all character from 0 to 5 index

str1[-4:] # retreive last four character of the string
str1[:6] # first 6 character of the string 

# Update and Delete String
str1[0:5] = 'HOLAA' # no update perform - strings are immutable

del str1 # delete a string



