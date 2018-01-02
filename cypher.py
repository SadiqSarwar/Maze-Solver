#header file.
from time import sleep
import sys

#Create Cypher class.
class Cypher:
    
    #Create intro function.
    def intro(self):
        print("You have chosen 'Cypher' as your character")
        sleep(1.0)    #Pause code 1 seconds.
        print("Loading...")
        sleep(2.0)    #Pause code 2 seconds.
        print("The game will now begin! \n")

    #Create setScene function.
    def setScene(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("You are with Neo, Morpheus, and Trinity in a large building.")
        print("You have been ambushed by agents, and have hidden inside the bathroom walls")
        print("in attempt of escaping the agents.")
        print("Make the correct choices needed in order to escape the agents correctly. \n")

    #Create firstDecision function.
    def firstDecision(self):
        sleep(4.0)    #Pause code 4 seconds.
        print("----------------------------------Start------------------------------------")
        print("You guys slowly begin climbing down the walls, looking for an exit.")
        print("In the process, an agent approaches in suspicion.")
        print("             ,              ")
        print("        _.--` `--.          ")
        print("        |._ __{}_)          ")
        print("         |---.__\           ")
        print("        (   ^ _^            ")
        print("         |   _ |            ")
        print("         )\___/             ")
        print("     .---`:._]              ")
        print("     \      --.         \n  ")

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
        print("Morpheus accidentally trips on a piece of broken concrete.")
        print("The concrete dust falls down and hits on your face.")
        print("The dust starts tingling in your nose.\n")

        print("[Choices]")
        print("(1) Sneeze")
        print("(2) Try to hold in your sneeze.")

    #Create secondFail function.
    def secondFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You try to hold in your sneeze, so you don't make any noise")
        print("But the dust keeps tingling in your nose.")

    #Create thirdDecision function.
    def thirdDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You just cannot help it, and let out a powerful sneeze!")
        print("░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░░")
        print("░░░░░░▄▄█▀▀░░░░░░░░░░░░▀██▄▄▄▄▄░░░░░░")
        print("░░░░▄█▀░▄▄█▀▀▀▀░░░░░░░░░░░░▄█████▄░░░")
        print("░░▄█▀▄▄█▀░▄▀▀▀▀█▄░░░░░░░░▄▀▀░░▄██▄░░░")
        print("░▄▀░▀▀▀░▄▀░░░░░░░█░░░░░░█░░░░░▀▀░█░░░")
        print("░█░░░░░░█░▄▄▄░░░░█▄░░░░░█░░░░░░░▄█▄░░")
        print("█▀░░░░░▀█▄▀█▀░░░░█░░░░░░▀▄▄▄▄▄▄██▄█░░")
        print("█░░░░░░░░▀▀▄▄▄▄▄▀░░░░░░░░░▄▀░░▄▄░▀█▄░")
        print("█░░░░░░░░░░░░░░░░░░░░▄░▀▀█▀░█▀░▀▀▄░█░")
        print("█░░░░░░░░░░░░░░░░░░░░░░░█▀░█▀▀▀▀██░▀█")
        print("█░░░░░░░░░░░░░░░░░░░░░░░█░▄█▀▀▀▀▀███░")
        print("█░░░░░░░░░░░░░░░░░░░░░░░█░██░░░░░█░█░")
        print("▀█░░░░░░░░░░░░░░░░░░░░░░████░░░░█▀█▀░     _      _             _    ")
        print("░█░░░░░░░░░░░░░░░░░░░░░░███▀░░░░█░█░░    /_\  __| |_  ___  ___| |   ")
        print("░░█░░░░░░░░░░░░░░░░░░░░░█░█░░░░░█░░█░   / _ \/ _| ' \/ _ \/ _ \_|   ")
        print("░░▀▄░░░░░░░░░░░░░░░░░░░▄▀░█▀▀▀▄░▀▄░█░  /_/ \_\__|_||_\___/\___(_)   ")
        print("░░░▀▄░░░░░░░░░░░░▄▄░░░░█░░█▄▄▄▄█▄█░█░")
        print("░░░░▀▄░░░░░░░░░░░░░▀▀▄░█░░█▄██▀▄█░░█░")
        print("░░░░░▀█░░░░░░░░░░░░░░░▀█░░█▄░░▀█▀░▄▀░")

        sleep(1.0)    #Pause code 1 seconds.
        print("The agent hears you sneeze through the wall and immediately rushes over.")
        print("He figures out that you all are hiding in the wall and starts firing at it.")
        print("The bullets barely miss you.\n")
        
        print("[Choices]")
        print("(1) Continue climbing down and try to escape.")
        print("(2) Take out your gun and shoot back.")

    #Create thirdFail function.
    def thirdFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You take out your gun and start firing back at the enemy.")
        print("But the agents overwhlem you in fire power.")
        print("                                              ______                                               ")
        print("                                             |______|                                              ")           
        print("                            _                 |    |                                               ")
        print("                           | `-._             |    |                                               ")
        print("         __________________|_____`._______    /    /____________________________.-.____________    ")
        print("     __.`-------------------____----------`--/`._.`-----|                        o|            |   ")
        print("    ||                     (____)            |          | ======================  |____________|   ")
        print("    ||_______________________________________|__________| ======================  |                ")
        print("    '-._o                          o____(_)_____________| ============= ____..o---'                ")
        print("        `.           __0-------''-`          `---..--._(|_o______.-----`      `.O.`                ")
        print("          )     o  .' //       ||                                            __//__                ")
        print("         /        (   \\       ||                                           `------`               ")
        print("        /          \___________//        _____ _ _____ _ _____ _             |     |               ")
        print("       /         __/-----------`        |_   _/_\_   _/_\_   _/_\            |     |               ")
        print("    _./         (                         | |/ _ \| |/ _ \| |/ _ \           /     /               ")
        print("_.-`             )                        |_/_/ \_\_/_/ \_\_/_/ \_\         /     /                ")
        print("\\              (                                                          /     /                 ")
        print(" \\     _ o      )                                                       _/     /                  ")
        print("  \\_.-`        ( _                                                  _.-`   _.-`                   ")
        print("   (_____________)O)                                             _.-`   _.-`                       ") 
        print("                __\\__                                       _.-`   _.-`                           ")
        print("               `------`.                                 _.-`   _.-`                               ")
        print("                \      |                             _.-`   _.-`                                   ")                  
        print("                 \      \_                       _.-`   _.-`                                       ")
        print("                  `-._    `-._              __.-`   _.-`                                           ")
        print("                      `-._    `-.__.--===--`    _.-`                                               ") 
        print("                          `-._             \_.-`                                                   ")
        print("                              `-._.--=====-`                                                       ")
        print("You are shot multiple times all over the body.")
        print("You die immediately.")
        print("[Game Over]")

    #Create setScene function.
    def fourthDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You continue to to climb down, in hope that you could escape the agent.")
        print("But the agent comes and grabs Neo through the wall.")
        print("Morpheus jump out of the wall and attacks the agent, freeing Neo from the agents grasp.")
        print("Trinity tells you to leave Morpheus and escape with her and Neo.")
        print("The three of you leave and escape from the agents, planning to save Morpheus later.")
        print("Congradulations! You have won the game!")
        print("[Victory!]")
        

        

                           
        

    

    
        

    
    
   
        
        
        
    
