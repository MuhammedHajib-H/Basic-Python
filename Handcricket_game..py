import random


Comptr = random.randint(1,6)

## TOSS
print("TOSS TIME")
SumValue = None
Toss = input("Welcome to the toss, choose odd(o) or even(e):\n").lower()
TossNum = int(input(" choose a number for Toss 1 to 6:\n"))

if (TossNum>7 or TossNum<1):
    print("Invalid Input, ERROR 402 :(")
else:
    print(f"You chose {TossNum} \n computer chose {Comptr}")
    sumToss = TossNum + Comptr
    if (sumToss%2) == 0:
        SumValue = "e"
        print("It's even")
    else:
        SumValue = "o"   
        print("It's odd")


## PLAYER WON TOSS, CHOSE FOR BAT OR BOWL(EVEN/ODD)
if SumValue == Toss:
    Batbowl = input("Now.. Won the Toss, You Can choose bat(b) or bowl(a)").lower()
    ## PLAYER WON TOSS AND CHOOSES TO BAT
    ## 1ST INNINGS
    if Batbowl == "b":
        Balls = 100
        BallsBat = 0
        PlayerRuns = 0
        print("-----------------------------------\nYour batting\n")
        while BallsBat < Balls:
            Runs = int(input("Enter a number to bat: "))
            CompBowl = random.randint(1,6)
            
            if Runs==CompBowl:
                print(f"Your number is {Runs}, \n Computer's number is {CompBowl}")
                print(f"You are Out. \n Your total score is {PlayerRuns}\n")
                break
            elif Runs>=6:
                print("ERROR 408 :( , PLEASE TRY INPUTTING A NUMBER BELOW 7")
                continue
            else:
                PlayerRuns += Runs
                print(f"Your number: {Runs},\n  Computer's number: {CompBowl}")
                print(f"Your runs now are {PlayerRuns}\n")
            
            BallsBat += 1
            
        ## COMPUTER BATTING
        ## 2ND INNINGS
        print("-----------------------------------\nComputer batting\n")
        Balls2 = 100
        BallsBat2 = 0
        CompRuns2 = 0
        while BallsBat2 < Balls2:
            Bowl2 = int(input("Enter runs to bowl: "))
            CompBat2 = random.randint(1,6)
            
            if CompBat2 == Bowl2:
                print(f"Computer's number is {CompBat2},\n  Your number is {Bowl2}")
                print(f"Computer is Out. \n Computer's Total runs are {CompRuns2}")
                break
            else:
                CompRuns2 += CompBat2
                print(f"Computer's number is {CompBat2},\n  Your number is {Bowl2}")
                print(f"Computer's score is {CompRuns2}\n")
                
                if CompRuns2 > PlayerRuns:
                    break
            BallsBat2 += 1
            
        ## RESULTS
        print("-----------------------------------\nRESULTS: ")
            
        if CompRuns2 < PlayerRuns:
            print(f"\nYou have wow the game. \n\nYour total runs are {PlayerRuns} in {BallsBat} balls \n\n computer scored {CompRuns2} in {BallsBat2} bowls")
        elif CompRuns2 == PlayerRuns:
            print(f"The game is a tie,\n You score {PlayerRuns} \n  computer also scored {CompRuns2}")
        else:
            print(f"\nComputer won the game.\n\nComputer's total runs are {CompRuns2} in {BallsBat2} bowls,\n You score {PlayerRuns}")
    
    ## PLAYER WON TOSS AND CHOOSES TO BOWL
    ## 1ST INNINGS
    if Batbowl == "a":
        print("-----------------------------------\nComputer batting\n")
        Balls3 = 100
        BallsBat3 = 0
        CompRuns3 = 0
        while BallsBat3 < Balls3:
            Bowl3 = int(input("Enter runs to bowl: "))
            CompBat3 = random.randint(1,6)
           
            if CompBat3 == Bowl3:
                print(f"Computer's number is {CompBat3},\n Your number is {Bowl3}")
                print(f"Computer is Out.\n Computer's total runs are {CompRuns3}")
                break
            else:
                CompRuns3 += CompBat3
                print(f"Computer's number is {CompBat3},\n Your number is {Bowl3}")
                print(f"Computer's score is {CompRuns3}\n")
            BallsBat3 += 1
        
        ## PLAYER BATTING
        ## 2ND INNINGS
        Balls4 = 100
        BallsBat4 = 0
        PlayerRuns4 = 0
        print("-----------------------------------\nYour batting\n")
        while BallsBat4 < Balls4:
            Runs4 = int(input("Enter a number to bat: "))
            CompBowl4 = random.randint(1,6)
            
            if Runs4==CompBowl4:
                print(f"Your number is {PlayerRuns4},\n Computer's number is {CompBowl4}")
                print(f"You are Out.\n Your total score is {Runs4}\n")
                break
            elif Runs4>=6:
                print("ERROR 408 :( ---------INPUT A NUMBER BELOW 7")
                continue
            else:
                PlayerRuns4 += Runs4
                print(f"Your number: {Runs4},\n Computer's number: {CompBowl4}")
                print(f"Your runs now are {PlayerRuns4}\n")

                if PlayerRuns4 > CompRuns3:
                    break
            BallsBat4 += 1
        print("-----------------------------------\nRESULTS: ")
                
        if CompRuns3 < PlayerRuns4:
            print(f"\nYou have wown the game. \n\nYour total runs are {PlayerRuns4} and Bowls taken(Out of 100) are {BallsBat4}\n Computer's total runs are {CompRuns3}")
        elif CompRuns3 == PlayerRuns4:
            print(f"The game is a tie, \n You score {PlayerRuns4} \n computer also scored {CompRuns3}")
        else:
            print(f"\nComputer won the game.\n\nComputer's total runs are {CompRuns3} and in {BallsBat3} balls \n Your runs are {PlayerRuns4}")
## COMPUTER WON THE TOSS AND CHOOSES TO BAT      
else: 
    ## COMPUTER BATTING 
    ## 1ST INNINGS
    print("Computer has won the toss and it chooses to bat first\n")
    print("-----------------------------------\nComputer batting\n")
    Balls3 = 100
    BallsBat3 = 0
    CompRuns3 = 0
    while BallsBat3 < Balls3:
        Bowl3 = int(input("Enter runs to bowl: "))
        CompBat3 = random.randint(1,6)
        
        if CompBat3 == Bowl3:
            print(f"Computer's number is {CompBat3},\n Your number is {Bowl3}")
            print(f"Computer is Out. \n Computer's total runs are {CompRuns3}")
            break
        else:
            CompRuns3 += CompBat3
            print(f"Computer's number is {CompBat3},\n Your number is {Bowl3}")
            print(f"Computer's score is {CompRuns3}\n")
        BallsBat3 += 1
    
    ## COMPUTER BATTING
    ## 2ND INNINGS
    Balls4 = 100
    BallsBat4 = 0
    PlayerRuns4 = 0
    print("-----------------------------------\nYour batting\n")
    while BallsBat4 < Balls4:
        Runs4 = int(input("Enter a number to bat: "))
        CompBowl4 = random.randint(1,6)
        
        if Runs4==CompBowl4:
            print(f"Your number is {PlayerRuns4},\n  Computer's number is {CompBowl4}")
            print(f"You are Out. \n Your total score is {Runs4}\n")
            break
        elif Runs4>7:
            print("ERROR 408 :( , PLEASE TRY INPUTTING A NUMBER BELOW 7")
            continue
        else:
            PlayerRuns4 += Runs4
            print(f"Your number: {Runs4},\n  Computer's number: {CompBowl4}")
            print(f"Your runs now are {PlayerRuns4}\n")

            if PlayerRuns4 > CompRuns3:
                break
        BallsBat4 += 1
    print("-----------------------------------\nRESULTS: ")
            
    if CompRuns3 < PlayerRuns4:
        print(f"\nYou have wown the game. \n\nYour total runs are {PlayerRuns4} and Bowls taken(Out of 60) are {BallsBat4}\n Computer's total runs are {CompRuns3}")
    elif CompRuns3 == PlayerRuns4:
        print(f"The game is a tie,\n You score {PlayerRuns4} \n computer also scored {CompRuns3}")
    else:
        print(f"\nComputer won the game.\n\nComputer's total runs are {CompRuns3} and in {BallsBat3} balls \n your runs are {PlayerRuns4}")
        
input("Press any key to exit")