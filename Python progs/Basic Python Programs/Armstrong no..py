n = int(input("Enter a no."))
sum = 0
temp = n              #for while loop temp is given value of no inputed
while temp>0:         #until last digit 
    dig = temp % 10   #getting last digit from temp variable
    sum = sum + dig**3
    temp = temp//10   #removing last digit which already cubed and added in sum
if sum==n:
    print("Yes, It is an armstrong no.")