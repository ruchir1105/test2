# Take input from the user
number = int(input("Enter an integer: "))

# Initialize the reversed number as 0
reversed_number = 0

# While loop to reverse the digits
while number != 0:
    digit = number % 10  # Extract the last digit of the number
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number //= 10  # Remove the last digit from the number

# Print the reversed number
print("Reversed Number:", reversed_number)
