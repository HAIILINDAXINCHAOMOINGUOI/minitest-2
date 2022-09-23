# # Bài 1
# for i in range(3,13):
#     print(i, end = ' ')

# # Bài 2
# n = int(input('Input a number: '))

# for i in range(n+1):
#     print(i, end = ' ')

# # Bài 3
# n = int(input('Input a number: '))

# for i in range(1, n+1, 2):
#     print(i, end = ' ')

# Bài 4
from turtle import *

n = int(input('Input number of edges: '))
angle = 180*(n-2)/n

for i in range(n):
    forward(100)
    left(180 - angle)

mainloop()