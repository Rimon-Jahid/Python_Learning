class Student :
    def printname(self,name) :
        print(name) 
    def printcgpa(self,cgpa) :
        print(cgpa)

s1 = Student()
s1.age = 24
s1.printname("Rimon")
print(s1.age)
s1.printcgpa(3.50)