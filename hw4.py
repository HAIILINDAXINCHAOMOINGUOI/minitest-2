#Bài 6:
import turtle as pen
size=float(input("mời bạn nhập cạnh hình đa giác: "))
sides=int(input("mời bạn nhập số cạnh của đa giác: "))
for _ in range(sides):
   pen.forward(size)
pen.right(360/sides)