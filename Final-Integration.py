import time
import random


# Created a function for the game
def storyGame():
    # Jack Leser
    # A Mad-Libz Program where you can actually win
    # Intro to game and explanation
    print("Do you want to play the game? Type Y/N: ")
    yesOrNo = input("")
    # Made an if-else statement that takes an == relational operator
    # Made an if-elif-else statement
    if yesOrNo == "Y":
        print("Ok Let's Start!")
        time.sleep(2)
    elif yesOrNo == "N":
        print("Ok, Ending Game...")
        exit()
    else:
        print("We are going to start anyway")
        time.sleep(2)
    for x in range(1, 4):
        print(x)
        time.sleep(1)
    print("Mad-Libz!")
    print(
        "The game will prompt you to type a "
        "certain type of word, noun, verb, etc.\nyou will input those answers and we will create a funny story! ")
    time.sleep(3)
    # Example of how to play
    print("For example type an animal or object: ")
    animalExample = input("Type any animal or object: ")
    # Human Error Solution
    if animalExample == "" \
                        "":
        animalExample = input("Error: Type it again: ")
        if animalExample == "" \
                            "":
            print("Fine, have it your way")
        else:
            return

    else:
        animalExample = animalExample
    print("I own three " + animalExample + "'s")
    time.sleep(2)
    print(
        "Great, now we understand how it works,so while "
        "I figure out how to make a game with all my project requirements, have fun!")
    time.sleep(2)
    # Start of game
    # Setting variables:
    name = input("Type your name: ")
    # Human Error Solution
    if name == "" \
               "":
        randomNames = ["Luis", "Pedro", "Jack", "Haley", "Bert"]
        name = random.choice(randomNames)

    time.sleep(1)
    print("Wow what a unique name, " + name)
    time.sleep(1)
    placesToVisit = ["Nigeria", "Somalia", "North Korea", "Georgia"]
    city = input("What is a place you would never want to visit : ")
    # Human Error Solution
    if city == "" \
               "":
        city = random.choice(placesToVisit)
        print("I guess I will choose a place for you: " + city)

    else:
        return
    time.sleep(1)
    print("Wow Great Choice >:)")
    time.sleep(1)
    family = input("Type your least Favorite person: ")
    if family == "" \
                 "":
        print("You hate nobody?")
        time.sleep(1)
        family = input("Type someone you hate: ")
        if family == "" \
                     "":
            print("I guess I am going to choose your name! " + name + ".")
            family = name
        else:
            family = family
    else:
        return
    print("So the variables you chose: ", name, city, family, sep=' ')
    time.sleep(1)
    print("Hey " + name * 1 + " !")
    time.sleep(1)
    print(
        "We're going to your favorite place for vacation, " + city +
        "! You are going with the person you love the most! Yes it is, " + family + ".")
    time.sleep(2)
    # Now I am going to use the operators needed to create a story
    # Math Equation Variables Games
    # Story Plays out
    num1 = int(input("Type any number, dont worry it wont affect you! : "))
    num2 = int(input("Type a number lower than that number, dont worry it won't affect you: "))
    # Using if-else statement and >= sign
    firstProblem = num1 % num2
    time.sleep(2)
    print(
        "Ok so the vacation is off to a great start and you are so pumped to be  going to "
        + city + " with " + family + "!")
    # Explanation of where you are at in the game
    time.sleep(2)
    print("But now there are problems, you are:")
    time.sleep(2)
    print("1. Low on gas..")
    time.sleep(2)
    print("2. Only have $", firstProblem, " in your wallet..")
    time.sleep(2)
    print("3. In the middle of the place you actually hate the most!")
    # The Solution to the game
    time.sleep(2)
    print("All hope seems lost when you look around and you cant find " + family + ".")
    time.sleep(2)
    print(family + " comes back and gives you the ticket to a lottery ticket number he bought and guess what, YOU WON!")
    time.sleep(2)
    # Numeric Operators used
    winningLottery = (num1 * num2 - 1 + 4 ** 5)
    print("You won", winningLottery, "!")
    print("Not bad but just enough to get you home!")
    time.sleep(1)
    print("Do you want to go HOME or keep exploring " + city, "?")
    choice1 = input("type HOME or EXPLORE: ")
    if choice1 == "HOME":
        print("You went home, GAME OVER.")
        print("Thanks for playing with these variables: " + name, city, family, num1, num2, sep=',', end='')
        exit()
    elif choice1 == "EXPLORE":
        print("Time to explore")
        print("You traveled the country")
        print("You saw things you never thought you would, GOOD and BAD")
        print("Life almost seems to good to you right now")
        print("Choose a number: 1 or 2")
        choice2 = input("Choice: ")
        if choice2 == 1:
            print("You got a life sentence in", city, "jail.")
        elif choice2 == 2:
            print("You started a gang, making millions a year, you can never leave", city, ".")
        else:
            print("You went back home, enjoyed the memories you made, and went through life as you normally would.")
        print("Thanks for playing with these variables: " + name, city, family, num1, num2, sep=',', end='')

    else:
        print("You could not make a decision so I chose for you: HOME")
        print("Thanks for playing with these variables: " + name, city, family, num1, num2, sep=',', end='')
        exit()


storyGame()
