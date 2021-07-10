num = int(input("Enter Marks: "))

if 100 >= num >= 0:
    if num >= 50:
        print("PASS!")
    else:
        print("FAIL!")
else:
    print("INVALID MARKS!")

