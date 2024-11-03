def validate_time():
    while True:
        try:
            hours = int(input("Enter hours (0-23): "))
            minutes = int(input("Enter minutes (0-59): "))
            
            # Check if the inputs are within the valid range
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours, minutes
            else:
                print("Invalid input. Hours must be between 0 and 23, and minutes between 0 and 59.")
                
        except ValueError:
            print("Invalid input. Please enter integer values.")

def main():
    hours, minutes = validate_time()
    print(f"The time entered is {hours} hours and {minutes} minutes.")

if __name__ == "__main__":
    main()
