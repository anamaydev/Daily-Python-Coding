import random
import hangman_ascii
import hangman_words

print(hangman_ascii.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
word_length = len(chosen_word)
lives = 6

display = []
for dash in range(word_length):
	display.append('_')

end_of_game = False

while not end_of_game:
	
	guess = input("Guess a letter: ").lower()
	
	if guess in display:
		print(f"You've already guessed {guess}.")

	for index in range(word_length):
		letter = chosen_word[index]
		if letter == guess:
			display[index] = guess

	if guess not in chosen_word:
		print(f"You guessed the wrong word. You lose a life.")
		lives -= 1
	print(hangman_ascii.stages[lives])
	
	print(f"{''.join(display)}")

	if '_' not in display:
		end_of_game = True
		print("You win")
	if lives == 0:
		end_of_game = True
		print("You lose")
