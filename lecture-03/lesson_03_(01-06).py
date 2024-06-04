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