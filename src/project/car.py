# define the class
class Car:
#define the class variables

#define the the init function
    def __init__(self, make, model):
        self.make = make
        self.model = model
#add the methods
    def toString(self):
        print("MAKE: " + self.make + "    MODEL: " + self.model)



#create instance of the class and print them out
c1 = Car("Ford", "Mustang")
c1.toString()

c2 = Car("Chevrolet", "Corvette")
c2.toString()

c3 = Car("Toyota", "Camry")
c3.toString()

c4 = Car("Honda", "Civic")
c4.toString()
