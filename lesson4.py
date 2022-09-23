## Cấu trúc lặp for, while

# Cấu trúc lặp for
# range(start, stop, step)
# start mặc định là 0, step mặc định là 1

# for i in range(5):
#     print(i)

# for i in range(1,7,2):
#     print(i)

# In ra các dãy số sau:
# 0,1,2,...8
# 100,101,...105
# 3,6,9,12,15
# 9,8,7,...,2

# for i in range(9): # for i in range(0,9,1):
#     print(i, end = ',')

# for i in range(100,106):
#     print(i, end =',')

# for i in range(3,16,3):
#     print(i, end = ',')

# for i in range(9,1,-1):
#     print(i, end = ',')

# Vòng lặp while

# i = 0
# while i < 5:
#     print(i)
#     i = i + 1

# break, continue
# for i in range(10):
#     if i == 5:
#         continue # break
#     print(i)

# i = 0
# while i < 10:
#     if i == 5:
#         continue # break
#     print(i)
#     i = i + 1

# yêu cầu người dùng nhập vào một số n. In ra tổng các số từ 1 cho đến n.
# Cách 1: sử dụng for, cách 2: sử dụng while

# n = int(input('nhap số n: '))
# i = 1
# s = 0
# while i<n+1:
#     s += i
#     i += 1
# print(s)

# n = int(input('nhap số n: '))
# sum = 0

# for i in range(n+1):
#     # sum = sum + i
#     sum += i

# print(sum)

# Stackoverflow.com: trang web tìm và giải thích lỗi sai

# yêu cầu người dòng nhập vào một string. In string theo thứ tự ngược lại
# hello => olleh

# h e l l o
# 0 1 2 3 4 (index)

# len('hello') = 5

string = input('Nhập vào một string bất kì: ')
new_string = ''

for i in range(len(string)-1,-1,-1):
    # new_string = new_string + string[i]
    new_string += string[i]
print(new_string)
