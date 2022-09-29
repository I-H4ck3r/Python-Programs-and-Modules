n= int(input("Enter no till which you want series: "))
a,b = 0,1
print(a)
print(b)
for i in range(2,n):
    c = a+b
    a,b = b,c
    print(c)
    