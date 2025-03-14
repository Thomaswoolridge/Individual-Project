import random
def boat():
    print(r"""     (`-,-,""")
    print(r"""     ('(_,( ) """)      
    print(r"""      _   `_' """)  
    print(r"""   __|_|__|_|_ """)  
    print(r""" _|___________|__ """)  
    print(r"""|o o o o o o o o/  """)  
    print(r"""~'`~'`~'`~'`~'`~'`~  """) 

def plane():
    print(r"""        _ """)
    print(r"""      -=\`\ """)      
    print(r"""  |\ ____\_\__ """)  
    print(r'''-=\c`""""""" "`) ''')  
    print(r"""   `~~~~~/ /~~` """)  
    print(r"""     -==/ / """)  
    print(r"""       '-' """)  

print("Welcome to Adventure: The Text Based Journey")

characterName = "Matt Missle"

print("You are the world famous explorer " + characterName + "!\nWould you like to change this name? y or n?")
userAnswer = input("> ")

if userAnswer == "y":
    print("What would you like your new name to be?")
    characterName = input("Enter new name here: ")
    print("Congratulations! You are now the less famous explorer " + characterName + "!")
else:
    print("I'm glad you like the name " + characterName + "!")

moneyOffer = 10000
print("You've been hired by a mysterious group of billionaires\nThey want you to find the ancient treasure of the jungle\nThey are willing to pay", moneyOffer, "\nWill you accept the challenge? y or n?")

correctAnswer ="y"
while True:
    userChoice = input("> ")
    if userChoice == correctAnswer:
        print("You really are the best!\nLet the adventure begin!")
        break
    else:
        moneyOffer = moneyOffer +10000
        print("Are you sure you won't accept the challenge?\nThey will pay "+ str(moneyOffer) +"!")

print("The journey is long and treacherous!\nWill you take your trip to the jungle by boat or by plane?")
validChoice = "boat", "plane"
while True:
    userVehicle = input("> ")
    if userVehicle == "boat":
        print("You have choosen to go by boat")
        boat()
        break
    elif userVehicle == "plane":
        print("You have chosen to go by plane")
        plane()
        break
    else:
        print("That is an invalid choice please try again")

print("You've finally made it to the jungle!\nYou see a cave ahead but not far beyond you see temple ruins.\nWill you enter the cave or the temple")

nextStep = input("> ")
if nextStep == "cave":
    print("It is very dark in the cave.\nWill you take a torch? y or n?")
    torchChoice = input("> ")
    if torchChoice == "y":
      print("The torch illuminates the inside of the cave.\nYou see something shiny deep inside but there is a cave lake seperating you from it.\nWill you swim across the water or climb across the wall? swim or climb")
      caveTrip = input("> ")
      if caveTrip == "swim":
          print("You got a little wet but made it across.\nCongratulations! You got the treasure!\nThe billionaires not only give you $" + str(moneyOffer) + ", they also let you keep the treasure")
          print("You fly back home!\nThanks for playing!")
          plane()
      elif caveTrip == "climb":
          print("You aren't as strong as you used to be and lost your grip!\nOh no! You fell in the water and don't have the energy to stay afloat." + characterName + ", you drowned. Game Over.")
      else:
          print("You decided to go back home because of the difficuly.\nThe billionaires are now hunting your for the rest of your life.\nGame Over.")
    elif torchChoice == "n":
        print("It is so dark you stumble around and fall into a 500ft. chasm.\n" + characterName + ", you did NOT survive.\nGAME OVER!" ) 
    else:
        print("You changed your mind and went home.\nThe billionaires are furious!\nYou get no money game over!")
elif nextStep == "temple":
    print("The temple ruins seems very unstable and dangerous.\nWill you wear a hardhat? y or n?")
    hardhatChoice = input("> ")
    if hardhatChoice == "y":
        moneyOffer = moneyOffer * 250
        print("You made a smart choice!\nDebris falls from the ceiling and hits your helmet.\nYou are just fine!\nYou have stumbled across the room with the treasure.\nCongratulations, you win!\nThe billionaires have paid you $" + str(moneyOffer) + "!")
        print("You take a ship back home.\nYou made it safely!")
        boat()
        print("Bonus Round!\nTake a chance to win more or lose it all!\nWill you take the chance? y or n?")
        bonusChoice = input("> ")
        if bonusChoice == "y":
            bonusOptions = ["You get a lot more treasure!", "You get even more money from the billionaires!", "You lose all the treasure and money!", "You wake up in your bed.\nThis was all just a dream.", "A witch transfroms you into a bunny!"]
            print(random.choice(bonusOptions))
        else:
            print("Ok, Thank you for playing anyway.\nYou get to keep the $" + str(moneyOffer) + " your earned and any treasure found!")


    elif hardhatChoice =="n":
        print("You just took a huge risk and it didn't pay off.\n A 50lb stone fell from the ceiling and hit you in the head.\nYour head is now a pancake.\nGame Over.")
    else:
        print("You decided not to risk your life and go home.\nThe billionaires aren't happy but you give them their money back.\n This is the happy ending game over.")
else:
    print("You changed your mind and went home.\nThe billionaires are furious!\nYou get no money game over!")

