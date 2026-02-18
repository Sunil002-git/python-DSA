# DAY-11 INTERVIEW QUESTIONS

# Answer aloud:

# 1️⃣ Why use linked list instead of array?
# 2️⃣ What is a node?
# 3️⃣ What is the role of the next pointer?
# 4️⃣ Where are linked lists used in real systems?
# Notebook Entry
# Topic: Linked List Basics

# Structure:
# Node → data + next pointer

# Key Idea:
# Elements connected via pointers

# Practice Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create nodes
a = Node(1)
b = Node(2)
c = Node(3)

# connect
a.next = b
b.next = c

head = a

# print
temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("None")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_begin(head, value):
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head = insert_begin(head, 0)

temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("None")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_end(head, value):

    new_node = Node(value)

    # Case 1: If list is empty
    if head is None:
        return new_node

    # Case 2: List is not empty → go to last node
    temp = head

    while temp.next is not None:
        temp = temp.next

    # Now temp is last node
    temp.next = new_node

    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head = insert_end(head, 4)
temp = head
while temp:
    print(temp.data, end=" → ")
    temp = temp.next
print("None")

# 1️⃣ Insert at End
# Build list: 1 → 2 → 3 → 4
# Function:
# def insert_end(head, value):
# 📌 Hint:
# Traverse until next is None
