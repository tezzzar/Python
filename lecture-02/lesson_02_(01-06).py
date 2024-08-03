# Завдання 1
print("Завдання 1")
str1 = "James"
print(str1[0::2])
print()
# Завдання 2
print("Завдання 2")
string = "khokho"
def sym(string):
    """Ця функція перевіряє рядок на симетрію"""
    str_length = len(string)
    if str_length % 2 == 0:
        half_str = str_length // 2
        fh = string[:half_str]
        sh = string[half_str:]
        if fh == sh:
            return True
    return False
if sym(string):
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")
print()
# Завдання 3
print("Завдання 3")
string = "amaama"
def pal(string):
    """Ця функція перевіряє чи є рядок паліндромом"""
    str_length = len(string)
    for i in range(str_length // 2):
        if string[i] != string[str_length - i - 1]:
            return False
    return True
if pal(string):
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")
print()
# Завдання 4
print("Завдання 4")
str1 = "JhonDipPeta"
str2 = "JaSonAy"
def mid_chars(str1, str2):
    """Ця функція отримує три середні символи"""
    length1, length2 = len(str1), len(str2)
    mid1 = length1 // 2
    mid2 = length2 // 2
    mid_char1 = str1[mid1 - 1:mid1 + 2]
    mid_char2 = str2[mid2 - 1:mid2 + 2]
    return mid_char1, mid_char2
print("Вихідні дані для Case 1, Case 2:", mid_chars(str1, str2))
print()
# Завдання 5
print("Завдання 5")
from decimal import *
P = Decimal(input("Визначте основну суму: "))
r = Decimal(input("Визначте річну відсоткову ставку: "))
n = int(input("Визначте кількість разів нарахування відсотків на рік: "))
t = int(input("Визначте кількість років, за які нараховуються відсотки: "))
def complex_interest(P, r, n, t):
    """Функція обчислює складні відсотки за заданою формулою A = P * (1 + (r / n)) ** (n * t)"""
    dec = r / Decimal(100)
    A = P * (1 + (dec / n)) ** (n * t)
    return A
getcontext().prec = 10
result = complex_interest(P, r, n, t)
print("Складні відсотки:", result)
print()
# Завдання 6
print("Завдання 6")
P = 500000
r = 8
n = 24
def EMI(P, r, n):
    """Ця функція реалізує метод зменшення балансу EMI за формулою: EMI = P * [( r * (1 + r)^n)) / ((1 + r)^n - 1)]"""
    r_mon = r / (12 * 100)
    emi = P * r_mon * ((1 + r_mon)**n) / (((1 + r_mon)**n) - 1)
    return emi
fix_pay_amount = EMI(P, r, n)
print("EMI for 24 months:", fix_pay_amount)
print()