# first class functions

def fn():
    print("I'm first class function")

fn()

another_name = fn
another_name()

print(callable(fn))
print(callable(another_name))

print(callable(print))

print(callable(lambda s: s[::-1]))

print(callable([]))

print((lambda x: (x, x**2, x**3))(3))
print((lambda x: [x, x**2, x**3])(3))
print((lambda x: {1:x, 2:x**2, 3:x**3})(3))

