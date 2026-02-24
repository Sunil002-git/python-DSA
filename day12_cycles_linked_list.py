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
# Time : 
# Practice Set 3 — Find Length of Cycle
# Example
# Cycle length:
# 3 → 4 → 5 → 3
# Output: 3
def cycle_length(head):
    slow = head
    fast = head
    # step 1: Detect Cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Step 2 : Count Cycle Length
            count = 1
            temp = slow.next

            while temp != slow:
                count += 1
                temp = temp.next
            return count
    return 0

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3

print(cycle_length(n1))
# Time : O(n)
# space : O(1)
# Topic: Cycle Detection

# Practice Set 4 — Happy Number (Cycle Detection Idea)
# A number is happy if repeating sum of squares of digits reaches 1.
# Example: 19 → 82 → 68 → 100 → 1
# Return: True

def next_number(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total
# Method 1: Using Set (Easy to Understand)
def is_happy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = next_number(n)
    return True
print(is_happy(19))
print(is_happy(2))
# Method 2: Using Slow & Fast (Floyd’s Algorithm)
def is_happy(n):
    slow = n
    fast = n

    while True:
        slow = next_number(slow)
        fast = next_number(next_number(fast))

        if fast == 1:
            return True
        if slow == fast:
            return False
print(is_happy(19))
print(is_happy(1))
# Patterns:
# - Slow & fast pointers
# - Meeting point logic
# - Cycle length calculation

# Key Insight:
# Fast pointer laps slow pointer