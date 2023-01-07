print("Welcome to this BMI calculator")
weight = int(input("Pleas enter your weight in kilograms: "))
height = int(input("Please enter your height in meters: ")) ** 2

bmi = weight / height

print(f"Your Body Mass Index is {bmi:.2f}")