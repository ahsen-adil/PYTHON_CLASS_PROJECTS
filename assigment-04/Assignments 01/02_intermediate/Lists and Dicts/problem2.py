# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.

# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.



#Solution
#step 1:
list = [1 , 2 ,3 , "areeba" , "ayesha"]


#Function for accessing element
def access_elem(lst , index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

#Function for modifying element
def modify_elem(lst ,index , new_elem):
    try:
        lst[index] = new_elem
        return lst
    except IndexError:
        return "Index out of range."

#Function for slicing a list
def slice_list(lst , start_index , end_index):
    try:
        lst = lst[start_index :end_index]
        return lst
    
    except IndexError:
        return "Index out of range."
    
#index game    
def index_game():
    print(list)
    operation = input("Choose an operation: access, modify, slice: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_elem(list, index))

    if operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter the new value:")
        print(modify_elem(list, index  , new_value))

    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(list, start, end))
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    index_game()