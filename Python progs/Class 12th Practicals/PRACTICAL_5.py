#PROGRAM TO INPUT 10 VALUES IN A TUPLE AND DISPLAY ONLY THOSE VALUES OF TUPLE WHICH ARE DIVISIBLE BY 4

t1=int(input("Enter something:"))
t2=int(input("Enter something:"))
t3=int(input("Enter something:"))
t4=int(input("Enter something:"))
t5=int(input("Enter something:"))
t6=int(input("Enter something:"))
t7=int(input("Enter something:"))
t8=int(input("Enter something:"))
t9=int(input("Enter something:"))
t10=int(input("Enter something:"))
tup1=(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10)
print(tup1)
for i in tup1:
    if i%4==0:
        print(i)          
              
