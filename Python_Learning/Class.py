class Person :
    def __init__(self,name):
       self.name = name 

    def talk(self) :
        print(f"He is {self.name}")


person1 = Person("Rimon")
person1.talk()