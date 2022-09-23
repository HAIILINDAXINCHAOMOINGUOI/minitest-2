## Bài 1
# print('== Registration ==')

# username = input('Username: ')
# password = input('Password: ')
# email = input('Email: ')

# print('Registered successfully.')

## Bài 2
# print('== Registration ==')

# username = input('Username: ')
# password = input('Password: ')

# repeat_pass = input('Repeat password: ')

# while repeat_pass != password:
#     print('Passwords not match. Please input again')
#     repeat_pass = input('Repeat password: ')

# email = input('Email: ')

# print('Registered successfully.')

## Bài 3
print('== Registration ==')

username = input('Username: ')

# Check if password is valid or not
password = None

while True:
    password = input('Password: ')

    has_letter = False
    has_digits = False

    for ch in password:
        if (ch > 'a' and ch < 'z') or (ch > 'A' and ch < 'Z'):  # check if password contains a letter
            has_letter = True
        if ch > '0' and ch < '9':  # check if password contains a digit
            has_digits = True

    if has_letter and has_digits and len(password) >= 8: 
        break
    else:
        print('Invalid password. Please input again.')

# Check if email is valid or not
email = None

# check valid email
while True:

    email = input('Email: ')

    if ('.' in email) and ('@' in email):
        break
    else:
        print('Invalid email. Please input again.')

# print result
print('\nRegistered successfully.')