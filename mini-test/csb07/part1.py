arr = ['blue', 'green', 'yellow', 'orange']
print('Color list: ')

# bai 2
def getColorList(arr):
    str = ""
    for i in arr:
        if i == arr[-1]:
            str += i
        else:
            str += i + ', '
    return str
print(getColorList(arr))

# bai 3
color = input('Input a new color: ')

if color not in arr:
    arr.append(color)
print('New color list: ')
print(getColorList(arr))



rr = ['blue', 'green', 'yellow', 'orange']
print('Color list: ')

def getColorList(arr):
    str = ""
    for i in arr:
        if i == arr[-1]:
            str += i
        else:
            str += i + ', '
    return str
print(getColorList(arr))

# bai 1
index = int(input('Input position: '))
print(f'Color at position {index}: {arr[index]}')

# bai 2
kill = input('Item to delete: ')
if kill.isnumeric():
    if kill in arr:
        arr.pop(int(kill))
else:
    arr.remove(kill)
    
print(getColorList(arr))






