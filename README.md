# Data Structures and Algorithms - Comprehensive Guide
## Overview
This repository contains Python implementations of various data structures based on the classification from the course notes, along with real-world applications and examples.

## Data Structure Classification
## Linear Data Structures
Linear data structures are data structures whose elements are stored in a non-hierarchical way, where each element has successors and predecessors except the first and last element. There are four types namely: Arrays, Stacks, Linked Lists, and Queues, as illustrated below.  

### 1. Arrays  
**Definition:** A linear data structure that stores a collection of elements in contiguous memory locations. This allows the computer to calculate the position of any element using a mathematical formula based on its index. 

**Key Characteristics:**
- **Fixed Size:** Traditionally allocated with a set size; resizing requires creating a new array and copying data.
- **Zero-Based Indexing:** The first element is at index 0.
- **Access Speed (O(1)):** Direct access to any element via its index is nearly instantaneous.
- **Modification Speed (O(n)):** Inserting or deleting from the middle requires "shifting" all subsequent elements to maintain the contiguous order.
- **Cache Friendliness:** Due to contiguous storage, arrays are highly optimized for modern CPU architectures.

**Best Use Case:** When you need fast random access to data and the total number of elements stays relatively constant.

**Application:** Image processing and contact lists - Arrays provide constant-time access to elements if you know the index. In an image, pixels are stored in a 2D array because the computer needs to access specific coordinates (x, y) instantly.


### 2. Stacks
**Definition:** A Stack is a linear data structure that serves as a collection of elements with two principal operations: push and pop. It operates on the Last-In, First-Out (LIFO) principle—meaning the most recent element added is the first one to be removed.

**Real-World Analogy:** Cafeteria Trays: You place a new tray on top of the pile (Push). When someone needs a tray, they take the one that was just placed there (Pop).

**Key Characteristics:**  
- **Unidirectional:** Access is restricted to a single end (The Top).  
- **Recursive Nature:** Stacks are used internally by operating systems to manage function calls (the "Call Stack").  
- **Memory Efficiency:** Since elements are only added/removed from the top, there is no need to "shift" elements like in an Array.

**Operations:**  
- **Push:** Adds an element to the Top of the stack.
- **Pop:** Removes the element from the Top of the stack.
- **Peek:** Returns the top element without removing it.
- **isEmpty:** Checks if the stack contains any elements.

**Application:** Browser history - You always want the last page you visited to be the first one you go back to.

### **3. Queues**

**Definition:** A Queue is a linear data structure that operates on the First-In, First-Out (FIFO) principle. In a queue, the first element added is the first one to be removed, much like a real-life waiting line.

**Real-world Analogy:** The first person to arrive at the counter in a coffee shop is the first person served.  

**Key Characteristics:**

- **Enqueue:** Adding an element to the back (rear) of the queue.  
- **Dequeue:** Removing an element from the front of the queue.  
- **Peek/Front:**	Returns the front element without removing it.  
- **IsFull/isEmpty:** Checks the capacity or state of the queue

**Application:** Printer task scheduling - It ensures fairness. The first person to hit "Print" gets their document first.

### **4. Linked Lists**

**Definition:**  
A Linked List is a linear data structure where elements are not stored in contiguous (adjacent) memory locations. Instead, the elements are linked using pointers.  
Each element is called a Node, which acts as a container for both the data and the address of the next item in the sequence. 

**Real-world Analogy:** A Scavenger Hunt. You find the first clue (Head), which tells you where the second clue is, which tells you where the third clue is.

The Head: The very first node in the list. If you lose the Head, you lose the whole list.  

A node is typically represented as a record or object with two fields:  
- **Data:** The actual value being stored (Integer, String, etc.  
- **Next:** A reference (pointer) to the subsequent node. The last node's next pointer is null or None.

**Key Characteristics:**
- **Dynamic Size:** Unlike standard arrays, linked lists can grow or shrink during execution without expensive resizing/copying.  
- **Efficient Insertions/Deletions:** Adding or removing elements doesn't require "shifting" the entire structure; you only need to update the pointers of the surrounding nodes.  
- **Memory Overhead:** Uses more memory than an array because it must store a next pointer for every single piece of data.

**Operations:**  
- **Access/Search:** Finding a specific value by traversing from the Head.
- **Insert (at Head):** Creating a new node and making it the new Head.
- **Insert (at Tail):** Traversing to the end to link a new node.
- **Delete (at Head)** Moving the Head pointer to the second node

**Application:** Music player playlists or "Undo" functionality in Word - In a playlist, "Next" and "Previous" are just pointers to the next node.

## Non-linear Data Structures
Non-linear data structures arrange data elements hierarchically or interconnectedly rather than sequentially, allowing for multi-level relationships
There are two types of non-linear data structures namely: Trees and Graphs

### 1. Trees
A Tree is a non-linear data structure representing a hierarchy. It consists of Nodes connected by Edges  
Trees are chosen when you need to store data that has a natural hierarchy or when you need faster searching than a Linked List but more flexibility than a sorted Array.  

**Real-World Analogy:** In companies, the CEO is at the top, Managers are below them, and individual contributors are at the bottom.  

**Key Terminology**  
- Root: The topmost node of the tree (the starting point).
- Parent / Child: A node directly above another is the parent; the nodes below it are children.
- Leaf: A node with no children (the "end" of a branch).
- Subtree: Any node and all its descendants can be viewed as a smaller tree within the larger one.
- Height: The number of edges on the longest path from the root to a leaf

**Application:** File systems (Folders/Subfolders) - Trees represent hierarchical data. A folder contains files, which might contain more folders.

### 2. Graphs
A Graph is a non-linear data structure consisting of a set of vertices (nodes) connected by edges. They are used to model complex relationships between entities that are not strictly hierarchical, such as networks, maps, or social connections.

**Real-World Analogy**: A social network where users are vertices and friendships or followers are edges. Similarly, cities are vertices and roads are edges in a transportation map.

**Key Terminology**
- **Vertex (Node):** A fundamental unit representing an entity in the graph (e.g., a person or a city).
- **Edge:** A connection between two vertices (e.g., friendship or road).
- **Directed / Undirected:**
Directed - edges have a direction (A → B).
Undirected - edges go both ways (A ↔ B).
- **Weighted / Unweighted:**
Weighted - edges have a cost or value (e.g., distance, time, or price).
Unweighted - edges are all equal (exist or don’t exist).
- **Neighbor:** A vertex that is directly connected to another vertex via an edge.
- **Degree:** Number of edges connected to a vertex - In directed graphs, you have in-degree (edges coming in) and out-degree (edges going out).
- **Path:** A sequence of vertices connected by edges.
- **Cycle:** A path where the first and last vertices are the same.
- **Connected Graph:** A graph where there is a path between every pair of vertices.

**Application:** Google Maps and Social Networks (Facebook/LinkedIn) - Graphs are perfect when you need to represent relationships, connections, and networks where data cannot be organized strictly in a hierarchy (like trees) or sequentially (like arrays).
