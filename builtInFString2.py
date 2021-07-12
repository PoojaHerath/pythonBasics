a = "cat"
print("r" + a[1:3])
print(a[0:2] + "r")
print(a[0] + "u" + a[2])


word = "Python Programming"

print(word.lower())
print(word.upper())


word3 = "Python   "
print(len(word3))
y = word3.rstrip()
print(len(y))


word4 = ",Python"
print(len(word4))
w = word4.lstrip(",")
print(w)
print(len(w))


word5 = "....Python...."
print(len(word5))
v = word5.strip(".")
print(v)
print(len(v))


word6 = "Python"
word7 = "Programming"
word8 = "Java"
word9 = "Java Programming"

print(word6.startswith("p"))
print(word8.startswith("p"))
print(word8.startswith("Ja"))
print(word8.startswith("Java"))

print(word6.endswith("n"))
print(word7.endswith("n"))
print(word7.endswith("Programming"))







