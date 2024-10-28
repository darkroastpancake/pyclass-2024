# Time Calc Program

# Input
average_speed = float(input("Enter your average speed (mph): "))
speed_limit = float(input("Enter the speed limit (mph): "))
distance = float(input("Enter the distance traveled (miles): "))

# Calculate time @ each speed
time_with_limit = distance / speed_limit
time_with_avg_speed = distance / average_speed

# Calculate time saved
time_saved = (time_with_limit - time_with_avg_speed) * 60

# Output
print(f"Time saved: {time_saved:.1f} minutes")
