def func(farenheight):
    return (farenheight- 32)*5/9


f = float(input("enter your temperature(f) \n"))

answer = func(f)

print(answer," degrees celsius")