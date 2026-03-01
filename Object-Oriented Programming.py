# We are going to solve one of the past paper question
#from oops which I find it quite interesting
#9618_w23_qp_43

#Question 3

#To make an object, we need to first declare a class, a blueprint
#for our object.

class Character:
    def __init__(self, PName, PXPosition, PYPosition):
        self.__Name = PName #String
        self.__XPosition = PXPosition #Integer
        self.__YPosition = PYPosition #Integer

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
    def __init__(self, PName, PXPosition, PYPosition):
        super().__init__(PName, PXPosition, PYPosition)
        #we are inheriting the attributes from parent class


    def Move(self, direction):
        #we are modifying the parent's method, which is an example of polymorphism
        #by overriding the Move() method

        if direction == "up":
            self.SetYPosition(self.GetYPosition() + 20)
        elif direction == "down":
            self.SetYPosition(self.GetYPosition() - 20)
        elif direction == "left":
            self.SetXPosition(self.GetXPosition() - 20)
        elif direction == "right":
            self.SetXPosition(self.GetXPosition() + 20)

#main program

Jack = Character("Jack", 50, 50)
Karla = BikeCharacter("Karla",100,50)

User_character = input("Enter a character name you would like to move: ")

while User_character != "jack" and User_character != "karla":
    User_character = input("Invalid input. Try again: ")

User_direction = input("Enter a direction (up/down/left/right): ")

while User_direction != "up" and User_direction != "down" and User_direction != "left" and User_direction != "right":
    User_direction = input("Invalid input. Try again: ")

if User_character == "jack":
    Jack.Move(User_direction)
else:
    Karla.Move(User_direction)




