# MOSES MWAI WAHOME
# SCT211-0029/2022

print("This is a bmi calculator that queries for your weight and height")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

# Get the square of height
height *= height

# Calculate BMI 
bmi  = weight / height

if (bmi < 18.5):
    print("You are underweight")
elif (bmi > 24.9):
    print("You are overweight.")
else:
    print("You have normal weight.")