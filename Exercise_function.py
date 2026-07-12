# Q1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height
# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def calculate_area(d1, d2, shape="triangle"):
    if shape == "triangle":
        area = 1/2*(d1*d2)
    elif shape == "rectangle":
        area = d1 * d2
    else:
        print('Error: area is neither triangle nor rectangle')
        area=None
    return area

d1 = 10
d2 = 20
triangle_area = calculate_area(d1, d2, "triangle")
print("Area of a triangle is: ", triangle_area)

rectangle_area = calculate_area(d1, d2, "rectangle")
print("Area of a rectangle is:", rectangle_area)

square_area = calculate_area(d1, d2, "square")
print("Area of a square is:", square_area)