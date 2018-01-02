#This Class is for Input Validation.
class Check:
    #Declare the constructor(Initializes the attribute).
    #def __int__(self, ): This is the Syntax for the Constructor.
    def __int__(self,userInput):
        #Pass by value from main()
        self.userInput = userInput
    #Make Sure the Quantiy is Checked from main()
    def setValue(self, userInput):
        self.userInput = userInput
        
    #Input Validation(Negative Numbers).
    #Self creates the object.
    def checkValue(self, userInput):
        counter = 0
        while True:
            try:
                if counter < 1:
                    userInput = self.userInput
                    newValue = int(userInput)
                else:
                    newValue = int(input("Please re-enter the number of your decision: "))
                while newValue < 0:
                    print("Invalid Input [No Negative Numbers]")
                    newValue = int(input("Please re-enter the number of your decision: "))
            except ValueError:
                #Reset to the if Statement.
                counter = counter + 1
                print("Invalid Input [Must Enter Numbers]")
                continue
            else:
                break
        return (newValue)
