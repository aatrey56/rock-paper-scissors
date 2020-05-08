import random


def intro_paragraph(): #funtion for the introduction separate from the game
    print("Hello, my name is Aatrey and today you will be joining me on a wonderful adventure through the world of rock paper scissors.")
    print("To play, enter rock for rock, which beats scissors, paper for paper, which beats rock, or scissors for scissors, which beats paper. If you enter anything else it won't work.")


def rock_paper_scissors(): #Function for the game
    i = 0

    while i == 0: #loops until user does not select yes when asked to play again
        UA = raw_input("Rock, paper, or scissors?")
        CA = random.randint(0,2)
        if (UA == "rock" and CA == 0):  #Conditionals of computer and user choices
            print("Computer chose rock.\nYou tied")
        elif (UA == "rock" and CA == 1):
            print("Computer chose paper.\nL")
        elif (UA == "rock" and CA == 2):
            print("Computer chose scissors.\nW")
        elif (UA == "paper" and CA == 0):
            print("Computer chose rock.\nW")
        elif (UA == "paper" and CA == 1):
            print("Computer chose paper.\nYou tied")
        elif (UA == "paper" and CA == 2):
            print("Computer chose scissors.\nL")
        elif (UA == "scissors" and CA == 0):
            print("Computer chose rock.\nL")
        elif (UA == "scissors" and CA == 1):
            print("Computer chose paper.\nW")
        elif (UA == "scissors" and CA == 2):
            print("Computer chose scissors.\nYou tied")
        else:
            print("Invalid")


        ask = raw_input("Play again?") #Asks to play again

        if(ask.lower == "yes"):
            i = 0 #Loops the program until user doesn't want to play again
        else:
            print("bye")
            i+=1 #makes while statement false since i would equal 1 not 0


def main(): #Function combining intro and game
    intro_paragraph()
    rock_paper_scissors()


if __name__ == '__main__':
    main()
