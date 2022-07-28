#create the parent class
class Vehicle:
    def __init__(self,name,color):
        #your code here
        self.name = name
        self.color = color

    def max_speed(self):
        #your code here
        pass

class Car(Vehicle):
    def max_speed(self):
        #your code here
        print("250")

class Bus(Vehicle):
    def max_speed(self):
        #your code here
        print("150")

#creat instance of the three classes and call the max_speed() function on them

car1 = Vehicle("tesla", "black")
car2 = Car("toyota", "red")
car3 = Bus("school bus", "yellow")

car1.max_speed()
car2.max_speed()
car3.max_speed()
