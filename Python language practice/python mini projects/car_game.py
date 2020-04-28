command=""
started=False
while True:
    command=input(">").lower()
    if command=="start":
        if started:
            print("car is already started!")
        else:
            started=True
            print("car is started!")
    elif command=="stop":
        if not started:
            print("car is already stopped")
        else:
            started=False
            print("car is stop!")
    elif command=="help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - tor quit the game
        """)
    elif command=="quit":
        break
    else:
        print("invalid command!")