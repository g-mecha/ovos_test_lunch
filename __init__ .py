print("hello world")

def Question():
    print ("You are hungry, what do you want to eat?")

    userInput = input().lower()
    if (userInput == "pizza"): print("You got a pizza")
    elif (userInput == "hamburger"): print("You got a hamburger")
    else: 
        print("You don't feel like eating that")
        Question()

Question()