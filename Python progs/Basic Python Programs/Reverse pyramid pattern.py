num=int(input("Enter the no. of rows:"))
for i in range(num,0,-1):
    for j in range(0,num,-i):
        print(end="")
    for j in range(0,i):
        print("*",end="")
    print()
    
