from collections import deque

# Using deque for O(1) performance (no shifting items in memory)
my_queue = deque()

print("--- Professional Queue Manager (FIFO) ---")

while True:
    # We convert to list only for a clean display
    print(f"\nCurrent Queue: {list(my_queue)}")
    print("Options: 1. Enqueue | 2. Dequeue | 3. Peek | 4. Exit")
    
    choice = input("Enter choice: ").strip()

    # Enqueue adds to the back of the queue
    if choice == "1":
        item = input("Enter value: ").strip()
        if item:
            my_queue.append(item)
            print(f"Success: '{item}' added to the back.")
        else:
            print("Error: Input cannot be empty.")

    # Dequeue removes the front item (the first one added)
    elif choice == "2":
        if my_queue:
            removed_item = my_queue.popleft() 
            print(f"Served: '{removed_item}' has left the front.")
        else:
            print("Error: The queue is currently empty.")

    elif choice == "3":
        # Peek allows looking at the front without removing it
        if my_queue:
            print(f"Next in line: {my_queue[0]}")
        else:
            print("The queue is empty.")

    # Exit option
    elif choice == "4":
        print("Exiting...")
        break
        
    else:
        print("Invalid choice, please try again.")