# Define the input and output file paths
input_file_path = 'file1.txt'      # Change 'file1.txt' to your input file path
output_file_path = 'file2.txt'     # Change 'file2.txt' to your output file path

# Open the input file in read mode and the output file in write mode
try:
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # Initialize line number counter
        line_number = 1
        print(list(input_file))

        # Read each line from the input file
        for line in input_file:
            # Write the line number and the line content to the output file
            output_file.write(f"{line_number}: {line}")
            
            # Increment the line number counter
            line_number += 1

    print(f"Lines from '{input_file_path}' copied to '{output_file_path}' with line numbers.")
except FileNotFoundError:
    print("Input file not found.")
except Exception as e:
    print("An error occurred:", e)
