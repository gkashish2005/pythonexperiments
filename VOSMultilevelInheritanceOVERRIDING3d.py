""" Aim: Write a program in python to calculate volume of sphere using multilevel inheritance demonstrating method overriding.
NAME: KASHISH GUPTA 231P081/09"""
class Circle:
    def __init__(self):
        self.radius = 0  
    def accept_radius(self):
        self.radius = float(input("Enter the radius of the sphere: "))
class Area(Circle):
    def __init__(self):
        super().__init__()  
    def accept_radius(self):
        print("In Area class: Calculating area of the circle.")
        super().accept_radius()  
    def calculate_area(self):
        area = 3.14159 * (self.radius ** 2)  
        print(f"Area of the circle: {area:.2f}")
class Volume(Area):
    def __init__(self):
        super().__init__()  
    def accept_radius(self):
        print("In Volume class: Calculating volume of the sphere.")
        super().accept_radius()  
    def calculate_volume(self):
        volume = (4/3) * 3.14159 * (self.radius ** 3)  
        print(f"Volume of the sphere: {volume:.2f}")
sphere = Volume()
sphere.accept_radius() 
sphere.calculate_area()  
sphere.calculate_volume()
print("~A Program written by kashish gupta 231P081/09")
