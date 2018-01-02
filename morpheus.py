#header file.
from time import sleep
import sys

#Create Morpheus class.
class Morpheus:

    #Create intro function.
    def intro(self):
        print("You have chosen 'Morpheus' as your character")
        sleep(1.0)    #Pause code 1 seconds.
        print("Loading...")
        sleep(2.0)    #Pause code 2 seconds.
        print("The game will now begin! \n")

    #Create setScene function.
    def setScene(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("You are with Neo, Cypher, and Trinity in a large building.")
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
        print("(1) Stop Moving")
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
        print("Everyone stops moving abruptly in fear of getting caught.")
        print("You hear the agent walk away.")
        print("You can either motion for them to move down or climb back up.\n")
        
        print("[Choices]")
        print("(1) Motion for everyone to move down")
        print("(2) Climb back up the shaft.")

    #Create secondFail function.
    def secondFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You all start moving up the wall. ")
        print("You trip and fall on everyone falling to your inevitable death.")
        print("[Game Over]")

    #Create thirdDecision function.
    def thirdDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("All of a sudden Cypher sneezes alerting the Agent")
        print("    ||||||||||||||")
        print("   =              \       ,")
        print("   =               |")
        print("  _=            ___/")
        print(" / _\           (o)\"")
        print("| | \            _  \"")
        print("| |/            (____)")
        print(" \__/          /   |")
        print("  /           /  ___)")
        print(" /    \       \    _)                       )")
        print("\      \           /                       (")
        print("\/ \      \_________/   |\_________________,_ )")
        print(" \/ \      /            |     ==== _______)__)")
        print("\/ \    /           __/___  ====_/")
        print(" \/ \  /           (O____)\\_(_/")
        print("                  (O_ ____)")
        print("                   (O____)")

        print("The agent begins firing through the wall")
        print("You can either jump through the wall and attack or cower in fear\n")
        
        print("[Choices]")
        print("(1) Cower in fear")
        print("(2) Jump through wall")

    #Create thirdFail function.
    def thirdFail(self):
        print("---------------------------------------------------------------------------")
        print(""" @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@""")
        print("You got shot and killed.")
        print("[Game Over]")

    #Create fourthDecision function.
    def fourthDecision(self):
        print("---------------------------------------------------------------------------")
        print('')
    

    
        

    
    
   
        
        
        
    
