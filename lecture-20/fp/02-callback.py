
def inner():
    print("I'm inner function")

def outer(fn):
    fn()

outer(inner)

animals = ['ferret', 'vole', 'dog', 'cat', 'gecko']

print(sorted(animals))
print(animals)

print(sorted(animals, key=len))
print(sorted(animals, key=len, reverse=True))

a = [10,3,5,1,9]

print(a)

a.sort()
print(a)

m = [[11,202], [2, 200], [88, 99]]

m.sort()

print(m)

m.sort(key=lambda x: x[0])

print(m)

m.sort(key=lambda x: x[1])

print(m)