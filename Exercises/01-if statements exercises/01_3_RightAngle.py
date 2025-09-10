angle_a = float(input("Enter 3 angles (deg) and program will check if angle is valid. Enter first angle:"))
angle_b = float(input("Enter second angle:"))
angle_c = float(input("Enter third angle:"))

if (angle_a < 0.0) or (angle_b < 0.0) or (angle_c < 0.0):
    print(f"Invalid triangle: At least one angle is negative")
elif ((180 - angle_a - angle_b - angle_c) != 0.0):
    print(f"Invalid triangle: Sum of angles is not 180 deg")
else:
    print(f"Triangle is valid")