P=int(input("Enter Principle Amount:"))
R=int(input("Enter interest rate:"))
T=int(input("Enter time in years:"))
ci=P*pow((1+R/100),T)-P
print("COUMPOUND INTEREST:",ci)
