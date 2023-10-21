# Initialize an empty list to store the numbers
numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break  # Exit the loop if the user enters an empty string
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if len(numbers) >= 5:
    # Sort the list in descending order
    numbers.sort(reverse=True)
    top_5_numbers = numbers[:5]
    print("The five greatest numbers (in descending order) are:")
    for num in top_5_numbers:
        print(num)
else:
    print("You entered less than 5 numbers, so there are not enough to determine the top five.")
