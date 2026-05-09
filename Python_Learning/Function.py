def salary_Function(name,position,salary) :
    print(f"Employee name is {name}")
    print(f"Employee position is {position}")
    print(f"Employee salary is {salary}")
    bonus = salary + 4000
    return bonus
name = input("What is your name ")
position = input ("What is your position ")
salary = int (input ("What is your salary "))
print(f"The bonus of the empolyee is {salary_Function(name=name,position=position,salary=salary)}")