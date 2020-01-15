def calculate_bmi_category(bmi):
    try:
        if float(bmi) <= 0:
            raise ValueError
    except ValueError:
        print('ERROR! BMI must be a positive number')
        raise

    if 0 < bmi <= 15:
        return 'Very severely underweight'
    if 15 < bmi <= 16:
        return 'Severely underweight'
    if 16 < bmi <= 18.5:
        return 'Underweight'
    if 18.5 < bmi <= 25:
        return 'Normal (healthy weight)'
    if 25 < bmi <= 30:
        return 'Overweight'
    if 30 < bmi <= 35:
        return 'Obese Class I (Moderately obese)'
    if 35 < bmi <= 40:
        return 'Obese Class II (Severely obese)'
    if 40 < bmi <= 45:
        return 'Obese Class III (Very severely obese)'
    if 45 < bmi <= 50:
        return 'Obese Class IV (Morbidly obese)'
    if 50 < bmi <= 60:
        return 'Obese Class V (Super obese)'
    if bmi > 60:
        return 'Obese Class VI (Hyper obese)'


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

