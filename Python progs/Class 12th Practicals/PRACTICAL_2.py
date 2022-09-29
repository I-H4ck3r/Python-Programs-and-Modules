a = int(input("Enter a no."))
if a%4 == 0:
    if a%100 == 0 and a%400 != 0:
        print("n")
    else:
        print("y")
else:
    print("n")
