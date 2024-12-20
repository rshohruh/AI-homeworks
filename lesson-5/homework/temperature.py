def convert_cel_to_far(degree: float) -> float:
    return round(degree * 9 / 5 + 32, 2)

def convert_far_to_cel(degree: float) -> float:
    return round((degree - 32) * 5 / 9, 2)

f_degree = float(input("Enter a temperature in degrees F: "))
print(f"{f_degree} degrees F = {convert_far_to_cel(f_degree)} degrees C")

c_degree = float(input("Enter a temperature in degrees C: "))
print(f"{c_degree} degrees C = {convert_cel_to_far(c_degree)} degrees F")