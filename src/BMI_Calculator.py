def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        if weight <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        print('ERROR! Values must be positive numbers')
        raise
    return weight/(height*height)
