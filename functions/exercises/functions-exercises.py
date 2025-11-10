# Part 1 A -- Make a Line

print("Line")
def make_line(size):
    line = ""
    for i in range(size):
        line += "#" 
    return line
print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
print("Square")
def make_square(size):
 square = ""
 for i in range(size):
     for j in range(size):
         square += "#"
     square += "\n"
 return square
print(make_square(5))


# Part 1 C -- Make a Rectangle
print("Rectangle")
def make_rectangle(width,height):
 rectangle = ""
 for i in range(height):
     for j in range(width):
         rectangle += "#"
     rectangle += "\n"
 return rectangle
print(make_rectangle(10,5))


# Part 2 A -- Make a Stairs
print("stairs")
def make_stairs(size):
 stairs = ""
 for i in range(size):
     stairs += "#" * (i+1) + "\n"

 return stairs
print(make_stairs(5))


# Part 2 B -- Make Space-Line 
print("Space-Line")
def make_space_line(spaces, size):
    line = ""
    line += " " * spaces      
    line += "#" * size        
    return line
print(make_space_line(3, 5))

# Part 2 C -- Make Isosceles Triangle
print("ISOSCELES TRIANGLE")
def make_triangle(size):
 triangle = ""
 for i in range(size):
    triangle += " " * (size - i - 1) + "*" * (2 * i + 1) + "\n"
 return triangle
print(make_triangle(5))

# Part 3 -- Make a Diamond
print("DIAMOND")
def make_diamond(size):
    diamond = ""
    for i in range(size):
        diamond += " " * (size - i - 1) + "*" * (2 * i + 1) + "\n"
    for i in range(size - 2, -1, -1):
        diamond += " " * (size - i - 1) + "*" * (2 * i + 1) + "\n"
    return diamond
print(make_diamond(5))



