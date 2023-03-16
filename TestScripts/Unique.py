# Python program to find largest
# number in a list
def unique(list1):
    # create set based on list
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    print(unique_list)
 
# list of numbers
list1 = ["","a","b","c","c"]
 
 
# printing the maximum element
print("all unique elements are:")
unique(list1)