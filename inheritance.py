class parent:
    def m1(self):
        print("m1()-method")
class child(parent):
    def m2(self):
        print("m2()-method")
obj=child()
obj.m1()
obj.m2()
