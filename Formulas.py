a = ["1. Perimeter of Square", "2. Area of Square", "3. Perimeter of Rectangle"]
for i in a:
    print(i)
user_input = int(input())
if user_input == 1:
    sidesofsquare = int(input("Enter a side of Square: "))
    print("Perimeter of Square for given value is: ", sidesofsquare * 4)
elif user_input == 2:
    areaofsquare = int(input("Enter a side of Square: "))
    print("Area of Square for given value is: ", areaofsquare ** 4)
elif user_input == 3:
    length = int(input("Enter a Length of Rectangle: "))
    width = int(input("Enter a Width of Rectangle: "))
    print("Perimeter of Rectangle for given value is: ", length * width)
    
