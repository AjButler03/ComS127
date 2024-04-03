# Andrew Butler             12-2-2022
# classes demo (object oriented shit, lets fuckin go)

class Car:

    # class attribute. Will be the same for all instances of car, and will change for all if changed for one.
    wheels = 4

    # initializer
    # Note: init function is not constructor, constructor is something that happens in the background.
    def __init__(self, color, style):
        self.color = color
        self.style = style
    
    # methods
    def showDescription(self):
        print("I am a", self.color, self.style)
    #setter; setting attributes
    def changeColor(self, color):
        if type(color) == str:
            self.color = color
        else:
            print("Error: color must be a string")
    # getter; returns info about attributes
    def checkColor(self):
        return self.color

obj1 = Car("Black", "Sedan")

# print(obj1.color)
# print(obj1.style)

# obj1.color = "red"

# print(obj1.color)
# print(obj1.style)

obj1.showDescription()
obj1.changeColor("Green")
obj1.showDescription()
