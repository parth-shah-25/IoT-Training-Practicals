class A:
    var1 = "OUTSIDE CONSTRUCTOR....In class A."
    def __init__(self):
        self.var1 = "In Class A's Constructor. (This is a Instance Variable)"
        self.varC = "Special varialbe"
        self.demo = 22


class B(A):

    var2 = "In Class B."
    def __init__(self):
        super().__init__()
        self.var3 = "In Class B's Constructor. (This is an Instance Variable)"
        print(super().var1)


a = A()
b = B()

print(b.var3)