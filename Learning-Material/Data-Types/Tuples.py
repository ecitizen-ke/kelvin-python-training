# Tuples are declared with round brackets ()
# Tuples are immutable (cannot be changed) but can be added upon
# Standard counting index for tuples starts from 0 (left to right) and -1 (right to left)

# Declare dimensions tuple
dimensions = (55, 112)
print(dimensions[0])
print(dimensions[1])

"""
A buffet-style restaurant offers five basic foods. Think of five simple foods
and store them in a tuple
a) for loop to print each food offered
b) try and modify/change the items
c) the restaurant wants to change 2 items in the menu. write a line of code
     that rewrites the tuple and then use a for loop to print each item.
"""

# Store the menu items in a tuple
menu = ("Beef", "Soup", "Chicken", "Mukimo", "Vegtable Salad")

# Print each food offered using a for loop
for option in menu:
    print(option)

# Convert the tuple to a list to modify it using the list method
new_menu = list(menu)
# Add "Pizza" to the menu
new_menu.append("Pizza")
# Print the updated menu
print(new_menu)

# Modify two items in the menu
new_menu[2] = "Omena"
new_menu[3] = "Ugali"

# Convert new_menu back to tuple
menu  = new_menu

# Print each food in the updated menu using a for loop
for food in menu:
    print(f"This is the updated menu {food}")