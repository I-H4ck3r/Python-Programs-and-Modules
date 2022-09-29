#PROGRAM TO SHIFT ALL THE ZEROES TO RIGHT AND ALL THE NON ZERO NUMBERS TO LEFT OF THE LIST

lst=eval(input("Enter list:"))
length=len(lst)
end=length-1
print("original list:",lst)
i=0
while(i<=end):
    ele=lst[i]
    if ele==0:
        for j in range(i,end):
            lst[j]=lst[j+1]
        else:
            lst[end]=0
            end-=1
    if lst[i]!=0:
        i+=1
print("Zero shifted:",lst)
    
