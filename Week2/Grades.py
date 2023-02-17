def percentage(num1,num2):#Returns a percentage
    return (num1/num2)*100

num1 = float(input("Enter marks earned \n"))

num2 = float(input("Enter maximum marks \n"))

final_value = percentage(num1,num2)

if (final_value < 40):
    print("E")
elif (final_value >= 40) and (final_value < 50):
    print("D")
elif (final_value >= 50) and (final_value < 60):
    print("C")
elif (final_value >= 60) and (final_value < 80):
    print("B")
elif (final_value >= 80) and (final_value < 100):
    print("A")

