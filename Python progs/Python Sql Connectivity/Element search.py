flag = 0
l = [4,67,23,46,67]
item = int(input("Enter any number to be searched:"))
for i in range(0,len(l)):
    if item == l[i]:
        print(item,"is the number you searched","at index",i)
        flag = 1
        break
if flag == 1:
    print("The element is found at index",index)
else:
    print("Item not found.")

