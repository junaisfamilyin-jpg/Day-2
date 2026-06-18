import math

class circle:
    def __init__(self, radius):
        self.radius = radius

        self.area_value = math.pi * (radius ** 2)
        self.perimeter_value = 2 * math.pi * radius

    def area(self):
        return self.area_value
    
    def perimeter(self):
        return self.perimeter_value
    
Enter_Radius = float(input("Enter the Radius of the circle: "))

my_circle = circle(Enter_Radius)

print(f"Area: {my_circle.area():.2f}")
print(f"Perimeter: {my_circle.perimeter():.2f}")
