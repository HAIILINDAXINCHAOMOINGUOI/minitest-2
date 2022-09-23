
#Bài 1,2:
from types import type
a=int(input(type,"input a roman number"))
numbers_2 = {'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}
numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}

    
if a==numbers and numbers_2:
    print("this is roman number")
else:
    print("this isn't roman number")

#bài 3:
number_list = [{'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX'}]



b=int(input("Input a roman number"))
if b==number_list:
    print("this is roman number")
else:
    print("this isn't roman number")
#Bài 4,5:

names = {
'students': [
{'firstName': 'Nikki', 'lastName': 'Roysden'},
{'firstName': 'Mervin', 'lastName': 'Friedland'},
{'firstName': 'Aron', 'lastName': 'Wilkins'}
],
'teachers': [
{'firstName': 'Amberly', 'lastName': 'Calico'},
{'firstName': 'Regine', 'lastName': 'Agtarap'}
]
}

# Bài 6:
c=int=(input("Input squence: "))
