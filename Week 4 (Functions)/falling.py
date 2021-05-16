################################################################################
# Author: Karteikay Dhuper
# Date: March 3rd 2021
# Description: Program calcuates falling distance from 1 to 10 seconds
################################################################################

# Write function(s) here
def falling_distance(i):
    # logic for falling distance
    distance = (1/2)*(9.81)*(i)**2
    return distance

def main():
    # Write your 'mainline logic' here
    print("Time (s)  Distance (m)")
    print("----------------------")
    # nested for loop that iterates function
    for i in range(0,10):
        print(f"      {i+1:2d}", end = "        ")
        i+=1
        for j in range(i):
            #variable stores function output
            distance = falling_distance(i)
            print(f"{distance:6.2f}")
            break

if __name__ == '__main__':
    main()
