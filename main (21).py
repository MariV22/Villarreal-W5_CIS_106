# Get user inputs for start, stop, and increment values
start_value = int(input("Enter the start value: "))
stop_value = int(input("Enter the stop value: "))
increment_value = int(input("Enter the increment value: "))

# Initialize the current value to the start value
current_value = start_value

# Loop while the current value is less than or equal to the stop value
while current_value <= stop_value:
    # Print the current value
    print(current_value)
    # Increment the current value by the increment value
    current_value += increment_value