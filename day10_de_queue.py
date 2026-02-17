# Deque in Python
# A deque stands for Double-Ended Queue. It is a special type of data structure that allows you to add and remove elements from both ends efficiently. This makes it useful in applications like task scheduling, sliding window problems and real-time data processing.
# Why Do We Need deque?
# It supports O(1) time for adding/removing elements from both ends.
# It is more efficient than lists for front-end operations.
# It can function as both a queue (FIFO) and a stack (LIFO).
# Ideal for scheduling, sliding window problems and real-time data processing.
# It offers powerful built-in methods like appendleft(), popleft() and rotate().
# Appending and Deleting Dequeue Items
# append(x): Adds x to the right end of the deque.
# appendleft(x): Adds x to the left end of the deque.
# extend(iterable): Adds all elements from the iterable to the right end.
# extendleft(iterable): Adds all elements from the iterable to the left end (in reverse order).
# remove(value): Removes the first occurrence of the specified value from the deque. If value is not found, it raises a ValueError.
# pop(): Removes and returns an element from the right end.
# popleft(): Removes and returns an element from the left end.
# clear(): Removes all elements from the deque.
from collections import deque

de = deque(['name', 'age', 'DOB'])

de.append("append right")
de.appendleft("append left")
de.extend(["extend", "deque"])
de.extendleft(["extending", "to", "left", 20])
de.remove(20)
# de.pop()
de.popleft()
print(de)
de.clear()
print(de)
# Accessing Item and length of deque
# Indexing: Access elements by position using positive or negative indices.
# len(): Returns the number of elements in the deque.

dq = deque([1,3,4,4,5,6])
print(len(dq))
print(dq[2])

#Count, Rotation and Reversal of a deque
# count(value): This method counts the number of occurrences of a specific element in the deque.
# rotate(n): This method rotates the deque by n steps. Positive n rotates to the right and negative n rotates to the left.
# reverse(): This method reverses the order of elements in the deque.

dq = deque([10, 20, 30, 40, 50, 20, 30, 20])
# # 1. Counting occurrences of a value
print(dq.count(20))
print(dq.count(30))

# 2. Rotating the deque
dq.rotate(-3)
print(dq)

# 3. Reversing the deque
dq.reverse()
print(dq)


# Answer aloud:

# 1️⃣ Difference between stack and queue?
# 2️⃣ Why deque instead of list?
# 3️⃣ Where is queue used in real life?
# 4️⃣ Why queue is needed for BFS?

# Topic: Queue Basics
# Concept: FIFO
# Python: collections.deque

# Use cases:
# Scheduling, BFS, streaming problems


stream = "aabc"

freq = {}
q = deque()

for ch in stream:
    freq[ch] = freq.get(ch, 0) + 1
    q.append(ch)

    while q and freq[q[0]] > 1:
        q.popleft()

    if q:
        print(q[0], end=" ")
    else:
        print(-1, end=" ")
print()
# We need:
# queue → maintain order
# dictionary → count frequency
# ⏱ Complexity
# Time: O(n)
# Space: O(n)

# Generate Binary Numbers from 1 to N

n = 5
q = deque(["1"])
for _ in range(n):
    front = q.popleft()
    print(front, end=" ")

    q.append(front + "0")
    q.append(front + "1")
# Steps:
# start with "1"
# dequeue
# append 0 & 1

# Practice Set 1 — Queue Basics
# 1️⃣ Implement a Queue Using deque

# Create functions:
# enqueue(x)
# dequeue()
# peek()
# is_empty()
class FIFO:
    def __init__(self):
        self.d = deque([])
    def enqueue(self, x):
        self.d.append(x)
    def dequeue(self):
        if not self.d:
            raise IndexError("Deque from empty queue")
        return self.d.popleft()
    def peek(self):
        if not self.d:
            raise IndexError("Deque from empty queue")
        return self.d[0]
    def is_empty(self):
        return len(self.d) == 0

s = FIFO()
s.enqueue(10)
s.enqueue(20)
print("Dequeued:", s.dequeue())   # 10
print("Peek:", s.peek())          # 20
print("Queue:", s.d) 

# 2️⃣ First Unique Character in Stream
stream = "aabcdb"
# output = a -1 b b b c
freq = {}
q = deque()

for ch in stream:
    freq[ch] = freq.get(ch, 0) + 1
    q.append(ch)

    while q and freq[q[0]] > 1:
        q.popleft()

    if q:
        print(q[0], end=" ")
    else:
        print(-1, end=" ")
print()
# Practice Set 2 — Queue Logic Problems
# 3️⃣ Generate Binary Numbers from 1 to N

n = 6
q = deque(["1"])
# 1 10 11 100 101 110
for _ in range(n):
    front = q.popleft()
    print(front, end=" ")

    q.append(front + "0")
    q.append(front + "1")
print()

# Reverse First K Elements of a Queue
q = deque([1,2,3,4,5])
k = 3
n = len(q)
stack = []
for i in range(k):
    front = q.popleft()
    stack.append(front)
# for j in range(len(stack)):
while stack:
    left = stack.pop()
    q.append(left)
# q.extend(stack)
q.rotate(k-n)
print(q)
from collections import deque

q = deque([1,2,3,4,5])
k = 3
n = len(q)

stack = []

# 1) take first k into stack
for _ in range(k):
    stack.append(q.popleft())

# 2) put back from stack (reversed)
while stack:
    q.append(stack.pop())

# 3) move remaining (n-k) to back
for _ in range(n - k):
    q.append(q.popleft())

print(q)  # deque([3, 2, 1, 4, 5])
# Practice Set 3 — Deque Power
# Sliding Window Maximum (Intro)
arr = [1,3,-1,-3,5,3,6,7]
k = 3
# [3,3,5,5,6,7]

# Hint:
# deque stores indices
# maintain decreasing order

from collections import deque

arr = [1,3,-1,-3,5,3,6,7]
k = 3

dq = deque()   # stores indices, values will be in decreasing order
ans = []

for i in range(len(arr)):

    # 1) Remove indices that are out of this window (i-k)
    if dq and dq[0] <= i - k:
        dq.popleft()

    # 2) Maintain decreasing order in dq
    while dq and arr[dq[-1]] <= arr[i]:
        dq.pop()

    # 3) Add current index
    dq.append(i)

    # 4) Window formed, record max
    if i >= k - 1:
        ans.append(arr[dq[0]])

print(ans)   # [3, 3, 5, 5, 6, 7]


# Topic: Queue & Deque Practice

# Patterns:
# - FIFO processing
# - Stream handling
# - Deque for window optimization

# Mistakes:
# (using list pop(0) / wrong order)
