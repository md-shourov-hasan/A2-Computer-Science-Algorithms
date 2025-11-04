# We are going to solve one of the past paper question
#from oops which I find it quite interesting
#9618_w23_qp_43

#Question 3

#To make an object, we need to first declare a class, a blueprint
#for our object.

class Character:
    def __init__(self, Name, XPosition, YPosition):
        self.__Name = Name #String
        self.__XPosition = XPosition #Integer
        self.__YPosition = YPosition #Integer

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, Value):
        if Value > 10000:
            Value = 10000
        elif Value < 0:
            Value = 0
        self.__XPosition = Value

    def SetYPosition(self, Value):
        if Value > 10000:
            Value = 10000
        elif Value < 0:
            Value = 0
        self.__YPosition = Value

    def Move(self, direction):
        if direction == "up":
            self.SetYPosition(self.GetYPosition() + 10)
        elif direction == "down":
            self.SetYPosition(self.GetYPosition() - 10)
        elif direction == "left":
            self.SetXPosition(self.GetXPosition() - 10)
        elif direction == "right":
            self.SetXPosition(self.GetXPosition() + 10)

class BikeCharacter(Character):
# To be continued






#main program

Jack = Character("Jack", 50, 50)



