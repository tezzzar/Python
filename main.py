# Лекція 1

a = 2
b = 2

# + - * / // % **
c = a + b

A = "hello"
# A123_rrr _abc x y a1 c3

print(c)
print(a, b, c, sep=":", end="\t")
print(c)

# name = input("Enter name: ")

# print(A, name)

x = int(input("Enter x: "))
y = int(input("Enter y: "))
o = input("Enter operation: ")

first = "sum" if o == '+' else "not sum"
print(first)

if o == '+':
    print("x + y = ", x + y)
elif o == "-":
    print("x - y = ", x - y)
else:
    print("Bad operation!")

match o:
    case "+":
        print("x + y = ", x + y)
    case '-':
        print("x - y = ", x - y)
    case _:
        print("Bad operation!")



# lecture 02

var = "This is string" # 'This is string' ```This is string``` """This is string"""

print(type(var)) # str <class 'str'>
print(len(var)) # 14

var = 1
print(type(var)) # <class 'int'>

# duch darch

# print(len(var)) # TypeError
# <class 'int'>
# Traceback (most recent call last):
#   File "C:\projects\py-g34\main.py", line 13,
#     print(len(var))
#           ^^^^^^^^
# TypeError: object of type 'int' has no len()

var = True # False
# var = False
true = True
print(type(var)) # <class 'bool'>
print(var == true) # == != > < >= <=

a = 100
b = 0
o = '/'
# and or not xor >> <<
if (o == '/' and b == 0):
    pass


print("Hello" is not "World")
print("Hello" is "World")

print(type(bool(a))) # <class 'bool'>

print(bool(0)) # False
print(bool(''))

a = 10
print(a)
print(oct(a)) # 0o12
print(hex(a)) # 0xa # a b c d e f
print(bin(a)) # 0b1010

print(3 ** 159) # 7282483350946404208076885500996745047522350034970917293604274649554310785067


b = 5.55 # 1.8e308
print(1.8e308) # 7282483350946404208076885500996745047522350034970917293604274649554310785067 - inf
# print(b ** 1000)

# Traceback (most recent call last):
#   File "C:\projects\py-g34\main.py", line 53, in <module>
#     print(b ** 1000)
#           ~~^^~~~~~
# OverflowError: (34, 'Result too large')

print(round(b)) # 6
#  abs divmod max min pow sum

import math

print(math.pi)
print(math.sqrt(77))
# sin cos log

from decimal import *
print(getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

getcontext().prec = 10

print(getcontext())

print(Decimal('1.10').normalize())
print(Decimal('1.11e1').normalize())

v1 = Decimal('1.0001')
v2 = Decimal('1.01')
print( v1, v2)
print( v1.quantize(v2))

print( v2.quantize(v1))

print("""
Usage: thing [OPTION]
    -h  Display this help
    -H  Host to connect to
""")

print("Hello\nWorld")
print("Hello\tWorld")
print(r"Hello\nWorld")
print(R"Hello\nWorld")

hel = "Hello World"
print(hel[3:10])
print(hel[2:])
print(hel[:10])
print(hel[:-2])
print(hel[1:10:2])
print(hel.split()) # ['Hello', 'World']

tel = "050-123-456-777"
print(tel.split("-")) # ['050', '123', '456', '777']
print(tel.partition("-")) # ('050', '-', '123-456-777')

print(str(math.pi)) # 3.141592653589793

name = "John Doe"
age = 33
print("".join(["My name is ", name, ", and I am ", str(age), " years old"]))

print("My name %s, and I am %d years old" % (name, age))
print("My name {}, and I am {} years old".format(name, age))
print(F"My name {name}, and I am {age} years old")

print(chr(8364)) #€
print(ord('€'))

print(name.capitalize())
print(name.upper())
print(name.title())
print(name.lower()) # john doe
#  name.lower().istitle()
print(name.lower().istitle())

if (name.lower().istitle()):
    pass
else:
    print(name.title())


def fn():
    return "Hello Function"

def summa(a, b):
    """This function adds two numbers"""

    return a + b

print(fn())
print(summa(11111, 22222))

import this

# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

x = 0
while x < 10:
    if x == 7:
        break
    x += 1
else:
    print(f"{x} not less then 10")

print(x)
