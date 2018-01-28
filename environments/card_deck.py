import random

card_suits = ["C","S","H","D"]
card_value = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
deck = []

for i in card_suits:
	for x in card_value:
		card = str(x) + i
		deck += [card]
random.shuffle(deck)
print(deck)
#print(len(deck))
