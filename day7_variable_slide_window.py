# Problem 1: Longest Substring Without Repeating Characters
s = "abcabcbb"

# Think in English
# Use a set to track unique characters
# Expand right
# If duplicate appears → shrink from left
# Track max length
char_set = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left+=1

    char_set.add(s[right])
    max_len = max(max_len, right-left+1)

print(max_len)
# Time: O(n)
# Space: O(n)
# Interview line: “Each character enters and leaves the window once.”
# Problem 2: Longest Substring With At Most K Distinct Characters
s = "eceba"
k = 2

left = 0
freq = {}
max_len = 0
for right in range(len(s)):
    freq[s[right]] = freq.get(s[right], 0) + 1

    while len(freq) > k:
        freq[s[left]] -= 1
        if freq[s[left]] == 0:
            del freq[s[left]]
        left += 1
    
    max_len = max(max_len, right-left+1)
print(max_len)

# Time: O(n)
# Space: O(n)

# Problem 3: Smallest Subarray With Sum ≥ Target
arr = [2,3,1,2,4,3]
target = 7

left = 0
min_len = float('inf')
window_sum = 0

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum >= target:
        min_len = min(min_len, right - left + 1)
        window_sum -= arr[left]
        left+=1

print(min_len)

# One golden rule (write this down)
# Right pointer expands the window
# Left pointer shrinks the window
# Universal Variable Sliding Window Template
# left = 0

# for right in range(n):
#     add s[right] to window

#     while window is invalid:
#         remove s[left] from window
#         left += 1

#     update answer

# Practice Set 1 — Longest Window
# 1️⃣ Longest Substring Without Repeating Characters
s = "pwwkew"

left = 0
freq = set()
max_len = 0

for right in range(len(s)):
    while s[right] in freq:
        freq.remove(s[left])
        left += 1

    freq.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)
# Time = O(n)
# Space = O(n)

# 2️⃣ Longest Substring With At Most 2 Distinct Characters
s = "ccaabbb"
k = 2

left = 0
max_len = 0
freq = {}

for right in range(len(s)):
    freq[s[right]] = freq.get(s[right], 0) + 1

    while len(freq) > k:
        freq[s[left]] -= 1
        if freq[s[left]] == 0:
            del freq[s[left]]
        left += 1

    max_len = max(max_len, right-left+1)
print(max_len)

# Time = O(n)
# Space = O(n)

# Practice Set 2 — Smallest Window
# 3️⃣ Smallest Subarray With Sum ≥ Target

arr = [2,3,1,2,4,3]
target = 7

min_len = float('inf')
left = 0
window_sum = 0

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum >= target:
        min_len = min(min_len, right - left + 1)
        window_sum -= arr[left]
        left += 1

    
print(min_len if min_len != float('inf') else 0)

# 4️⃣ Smallest Substring Containing All Characters of Pattern
s = "ADOBECODEBANC"
p = "ABC"
# Hint:
# Track required characters
# Count when condition satisfied
# Shrink to minimize
# freq = {}
# for t in p:
#     freq[t] = freq.get(t, 0) + 1
# print(freq)

# left = 0

# for right in range(len(s)):
    

# Example 1: Longest Substring Without Repeating Characters
s = "abcabcbb"
char_set = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left+=1
    char_set.add(s[right])
    max_len = max(max_len, right - left + 1)
print(max_len)

# Example 2: Longest Substring With At Most K Distinct

s = "eceba"
k = 2
freq = {}
left = 0
max_len = 0

for right in range(len(s)):
    freq[s[right]] = freq.get(s[right], 0) + 1

    while len(freq) > k:
        freq[s[left]] -= 1
        if freq[s[left]] == 0:
            del freq[s[left]]
        left += 1

        max_len = max(max_len, right - left + 1)
print(max_len)

# Example 3: Smallest Subarray With Sum ≥ Target
# Condition: Shrink when sum ≥ target (to minimize)

arr = [2,3,1,2,4,3]
target = 7
window_sum = 0
left = 0
min_len = float('inf')

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum >= target:
        min_len = min(min_len, right -left + 1)
        window_sum -= arr[left]
        left += 1

print(min_len if min_len != float('inf') else 0)    

# Example 4: Maximum Sum Subarray ≤ K
# Condition: Window invalid if sum > k
arr = [2,1,5,1,3,2]
k = 7
window_sum = 0
left = 0
# max_len = float('-inf')
max_sum = 0

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum > k:
        window_sum -= arr[left]
        left += 1
    max_sum = max(max_sum, window_sum)
print(max_sum) 

# LEVEL 1 — Warm Up
# Max Sum Subarray of Size K
# Hint: Fixed window (no shrinking needed)
arr = [2,1,5,1,3,2]
k=3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k,len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    max_sum = max(window_sum, max_sum)


print(max_sum)
# Time = O(n)
# space = O(1)

# 2️⃣ Smallest Subarray with Sum ≥ S
# Find: Minimum length
# 💡 Hint: Shrink when sum ≥ S
arr =  [2,3,1,2,4,3]
S=7

min_len = float('inf')
window_sum = 0
left = 0

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum >= S:
        min_len = min(min_len, right-left + 1)
        window_sum -= arr[left]
        left += 1
    
print(min_len)
# Time = O(n)
# space = O(1) 

#LEVEL 2 — Core Variable Window
# 3️⃣ Longest Substring Without Repeating
# Input: "pwwkew"
# Find: Length
# 💡 Hint: Set + remove duplicates

# 4️⃣ Longest Substring With At Most K Distinct
# Input: "araaci", k=2
# 💡 Hint: Dictionary size ≤ k

# 5️⃣ Max Sum Subarray ≤ K
# Input: [3,1,2,7,4,2,1,1,5], k=8
# 💡 Hint: Shrink when sum > k
arr = [3,1,2,7,4,2,1,1,5]
k = 8
max_sum = float('-inf')
window_sum = 0
left = 0
for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum > k:
        window_sum -= arr[left]
        left += 1
    
    max_sum = max(max_sum, window_sum)
        

print(max_sum)


# 🟠 LEVEL 3 — Pattern + Window
# 6️⃣ Minimum Window Substring
# Input: "ADOBECODEBANC", "ABC"
# 💡 Hint: Need-map + formed counter

s = "ADOBECODEBANC"
p = "ABC"

# step 1: Frequency of pattern
freq = {}
for ch in p:
    freq[ch] = freq.get(ch, 0) + 1
left = 0
formed = 0
required = len(freq)
window_freq  = {}

min_len = float('inf')
start = 0
# Step 2: Expand Window
for right in range(len(s)):
    char = s[right]
    window_freq[char] = window_freq.get(char, 0) + 1

    if char in freq and window_freq[char] == freq[char]:
        formed += 1
    
    # step 3: Shrink window
    while formed == required:
        if right - left + 1 < min_len:
            min_len = right - left + 1
            start = left
        
        left_char = s[left]
        window_freq[left_char] -= 1
        if left_char in freq and window_freq[left_char] < freq[left_char]:
            formed -= 1
        left += 1

# Step 4: result
print("" if min_len == float('inf') else s[start:start + min_len])
# 7️⃣ Longest Substring After K Replacements
# Input: "AABABBA", k=1
# 💡 Hint: Track most frequent char

# 8️⃣ Fruits Into Baskets
# Input: ["A","B","C","B","B","C"]
# 💡 Hint: At most 2 distinct

# 🔴 LEVEL 4 — Advanced
# 9️⃣ Longest Subarray With Ones After K Zeros
# Input: [1,1,1,0,0,0,1,1,1,1,0], k=2
# 💡 Hint: Count zeros

# 🔟 Permutation in String
# Input: "oidbcaf", "abc"
# 💡 Hint: Sliding window + frequency match

# Your Training Rule (Very Important)
# For EACH problem, write this first:

# Invalid when: __________
# Shrink when: __________
# Answer when: __________

# Example:

# Invalid when: duplicates > 1
# Shrink when: duplicate appears
# Answer when: window valid

# 1️⃣ Why variable sliding window instead of fixed?
# fixed used when variable is known so we use variable sliding when the variable dynamic
# 2️⃣ Why do we use while instead of if when shrinking?
# if works for only once while iterates untill the condition is valid
# 3️⃣ When does variable sliding window fail?
# if there is a negative value in the array
# 4️⃣ Time & space complexity?