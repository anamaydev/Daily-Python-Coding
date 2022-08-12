import caesar_cipher_ascii
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text_c, shift_c, op):
	if op == "encode":
		cipher_text = ""
		for letter in text_c:
			if letter in alphabet:
				index_ec = alphabet.index(letter)
				shift_index = index_ec + shift_c
				shift_index = shift_index % 26
				new_letter = alphabet[shift_index]
				cipher_text += new_letter
			else:
				cipher_text += letter
		print(f"The {op}d text is {cipher_text}")
	
	elif op == "decode":
		plain_text = ""
		for letter in text_c:
			if letter in alphabet:
				index_dc = alphabet.index(letter)
				shift_index = index_dc - shift_c
				new_letter = alphabet[shift_index]
				plain_text += new_letter
			else:
				plain_text += letter
		print(f"The {op}d text is {plain_text}")
	
	else:
		print("Enter valid input.")

print(caesar_cipher_ascii.logo)

to_continue = True
while to_continue:
	operation = input("What operation you would like to do, encode or decode: ").lower()
	text = input("Type your message: ").lower()
	shift = int(input("Shift number: "))

	caesar(text, shift, operation)
	continue_input = input("Type 'yes' to go again, 'no' to end the program: ").lower()
	if continue_input == 'no':
		to_continue = False
