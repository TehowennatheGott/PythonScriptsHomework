import random



for x in range(10):
    x = random.randint(-50,50)
    if ( x <= -30):
        print(f"{x} = Blue")
    elif ( x > -30 and x <= -10):
        print(f"{x} = Green")
    elif ( x > -10 and x <= 10):
        print(f"{x} = Yellow")
    elif ( x > 10 and x <= 30):
        print(f"{x} = Orange")
    elif (x > 30):
        print(f"{x} = Red")