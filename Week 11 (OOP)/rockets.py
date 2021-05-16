################################################################################
# Author: Karteikay Dhuper
# Date: April 24th 2021
# Description This program displays the amount of money it costs everytime 5
# different rockets are launched.
################################################################################

class Rocket: # parent class

    def __init__ (self, name, booster_cost, upper_stage_cost, fuel_cost): # constructor method deals with variable instantiation
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost

    def cost_per_launch(self):
        launchCost = (self.booster_cost)+(self.upper_stage_cost)+(self.fuel_cost) # calculation for a singlular launch
        return launchCost

class ReusableRocket( Rocket ): # child class

    def __init__ (self, name, booster_cost, upper_stage_cost, fuel_cost, uses):
        Rocket.__init__(self, name, booster_cost, upper_stage_cost, fuel_cost) # invokes the __init__ of the parent class
        self.uses = uses #initializes the additional "uses" variable in this child class

    def cost_per_launch(self): # overrides "Rocket's" cost_per_launch method by including "uses" into the calculation
        reuseableCostPerLaunch = (self.booster_cost / self.uses) + (self.upper_stage_cost)+(self.fuel_cost) # calculation for a launch taking amount of "uses" into account
        return reuseableCostPerLaunch


def main(): # main function

    # creating object instances of the ReusableRocket child class
    Atlas_V = ReusableRocket("Atlas V", 65.4, 42.6, 0.23, 1)
    Ariane_5 = ReusableRocket("Ariane 5", 83.5, 55.6, 0.69, 1)
    Long_March_3B = ReusableRocket("Long March 3B", 28.5, 19.0, 2.38, 1)
    Soyuz_2 = ReusableRocket("Soyuz 2", 20.9, 13.9, 0.24, 1)
    Falcon_9 = ReusableRocket("Falcon 9", 43.0, 18.6, 0.45, 10)

    # print statements
    print(f"This Atlas V cost ${Atlas_V.cost_per_launch()} million per launch.")
    print(f"This Ariane 5 cost ${Ariane_5.cost_per_launch()} million per launch.")
    print(f"This Long March 3B cost ${Long_March_3B.cost_per_launch()} million per launch.")
    print(f"This Soyuz 2 cost ${Soyuz_2.cost_per_launch()} million per launch.")
    print(f"This Falcon 9 cost ${Falcon_9.cost_per_launch()} million per launch.")


if __name__ == '__main__':
    main()
