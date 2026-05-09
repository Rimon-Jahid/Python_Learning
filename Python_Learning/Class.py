class Person :
    def __init__(self,name):
       self.name = name 

    def talk(self) :
        print("He is talking")


person1 = Person
person1.talk(person1)
person2 = Person("Rimon")
print(person2.name)