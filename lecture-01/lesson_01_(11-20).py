# Завдання 11
print("Завдання 11")
a = 15
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print()
# Завдання 12
print("Завдання 12")
a = 6
b = 3
print(a+b, a-b, a*b, a/b, a**b, sep="&")
print()
# Завдання 13
print("Завдання 13")
num = input("Введіть число: ")
num1 = float(num)
num2 = int(num1)
print(num1)
print(num2)
print()
# Завдання 14
print("Завдання 14")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))
print(int(a))
print(int(b))
print(int(c))
print()
# Завдання 15
print("Завдання 15")
speed = int(input("Введіть швидкість: "))
print(speed * 6)
print(speed * 10)
print(speed * 15)
print()
# Завдання 16
print("Завдання 16")
price = int(input("Введіть ціну товару: "))
discount = float(input("Введіть розмір знижки: "))
print("Ціна товару з урахуванням знижки:", price - price * discount)
print()
# Завдання 17
print("Завдання 17")
s = int(input("Введіть суму нарахованої платні: "))
p = float(input("Введіть суму податку у %: "))
print("Ви отримаєте на руки:", s - s * p / 100)
print()
# Завдання 18
print("Завдання 18")
n1 = 1737
n2 = 100
n3 = 384400000
km1 = n1 // 1000
km2 = n2 // 1000
km3 = n3 // 1000
print(km1)
print(km2)
print(km3)
print()
# Завдання 19
print("Завдання 19")
s = 1000
p = 8
print(s + s * p / 100)
print()
# Завдання 20
print("Завдання 20")
seconds = (int(input("Enter the number of seconds: ")))
days = seconds // 86400
seconds = seconds % 86400
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(str(days) + " day(s), " + str(hours) + " hour(s), " + str(minutes) + " minute(s), " + str(seconds) + " second(s).")
print()