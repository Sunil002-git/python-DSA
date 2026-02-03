# Pattern “Visit every element once and do something”
# Template
# for i in range(len(arr)):
    # use arr[i]
# or
# for value in arr:
    # use value
# PART 3 — PROBLEMS (60 minutes)
# ✅ Problem 1: Find Maximum Element

# Task: Find the largest number in a list.

# 🔹 Think in English

# Assume first element is max

# Compare with remaining

# Update if bigger

arr = [3,5,1,9,2]
max_val = arr[0]

# for i in arr:
#     if i > max_val:
#         max_val = i

# print(max_val)
for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]

print(max_val)
# Time : O(n)
# Space : o(1)
# Problem 2: Count Even Numbers

# Task: Count how many even numbers are in the array.
arr = [1, 2, 3, 4, 6, 7]
count = 0

for i in arr:
    if i%2 == 0:
        count += 1

print(count)
# Problem 3: Reverse an Array (WITHOUT using reverse())
arr3 = [1,2,3,4,5]
rev = []

for i in range(len(arr3)-1 , -1, -1):
    rev.append(arr3[i])

print(rev)

# ⏱️ PART 4 — Interview Thinking (15 minutes)

# Answer these out loud (yes, literally):

# Why did you choose arr[0] as max?
# You need a real value from the array to cpompare against.
# arr[0] is the first element, guarnatreed to exist(assuming array is not empty.)
# This avoids using artificial values like 0 or -9999 , which can break logic.

# Time complexity of all 3 programs?
# Time complexity is O(n) because only one loop is used but the space complecities are 
# O(1) -> Only one variable is used
# O(1)
# O(n) (new array created)
# What happens if array has 1 element?
# loops through that one element the result for every thing is that one element
# What if array is empty? (edge case!)
# IndexError: list index out of range
if len(arr) == 0:
    print("Array is empty")
else:
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    print(max_val)
# 💡 Interviewers LOVE when you mention edge cases.