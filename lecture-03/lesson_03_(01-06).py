# Завдання 1
print("Завдання 1")
def every_nth(lst, n):
    return [lst[i] for i in range(n-1, len(lst), n)]
result = every_nth([1, 2, 3, 4, 5, 6], 2)
print(result)
print()
# Завдання 2
print("Завдання 2")
def min_n(lst, n):
    return sorted(lst)[:n]
print(min_n([1, 2, 3], 1))
print(min_n([1, 2, 3], 2))
print()
# Завдання 3
print("Завдання 3")
def max_n(lst, n):
    return sorted(lst, reverse=True)[:n]
print(max_n([1, 2, 3], 1))
print(max_n([1, 2, 3], 2))
print()
# Завдання 4
print("Завдання 4")
def includes_any(lst, values):
    return any(value in lst for value in values)
print(includes_any([1, 2, 3, 4], [2, 9]))
print(includes_any([1, 2, 3, 4], [8, 9]))
print()
# Завдання 5
print("Завдання 5")
def roll(lst, n):
    return lst[-n:] + lst[:-n]
print(roll([1, 2, 3, 4, 5], 2))
print(roll([1, 2, 3, 4, 5], -2) )
print()
# Завдання 6
print("Завдання 6")
import random
def game():
    random_number = random.randint(1, 100)
    while True:
        user_number = int(input("Введіть число від 1 до 100: "))
        if user_number == random_number:
            print("Ви вгадали номер !")
            break
        elif user_number > random_number:
            print("Завелике число, спробуйте ще !")
        else:
            print("Замале число, спробуйте ще !")
game()
print()