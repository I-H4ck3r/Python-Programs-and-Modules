i=0
m={}
while i<5:
    A=input("Enter the student name:")
    B=int(input("Enter roll no.:"))
    C=int(input("Enter age:"))
    m[B]=(A,C)
    i+=1
print("Dictionary is")
print(m)
