class flower:
    def __init__(self,name,petal,price):
        self.name=name
        self.petal=petal
        self.price=price
    def get_all(self):
        return f'{self.name}, {self.petal}, {self.price}'

rose = flower("Rose", int("4"), float("1.50"))
lily = flower("Lily", int("5"), float("2.45"))
daisy = flower("Daisy", int("6"), float("3.55"))

print(daisy.get_all())
#flow = input("What flower do u want? (rose, lily, daisy) : ")
#if flow == "rose":
#    print(rose.get_all())
#elif flow == "lily":
#    print(lily.get_all())
#else:
#    print(daisy.get_all())