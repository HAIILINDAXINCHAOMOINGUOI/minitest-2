# Họ và tên: Trịnh Quốc Thanh - HW1

# Bài 1: Welcome, User!
name = input('Input your name: ')
print(f'Welcome, {name}!')

# Bài 2: Đăng kí tài khoản
first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
phone_number = input('What is your phone number: ')

print('Your registered name is {first_name} {last_name}.')
print(f'Your phone number is {phone_number}') # 0966064681

# Bài 3:

Name        :   Michael
Birthdate   :   01/01/2001
print('Name\t\t:\tThanh')

# Bài 4:
year = input('What year is it: ')

print("                      . : .")
print("                    '.  :  .'")
print("  HAPPY NEW YEAR   .  '.:.'  .")
print(f"   !!! {year} !!!    .  .':'.  .")
# print("   !!! {} !!!    .  .':'.  .".format(year))
print("                    .'  :  '.")
print("                      ' : '")

# Bài 5: 
from turtle import *

forward(50)
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(50)

left(90)
shape('turtle')

mainloop()

# Bài 6:
from turtle import *

shape('turtle')

# draw smaller square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
# vòng lặp for
# for i in range(4): 
#     forward(100)
#     left(90)

# move to start bigger square
penup()
forward(10)
left(90)
pendown()

# draw bigger square
pensize(3)
forward(110)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(10)

mainloop()

# Bài 7
from turtle import *

shape('turtle')

# draw square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

# move to center
penup()
left(90)
forward(50)
left(90)
forward(50)

# move to new square corner
left(45)
forward(50)
left(90)
forward(50)
left(90)
pendown()

# draw square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

# move to center
penup()
left(90)
forward(50)
left(90)
forward(50)
left(45)

mainloop()