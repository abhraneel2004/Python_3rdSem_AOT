# Open the text file
file_path = 'electricity_bills.txt'  # Replace 'electricity_bills.txt' with your file path
try:
    with open(file_path, 'r') as file:
        # Initialize variables to store consumption for July and November
        july_consumption = 0
        november_consumption = 0

        # Read each line in the file
        for line in file:
            # Split the line into parts (assuming the format is 'customer_name month consumption')
            parts = line.strip().split()

            # Ensure that the line has at least 3 parts
            if len(parts) >= 3:
                name = parts[0]
                month = parts[1].lower()  # Convert month to lowercase for case-insensitive comparison
                consumption = int(parts[2])  # Parse consumption as an integer

                # Check if the month is July or November and update consumption accordingly
                if month == 'july':
                    print(name,month,consumption)
                    july_consumption += consumption
                elif month == 'november':
                    print(name,month,consumption)
                    november_consumption += consumption

        # Print the electricity consumption for July and November
        print("Electricity consumption for July:", july_consumption)
        print("Electricity consumption for November:", november_consumption)

except FileNotFoundError:
    print("The file", file_path, "was not found.")
except Exception as e:
    print("An error occurred:", e)
