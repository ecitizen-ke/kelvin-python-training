def sum_items(items):
    # Initialize a variable total to store the sum
    total = 0
    
    # Iterate over each item in the items list
    for item in items:
        # Add the current item to the total
        total += item
    
    # Return the total sum
    return total

# Define a list of items
my_items = [1, 2, 3]

# Print the sum of the items using the sum_items function
print(sum_items(my_items))
