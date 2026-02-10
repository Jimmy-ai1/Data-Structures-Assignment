# Assigning head to None
head = None

print("--- Simple Linked List Manager ---")

while True:
    print("\nOptions: 1. Add | 2. Display | 3. Remove Front | 4. Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
        val = input("Enter node data: ").strip()
        new_node = {"data": val, "next": None}
        
        # If the list is empty, the new node becomes the head. Otherwise, we find the end and link it.
        if head is None:
            head = new_node
        else:
            current = head
            while current["next"]:
                current = current["next"]
            current["next"] = new_node
        print(f"Linked '{val}' to the chain.")

    elif choice == "2":
        # Visualize the linked list with arrows to show the connections
        if not head:
            print("The list is empty.")
        else:
            print("\nHead", end="")
            curr = head
            while curr:
                print(f" -> [{curr['data']}]", end="")
                curr = curr["next"]
            print(" -> None")

    elif choice == "3":
        # Removes the front node (the head) and makes the second node the new head
        if head:
            removed = head["data"]
            head = head["next"]
            print(f"Removed '{removed}'. The second node is now the Head.")
        else:
            print("Nothing to remove.")
    
    # Exit option
    elif choice == "4":
        break