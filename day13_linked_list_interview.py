# DAY-13 — LINKED LIST INTERVIEW PATTERNS
# These are asked frequently:
# remove nth node
# merge two lists
# reverse in groups
# intersection point
# They look scary but use the same pointer logic you learned.

# Problem 1 — Remove Nth Node From End
# 1 → 2 → 3 → 4 → 5
# n = 2
# Output : 1 → 2 → 3 → 5

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_list(head):
    cur = head
    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next
    print("None")
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    # Move fast n+1 steps ahead
    for _ in range(n+1):
        fast = fast.next

    # # Move fast n+1 steps ahead
    while fast:
        slow = slow.next
        fast = fast.next
    # Delete Node
    slow.next = slow.next.next

    return dummy.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
head = n1
print("Before:")
print_list(head)
head = remove_nth_from_end(head, 2)
print("After:")
print_list(head)

# Problem 2 — Merge Two Sorted Lists ⭐
#  input
# 1 → 3 → 5
# 2 → 4 → 6
# output - > 1 → 2 → 3 → 4 → 5 → 6
def merge_two_lists(l1, l2):

    dummy = Node(0)     # fake start
    tail = dummy       # builds result

    # While both lists have nodes
    while l1 and l2:

        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next   # move tail

    # Attach remaining nodes
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next

# Build list : 1->3-> 5
a1 = Node(1)
a2 = Node(3)
a3 = Node(5)
a1.next = a2
a2.next = a3

# Build List : 2->4->6
b1 = Node(2)
b2 = Node(4)
b3 = Node(6)
b1.next = b2
b2.next = b3

merged = merge_two_lists(a1,b1)
print_list(merged)
# Complexity

# Time: O(n + m)
# Space: O(1) (no new nodes created)

# Problem 3 — Find Intersection of Two Lists
# Return node where two lists intersect.

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    p1 = headA
    p2 = headB

    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1

c1 = Node(4)
c2 = Node(5)
c1.next = c2

# List A
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a1.next = a2
a2.next = a3
a3.next = c1

# List B
b1 = Node(9)
b2 = Node(8)
b1.next = b2
b2.next = c1

print(get_intersection_node(a1, b1).data)

# Time: O(n + m)
# Space: O(1)

prev = None
current = head
while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node