names = []
for x in range (0,10) :
    name = input("Enter Name: ")
    names.append(name)

for x in range (0,10) :
    name = len (names)
    print(names.pop(0))
    print(names)


