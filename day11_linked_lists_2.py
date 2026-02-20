# 🟢 Practice Set 1 — Build & Traverse
# 1️⃣ Insert at End
# Build list: 1 → 2 → 3 → 4
# Function: def insert_end(head, value)
# Hint:Traverse until next is None

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def print_list(head):
#     current = head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")

# def insert_end(head, value):
#     new_node = Node(value)

#     if head is None:
#         return new_node
    
#     current = head
#     while current.next:
#         current = current.next
    
#     current.next = new_node
#     return head

# head = Node(1)
# head = insert_end(head, 2)
# head = insert_end(head, 3)
# head = insert_end(head, 4)

# print_list(head)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.next = b
# b.next = c

# head = a

# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

# # If next == None -> Last Node
# # Ex: 1 -> 2 -> 3 -> None
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def print_list(head):
#     temp = head
#     while temp:
#         print(temp.data, end=" → ")
#         temp = temp.next
#     print("None")


# def delete_value(head, value):

#     if head is None:
#         return head

#     if head.data == value:
#         return head.next

#     current = head

#     while current.next:
#         if current.next.data == value:
#             current.next = current.next.next
#             return head
#         current = current.next

#     return head


# # --------- MAIN PART ---------

# # Build list: 1 → 2 → 3 → 4
# head = Node(1) 
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)

# print("Before delete:")         
# print_list(head)

# # Call function
# head = delete_value(head, 3)

# print("After delete:")
# print_list(head)


# set up node + helper function
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# insert at End
def insert_end(head, value):
    new_node = Node(value)

    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    return head
# ⏱ Time: O(n)
# 💾 Space: O(1)
def insert_begin(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node
# ⏱ Time: O(1)
# 💾 Space: O(1)
# Insert at Position

def insert_at_position(head, value, pos):
    new_node = Node(value)

    if pos == 0:
        new_node.next = head
        return new_node
    
    current = head
    for _ in range(pos - 1):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node

    return head
# Delete a value

def delete_value(head, value):
    if head is None:
        return head
    
    if head.data == value:
        return head.next
    
    current = head
    while current.next:
        if current.next.data == value:
            current.next = current.next.next
            break
        current = current.next
    return head

def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
# Find Middle of Linked List
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data
# Interview line: “Fast moves twice, slow reaches middle.”
head = Node(1)
head = insert_end(head, 2)
head = insert_end(head, 3)
head = insert_end(head, 4)
head = insert_begin(head, 0)
head = insert_at_position(head, 9, 2)
head = delete_value(head, 9)
head = reverse_list(head)
print_list(head)