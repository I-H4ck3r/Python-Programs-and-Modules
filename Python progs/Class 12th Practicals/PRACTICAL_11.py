#PROGRAM TO SEARCH FOR AN ELEMENT IN A GIVEN LIST OF NUMBERS

lst=eval(input("Enter List:"))
length=len(lst)
element=int(input("Enter element to be searched for:"))
for i in range(0,length):
    if element==lst[i]:
        print(element,"found at index",i)
        break
else:
    print(element,"not found in the list")
