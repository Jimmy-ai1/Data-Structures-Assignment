# Create an empty list to hold the array items
my_array = []

print("--- Simple Array Manager ---")

while True:
    print(f"\nYour current array is: {my_array}")
    print("Options: 1. Add  |  2. Remove  |  3. Exit")
    
    # Get user input and strip whitespace
    choice = input("Select an option: ").strip()

    
    if choice == "1":
        # Adding an item to an array (it goes to the end)
        new_item = input("Value to add: ").strip()
        if new_item:
            my_array.append(new_item)
            print(f"'{new_item}' added.")
        else:
            print("You can't add an empty item!")

    elif choice == "2":
        # Removing an item from an array (removes the first occurrence)
        item_to_remove = input("Value to remove: ").strip()
        if item_to_remove in my_array:
            my_array.remove(item_to_remove)
            print(f"'{item_to_remove}' removed.")
        else:
            print(f"Error: '{item_to_remove}' not found.")
    
    # Exit option
    elif choice == "3":
        print("Exiting. Happy coding!")
        break
    
    else:

        print("Oops! Please enter 1, 2, or 3.")
