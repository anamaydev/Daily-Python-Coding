print("Welcome to the Love Calculator")
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

new_name = name1.lower() + name2.lower()

t = new_name.count("t")
r = new_name.count("r")
u = new_name.count("u")
e = new_name.count("e")

tens_place = t + r + u + e

l = new_name.count("l")
o = new_name.count("o")
v = new_name.count("v")

ones_place = l + o + v + e

total = tens_place * 10 + ones_place

if total <= 10 and total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
	
