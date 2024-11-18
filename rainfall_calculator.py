# Inital list to store monthly rainfall data
monthly_rainfall = []

# List of month names for user-friendly input
month_names = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Loop to gather rainfall data for each month
for month in month_names:
    while True:
        try:
            # Prompt user for input with month name
            rainfall = float(input(f"Enter the total rainfall for {month} (in inches): "))
            
            # Check if the input is a positive number
            if rainfall < 0:
                print("Rainfall cannot be negative. Please enter a valid number.")
            else:
                monthly_rainfall.append(rainfall)
                break  # Exit the loop once valid input is entered
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# Calculate total rainfall for the year
total_rainfall = sum(monthly_rainfall)

# Calculate the average monthly rainfall
average_rainfall = total_rainfall / 12

# Find the month with the highest and lowest rainfall
max_rainfall = max(monthly_rainfall)
min_rainfall = min(monthly_rainfall)

# Find the names of the months with the highest and lowest rainfall
max_month = month_names[monthly_rainfall.index(max_rainfall)]
min_month = month_names[monthly_rainfall.index(min_rainfall)]

# Display results with a user-friendly format
print("\n--- Rainfall Analysis ---")
print(f"Total rainfall for the year: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
print(f"Highest rainfall was in {max_month} with {max_rainfall:.2f} inches")
print(f"Lowest rainfall was in {min_month} with {min_rainfall:.2f} inches")