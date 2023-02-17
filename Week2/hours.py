def Wagie(num1,num2):
    if (num1 < 40):
        return num1*num2
    if (num1 >= 40) and (num1 < 45):
        return (num1 - 40)*1.5+40
    if (num1 >= 45) and (num1 < 50):
        return (num1 - 45)*1.75+(5*1.5)+40
    if (num1 >= 50):
        return (num1 - 50)*2+(5*1.75) + (5*1.5)+40

num1 = float(input("Enter your time worked \n"))
num2 = float(input("Enter your wage per hour \n"))

wage = Wagie(num1,num2)
print(wage,"Dollars owed")
