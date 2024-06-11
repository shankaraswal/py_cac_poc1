def area_states(side):
    area = side * side
    perimeter = 4 * side
    return area, perimeter

area, perimeter = area_states(12)

print("Area : ", area, "  Perimeter : ", perimeter)