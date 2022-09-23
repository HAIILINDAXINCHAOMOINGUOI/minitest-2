#Bài 3:
import math
def isPrimeNumber(n):
    if(n<2):
        return False

    squareRoot=int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i ==0):
            return False

n=int(input("NHập số nguyên dương b là: "))
print(n, "số nguyên đầu tiên là: ")
dem=0
i=2
sb =""
while (dem<n):
    if(isPrimeNumber(i)):
        sb=sb + str(i)+""
    i = i+1
print(sb)
#Bài 5:from datetime import datetime
from datetime import datetime 
now = datetime.now()
print(now)
#Bài 2:

def is_print(num):
   for i in range (2,int((num)**1/2)):
    if num % i == 0:
        return f'{num} is not a prime number'
    return f'{num} is a prime number'  
    
print(is_print(19)) 
