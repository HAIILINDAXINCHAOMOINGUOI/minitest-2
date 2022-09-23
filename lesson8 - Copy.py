# Function, scope và module

# def print_name():
#     print('Hello Thanh')
#     print('Hello Duc')
#     print('Hello Minh')

# print_name()

# def print_name(name):
#     print(f'Hello {name}')

# print_name('Thanh')
# print_name('Duc')
# print_name('Minh')

# def area_of_triangle(width, height):
#     return width * height * 0.5
    
# area = area_of_triangle(5, 10)
# print(area)

# Scope of variables
# global
# local

# a = 12

# def add():
#     a = 'Thanh'
#     print(a)

# add()

# def add_2():
#     print(a)

# add_2()

# Bài 1: Viết 1 function để xác định 1 số có là số nguyên hay không.

# def is_int(num):
#     if num == int(num):
#         return f'{num} là số nguyên'
#     else:
#         return f'{num} không là số nguyên'

# number = float(input('Enter a number: '))
# print(is_int(number))


# import test as t

# t.print_name('Thanh')

# import random

# number = random.randint(10, 20)
# print(number)

# Bài 2: viết function để tìm ra số lớn hơn trong 2 số

def find_larger(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return 'Hai số bằng nhau'

# print(find_larger(5, 5))

# Bài 3: Viết function để tính tổng 2 số

def add(num1, num2):
    return num1 + num2

# print(add(4, 6))

# Bài 4: Viết function để tìm số nhỏ nhất của 1 dãy

mylist = [5, 8, 15, 51, 13, 9, 1, 24, 82, 26, 44, 108]

def find_min(list):
    min = list[0]
    for item in list:
        if item < min:
            min = item
    return min

# print(find_min(mylist))

# Bài 5: 
# Tam giác pascal
# 1
# 1 1 
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1 (n = 5)
# 1 5 10 10 5 1 (n = 6)

# Nhập n. In ra n hàng của tam giác pascal.

n = int(input('Enter a number: '))

def pascal(n):
    pass
