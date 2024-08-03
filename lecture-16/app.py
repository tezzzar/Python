import csv

# data = [
#     [1,2,3],
#     ['Good morning', 'Good evening', 'Good afternoon'],
# ]

# with open('data1.csv', 'w') as fh:
#     writer = csv.writer(fh)
#     writer.writerows(data)

# with open('data1.csv', newline='') as fh:
#     reader = csv.reader(fh)
#     for row in reader:
#         print(row)


# with open('data2.csv', 'w') as fh:
#     fields = ['country', 'capital']

#     writer = csv.DictWriter(fh, fieldnames=fields)
#     writer.writeheader()
#     writer.writerow({
#         'country' : 'France',
#         'capital': 'Paris'
#     })
#     writer.writerow({
#         'country' : 'Italy',
#         'capital': 'Rome'
#     })
#     writer.writerow({
#         'country' : 'Spain',
#         'capital': 'Madrid'
#     })


# with open('data2.csv') as fh:
#     fields = ['country', 'capital']

#     reader = csv.DictReader(fh)
#     for row in reader:
#         print(row['country'], row['capital'])


gc = (n**2 for n in range(100))

# print(gc)

# for n in gc: print(n)


def m_y():
    yield "step 1"
    yield "step 2"
    yield "step 3"


m_o = m_y()

# print(next(m_o))
# print(next(m_o))
# print(next(m_o))
# print(next(m_o))


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
# sum_of_first_n = sum(firstn(1000000))


# print(sum_of_first_n)

file_name = 'data.csv'


def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

csv_gen = csv_reader("data.csv")

row_count = 0
for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")

# Нове визначення csv_reader():
def yield_reader(file_name):
    for row in open(file_name, "r"):
        # result = file.read().split("\n")
        yield row

yield_gen = yield_reader(file_name)

row_count = 0
for row in yield_gen:
    row_count += 1

print(f"Row count is {row_count}")
