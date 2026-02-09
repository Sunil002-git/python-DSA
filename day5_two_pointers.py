# 1. Plaindrome (Two pointers Version)

s = "racecar"
left = 0
right = len(s) - 1
is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)

# Reverse Array In-Place
arr = [1,2,3,4,5]
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    break
left += 1
right -= 1

print(arr)

# Problem 3: Remove Duplicates from Sorted Array
arr = [1, 1, 2, 2, 3]
slow = 0

for fast in range(1,len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]
print(arr[:slow+1])

# 4. CHeck Palindromez
s = "madam"

left = 0
right = len(s) - 1
is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)
# Tine O(n)
# space O(1)

# Reverse String In-Place
s = ["h", "e", "l", "l", "o"] #["o", "l", "l", "e", "h"]
left = 0
right = len(s)-1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
    
print(s)

# Find Pair With Given Sum (Sorted Array)
arr = [1, 2, 4, 6, 8, 10]
target = 10

left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        print(arr[left], arr[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
    	
# Practice Set 2 — Slow & Fast Pointers
# Remove Duplicates (Sorted Array)
arr = [0,0,1,1,1,2,2,3]
slow = 0

for fast in range(1,len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]
print(arr[:slow+1])

# Move All Zeros to End (In-Place)
arr = [0,1,0,3,12]
# Output = [1,3,12,0,0]
slow = 0
for fast in range(len(arr)):
    if arr[fast] != 0:
        arr[slow] = arr[fast]
        slow +=1
for i in range(slow, len(arr)):
    arr[i] = 0

print(arr)

# 1️⃣ Why two pointers instead of nested loops?

# Answer:

# Two pointers allow me to solve the problem in a single pass, reducing the time complexity from O(n²) to O(n).
# It also improves space efficiency and makes the logic cleaner.

# One-line strong version:

# “Two pointers avoid unnecessary comparisons and improve efficiency.”

# 2️⃣ Difference between left-right vs slow-fast pointers?

# Answer:

# Left–Right pointers:

# Start from both ends

# Move inward

# Used when data is symmetrical or sorted

# Examples: palindrome, reverse array, pair sum in sorted array

# Slow–Fast pointers:

# Move in the same direction

# Slow tracks valid position

# Fast explores input

# Examples: remove duplicates, move zeros, cycle detection

# Interview sentence:

# “Left-right is used for symmetry, slow-fast is used for filtering or compaction.”

# 3️⃣ When is two pointers NOT useful?

# Answer:

# Two pointers are not useful when the data is unsorted, order does not help, or when random access is not possible.

# Examples:

# Unsorted array pair sum (hashmap better)

# Graphs or trees

# Problems needing all combinations

# Good closing line:

# “In such cases, a hashmap or different approach is more suitable.”

# 4️⃣ Time & space complexity of each solution?

# You can say this generically (interviewers love this):

# “All two-pointer solutions run in O(n) time because each pointer moves at most n times, and O(1) space because no extra data structures are used.”

# If they ask individually:

# Palindrome → O(n), O(1)

# Reverse array → O(n), O(1)

# Pair sum (sorted) → O(n), O(1)

# Remove duplicates → O(n), O(1)

# Move zeros → O(n), O(1)

# 🧠 INTERVIEW POWER TIP (Very Important)

# End your explanation with:

# “This approach is optimal in both time and space.”

# That sentence alone signals strong fundamentals.

# 🎯 Where You Are Now

# You can now:

# Choose the right pattern

# Justify it

# Explain trade-offs

# State complexity confidently

# This is exactly what interviewers want.