print("Please enter the following quantities.")

p = float(input("  "+"How much is the initial deposit? "))
r = float(input("  "+"What is the annual interest rate in percent? "))/100
n = int(input("  "+"How many times per year is the interest compounded? "))
t = float(input("  "+"How many years will the account be left to earn interest? "))

future_Value = p*((1+(r/n))**(n*t))

print(" ")
print(f"At the end of {t} years, " + f"the account will be worth ${future_Value:,.2f}.")
