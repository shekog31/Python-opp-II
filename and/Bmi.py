a=float(input("What is your height?"))
b=float(input("What is your weight?"))

bmi=b/(a/100)**2

print(bmi, "Is your BMI")

if bmi<=18:
    print("You're underweight")
elif bmi<=24:
    print("You're healthy")
elif bmi>=30:
    print("You're almost overweight")
else:
    print("You're overweight")  