#header file.
#importing character files of the game.
import sys
from time import sleep
from check import Check
from cypher import Cypher
from trinity import Trinity
from agent import Agent
from morpheus import Morpheus
from title import Title
from end import End

#Linking the other files by creating objects.
#Creating a linker to access the other files through a new variable name.
charCypher = Cypher()
charTrinity = Trinity()
charAgent = Agent()
charMorpheus = Morpheus()
setTitle = Title()
setEnd = End()
valCheck = Check()

#Define and call the main function.
def main():
    #call the GameTitle function through the Title class.
    setTitle.GameTitle()
    print('')
    #Introduce the game and player options.
    print("Welcome to the Matrix Game.")
    print("Pick a character and play through his/her point of view.")
    print("Make the correct decisions in order to play through and triumph.\n")

    #Define and call the game function.
    def game():
        #Introduce the user with a set of playable characters.
        print('')
        print("Characters: ")
        print("1.Morpheus")
        print("2.Agent")
        print("3.Trinity")
        print("4.Cypher\n")
        #Prompt user for which character he/she wants to play as. 
        userInput = input("Please enter the number of the character you would like to play as [Enter 0 to Quit]: ")
        #Call the ValCheck class to check Input Validation.
        valCheck.setValue(userInput)
        userInput = valCheck.checkValue(userInput)
        userInput = str(userInput)
        #Call the Morpheus class if user enters the number "1".
        if (userInput == "1"):
            charMorpheus.intro()    #Call the Intro function within the Morpheus Class.
            charMorpheus.setScene()    #Call the setScene function within the Morpheus Class.
            charMorpheus.firstDecision()    #Call the firstDecision function within the Morpheus Class.
            userInput = input("What would you like to do?: ")    #Prompt user which decision they want to make.
            #Call the ValCheck class to check Input Validation.
            valCheck.setValue(userInput)
            userInput = valCheck.checkValue(userInput)
            userInput = str(userInput)
            if (userInput == "1"):
                charMorpheus.secondDecision()    #Call the secondDecision function within the Morpheus Class.
                userInput = input("What would you like to do?: ")
                #Call the ValCheck class to check Input Validation.
                valCheck.setValue(userInput)
                userInput = valCheck.checkValue(userInput)
                userInput = str(userInput)
                if (userInput == "1"):
                    charMorpheus.thirdDecision()    #Call the thirdDecision function within the Morpheus Class.
                    userInput = input("What would you like to do?: ")
                    #Call the ValCheck class to check Input Validation.
                    valCheck.setValue(userInput)
                    userInput = valCheck.checkValue(userInput)
                    userInput = str(userInput)
                    if (userInput == "1"):
                        charMorpheus.thirdFail()    #Call the thirdFail function within the Morpheus Class.
                        sleep(3.0)    #Pause code 3 seconds.
                        print("---------------------------------------------------------------------------")
                        print("Game will now restart.\n")
                        game() 
                    elif (userInput == "2"):
                        charMorpheus.fourthDecision()    #Call the fourthDecision function within the Morpheus Class.
                        sleep(1.0)    #Pause code 1 seconds.
                        setEnd.GameEnd()    #Call the GameEnd function within the setEnd Class.
                        game()    #Call the game function to restart the game.
                elif (userInput == "2"):
                    charMorpheus.secondFail()    #Call the secondFail function within the Morpheus Class.
                    sleep(3.0)    #Pause code 3 seconds.
                    print("---------------------------------------------------------------------------")
                    print("Game will now restart.\n")
                    game()    #Call the game function to restart the game.
            elif (userInput == "2"):
                charMorpheus.firstFail()    #Call the firstFail function within the Morpheus Class.
                sleep(3.0)    #Pause code 3 seconds.
                print("---------------------------------------------------------------------------")
                print("Game will now restart.\n")
                game()    #Call the game function to restart the game.

        #Call the Agent class if user enters the number "2".
        elif (userInput == "2"):
            charAgent.intro()    #Call the Intro function within the Agent Class.
            charAgent.setScene()    #Call the setScene function within the Agent Class.
            charAgent.firstDecision()    #Call the firstDecision function within the Agent Class.
            userInput = input("What would you like to do?: ")    #Prompt user which decision they want to make.
            #Call the ValCheck class to check Input Validation.
            valCheck.setValue(userInput)
            userInput = valCheck.checkValue(userInput)
            userInput = str(userInput)
            if (userInput == "2"):
                charAgent.secondDecision()    #Call the secondDecision function within the Agent Class.
                userInput = input("What would you like to do?: ")
                #Call the ValCheck class to check Input Validation.
                valCheck.setValue(userInput)
                userInput = valCheck.checkValue(userInput)
                userInput = str(userInput)
                if (userInput == "1"):
                    charAgent.thirdDecision()    #Call the thirdDecision function within the Agent Class.
                    userInput = input("What would you like to do?: ")
                    #Call the ValCheck class to check Input Validation.
                    valCheck.setValue(userInput)
                    userInput = valCheck.checkValue(userInput)
                    userInput = str(userInput)
                    if (userInput == "1"):
                        charAgent.fourthDecision()    #Call the fourthDecision function within the Agent Class.
                        userInput = input("What would you like to do?: ")
                        #Call the ValCheck class to check Input Validation.
                        valCheck.setValue(userInput)
                        userInput = valCheck.checkValue(userInput)
                        userInput = str(userInput)
                        if (userInput == "1"):
                            charAgent.fourthFail() #Call the fourthFail function within the Agent Class.
                            sleep(3.0)
                            print("---------------------------------------------------------------------------")
                            print("Game will now restart.\n")
                            game()    #Call the game function to restart the game.
                        elif (userInput == "2"):
                            charAgent.fifthDecision()    #Call the fifthDecision function within the Agent Class.
                            setEnd.GameEnd()    #Call the GameEnd function within the setEnd Class.
                    elif (userInput == "2"):
                        charAgent.thirdFail()    #Call the thirdFail function within the Agent Class.
                        sleep(3.0)    #Pause code 3 seconds.
                        print("---------------------------------------------------------------------------")
                        print("Game will now restart.\n")
                        game()    #Call the game function to restart the game.
                elif (userInput == "2"):
                    charAgent.secondFail()    #Call the secondFail function within the Agent Class.
                    sleep(3.0)    #Pause code 3 seconds. 
                    print("---------------------------------------------------------------------------")
                    print("Game will now restart.\n")
                    game()    #Call the game function to restart the game.
            elif (userInput == "1"):
                charAgent.firstFail()    #Call the firstFail function within the Agent Class.
                sleep(3.0)    #Pause code 3 seconds.
                print("---------------------------------------------------------------------------")
                print("Game will now restart.\n")
                game()    #Call the game function to restart the game.
            else:
                print("Incorrect Decision")

        #Call the Trinity class if user enters the number "3"
        elif (userInput == "3"):
            charTrinity.intro()    #Call the Intro function within the Trinity Class.
            charTrinity.setScene()    #Call the setScene function within the Trinity Class.
            charTrinity.firstDecision()    #Call the firstDecision function within the Trinity Class.
            userInput = input("What would you like to do?: ")
            #Call the ValCheck class to check Input Validation.
            valCheck.setValue(userInput)
            userInput = valCheck.checkValue(userInput)
            userInput = str(userInput)
            if (userInput == "1"):
                charTrinity.secondDecision()    #Call the secondDecision function within the Trinity Class.
                userInput = input("What would you like to do?: ")
                #Call the ValCheck class to check Input Validation.
                valCheck.setValue(userInput)
                userInput = valCheck.checkValue(userInput)
                userInput = str(userInput)
                if (userInput == "1"):
                    charTrinity.thirdDecision()    #Call the thirdDecision function within the Trinity Class.
                    userInput = input("What would you like to do?: ")
                    #Call the ValCheck class to check Input Validation.
                    valCheck.setValue(userInput)
                    userInput = valCheck.checkValue(userInput)
                    userInput = str(userInput)
                    if (userInput == "1"):
                        charTrinity.fourthDecision()    #Call the fourthDecision function within the Trinity Class.
                        setEnd.GameEnd()    #Call the GameEnd function within the setEnd Class.
                    elif (userInput == "2"):
                        charTrinity.thirdFail()    #Call the thirdFail function within the Trinity Class.
                        sleep(3.0)    #Pause code 3 seconds.
                        print("---------------------------------------------------------------------------")
                        print("Game will now restart.\n")
                        game()    #Call the game function to restart the game.
                elif (userInput == "2"):
                    charTrinity.secondFail()    #Call the secondFail function within the Trinity Class.
                    sleep(3.0)    #Pause code 3 seconds.
                    print("---------------------------------------------------------------------------")
                    print("Game will now restart.\n")
                    game()    #Call the game function to restart the game.
            elif (userInput == "2"):
                charTrinity.firstFail()    #Call the firstFail function within the Trinity Class.
                sleep(3.0)    #Pause code 3 seconds.
                print("---------------------------------------------------------------------------")
                print("Game will now restart.\n")
                game()    #Call the game function to restart the game.
            else:
                print("Incorrect Decision")

        #Call Cypher class if user enters the number "4"               
        elif (userInput == "4"):
            charCypher.intro()    #Call the Intro function within the Cypher Class.
            charCypher.setScene()    #Call the setScene function within the Cypher Class.
            charCypher.firstDecision()    #Call the firstDecision function within the Cypher Class.
            userInput = input("What would you like to do?: ")
            #Call the ValCheck class to check Input Validation.
            valCheck.setValue(userInput)
            userInput = valCheck.checkValue(userInput)
            userInput = str(userInput)
            if (userInput == "1"):
                charCypher.secondDecision()    #Call the secondDecision function within the Cypher Class.
                userInput = input("What would you like to do?: ")
                #Call the ValCheck class to check Input Validation.
                valCheck.setValue(userInput)
                userInput = valCheck.checkValue(userInput)
                userInput = str(userInput)
                if (userInput == "1"):
                    charCypher.thirdDecision()    #Call the thirdDecision function within the Cypher Class.
                    userInput = input("What would you like to do?: ")
                    #Call the ValCheck class to check Input Validation.
                    valCheck.setValue(userInput)
                    userInput = valCheck.checkValue(userInput)
                    userInput = str(userInput)
                    if (userInput == "1"):
                        charCypher.fourthDecision()    #Call the fourthDecision function within the Cypher Class.
                        setEnd.GameEnd()    #Call the GameEnd function within the setEnd Class.
                    elif (userInput == "2"):
                        charCypher.thirdFail()    #Call the thirdFail function within the Cypher Class.
                        sleep(3.0)    #Pause code 3 seconds.
                        print("---------------------------------------------------------------------------")
                        print("Game will now restart.\n")
                        game()    #Call the game function to restart the game.
                elif (userInput == "2"):
                    charCypher.secondFail()    #Call the secondFail function within the Cypher Class.
                    charCypher.thirdDecision()    #Call the thirdFail function within the Cypher Class.
                    userInput = input("What would you like to do?: ")
                    #Call the ValCheck class to check Input Validation.
                    valCheck.setValue(userInput)
                    userInput = valCheck.checkValue(userInput)
                    userInput = str(userInput)
                    if (userInput == "1"):
                        charCypher.fourthDecision()    #Call the fourthDecision function within the Cypher Class.
                        setEnd.GameEnd()    #Call the GameEnd function within the setEnd Class.
                    elif (userInput == "2"):
                        charCypher.thirdFail()    #Call the thirdFail function within the Cypher Class.
                        sleep(3.0)    #Pause code 3 seconds.
                        print("---------------------------------------------------------------------------")
                        print("Game will now restart.\n")
                        game()    #Call the game function to restart the game.
            elif (userInput == "2"):
                charCypher.firstFail()    #Call the firstFail function within the Cypher Class.
                sleep(3.0)    #Pause code 3 seconds.
                print("---------------------------------------------------------------------------")
                print("Game will now restart.\n")
                game()    #Call the game function to restart the game.
            else:
                print("Incorrect Decision")

        #Display exit message and close the game if user enters the number "0"
        elif (userInput == "0"):
            print("Thank You for playing the Matrix game. We hope you enjoyed! :D")
            exit()    #Exit the program.
            
            
    game()            
        
            
main()
