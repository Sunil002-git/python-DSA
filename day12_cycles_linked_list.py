# Why Cycle Detection Matters

# Used in:

# ✔ detecting loops in linked list
# ✔ Floyd’s algorithm
# ✔ circular structures
# ✔ memory corruption detection
# ✔ graph cycle logic (later)
# 1 → 2 → 3 → 4
#         ↑   ↓
#         ← ← ←
# DAY-12 INTERVIEW QUESTIONS

# Answer aloud:

# 1️⃣ Why do slow & fast pointers meet in a cycle?
# 2️⃣ Why not use a hashmap to detect cycle?
# 3️⃣ What happens if fast reaches None?
# 4️⃣ Real-life use of cycle detection?
# Practice Set 2 — Find Where Cycle Starts ⭐ If a cycle exists, return the node where it begins. Example 1 → 2 → 3 → 4 → 5 ↑ ↓ ← ← ← ← ←
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
def insert_end(head, value):
    new_node = Node(value)

    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    return head
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# create cycle: 5 -> 3
n5.next = n3

start = has_cycle(n1)
print(start.data if start else None)

# Practice Set 3 — Find Length of Cycle
# Example
# Cycle length:
# 3 → 4 → 5 → 3
# Output: 3

# Topic: Cycle Detection

# Patterns:
# - Slow & fast pointers
# - Meeting point logic
# - Cycle length calculation

# Key Insight:
# Fast pointer laps slow pointer