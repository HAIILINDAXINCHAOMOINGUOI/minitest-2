# Bài 1
n = int(input('Input a number: '))

if n > 13:
    print('This number is larger than 13')
else:
    print('This number is not larger than 13')

# Bài 2
n = int(input('Input a number: '))

if n % 2 == 0:
    print('This number is even')
else:
    print('This number is not even')

# Bài 3
n = int(input('Input a month: '))

if n == '1' or n == '3' or n == '5' or n == '7' or n == '8' or n == '10' or n == '12':
    print('This month has 31 days')
elif n == '4' or n == '6' or n == '9' or n == '11':
    print("this month have 30 days")
else:
    print("this moth have 28/29 days")