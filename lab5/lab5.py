import random

def print_intro():
    print("Welcome to Camel!") 
    print("In your desperation, you have stolen a camel to make your way \nacross the great Mobi Desert.")
    print("The locals want their camel back and are chasing you down!")
    print("Survive your desert trek and run out the locals.")

def main():
    print_intro()

if __name__ == "__main__":
    main()
# Variables
done = False
milesTraveled = 0
nativesTraveled = -20
camelTiredness = 0
thirst = 0
canteen = 3
oasis = -1

#Game loop

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check")
    print("Q. Quit.")
    print()


    # users input
    user_choice = input("What will you do? ")

    # check if they quit
    if user_choice.upper() == "Q" :
        done = True
    # updated game status
    elif user_choice.upper() == "E" :
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteen)
        print("The natives are", milesTraveled - nativesTraveled, "miles behind you.")
        print()
    # stop for the night
    elif user_choice.upper() == "D" : 
        print("You stop for the night.")
        print("Your camel is happy.")
        print("The natives don't stop.")
        print()
        camelTiredness = 0
        nativesTraveled += random.randrange(7, 14)
    # full speed ahead
    elif user_choice.upper() == "C" :
        miles = random.randrange(10, 20)
        milesTraveled += miles
        thirst += 1
        camelTiredness += random.randrange(1, 3)
        nativesTraveled += random.randrange(7, 14)
        oasis = random.randrange(20)
        if oasis == 10 :
            thirst = 0
            camelTiredness = 0
            canteen = 3
            print("As you travel you happen upon an oasis!")
            print("You fill your canteen and your stomach with water, and")
            print("Your camel is rested!")
            print("The natives continue the chase.")
            print()
        else :
            print("You push onward at full speed, moving a total of", miles, "miles")
            print("Your thirst increases")
            print("The natives continue the chase.")
            print()
    # mid-speed ahead
    elif user_choice.upper() == "B" :
        miles = random.randrange(5, 12)
        milesTraveled += miles
        thirst += 1
        camelTiredness += 1
        nativesTraveled += random.randrange(7, 14)
        oasis = random.randrange(20)
        if oasis == 10:
            thirst = 0
            camelTiredness = 0
            canteen = 3
            print("As you travel you happen upon an oasis")
            print("You fill your canteen and your stomach with water, and")
            print("Your camel is rested!")
            print("The natives continue the chase")
            print()
        else :
            print("You move forward, moving a total of", miles, "miles")
            print("Your thirst increases")
            print("The natives continue the chase")
            print()
    # drink from canteen
    elif user_choice.upper() == "A" :
        if canteen > 0 :
            canteen -= 1
            thirst = 0
            print("You take a drink")
        else:
            print("Your canteen is empty. You imagine yourself as a lifeless, dry husk.")
    
    # Status update
    #Thirst
    if thirst > 5:
        print("You died of thirst")
        print("Game over.")
        print()
        done == True
    elif thirst > 4 :
        print("You are thirsty!")
    # Distance travled / win check
    if milesTraveled >= 200:
        print("Congratulations! You have crossesd the entire desert!")
        print("You win")
        print()
        done == True
    # camel tiredness
    if camelTiredness > 8 :
        print("Your camel died of exhaustion!")
        print("With no camel, the natives catch up to you and kill you")
        print("on the spot.")
        print("Game over")
        print()
        done == True
    elif camelTiredness > 5 :
        print("Your camel is tired")
        print()
    #natives distance from you
    if milesTraveled - nativesTraveled <= 0 :
        print("The natives have caught up with you!")
        print("They kill you on the spot, and take their camel back.")
        print("Game over")
        print()
        done == True
    elif milesTraveled - nativesTraveled < 15 :
        print("You see faint shapes on the horizon behind you.")
        print("The natives are getting close!")
        print()
print("Exiting Game. Goodbye.")
input("")