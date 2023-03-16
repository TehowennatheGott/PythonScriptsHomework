list1 = ['little','blue','widget']
list2 = ['there','is','a','little','blue','cup','on','the','table']
list4 = [3,4,5,6,7,8]
list5 = [2,3,5,6,9,7]

list3 = list(set(list4)&set(list5))#makes an aggregate set from 2 other sets

print(list3)