# Data-Structures-Assignment
Linear data structures are data structures whose elements are stored in non-hierarchical way where each element has the
successors and predecessors except the first and last element. There are four types namely: Arrays, Stacks, Linked Lists, and Queues 
as illustrated below.  
To access any specific illustration, Click the code button in the top right 

## **1. Arrays**

**Definition:** A linear data structure consisting of a collection of elements, stored under one variable name and, identified by at least one array index or key.

**Key Characteristics:**
- Fixed Size: In low-level languages, arrays have a set size (though Python lists are dynamic).
- Indexing: Elements are accessed using numbers starting from 0.
- Contiguous Memory: Elements are stored right next to each other in the computer's RAM.
- Time Complexity: * Accessing an element: $O(1)$ (Very fast).
- Searching/Inserting: $O(n)$ (Requires shifting or looking through elements).

## **2. Stacks**

**Definition:** A Stack is a linear data structure where elements are added and removed from the same end (the Top).
It follows the **Last-In, First-Out (LIFO) principle**; the last element added is the first one removed.

**Real-world Analogy:** A stack of cafeteria trays. You only ever take the one from the very top.

**Operations:**

- Push: Adding an item.
- Pop: Removing the most recently added item

## **3. Queues**

**Definition:** A Queue is a linear data structure that follows the **FIFO (First-In, First-Out) principle**. This means the first element added to the queue will be the first one to be removed.

**Key Characteristics:**

-**Enqueue:** Adding an element to the back (rear) of the queue.  
-**Dequeue:** Removing an element from the front of the queue.  
-**Front/Head:** The end where elements are removed.  
-**Rear/Tail:** The end where elements are added.  

**Real-world Analogy:** A line of people waiting for coffee. The person who got in line first gets their coffee first

## **4. Linked Lists**

**Definition:** A Linked List is a linear data structure where elements are not stored in adjacent memory locations. Instead, each element is an object called a **Node**.  
Each node contains two parts:  
- **Data:** The value you want to store (like a number or name).
- **Next:** A "pointer" or link to the next node in the sequence.

The Head: The very first node in the list. If you lose the Head, you lose the whole list!

**Real-world Analogy:** A Scavenger Hunt. You find the first clue (Head), which tells you where the second clue is, which tells you where the third clue is.
