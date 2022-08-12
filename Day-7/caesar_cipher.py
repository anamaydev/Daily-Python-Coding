alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text_c, shift_c, op):
	if op == "encode":
		cipher_text = ""
		for letter in text_c:
			index_ec = alphabet.index(letter)
			shift_index = index_ec + shift_c
			if shift_index > 25:
				shift_index = shift_index % 25 -1
			new_letter = alphabet[shift_index]
			cipher_text += new_letter
		print(cipher_text)
	
	elif op == "decode":
		plain_text = ""
		for letter in text_c:
			index_dc = alphabet.index(letter)
			shfit_index = index_dc - shift_c
			new_letter = alphabet[shift_index]
			plain_text += new_letter
		print(plain_text)
	
	else:
		print("Enter valid input.")


operation = input("What operation you would like to do, encode or decode: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Shift number: "))

caeser(text, shift, operation)
