class parent1:
    def m1 (self):
        print("m1")
class parent2:
    def m1 (self):
        print("m2")
class child(parent2,parent1):
    def m3(self):
        print("m3")
obj=child()
obj.m1()

obj.m3()
        