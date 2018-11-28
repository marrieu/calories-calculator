    
from caloriescalculator.calories import Calories

print('Lets estimate your calorie intake..')

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        # asserting weight is in Kg
        if not weight < 120:
            raise AssertionError('Weight needs to be in Kg. e.g: 61, 84..')
        break
    except AssertionError as e:
        print(e)
         

while True:
    try:
        height = float(input("Enter your height in cm: "))
        # asserting weight is in Kg
        if not height > 100:
            raise AssertionError('Height needs to be in centimeters. e.g: 167, 179..')
        break
    except AssertionError as e:
        print(e)
            
    
age = int(input("Enter your age: "))

while True:
    try:
        sex = str(input("Enter your sex (M for Male and F for Female): "))
        # asserting weight is in Kg
        if sex not in ['M','F']:
            raise AssertionError('Please enter the letter M or F')
        break
    except AssertionError as e:
        print(e)

C = Calories(weight, height, age, sex)

activity = float(input('''
1.2 - Sedentary: Little or no physical activity.
1.3 - Lightly Active: Light exercise or activity 1-3 days per week.
1.5 - Moderately Active: Moderate exercise or activity 3-5 days per week.
1.7 - Very Active: Hard exercise or activity 6-7 days per week.
1.9 - Extremely Active: Hard daily exercise or activity and physical work 

Enter your activity multiplier according to the table above (number between 1.2 to 1.9): '''))

print('''Your daily calorie intake:
{} for maintain
{} for losing
{} for gaining '''.format(round(C.TDEE(activity)), round(C.cut()), round(C.bulk())))



