class Bird:
    def fly(self):
        print("fly with wings")
class Airplane:
    def fly(self):
        print("fly with fuel")
class Fish:
    def swim(self):
        print("fish swim in sea")
obj=Fish()
obj.swim()
for obj in Bird(),Airplane(),Fish():
    obj.fly()
