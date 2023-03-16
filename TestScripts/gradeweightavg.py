import os
from statistics import mean

print(os.getcwd())
#ranges
with open("grades.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]
        new_list = [int(n) for n in grades]
        print("Name:", name)
        part1 =(sum(new_list[0:5])*.30)
        part2 =(sum(new_list[6:8])*.50)
        part3 =(sum(new_list[9:10])*.25)
        print("Grade:",((part1+part2+part3)/25)*100,"%")
        #print("Grade:",mean(new_list))