car_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("Car is already started!")
        else:
            print("Car is started.")
            car_started = True
    elif command == "stop":
        if car_started:
            print("Car stopped.")
            car_started = False
        else:
            print("Car is already stopped!")
    elif command == "quit":
        break
    else:
        print("Command not recognized.")
    