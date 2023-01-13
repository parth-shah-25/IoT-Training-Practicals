class Animal:
    def inDerived(self):
        print("In Derived class...")
    
class Dog(Animal):
    def inChild(self):
        print("In Child class...")

obj1 = Dog()
obj1.inDerived()
obj1.inChild()
