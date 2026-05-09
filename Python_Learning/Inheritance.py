class Person :
    
    def pname(self,name) :
        print(name)

    
    def page(self,age) :
        print(age)


    def pdob(self,dateofbirth):
        print(dateofbirth)


class Student(Person) :
    def __init__(self, id):
        self.id = id
    

    def stid(self) :
        print(self.id)


class Teacher(Person) :
    def __init__(self, dep) :
        self.dep = dep

    def pdep(self) :
        print(self.dep)


s1 = Student("241-15-604")
s1.pname("Rimon")
s1.stid()
s1.page(23)

t1 = Teacher("CSE")
t1.pname("Jakaria")
t1.pdep()
t1.page(33)

