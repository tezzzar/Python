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
miles = round(feet * 0.000189393939, 3)
print("The distance in inches is", feet * 12, "inches.")
print("The distance in yards is", feet * 0.333333333, "yards.")
print("The distance in miles is", miles, "miles.")
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