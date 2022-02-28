import time
lights = ["Yellow", "Green", "Red"]
for selection in lights:
    if selection == "Yellow":
        print(f"Light is {selection}, Ready")
    elif selection == "Green":
        print(f"Light is {selection}, Go")
    else:
        print(f"Light is {selection}, Stop")
    time.sleep(10)
