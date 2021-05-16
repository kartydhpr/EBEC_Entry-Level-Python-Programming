################################################################################
# Author: Karteikay Dhuper
# Date: April 18th 2021
# Description This program generates a pie chart of monthly sales from data
# provided by the user.
################################################################################
import matplotlib.pyplot as plt

def main():

    monthList = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    sales_list = []

    for month in range(len(monthList)): # iterates through monthList
        montly_sale = int(input(f"Enter the sales for {monthList[month]}: ")) # asks for user input for month in iteration
        sales_list.append(montly_sale) # adds it to list with all sales values

    # stores Purdue's "secondary color palatte"
    colorList = ('#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A')

    # plotting instructions
    fig, ax = plt.subplots()  # initializes plot
    ax.set_title("Monthly Sales Values") #gives it a title
    ax.pie(sales_list, colors = colorList, labels = monthList) # specifies pie chart with color and label values

if __name__ == '__main__':
    main()
    plt.show()
