def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length+ width)
    
    return area, perimeter
l=float(input("Enter length: "))
w=float(input("Enter width: "))

area, perimeter = calc_rectangle(l, w)
print(f"Area: {area}, Perimeter: {perimeter}")