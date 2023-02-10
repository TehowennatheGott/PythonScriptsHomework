def func(one,two):
    multi = one*two
    add = one+two
    div = one/two
    sub = one-two
    print(" Addition", add, "\n",
          "Subtraction", sub, "\n",
          "Multiplication", multi, "\n",
          "Division", div, "\n")
    
    

one = float(input("enter your first value\n"))

two = float(input("enter your second value\n"))

func(one,two)
