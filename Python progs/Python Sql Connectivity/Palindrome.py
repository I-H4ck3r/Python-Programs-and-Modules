a = input("Enter a string: ")
for i in range(0,len(a)):
    if a[i] == a[-i-1]:
        pass
    else:
        print("not")
        break
else:
    print("palindrome")
    