# Create a list
my_list = [10, 30, 20, 50, 40]
print("Original List:", my_list)

# Access list elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Add elements to the list
my_list.append(60)        # Adds element at the end
print("After appending 60:", my_list)

my_list.insert(2, 25)     # Inserts element at index 2
print("After inserting 25 at index 2:", my_list)

# Remove elements from the list
my_list.remove(30)        # Removes the first occurrence of 30
print("After removing 30:", my_list)

my_list.pop()             # Removes last element
print("After popping last element:", my_list)

# Sort the list
my_list.sort()
print("Sorted List:", my_list)

# Reverse the list
my_list.reverse()
print("Reversed List:", my_list)
