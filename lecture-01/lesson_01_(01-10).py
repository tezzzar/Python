# Завдання 1
print("Завдання 1")
name = "Alex"
print("Hello, ", name, "!", sep="")
print()
# Завдання 2
print("Завдання 2")
numbers = [42, 67, 81]
for number in numbers:
    dozens = number // 10
    print(dozens)
print()
# Завдання 3
print("Завдання 3")
radius = int(input("Задайте радіус кола: "))
p = 3.14159265358980
print("Площа кола:", p * radius ** 2)
print("Довжина кола:", 2 * p * radius)
print()
# Завдання 4
print("Завдання 4")
feet = int(input("Введіть зріст в футах: "))
inches = int(input("Введіть зріст в дюймах: "))
print("Your height is: ", feet * 30.48 + inches * 2.54, "cm.")
print()
# Завдання 5
print("Завдання 5")
feet = int(input("Input distance in feet: "))
print("The distance in inches is", feet * 12, "inches.")
print("The distance in yards is", feet * 0.333333333, "yards.")
print("The distance in miles is", round(feet * 0.000189393939, 3), "miles.")
print()
# Завдання 6
print("Завдання 6")
a = 34
b = 190
a, b = b, a
print(a, "\n", b)
print()
# Завдання 7
print("Завдання 7")
int1 = int(input("Введіть перше число: "))
int2 = int(input("Введіть друге число: "))
int3 = int(input("Введіть третє число: "))
print("Сума чисел:", int1 + int2 + int3)
print()
# Завдання 8
print("Завдання 8")
day = int(input("Введіть кількість днів: "))
hour = int(input("Введіть кількість годин: "))
min = int(input("Введіть кількість хвилин: "))
sec = int(input("Введіть кількість секунд: "))
print("The amounts of seconds:", (day * 24 * 60 * 60) + (hour * 60 * 60) + (min * 60) + sec)
print()
# Завдання 9
print("Завдання 9")
f = int(input("Enter the desired future value: "))
r = float(input("Enter the annual interest rate: "))
n = int(input("Enter the number of years the money will grow: "))
p = f / (1 + r) ** n
print("You will need to deposit this amount:", round(p, 2))
print()
# Завдання 10
print("Завдання 10")
a = 10
b = 18
c = (a ** 2 + b ** 2) ** 0.5
print(c)
print()