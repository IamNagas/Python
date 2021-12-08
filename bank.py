class Bank:
    min_Bal=500    #static variable
    def __init__(self,name):
        self.name=name  # instance variable
#          print("constructor excuting automaticlly")
         def deposit(self,amount):
             self.amount= amount   # instance variable
             Bank.BranchName= "bangalore"
c1=Bank("rahul")
c2=Bank("priyanka")
c1.loc="hyderabad"
c1.deposit=50000
print(c1.__dict__)
print(c2.__dict__)



print(Bank.__dict__)
print(Bank.min_Bal)


