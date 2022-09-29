#program to check whether a number is an armstrong number

#take input from the user
num=int(input("Enter a number:"))

#initialise sum
sum=0

#find the sumof the cube of each digit
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

#displat the result
if num==sum:
        print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
