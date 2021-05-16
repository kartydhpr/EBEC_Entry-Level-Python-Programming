numCookies = int(input("How many cookies do you want to make? "))

sugarNeeded = numCookies / 32
butterNeeded = numCookies /48
flourNeeded = numCookies /17.4545

print(f"To make {numCookies} cookies, you will need:")
print(f"{sugarNeeded:7.2f} cups of sugar")
print(f"{butterNeeded:7.2f} cups of butter")
print(f"{flourNeeded:7.2f} cups of flour")
