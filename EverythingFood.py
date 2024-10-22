#A health calculator that gives you a couple of health recommendations based on health metrics the user provides

#BackgroundInfo

print("\nBMI stands for Body Mass Index. \nIt tells you what your weight should be based on your height. \nIf your BMI is 18 or lower, then you are underweight. \nIf your BMI is 18.5 - 24.9, then your weight is normal. \nIf your BMI is 25 - 29.9, then you are overweight. \nIf your BMI is 30 or higher, then you are obese.")
print("\nBMR stands for Basal Metabolism Rate. \nBasically, it tells you how many calories your body uses when you are not moving at all.")


#UserInput

weight = eval(input("\nWhat is your weight in kilos?"))
weight2 = weight * 2.2
height1 = eval(input("\nWhat is your height in centimeters?"))
gender = input("\nWhat is your gender: male or female?")
age = eval(input("\nWhat is your age?"))
active = input("\nHow active are you?(sedentary - little to no exercise, light - light exercise/sports 1-3 days/week, moderate - moderate exercise/sports 3-5 days/week, very - hard exercise/sports 6-7 days a week)")
height2 = height1/100
calories_consumed = eval(input("About how many calories do you consume in a day?"))

#BMICalculator

BMI = weight/height2**2
BMIE = round(BMI)
print("Your BMI is," ,BMIE, ".")

#BMRCalculator

gender = gender.lower()
if gender == "female":
    BMR = 447.593+(9.247*weight)+(3.098*height1)-(4.33*age)
    BMRE = round(BMR)
    print("Your BMR is" ,BMR, ".")
elif gender == "male":
     BMR = 88.362+(13.397*weight)+(4.799*height1)-(5.677*age)
     BMRE = round(BMR)
     print("Your BMR is" ,BMRE , ".")

#CaloiesPerDay

active = active.lower()
if active == "sedentary":
     calories = BMR*1.2
     caloriesE = round(calories)
     print("You should consume" ,caloriesE, "calories per day.")
elif active == "light":
     calories = BMR*1.375
     caloriesE = round(calories)
     print("You should consume" ,caloriesE, "calories per day.")
elif active == "moderate":
     calories = BMR*1.55
     caloriesE = round(calories)
     print("You should consume" ,caloriesE, "calories per day.")
elif active == "very":
     calories = BMR*1.725
     caloriesE = round(calories)
     print("You should consume" ,caloriesE, "calories per day.")

#IfYouAreStarvingOrNot

if calories_consumed < calories:
     more = calories - calories_consumed
     print("Currently, you are starving. To be eating healthy, you need to eat", more, "more calories everyday.")
elif calories_consumed == calories:
     print("You eat a normal amount of calories everyday")
elif calories_consumed > calories:
     less = calories - calories_consumed
     print("You are overeating. To be eating healthy, you need to eat", less, "less calories everyday.")

#CaloriesToLose/GainWeight

if BMI < 18:
     calories2 = calories-500
     print("You are underweight so you need to gain more weight. \nTo gain one pound per week, you should eat", calories2, 'calories per day. \nYou should also redo all of these calculations every week so you can check your BMI and determine if you still need to gain weight or if you are good to just maintain your weight.')
elif int(BMI) in range(18, 25):
     print("Your weight is pretty normal, you don't need to do anything to it, just maintain what you have.")
elif BMI >= 25:
     calories2 = calories-500
     print("You are oerweight so you might want to lose some weight. To lose one pound of weight every week, you should eat", calories2, "calories per day. \nYou should also redo all of these calculations every week because as you get lighter, \nand if you still want to lose weight, you will need to eat less calories every week.")

#AmountOfWaterCalculator

waterweight = weight2/2.2
if age < 30:
     amount = waterweight * 40
if int(age) in range (30, 55):
     amount = waterweight * 35
if age > 55:
     amount = waterweight * 30

ounces = amount/28.3
ouncesE = round(ounces)
litersE = round(ouncesE/33.8)

print("\nYou should drink", ouncesE, 'ounces of water every day, or', litersE, 'liters of water.')


