list = [2,3456,32,5,2,543,45,32]
unique = []
for item in list :
    if item not in unique :
        unique.append(item)
print(unique)