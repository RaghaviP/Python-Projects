a = ["1. Perimeter of Square", "2. Area of Square", "3. Perimeter of Rectangle", "4. Area of Triangle", "5. Area of Trapezoid", "6. Area of Circle", "7. Surface Area of Cube", "8. The curved surface area of Cylinder", "9. The total surface area of Cylinder", "10. The volume of Cylinder", "11. The curved surface area of a cone", "12. Total surface area of cone", "13. Volume of a Cone", "14. Surface Area of a Sphere", "15. Volume of a Sphere"]
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
elif user_input == 4:
    base = int(input("Enter a Base of Triangle: "))
    height = int(input("Enter a Height of Triangle: "))
    print("Area of Triangle for given value is: ", (base * height)/2)
elif user_input == 5:
    base1 = int(input("Enter a Base1 of Trapezoid: "))
    base2 = int(input("Enter a Base2 of Trapezoid: "))
    height = int(input("Enter a Height of Trapezoid: "))
    print("Area of Trapezoid for given value is: ", (base1 + base2)/2 * height)
elif user_input == 6:
    pi = 3.14159265
    area = int(input("Enter a Radius of Circle: "))
    print("Area of Circle for given value is: ",((area ** 2) * pi)) 

    
