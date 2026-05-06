
print("I am your car assistance give me command")
while True :
    Command = input("> ")

    if Command.lower() == "help" :
        print("type start for start")
        print("type Stop for stop")
        print("type quit for quit")
    elif Command.lower() == "start" :
        print("car start")
    elif Command.lower() == "stop" :
        print("car stopped")
    elif Command.lower() == "quit" :
        break
    else :
        print("I dont understand your command")

