# ✅ Problem 1: Count Character Frequency
s = "programming"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
# “I use a hashmap to count frequency in one pass.”
# Pattern 2: First Non-Repeating Character
s = "swiss"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0)+1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
# Two passes, still O(n)
# ✅ Problem 3: Check for Duplicates
arr = [1,2,3,2]
seen = set()

has_duplicates = False
for num in arr:
    if num in seen:
        has_duplicates = True
        break
    seen.add(num)

print(has_duplicates)

# ✅ Two Sum (Very Important)
nums = [2,7,11,15]
target = 9

seen = {}
for i, num in enumerate(nums):
    rem = target - num
    if rem in seen:
        print(seen[rem], i)
        break
    seen[num] = i
# Time : O(n)
# Space: O(n)

# DSA NOTEBOOK — Day-4 Entry
# Topic: Hashmaps
# Patterns:
# 1) Frequency counting
# 2) Seen-before logic
# 3) Complement lookup

# Key Learning:
# # Hashmaps reduce O(n²) → O(n)
# 1️⃣ Why do we use a hashmap here instead of a list or nested loop?

# Answer:

# We use a hashmap because it gives O(1) average time lookup, which helps reduce time complexity from O(n²) to O(n).

# Follow-up line (strong answer):

# Using a list would require searching every time, which is inefficient for large inputs.

# 2️⃣ What is the time and space complexity of frequency counting?

# Answer:

# Time Complexity: O(n) — one traversal

# Space Complexity: O(k) — where k is number of unique elements

# Interview sentence:

# The extra space depends on the number of unique characters, not total length.

# 3️⃣ Why do we solve “First Non-Repeating Character” in two passes?

# Answer:

# First pass counts frequency, second pass preserves the original order to find the first character with frequency 1.

# Important keyword: order matters.

# 4️⃣ Explain Two Sum using hashmap (MOST IMPORTANT)

# Answer:

# I iterate through the array once, and for each element I check if its complement exists in the hashmap.
# If yes, I return the indices. Otherwise, I store the current element with its index.

# Complexity line:

# Time complexity is O(n) and space complexity is O(n).

# 5️⃣ What happens if hashmap lookup was not O(1)?

# Answer:

# Then the overall solution would degrade, possibly to O(n²), and hashmap would lose its advantage.

# (Shows you understand theory, not just syntax.)

# 6️⃣ Can hashmaps maintain order?

# Answer (Python-specific):

# Yes. From Python 3.7+, dictionaries preserve insertion order.

# This is a bonus answer — interviewers like this.

# 🧠 One Super-Important Interview Habit

# When answering, always include:

# WHY you chose hashmap

# TIME + SPACE complexity

# Even if they don’t ask — this makes you look senior.

# Problem 1: First Repeating Character
s = "abca"
#Output = a
seen = set()

for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)

# Find element that appears more than n/2 times.
Input = [2,2,1,2,3,2,2]
# Output: 2
count_input = 0
count_word = ""
new_input = {}
for i in Input:
    if i in new_input:
        new_input[i] += 1
    else:
        new_input[i] = 1
print(new_input)
for s in new_input:
    if new_input[s] > count_input:
        count_input = new_input[s]
        count_word = s
print(f"{count_word} : {count_input}")

s = "programming"
seen = set()

for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)

s = "I love python and I love django"
words = s.split()
repeat = set()
for ch in words:
    if ch in repeat:
        print(ch)
        break
    repeat.add(ch)


s = "I love python and I love django"
words = s.split()
repeat = {}
for ch in words:
    if ch in repeat:
        repeat[ch] += 1
    else:
        repeat[ch] = 1
for ch in words:
    if repeat[ch] == 1:
        print(ch)
        break

# Problem: Most Frequent Word
s = "apple banana apple orange banana apple"
words = s.split()
repeat = {}
for ch in words:
    if ch in repeat:
        repeat[ch] += 1
    else:
        repeat[ch] = 1
max_count = 0
max_word = ""

for ch in repeat:
    if repeat[ch] > max_count:
        max_count = repeat[ch]
        max_word = ch
print(f"{max_word} : {max_count} ")
# print(max(repeat, key=repeat.get))

# Problem: Second Most Frequent Word
#s = "apple banana apple orange banana apple orange orange"
s = "a b a c b b d"
words = s.split()

# Count frequency
freq = {}

for ch in words:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Track top two
most_freq = 0
second_freq = 0

most_word = ""
second_word = ""

for ch in freq:
    count = freq[ch]

    if count > most_freq:
        second_freq = most_freq
        second_word = most_word

        most_freq = count
        most_word = ch

    elif count > second_freq and count < most_freq:
        second_freq = count
        second_word = ch


print("Most frequent:", most_word, most_freq)
print("Second most:", second_word, second_freq)

s = "apple banana apple orange banana apple orange orange"
words = s.split()
freq = {}

most_freq = 0
most_word = ""

sec_freq = 0
sec_word = ""

for ch in words:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

for ch in freq:
    if freq[ch] > most_freq:
        sec_freq = most_freq
        sec_word = most_word

        most_freq = freq[ch]
        most_word = ch
    elif freq[ch] > sec_freq and freq[ch] < most_freq:
        sec_freq = freq[ch]
        sec_word = ch     
        
print("Most frequent:", most_word, most_freq)
print("Second most:", sec_word, sec_freq)

# ✅ Problem 3: Longest Substring Without Repeating Characters
# Task: Find length of longest substring with unique characters.
# Input: "abcabcbb"
# Output: 3   ("abc")