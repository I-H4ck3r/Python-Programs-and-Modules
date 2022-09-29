# Python Program to Remove Odd Index Characters in a String
 
str1 = input("Please Enter a String : ")

str2 = ''

for i in range(len(str1)):
    if(i % 2 == 0):
        str2 = str2 + str1[i]
        
print("Original String :  ", str1)
print("Final String :     ", str2)
