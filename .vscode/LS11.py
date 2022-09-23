
#   Phần 1:

laptop={
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30
}

print(laptop['MACBOOK'])

A=int(input("Input a brand: "))
if A==laptop:
    print(laptop[A])

#phần 2:
#1
laptp={
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
    'TOSHIBA':10
}
print(laptp)
#2
A=int(input("Input a brand: "))
b=int(input('input amount: '))
laptp[A]=b
#3
laptp['MACBOOK']:2
laptp['DELL']:60
print(laptp)
#4
print('Total product: ',laptp=['MACBOOK']+['DELL']+["HP"]+['ASUS']+['TOSHIBA'])

#Phần 3
laptops={
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
    'TOSHIBA':10
}

print(laptops['ASUS'])
C=int(input('ipnut a brand: '))
#phần 4
print(f"Total price: {laptops['ASUS']*5}")

#2
laptop = input("Input a brand: ")
qty = input('Input amount to buy: ')
print(f"Total price: {laptops[laptop] * qty}")
#Phần 6:
character = {
    'Name': 'Light',
    'Age': 17,
    'Strengths': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2
}

#2
character['Gold'] += 50
print(f"Gold: {character['Gold']}")

#3
character['Backpack'].append('Flint stone')
print(f"Backpack: {character['Backpack']}")
#Phần 7:
skills = {
    'Skill 1': {
        'Name': 'Tackle',
        'Minimum level': 1,
        'Damage': 5,
        'Hit rate': 0.3
    },
    'Skill 2': {
        'Name': 'Quick Attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5
    },
    'Skill 3': {
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2
    }
}

#2
for key, value in skills.items():
    print(f"{key}: {value['Name']}")
    #part 5:
#1
prices = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

quantities = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

values = {}
for key, value in quantities.items():
    values[key] = value * prices[key]

print(f"Total value of available brands: ")
for key, value in values.items():
    print(f"- {key}: {value}")

#2
sum = 0
for value in values.values():
    sum += value
print(f"Total value of available items: {sum}")


