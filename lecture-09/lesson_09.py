# Завдання 1
print("Завдання 1")

""" Дана функція сортує словник за ключами (d) і також в зворотньому порядку """


def sort_dict_by_key(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))


d = {"one": 1, "three": 3, "five": 5, "two": 2, "four": 4}
print(sort_dict_by_key(d))
print(sort_dict_by_key(d, True))

print()

# Завдання 2
print("Завдання 2")

""" Ця функція сумує значення в списку словників """


def sum_by(lst, fn):
    return sum(map(fn, lst))


print(sum_by([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]))

print()


# Завдання 3
print("Завдання 3")

""""Ця функція сортує список "a" відповідно до індексів у списку "b" """


def sort_by_indexes(a, b, reverse=False):
    zipped_lists = zip(b, a)
    sorted_pairs = sorted(zipped_lists, key=lambda x: x[0], reverse=reverse)
    return [x[1] for x in sorted_pairs]


a = ["eggs", "bread", "oranges", "jam", "apples", "milk"]
b = [3, 2, 6, 4, 1, 5]

print(sort_by_indexes(a, b))
print(sort_by_indexes(a, b, True))


print()

# Завдання 4
print("Завдання 4")

""" Ця функція обчислює середнє значення двох чи більше чисел """


def average(*args):
    total_sum = sum(args)
    count = len(args)
    return total_sum / count


print(average(*[1, 2, 3]))
print(average(1, 2, 3))


print()

# Завдання 5
print("Завдання 5")

""" Ця фуекція обчислює середнє значення списку після зіставлення кожного елемента зі значенням lambda """


def average_by(lst, fn=lambda x: x):
    mapped_values = list(map(fn, lst))
    total_sum = sum(mapped_values)
    count = len(mapped_values)
    # print(mapped_values)
    return total_sum / count


print(average_by([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda x: x["n"]))


print()
