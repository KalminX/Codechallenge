#program to find the area of triangle


#the function
def triangleArea(height, base):
	return (0.5 * height * base)

height = int(input("Enter the height of the triangle: "))
base = int(input("Enter the base of the triangle: "))

print(f"The area of a triangle of height {height}cm and base {base}cm is {triangleArea(height, base)} centimeter square.")
