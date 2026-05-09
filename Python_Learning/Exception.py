try :
    age = int(input("Enter your age : "))
    di = 1000 / age
    print(f"His age is {age} and his di is {di}")
except ZeroDivisionError:
    print("Age cant be 0")
except ValueError :
    print("Invalid age")

try :
    Name = input("Enter your name : ")
    div = 1000 / Name
    print(f"His name is {Name} and his di is {div}")
except Exception as error :
    print("Inavlid Value")