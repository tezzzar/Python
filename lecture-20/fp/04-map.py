
def square(n):
    return n ** 2

numbers = [1,2,3,4,5]

squered = map(square, numbers)

print(list(squered))

print(list(map(lambda n: n ** 2, numbers) ))

def to_fahrenheit(c):
    return 9 / 5 * c + 32

def to_celsius(f): 
    return (f -32) * 5 / 9

print(list(map(to_fahrenheit, numbers)))

print(list(map(to_celsius, numbers)))

print(list(map(float, ["11.3", "77.5", "-11.22"])))

print(list(map(int, ["11", "78", "-11"])))

from functools import reduce

print(reduce(lambda a, b: a + b, numbers))

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd']

for i in zip(a, b):
    print(i, type(i))


my_d = {1:'a', 2:'b', 3:'c'}

# swapped = {v:k for k, v in my_d.items()}
# swapped = dict((v,k) for k, v in my_d.items())
# swapped = dict(zip(my_d.values(), my_d))or
swapped = dict(zip(my_d.values(), my_d.keys()))
print(swapped) 