from BMI_Calculator import *
from Bubble_Sort import *


def run_bmi():
    print('Enter weight in Kilograms:')
    weight = input()

    print('Enter height in Meters:')
    height = input()

    bmi = calculate_bmi(weight, height)
    category = calculate_bmi_category(bmi)

    print('Your BMI value is: ', bmi)
    print('Your BMI category is: ', category)


def run_bubble_sort():
    arr = []
    while True:
        try:
            print('Enter a number or ''X'' to stop:')
            user_input = input()
            if user_input.lower() == 'x':
                break
            arr.append(int(user_input))
        except ValueError:
            print('Invalid value!')

    print(bubble_sort(arr))


if __name__ == '__main__':
    run_bmi()
    run_bubble_sort()
