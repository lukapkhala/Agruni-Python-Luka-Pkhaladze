import math
a = float(input("enter first side: ")) 
b = float(input("enter second side: "))
c = float(input("enter third side: "))

# Triangle inequality check
if a + b <= c or a + c <= b or b + c <= a:
    print("it isn't a triangle")
else:

    perimeter = a + b + c
    s = perimeter / 2  # semiperimeter
    area = math.sqrt(max(0.0, s * (s - a) * (s - b) * (s - c)))

    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")