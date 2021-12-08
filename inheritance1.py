class parent:
    def m1 (self):
        print("jr.ntr")
class child (parent):
    def m2 (self):
        print("harikrishna")
class grandChild(child):
    def m3 (self):
        print("sr.ntr")
obj=grandChild()
obj.m3()
obj.m2()
obj.m1()
        