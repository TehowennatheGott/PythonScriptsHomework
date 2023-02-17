def greatest(num1,num2,num3):#checks to see what is greatest
    if (num1>num2) and (num1>num3):
        print(num1,"is greatest")
    elif(num2>num1) and (num2>num3):
        print(num2,"is greatest")
    elif (num3>num1) and (num3>num1):
        print(num3,"is greatest")
    else:
        print("They are equal")#Catch in case you put 3,3,3
        
        
num1 = int(input("Enter your first value \n"))

num2 = int(input("Enter your second value \n"))

num3 = int(input("Enter your third value \n"))

greatest(num1,num2,num3)