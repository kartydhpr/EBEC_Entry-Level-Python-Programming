################################################################################
# Author: Karteikay Dhuper
# Date: 2/12/2021
# This program calculates the amount of discount
# based on number of items purchased
################################################################################

# declaration of variable that stores number of packages
numItems = int(input("Please input the number of packages to be purchased: "))

#conditional statement that checks if number of items is less than
#the minimum needed for a discount to be applied
if(0 <= numItems < 10):
    discount = 0
    print("  "+"No discount applied.")
    finalPrice = ( ( numItems*99 ) - ( (numItems * 99) * (discount) ) )
    print("  "+f"The final price for purchasing {numItems} packages is" + f" ${finalPrice:,.2f}.")

#conditional statement that checks if 10% discount can be applied
elif(10 <= numItems <= 19):
    discount = .10
    print("  "+"10% discount applied.")
    #variable that stores price after discount has been applied
    finalPrice = ( ( numItems*99 ) - ( (numItems * 99) * (discount) ) )
    print("  "+f"The final price for purchasing {numItems} packages is" + f" ${finalPrice:,.2f}.")

#conditional statement that checks if 25% discount can be applied
#only if condition for 10% wasn't met
elif(20 <= numItems <= 49):
    discount = .25
    print("  "+"25% discount applied.")
    #variable that stores price after discount has been applied
    finalPrice = ( ( numItems*99 ) - ( (numItems * 99) * (discount) ) )
    print("  "+f"The final price for purchasing {numItems} packages is" + f" ${finalPrice:,.2f}.")

#conditional statement that checks if 35% discount can be applied
#only if condition for 25% wasn't met
elif(50 <= numItems <= 99):
    discount = .35
    print("  "+"35% discount applied.")
    #variable that stores price after discount has been applied
    finalPrice = ( ( numItems*99 ) - ( (numItems * 99) * (discount) ) )
    print("  "+f"The final price for purchasing {numItems} packages is" + f" ${finalPrice:,.2f}.")

#conditional statement that checks if 45% discount can be applied
#only if condition for 35% wasn't met
elif(numItems >= 100):
    discount = .45
    print("  "+"45% discount applied.")
    #variable that stores price after discount has been applied
    finalPrice = ( ( numItems*99 ) - ( (numItems * 99) * (discount) ) )
    print("  "+f"The final price for purchasing {numItems} packages is" + f" ${finalPrice:,.2f}.")

# conditional statement that only gets called if input doesn't
# fall within range to receive discount
else:
    print("  "+"Invalid Input!")
