#program to calculate the area of a rectangle

#the function
def rectangleArea(length, breadth):
	return (length * breadth)

l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))

print(f"The area of a rectangle of length {l}cm and breadth {b}cm is {rectangleArea(l, b)} centimeter square")
