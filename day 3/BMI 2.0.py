print("Welcome to this BMI calculator")
weight = float(input("Pleas enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: ")) ** 2

bmi = weight / height

if bmi < 18.5:
    print("Underweight")
elif 18.5 < bmi < 25:
    print("Normal")
elif 25 < bmi < 40:
    print("Overweight")
else:
    print("obese")
