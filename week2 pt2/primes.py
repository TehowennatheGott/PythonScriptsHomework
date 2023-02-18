def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

for i in range(2,31):
    check = is_prime(i)
    if(check):
        print(i,"is prime")
    else:
        print(i,"is not prime")
    