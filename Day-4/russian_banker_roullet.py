import random

names = input("Enter the names(seperated by comma): ")
name_list = names.split(", ")
ele = len(name_list)
random_num = random.randint(0,ele-1)
print(name_list[random_num])
