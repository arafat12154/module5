import random
num_dice = int(input("How many dice do you want to roll? "))
total = 0
for _ in range(num_dice):
    # Generate a random number between 1 and 6 for each die (assuming standard six-sided dice)
    roll = random.randint(1, 6)
    total += roll
    print(f"Roll: {roll}")
print(f"Total sum: {total}")
