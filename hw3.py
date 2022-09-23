# Bài 1:
number = int(input('nhập vào một số: '))

if number % 2 == 0:
    print(f'{number} là số chẵn')
elif number == 0:
    print(f'{number} không xác định')
else:
    print(f'{number} là số lẻ')

# Bài 2:
# sử dụng type() để xác định kiểu dữ liệu

number = float(input('nhập vào một số: '))

if type(number) == int:
    print(f'{number} là số nguyên')
else:
    print(f'{number} không là số nguyên')

# Bài 4:
number = int(input('nhập vào một số: '))

if number % 3 == 0 or number % 5 == 0: # chia hết cho 1 trong 2 số
    if number % 5 != 0: # chỉ chia hết cho 3
        print(f'{number} is divisible by 3')
    elif number % 3 != 0: # chỉ chia hết cho 5
        print(f'{number} is divisible by 5')
    else: # chia hết cho cả 3 và 5
        print(f'{number} is divisible by 3 and 5')
else: # không chia hết cho cả 3 và 5
    print(f'{number} is not divisible by 3 or 5')

# Bài 5
username = input('Enter username: ')
password = input('Enter password: ')

if username == 'admin' and password == '12345':
    print('You are logged in')
else:
    print('Wrong username/password')

# Bài 6:
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))

if (a + b > c) and (b + c > a) and (c + a > b):
    if a == b and b == c: # nếu là tam giác đều
        print('là tam giác đều')
    elif a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b: # nếu là tam giác vuông
        print('là tam giác vuông')
    else:
        print('là 3 cạnh tam giác')
else:
    print('không là tam giác')