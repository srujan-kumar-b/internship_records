def calc_rectangle(length, width):
    area=length * width
    perimeter=2*(length + width)
    return area, perimeter
area, perimeter = calc_rectangle(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")