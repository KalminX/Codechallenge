#A program to calculate the area of a square


#the function
def squareArea(length):
	return (length * length)

side = int(input("Enter the length of one side in cm: "))
print(f"The area of the square of length {side}cm is {squareArea(side)} centimeter squares.")
