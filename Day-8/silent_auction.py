import os
from silent_auction_art import logo

print(logo)
bid_dict = {}
to_continue = True
max = 0
winner = ""

def dict_merge(key_name, value_bid):
	global max
	global winner
	bid_dict[key_name] = value_bid
	if bid_dict[key_name] > max:
		max = bid_dict[key_name]
		winner = key_name

while to_continue:
	name = input("Enter your name: ")
	bid = int(input("Enter bid amound: $"))
	dict_merge(name, bid)
	other = input("Are there any other bidders? Yes or No: ").lower()
	os.system('clear')
	if other == "no":
		to_continue = False

print(f"The winner is {winner} with a bid of ${max}.")
