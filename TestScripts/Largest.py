# Python program to find largest
# number in a list
 
# list of numbers
list1 = []
for i in range(5):
    newnum=input("enter a new number\n")
    list1.append(newnum)
# printing the maximum element
print("Largest element is:", max(list1))