    
from calories-calculator.calories import Calories

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

sex = str(input("Enter your sex (M for Male and F for Female): "))


while True:
    try:
        sex = str(input("Enter your sex (M for Male and F for Female): "))
        # asserting weight is in Kg
        if sex not in ["M","F"]:
            raise AssertionError('Please enter the letter M or F')
        break
    except AssertionError as e:
        print(e)

maria = calories(weight, height, age, sex)

print("Your Calories {}".format(maria.TDEE(1.5)))

