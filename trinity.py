#header file.
from time import sleep
import sys

#Create Trinity class.
class Trinity:

    #Create intro function.
    def intro(self):
        print("You have chosen 'Trinity' as your character")
        sleep(1.0)    #Pause code 1 seconds.
        print("Loading...")
        sleep(2.0)    #Pause code 2 seconds.
        print("The game will now begin! \n")

    #Create setScene function.
    def setScene(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("You are with Neo, Morpheus, and Cypher in a large building.")
        print("You have been ambushed by agents, and have hidden inside the bathroom walls")
        print("in attempt of escaping the agents.")
        print("Make the correct choices needed in order to escape the agents correctly. \n")

    #Create firstDecision function.
    def firstDecision(self):
        sleep(4.0)    #Pause code 4 seconds.
        print("----------------------------------Start------------------------------------")
        print("You guys slowly begin climbing down the walls, looking for an exit.")
        print("In the process, an agent approaches in suspicion.\n")

        print("[Choices]")
        print("(1) Signal for everyone to be quiet")
        print("(2) Continue Climbing Downwards")

    #Create firstFail function.
    def firstFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("The agent hears you making noise in the walls as you are climbing down.")
        print("He start firing at the wall and the bullet pierces through, hitting you in the chest.")
        print("You die immediately.")
        print("[Game Over]")

    #Create secondDecision function.
    def secondDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("▓╬╬╬╬╬╬╬╬╬╬╬▓╬▓▓╬▓╫─┌┌┘┌┘┌┘┌┘┌┘┌╒┌╒┌┘┌┘─")
        print("▓╬╫┼┼╫╬╬╬╬╬╬╬╬╬▓╬▓┼────┌───┌─────┌─┌─┌─┌")
        print("╬╬╬╬╬╬╬╬▓▓▓▓▓▓▓▓▓▓╬──┌┘┌╒┘┘┌┘┌┘┌┘┌╒┘╒┌╒─")
        print("╬┼╬╬╬╬╬╬╬▓╬▓▓▓╬▓╬▓▓┌─┘┌┘┌┘┌┘─┘┌┘┌╒┌┘┌┘┌─")
        print("▓╬╬╫╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓╫──┘┌┘─┘─┘┌┘─┘─┘┌┘┌╒─")
        print("▓╬╫╫╫╬╬╬╬╬╬╬▓▓╬▓╬╬╬▓─┌─┘┌┘┌┘┌┘┌┘─┘┌┘┌┘┌┌")
        print("▓╬╬╬╬╬╬╫╫╬▓▓▓▓███▓▓▓╫─┌┌┘┌┘┌┘┌┘─┘─┘┌┘┌┘─")
        print("▓╬╬╬╬╫╫╬╬╬╬╬╬╬╬▓███▓╬┌─┘─┘─┘┌┘┌┘┌┘─┘─┘┌┌")
        print("▓╬╬╬╬┼┼┼┼┼╬╬╬▓▓▓▓██▓▓┌┌─┘─┘┌┘┌┘─┘─┌─┌─┘─")
        print("▓▓╬╬╬╬╫╬╬╬╬▓▓▓▓████▓▓┌─┌─┘┌┘┌┘─┌─┌─┌─┘─┌")
        print("█▓╬╬╬╬╬╬▓▓▓▓▓▓▓█████┼─┌─┘┌┘─┘┌┘─┌─┌─┌─┌─")
        print("▓▓╬╬╬╬▓▓▓▓▓█▓█████▓▓─┌─┘┌┘─┌─┌─┌─┌─┘─┌─┌")
        print("▓▓╬╬▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓──┌─┘┌┘─┌─┌─┌─┌─┌─┌─")
        print("▓▓╫╬▓▓▓▓▓███▓████▓╬▓╬──┌─┌─┘─┌─┌─┌─┘─┘┌┌")
        print("▓╬┼╫╬╬▓▓▓██████▓╬┼╫╬▓╒┌─┌─┘─┌─┌─┘─┌─┌─┌─")
        print("▓╬┼╫╬╬╬╬╫╬▓█████╬┼┼╬╬▓╒──┌─┘─┘─┌─┘─┌─┌─┌")
        print("▓╬┼┼╫╫╫╫╬╬╬▓▓██▓▓╬╫╫╬╬▓┼┌─┌─┘─┌─┘─┌─┌─┘─")
        print("▓▓┼╫╫╫╫╬╬╬╬╬╬▓▓▓▓╬╬╬╬╬╬▓┼──┌─┘─┘─┘─┘─┘──")
        print("▓▓╫╫╫╫╫╫╬╬╬╬╬╬▓▓▓╬╬╬╬╬╬╫▓╬┌─┌─┌─┌─┘─┘─┘─")
        print("▓▓╬╬╬╬╬╬╬╬╬▓▓▓▓▓▓▓╬▓╬╬╫┼┼╬╬──┌─┘─┌─┘─┌──")
        print("▓▓╬╬╬╬╬╬╬╬▓▓▓▓▓▓▓▓▓╬╫╫╬┼┼╬▓╬┌─┘─┘─┌─┘─┘─")
        print("▓▓╬▓▓▓▓▓▓▓▓▓▓▓▓▓╬▓▓╒┌┼┼╫╬╬▓▓───┌─┘─┌─┘──")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╒┼╬▓██▓█╬──┘─┘─┘─┘─┘─")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████╬┌─┌─┌─┘─┘─┌─┌")
        print("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓┌─┌───┌─┌─┌─┌─┌─")
        print("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬▓▓┼───┌┌──┘─┌─┌─┌──")
        print("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬▓╬──┼┼╒╫┘─┌─┌─┌─┌─")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬▓╬▓╬▓╫─╬╒─╬┼┌─┌─┌─┘─┌")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╫╬▓█╬╫┌┼▓┼─┌─┘─┌─┌─")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬▓╬╬╬▓███▓╬╬▓▓┘──┌─┘─┘─┌")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬▓▓████▓╬╬▓▓▓──┌─┌─┌─┌─")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬▓▓▓▓██▓█▓╬▓▓▓▓▓─┌─┌─┌─┌──")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬▓▓▓▓▓▓──┌─┘─┌─┌─")
        print("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬▓▓───┌─┌─┘──")
        print("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓╬╬▓╬┌─┌─┌─┌─┌─")
        print("██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓╬╬▓▓───┌─┌─┘─┌")
        print("████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██────▓▓╬╬▓▓┌─┌─┌─┌─┌─")
        print("██████▓▓▓▓▓▓▓▓▓▓▓▓██───╫▓▓▓▓▓▓─┌─┘─┘─┌──")
        print("████████▓▓▓▓▓▓▓▓▓▓█▓──┌╫▓▓▓▓▓▓────┌─┌─┌─")
        print("████████████▓▓▓▓▓▓█▓─┌─╫▓▓▓╬▓▓───┌───┌──")
        print("███████████████████────╫█▓╬╬▓╬─┘┼┌┌─┌─┌─")
        print("▓╬┼╒┘┼╫╬▓▓███████▓─────╬█▓╬╬▓╬╬▓▓▓╫──┌─┌")
        print("┌─┌─────┌─────╒┘──┌───┌╬█▓╬╬▓▓▓▓▓▓▓┌┌───")
        print("───────┌─┌───┌─┌───┌─┌─╬▓▓╬▓▓▓▓╬▓▓▓╫─┌─┌")
        print("┘─┘─┌─┌─┌─┌─┌─────┌────▓▓▓╬╬▓▓▓╬╬╬▓╬┌───")
        print("─┌─┌─┌───┌─┌─┌─┌─┌─┌───▓▓▓╬╬▓▓╬╬╬▓▓▓─┌──")
        print("┘─┌─┌───────┌─────┌─┌─▓▓▓▓╬╬▓▓╬╬╬╬▓▓┼─┌─")
        print("─┌─┌─┌─┌─┌─────┌─┌─┌──▓▓▓▓╬╬▓▓╬╬╬╬╬▓▓▓┼┌")
        print("┘─┌───┌─┌───┌─┌─┌───┌─▓▓▓▓╬╬▓╬╬╬▓╬╬╬▓▓▓╒")
        print("Everyone stops moving abruptly in fear of getting caught and stays silent.")
        print("Dust surrounds everyone as Morpheus accidentally steps on loose cement.")
        print("Cypher accidentley sneezes from all the dust")
        print("The Agent hears Cypher sneeze, and starts looking towards the bathroom walls.")
        print("Your location has been compromised .")
        print("Agents starts shooting at the wall")
        print("The bullets barely miss you\n")

        print("[Choices]")
        print("(1) climb down and get out of range.")
        print("(2) Get out of the wall and fight back.")

    #Create secondFail function.
    def secondFail(self):
        sleep(1.0)   #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You jump out of the wall in attempt of fighting back.")
        print("But you are surrounded by agents and are overwhlemed by gunfire.")
        print("You are immediately shot to death by multiple bullets.")
        print("[Game Over]")

    #Create thirdDecision function.
    def thirdDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You climb down lower and get out of danger.")
        print("Morpheus jumps out of the wall and fights the agents to give you cover")
        print("You try to look for an escape and see two available options.")
        print("One of which is a trapdoor, while the other is a tunnel.\n")

        
        print("[Choices]")
        print("(1) Escape using the trapdoor.")
        print("     /\ ")
        print("    / / ")
        print("   / /| ")
        print("  / /,^%---_ ")
        print("  \/_<__\___\ ")
        print('')
        print("(2) Escape using the tunnel.")
        print("""       _   _
    =/       \=
  =/   ^   ^   \=
 =/   ^     ^   \=
  =\   ^   ^   /=
   =\    ^    /=
    =\       /=
       ~   ~
""")
        
    #Create thirdFail function.
    def thirdFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You decide that you want to take the tunnel as an escape route.")
        print("You start running towards the tunnel and direct everyone else to follow you to safety.")
        print("But suddenly more agents come from the tunnel exit and surround all of you.")
        print("They unleash a load of heavy gun fire and decimate you all to a pile of death.")
        print("[Game Over]")

    #Create fourthDecision function.
    def fourthDecision(self):
        print("You run towards the trapdoor and direct everyone to follow you.")
        print("You reach the trapdoor safely and escape with Neo and Cypher.")
        print("The three of you leave and escape from the agents, planning to save Morpheus later.")
        print("Congradulations! You have won the game!")
        print("[Victory!]\n")
        
        

        
        
        

                           
        

    

    
        

    
    
   
        
        
        
    
