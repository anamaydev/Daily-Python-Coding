import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator.")
let_len = int(input("How many letters you would like in your password: "))
num_len = int(input("How many numbers you would like in your password: "))
sym_len = int(input("How many symbols you would like in your password: "))

password = ""

for let in range(0, let_len):
	let_rand = letters[random.randint(0, len(letters)-1)]
	password += let_rand

for num in range(0, num_len):
	num_rand = numbers[random.randint(0, len(numbers)-1)]
	password += num_rand

for sym in range(0, sym_len):
	sym_rand = symbols[random.randint(0, len(symbols)-1)]
	password += sym_rand

pass_list = list(password)
random.shuffle(pass_list)
final_pass = "".join(pass_list)

print(final_pass)

