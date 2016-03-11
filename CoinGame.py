import random
coin = random.choice(["heads", "tails"])
print("I am flipping a coin, call it in the air; either heads or tails.")
userResponse = input()
if userResponse == "heads":
	print("You called heads")
if userResponse == "tails":
	print("You called tails")
print("The coin flipped to {}" .format(coin))
if userResponse == coin:
	print("Your Score = 1 point")
if userResponse != coin:
	print("Your Score = 0 points") 
