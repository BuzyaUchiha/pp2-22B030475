#task1
"""
import math
def degrees_to_radians(degrees):
    radians = degrees * math.pi / 180
    return radians
radians = degrees_to_radians(int(input()))
print(radians)
"""
#task2
"""
import math
def trapezoid_area(height, base1, base2):
    expected = (base1 + base2) * height / 2
    return expected
expected = trapezoid_area(int(input("Height: ")), int(input("Base, first value: ")), int(input("Base, second value: ")))
print(expected)
    """
#task3
"""
import math
def polygon_area(s, n):
    area = ((n / (2 * math.tan(math.pi/s)))*n*s)/2
    return area
are = polygon_area(int(input("Input number of sides: ")), int(input("Input the length of a side: ")))
print(are)
"""
#task4
def parallelogram_area(base, height):
    area = base * height
    return area
area = parallelogram_area(int(input("Length of base: ")), int(input("Height of parallelogram: ")))
print(f'Expected output: {area}')


