## Bài 1
# n = int(input('Input number: '))

# for i in range(1,n+1):
#     print('#' * i)

## Bài 2
# n = 0

# while n <= 0:
#     n = float(input('Input a positive number: '))

# print('Thank you.')

## Bài 3
# n = int(input('Input number: '))
# result = 1

# if n > 0:
#     for i in range(1, n+1):
#         result *= i
# elif n == 0:
#     result = 1
# else:
#     result = 'Invalid'

# print(f'{n}! = {result}')

## Bài 4
# n = input('Enter number: ')
# digits_sum = 0

# for num in n:
#     digits_sum += int(num)

# print(digits_sum)

## Bài 5
# print('Numbers with sum of digits = 9')

# count = 0
# num = 1000

# while count < 10:
#     digits_sum = 0

#     for i in str(num):
#         digits_sum += int(i)

#     if digits_sum == 9:
#         print(num, end = ' ')
#         count += 1

#     num += 1
    
## Bài 6
# from turtle import *

# n = int(input('Input number of edges: '))
# angle = (n-2)*180 / n

# for i in range(n):
#     forward(100)
#     left(180 - angle)

# mainloop()

## Bài 7
# from turtle import *

# radius = 1
# for i in range(20):
#     circle(radius, 180)
#     radius += 10

# mainloop()