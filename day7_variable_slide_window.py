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
freq = {}
for t in p:
    freq[t] = freq.get(t, 0) + 1
print(freq)

left = 0

for right in range(len(s)):
    


