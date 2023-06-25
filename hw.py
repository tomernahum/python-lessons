
def v1():
    min = 9999
    max = -9999
    while True:
        inputString = input("enter integer or done to finish: ")
        if inputString == "done":
            print("Exciting loop!")
            break
        
        #------

        try:
            inputNum = int(inputString)
        except:
            print("You have to enter either an integer or done")
            continue

        # now we know everythings valid

        if inputNum < min:
            min = inputNum
        if inputNum > max:
            max = inputNum
        
    print("minimum: "+ str(min) + ", maximum: " + str(max))

def v2():
    min = None
    max = None
    while True:
        inputString = input("enter integer or done to finish: ")
        
        if inputString == "done":
            print("Exciting loop!")
            break
        
        try:
            inputNum = int(inputString)
        except:
            print("You have to enter either an integer or done")
            continue


        # -- now we know input is valid ---

        if (min == None or max == None): #
            min = inputNum
            max = inputNum

        if (inputNum < min):
            min = inputNum
        
        if inputNum > max:
            max = inputNum
        
    print("minimum: "+ str(min) + ", maximum: " + str(max))







def validateSomethingConvertsToInt(potential_number):
    try:
        int(potential_number)
        return True
    except:
        return False

class MinMaxInator:
    min = None
    max = None

    def addNumber(self, input_num:int):
        if type(input_num) is not int:
            raise TypeError("Numbers must be Ints")
        
        if (self.min == None or self.max == None): #
            self.min = input_num
            self.max = input_num

        if (input_num < self.min):
            self.min = input_num
        
        if input_num > self.max:
            self.max = input_num
        


    def getMin():
        return min
    
    def getMax():
        return max
    



def v3():
    min_max_inator = MinMaxInator()
    while True:
        inputString = input("enter integer or done to finish: ")
        
        if inputString == "done":
            print("Exciting loop!")
            break

        if not validateSomethingConvertsToInt(inputString):
            print("Invalid Input!")
            continue

        min_max_inator.addNumber(int(inputString))

    print(f"min: {min_max_inator.getMin()}, max: {min_max_inator.getMax()}")