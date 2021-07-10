# user input
side1 = int(input("Enter Length of side 01: "))
side2 = int(input("Enter Length of side 02: "))
side3 = int(input("Enter Length of side 03: "))

# calculation
s = (side1+side2+side3)/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5

# output
print("The area of triangle is: ", area)


