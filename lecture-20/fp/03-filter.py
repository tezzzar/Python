
numbers = [-25, -12, 0, 14, 21, 77, 80]

def positive(numbers):
    p_numbers = []
    for n in numbers:
        if n > 0:
            p_numbers.append(n)
    return p_numbers

print(positive(numbers))


pos_numbers = filter(lambda n: n > 0, numbers)
print(positive(pos_numbers))

def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, numbers)))

print(list(filter(lambda x: x % 2 == 0, numbers)))

print(list(filter(lambda x: x % 2 == 0, range(50))))

obj = [0, 1, [], 4, 7, "", True, None, 8, False]

def ident(x):
    return x

print(list(filter(ident, obj)))

print(list(filter(None, obj)))

import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
            
print(is_prime(5))
print(is_prime(12))

print(list(filter(is_prime, range(1, 55))))

import statistics as st


sample = [10, 8, 10, 8,  2, 7, 9, 3, 34, 9, 5, 7, 77]

mean = st.mean(sample)
print(mean)


stdev = st.stdev(sample)

low = mean - 2 * stdev
high = mean + 2 * stdev
clean_data = list(filter(lambda x: low <= x <= high, sample))
print(clean_data)
