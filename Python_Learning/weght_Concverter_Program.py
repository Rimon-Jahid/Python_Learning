weight = float(input("Weight : "))
inp = input ("(L) or (K) : ")
inp = inp.upper()
if inp == "L" :
    weight *= 2.2046
    print(f"Your weight in kg = {weight}")
elif inp == "K" :
    weight *= 0.4535
    print(f"Your weight in Pound = {weight}")
else :
    print("Not in type")
