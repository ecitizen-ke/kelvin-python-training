# Writing to a file named "data.txt" (if it doesn't exist, it will be created)
file = open("data.txt", "a")  # Open the file in append mode
file.write("\nMy name is Joseph")  # Write a line to the file
file.write("\nMy name is Julius")  # Write a line to the file
file.write("\nMy name is Joane")  # Write a line to the file
file.write("\nMy name is Josephine")  # Write a line to the file
file.write("\nMy name is Juniper]")  # Write a line to the file

# Read the contents of the file "data.txt" and print them
file = open("data.txt", "r")  # Open the file in read mode
print(file.read())  # Read and print the contents of the file

# Create a Python program that prompts the user to enter a message and writes it to a file named "output.txt".
# Implement exception handling to handle any errors that may occur during file writing.
try:
    # Prompt the user to enter a message
    message = input("Enter a message:")

    # Open the file "output.txt" for writing
    file = open("output.txt", "w")  # Open the file in write mode

    # Write the message to the file
    file.write(message)  # Write the message to the file

    print("Message has been written to the file")

except Exception as e:
    print("An error occurred while trying to write to the file.", e)

# Read the text file "data.txt" and print its contents.
# Implement exception handling to handle the case where the file does not exist.
try:
    file = open("data.txt", "r")  # Open the file in read mode
    print(file.read())  # Read and print the contents of the file

except Exception as e:
    print("File does not exist")

# Open a text file named "sample.txt", read its contents, and then close the file.
file = open("sample.txt", "r")  # Open the file in read mode
print(file.read())  # Read and print the contents of the file
file.close()  # Close the file

# Create a Python program that reads data from a CSV file ("data.csv") containing student information (e.g., name, age, grade).
# Parse the CSV file and print out the student information.
# Implement exception handling to handle any errors that may occur during file reading or parsing.
try:
    file = open('data.csv')  # Open the CSV file
    print(file.read())  # Read and print the contents of the file
    file.close()  # Close the file

except Exception as e:
    file = open('data.csv')  # Open the CSV file
    print(file.read())  # Read and print the contents of the file
