while True:
    a = ["1. Perimeter of Square", "2. Area of Square", "3. Perimeter of Rectangle", "4. Area of Triangle", "5. Area of Trapezoid", "6. Area of Circle", "7. Surface Area of Cube", "8. The curved surface area of Cylinder", "9. The total surface area of Cylinder", "10. The volume of Cylinder", "11. The curved surface area of a cone", "12. Total surface area of cone", "13. Volume of a Cone", "14. Surface Area of a Sphere", "15. Volume of a Sphere","0. Exit"]
    pi = 3.14
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
        length = int(input("Enter a length of Rectangle: "))
        width = int(input("Enter a width of Rectangle: "))
        print("Perimeter of Rectangle for given value is: ", length * width)
    elif user_input == 4:
        base = int(input("Enter a base of Triangle: "))
        height = int(input("Enter a height of Triangle: "))
        print("Area of Triangle for given value is: ", (base * height)/2)
    elif user_input == 5:
        base1 = int(input("Enter a base1 of Trapezoid: "))
        base2 = int(input("Enter a base2 of Trapezoid: "))
        height = int(input("Enter a height of Trapezoid: "))
        print("Area of Trapezoid for given value is: ", (base1 + base2)/2 * height)
    elif user_input == 6:
        area = int(input("Enter a radius of Circle: "))
        print("Area of Circle for given value is: ",((area ** 2) * pi))
    elif user_input == 7:
        sides = 6
        area = int(input("Enter a edge of Cube: "))
        print("Surface area of Cube for given value is: ", (sides * (area * area))) 
    elif user_input == 8:
        radius = int(input("Enter a radius of Cylinder: "))
        height = int(input("Enter a height of Cylinder: "))
        lh = height + radius
        print("curved surface area of Cylinder for given value is: ", (2 * radius) * lh * pi)
    elif user_input == 9:
        radius = int(input("Enter a radius of Cylinder: "))
        height = int(input("Enter a height of Cylinder: "))
        lh = radius + height
        print("The total surface area of Cylinder for given value is: ", (2 * radius) * lh * pi)
    elif user_input == 10:
        radius = int(input("Enter a radius of Cylinder: "))
        height = int(input("Enter a height of Cylinder: "))
        print("The volume of Cylinder for given value is: ", (pi * radius * radius * height))
    elif user_input == 11:
        radius = int(input("Enter a radius of Cone: "))
        length = int(input("Enter a lenght of Cone: "))
        print("The curved surface area of a cone for given value is: ", (pi * radius * length))
    elif user_input == 12:
        radius = int(input("Enter a radius of Cone: "))
        length = int(input("Enter a length of Cone: "))
        print("Total surface area of cone for given value is: ", (pi * (radius * length) + pi * (radius *radius)))
    elif user_input == 13:
        radius = int(input("Enter a radius of Cone: "))
        height = int(input("Enter a height of Cone: "))
        print("Volume of a Cone for given value is: ", (1/3 * pi * radius *radius *height))
    elif user_input == 14:
        radius = int(input("Enter a radius of Sphere: "))
        print("Surface Area of a Sphere for given value is: ", (4 * pi * radius *radius))
    elif user_input == 15:
        radius = int(input("Enter a radius of Sphere: "))
        print("Volume of a Sphere for given value is: ", (4/3 * pi * radius * radius * radius))
    elif user_input == 0:
        break
