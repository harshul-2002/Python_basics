#  taking input in  python

# val = input()
# print(f"your no is {val}")

# oops
# making a class person which has  name , age etc of person

class person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def getname(self):
        return self.name
    
    def getage(self):
        return self.age
        
p_1 = person("harsh",21)
print(p_1.getage())    


#  inheritence 

class car:
    def __init__(self):
        self.wheels = 4
        self.seats =5
    def drive(self):
        print("driving a car....")

mycar = car()

mycar.drive()


class supercar(car):
    def __init__(self):
        super().__init__()
        self.engine_power = "800 hp"
        self.seats = 2
    
    def drive(self):
        print("driving a super car...")

new_car = supercar()

new_car.drive()
mycar.drive()
