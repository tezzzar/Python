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



# lecture 03

numbers = []
contacts = list()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 11, 13]

contacts = ["John Doe", 1234567, "Some Sity", True]

print(numbers)
print(type(numbers))
tpl = ()
tup = tuple()

tup = ('a','b', 'c')
tpl = (1,2,3) # 1,2,3 (6,)
print(tup)

print(type(tup))

x = range(5)
print(x)
print(type(x))

print(range(-5, 5, 2))

print(list(range(-5, 5, 2)))
print(tuple(range(-5, 5, 2)))

my_tuple = tuple(range(-5, 5, 2))

print(my_tuple[2])

print((1,2,3) < (0,2,2))
# print((1,2,3) < [0,2,2]) # TypeError: '<' not supported between instances of 'tuple' and 'list'

print(list((1,2,3)) < [0,2,2])
print((1,2,3) < tuple([0,2,2]))

print(numbers.index(7))
print(numbers.index(5, 6, 12))

print("John Doe" not in contacts)

print(numbers.count(5))
print(min(numbers))
print(max(numbers))

print(max(tup)) # a b c 
print(id(numbers))
numbers += 8, 88, 88 
print(id(numbers))
print(numbers)

print(id(tpl))
tpl += 5, 55, 555
print(id(tpl))
print(tpl) # (1, 2, 3, 5, 55, 555)

for item in numbers:
    print(item)

for item in tpl:
    if item == 5:
        continue
    print(item)
else:
    print("All done!")

for item in tpl:
    if item == 55:
        break
    print(item)

index = 0
for item in numbers:
    print(index, item)
    index += 1

for index in range(len(numbers)):
    item = numbers[index]
    print(index, item)

for index, item in enumerate(numbers):
    print(index, item)

print(numbers[2:8])
print(numbers[:8])
print(numbers[1:10:2])

numbers.append(7777)
print(numbers)

numbers.extend([888, 555, 444])
print(numbers)

numbers.insert(4, 4444444)
print(numbers)
print(numbers.pop())
print(numbers)

print(numbers.pop(4))
print(numbers)

numbers.remove(888)
print(numbers)

del numbers[5]
print(numbers)

cache = [1, 2, 3, 4, 5, 7, 8, 9, 10, 5, 11, 13, 8, 88, 88, 7777, 555]
print(cache)
# cache[:] = []
cache.clear()
print(cache)

new_numbers = numbers
print(id(new_numbers))
print(id(numbers))
print(new_numbers)

copy_numbers = numbers[:]
print(id(numbers))
print(id(copy_numbers))
from copy import copy
copy_2_numbers = copy(numbers)
print(id(copy_2_numbers))
print(id(copy_numbers))

from copy import deepcopy

matrix = [
    [1,2,3],
    [4,5,6],
    [7,7,8]
]

matrix_copy = deepcopy(matrix)

print(id(matrix[0]) == id(matrix_copy[0]))
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

l = ['g', 'y', 'aaa', 'ab', 'bbbb', 'd', 'c']
l.sort()
print(l)

l.sort(key=len)
print(l)

fruits = ('apple', 'mango', 'papaya', 'cherry')

green, *tropic, red = fruits
print(green)
print(tropic)
print(red)

import random

print(random.random())
print(random.random())

print(random.randint(0, 10))
print(random.randint(5, 55))

print(random.choice(l))
print(random.choice(l))
print(random.choice(l))

random.shuffle(l)

print(random.choice(l))
print(random.choice(l))
print(random.choice(l))



# lecture 04

contacts = []


contact = {
    'first_name': 'john',
    'last_name': 'doe',
    'phone_number': '380111234567'
}

contacts.append(contact)

TITLE = "Your phone book"

def hello():
    print(F"Hi! Is's me, {TITLE.upper()}")

def bye():
    print(F"Thanks for using {TITLE}")

def make_your_choice():
    return input(f"Please make Your choice (l,a,u,r,h or q ) here>>> ")

def help_me():
    print("""
    All that You can do:
        l : List existing contacts
        a : Add new contact
        u : Update existing contact
        r : Remove existing contact
        h : Print this help
        q : Exit
    """)

def contact_list():
    if len(contacts) > 0:
        for contact in contacts:
            for k, v in contact.items():
                print(k, '=>', v)

    else:
        print("Your contact list is empty. Go back to menu yo add a new contact.")

def add_contact():
    contact = {}
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    phone_number = input("Enter phone number: ").strip()
    contact['first_name'] = first_name
    contact['last_name'] = last_name
    contact['phone_number'] = phone_number
    return contact

def update_contact(contact):
    old_phone_number = contact['phone_number']
    old_first_name = contact['first_name']
    old_last_name = contact['last_name']

    phone_number = input(f"Edit phone number: ({old_phone_number}) => ").strip() or old_phone_number
    print(phone_number)
    first_name = input(f"Edit first name: ({old_first_name}) => ").strip() or old_first_name
    last_name = input(f"Edit last name: ({old_last_name}) => ").strip() or old_last_name

    return {'first_name':first_name.lower(), 'last_name': last_name.lower(), 'phone_number': phone_number}

def remove_contact(contact):
    index = contacts.index(contact)
    confirm = input("Are You sure You want to delete this  contact? (y/n): ").strip()
    if confirm.lower() in ('yes', 'y'):
        contacts.pop(index)


def lookup_contact(name):
    words = name.split()
    if len(words) == 2:
        first_name, last_name = words
    elif len(words) == 1:
        first_name = words[0]
        last_name = ''
    for d in contacts:
        if d['first_name'] == first_name.lower() and d['last_name'] == last_name.lower():
            return d
        elif d['first_name'] == first_name.lower() and last_name == '':
            return d

def main():
    hello()

    while True:
        match make_your_choice():
            case 'a':
                new_contact = add_contact()
                contacts.append(new_contact)
            case 'l':
                contact_list()

            case 'u':
                name = input("What name You looking for: ")
                contact = lookup_contact(name)
                # print(contact)
                contact.update(update_contact(contact))

            case 'r':
                name = input("What name You looking for: ")
                contact = lookup_contact(name)
                remove_contact(contact)

            case 'q':
                bye()
                break
            case _:
                help_me()

main()