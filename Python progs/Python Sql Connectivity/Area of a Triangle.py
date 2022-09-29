# Python Program to find Area of a Triangle

a = float(input('Please Enter the First side of a Triangle: '))
b = float(input('Please Enter the Second side of a Triangle: '))
c = float(input('Please Enter the Third side of a Triangle: '))

s = (a + b + c) / 2

Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(" The Area of a Triangle is " ,Area)
