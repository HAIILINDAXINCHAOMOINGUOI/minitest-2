## Cấu trúc dữ liệu list và tuple

# List
# fruits = ['apple', 'banana', 'cherry']
# print(fruits)

# mylist = ['Thanh', 'Duc', 'A', 'B', 10, 20, 30]
# Index     0        1     2    3    4   5   6
# print(mylist)
# print(mylist[4])
# print(len(mylist))

## add item to the list
# mylist.append(40)
# mylist.append('C')
# mylist.insert(4, 'C')

## remove item from the list
# mylist.remove(10) # xóa theo giá trị
# mylist.pop(4) # xóa theo index
# mylist.pop()
# mylist.clear() # xóa toàn bộ list
# print('C' in mylist)

# mylist = ['Thanh', 'Duc', 'A', 'B', 10, 20, 30]

# for item in mylist:
#     print(item)

# for i in range(len(mylist)):
#     print(mylist[i])

# list_1 = ['a', 'b', 'c']
# list_2 = [1, 2, 3]

# print(list_1 + list_2)
# list_1.extend(list_2)
# print(list_1)

# mylist = ['Thanh', 'Duc', 'A', 'B', 10, 20, 30]
# new_list = mylist.copy()
# print(new_list)

# Yêu cầu người dùng nhập vào 1 số (thực hiện lại 5 lần). Tạo 1 list để chứa 5 số trên

# mylist = []

# for i in range(5):
#     number = int(input('enter a number: '))
#     mylist.append(number)

# print(mylist)

## Kiểu dữ liệu tuple

mytuple = ('Thanh', 'Duc', 'A', 'B', 10, 20, 30)
# Index       0       1     2    3    4   5   6
# mytuple = ('Thanh', 'Duc', 'A', 'B', 10, 20, 30, 40)
# mylist = list(mytuple)
# mylist.append(40)
# mytuple = tuple(mylist)
# print(mytuple)

# print(mytuple[3])
# print(len(mytuple))

# for item in mytuple:
#     print(item)

# for i in range(len(mytuple)):
#     print(mytuple[i])

# number = [4, 7, 10, -5, 80, -26, 35]
# Tính tổng list trên, không được sử dụng hàm có sẵn sum()

# sum = 0
# for i in number:
#     sum += i

# print(sum)

# for i in range(len(number)):
#     sum += number[i]

# print(sum)

number = [4, 7, 10, -5, 80, -26, 35]
# Tìm số lớn nhất của dãy, không sử dụng max()

# max_num = number[0]

# for item in number:
#     if item > max_num:
#         max_num = item

# for i in range(len(number)):
#     if number[i] > max_num:
#         max_num = number[i]

# print(max_num)


number = [4, 7, 10, -5, -26, 80, 35]
# => [-26, -5, 4, 7, 10, 35, 80]
# Sắp xếp theo thứ tự tăng dần, không sử dùng sorted()

sorted_list = []

for i in range(len(number)):
    min_num = number[0]
    for item in number:
        if item < min_num:
            min_num = item
    number.remove(min_num)
    sorted_list.append(min_num)
    

print(sorted_list)

