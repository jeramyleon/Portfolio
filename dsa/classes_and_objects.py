class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print('My name is', self.name)


robot1 = Robot('Tom', 'red', 30)
robot2 = Robot('Jerry', 'blue', 40)

robot1.introduceSelf()
robot2.introduceSelf() 


class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
     
    def sitDown(self):
            self.isSitting = True

    def standUp(self):
            self.isSitting = False
 
person1 = Person('Drake', 'aggressive', False)
person2 = Person('Kanye', 'talkative', True)

person1.robotOwned = robot2
person2.robotOwned = robot1

person1.robotOwned.introduceSelf()
person2.robotOwned.introduceSelf()

robot1.lookingAt = robot2
robot2.lookingAt = robot1

