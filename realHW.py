def opt():
    print("Choose an option")
    print("1: Add a Name")
    print("2: Change a Name")
    print("3: Delete a Name")    
    print("4: View names")
    print("5: Exit")
names = []

opt()
while True:
    option = int(input("choose between options 1 - 5"))
    if option == 1:
        name = input(("choose name"))
        names.append(name)
        opt()
    if option == 3:
        delete = input("what name would you like to delete")
        if delete in names:
            names.remove(delete)
        else:
            print("name not available")
        opt()
    if option == 2:
        change = input("what name would you like to change")
        new_name = input("what would you like your new name to be.")
        index = 0
        for x in names:
            if x == change:
                names[index] = new_name
            else:
                index = index + 1
        opt()
    if option == 4:
        print(names)
        opt()
    if option == 5:
        print("goodbye")
        break