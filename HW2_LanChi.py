# bài1: hình tròn
a = int(input('radius: '))
b = (3.1416)
c = (2) 
print(f'Perimeter(P): {a*b*c}')
d = (a**c)
print(f'Area(S){b*d}')

# bài2: đường chéo hình vuông
a = int(input('length of edge: '))
b = (1.4142135623730951)
print(f'length of diagonal line: {a*b}')

# bài3: email
account_name = input('input your name: ')
domain_name = input('input your domain: ')
a = '@'
print(f'Full email: {account_name}{a}{domain_name}')

# bài4: ngày tháng
a = input(f'MM: ')
b = input(f'DD: ')
c = input(f'YYYY: ')
d = '/'
print(f'Date in MM/DD/YYYY format: {a}{d}{b}{d}{c}')
print(f'Date in DD/MM/YYYY format: {b}{d}{a}{d}{c}')

# bài5: lãi suất
a = int(input('Deposit: '))
b = (1.05)
print(f'Account after 1 year: {a*b}')
d = (2)
c = (b**d) 
print(f'Account after 2 years: {a*c}')
e = (10)
f = (b**e)
print(f'Account after 10 years: {a*f}')

# bài 6: gmail logo
from turtle import *
forward(200)
right(90)
forward(150)
right(90)
forward(200)
right(90)
forward(150)
shape('turtle')
pencolor('red')

right(180)
width(15)
forward(150)
right(180)
forward(150)
pencolor('red')
right(135)
forward(142)
left(90)
forward(142)
right(135)
forward(150)
mainloop()

#bài7: squarelogo 
from turtle import *
pencolor('#cf8f03')
width(13)
left(35)
forward(100)
right(70)
forward(100)
right(110)
forward(100)
right(70)
forward(100)
right(145)
pencolor('white')
width(0)
fd(50)

pencolor('#0b2c3c')
width(13)
left(35)
forward(100)
right(70)
forward(100)
right(110)
forward(100)
right(70)
forward(100)
right(110)


mainloop()

