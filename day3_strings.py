# word = "reviver"
# is_palindrome = True
# for i in range(len(word)//2):
#     if word[i] == word[-i-1]:
#         pass
#     else:
#         is_palindrome = False
#         break
# print(is_palindrome)

# # arr = ["s", "u", "n", "i", "l"]

# # for i in range(len(arr)):
# #     print(i)
# #     print(arr[i])

# # Count Vowels

# s = "educationeefdewasxscsfuiouiuhj"
# vowels = "aeiou"
# count = 0

# for w in s:
#     if w in vowels:
#         count += 1
# # for w in s:
# #     if w not in vowels:
# #         pass
# #     else:
# #         count += 1

# print(count)


# # ✅ Problem 3: Reverse Words in a String
# import string
# s = "learn python daily"
# words = s.split() # makes list of separarated words ["daily", "python", "learn"]
# words.reverse()
# result = " ".join(words)
# print(result)

# # alternate solution
# s = "learn python daily"

# result = " ".join(s.split()[::-1])
# print(result)

# Problem 4: First Non-Repeating Character
# Input: "aabbcdde"
# Output: "c"
 
input_word = "aabbcdde"


for i in input_word:
    if input_word.count(i) == 1:
        print(i)
        print(input_word.index(i))
        break
# Problem 5: Remove Duplicate Characters
# Input: "programming"
# Output: "progamin"
word = "programming"
seen = set()
result = ""

for ch in word:
    if ch not in seen:
        seen.add(ch)
        result += ch
print(result)

word = "programming"
result = []

for ch in word:
    if ch not in result:
        result.append(ch)
        
print(result)
print("".join(result))

# Problem 1: Count Words
# Input:  "I am learning django"
# Output: 4

sentance = "I am learning django"
count = len(sentance.split())
print(count)

# ✅ Problem 2: Check Anagram
# Input: "listen", "silent"
# Output: True

input1 = "listen"
input2 = "silent"
if sorted(input1) == sorted(input2):
    print(True)
else:
    print(False)

# Problem 3: Longest Word
# Input: "I love learning python daily"
# Output: learning

word = "I love learning python daily"
words = word.split()
longest_word = words[0]
for w in words:
    print(f"{w} : {len(w)}")
    if len(w) > len(longest_word):
        longest_word = w
print(longest_word)

# Problem 4: Capitalize Each Word
# Input: "learn python daily"
# Output: "Learn Python Daily"

Input = "learn python daily"
Input_split = Input.split()
result = ""
for w in Input_split:
    output = w.capitalize()
    result += output + " "
print(result)

# Problem 5: Check Rotation
# Input: "abcd", "cdab"
# Output: True

s1 = "abcd"
s2 = "cdab"

if s2 in (s1 + s2):
    print(True)
else:
    print(False)

#Interview Questions
# 1️⃣ Why can’t we modify a string directly?

# Because strings in Python are immutable.

# That means:

# Once a string is created, it cannot be changed in place

# Any “modification” actually creates a new string
# s = "hello"
# s[0] = "H"   # ❌ Error

# 2️⃣ Time complexity of palindrome check?

# For the palindrome logic we used:

# for i in range(len(s)//2):
#     if s[i] != s[-i-1]:
#         return False


# We check half of the string

# Each comparison is O(1)

# So:

# Time Complexity: O(n)

# Space Complexity: O(1) (no extra memory)

# 💬 Interview answer:

# “Palindrome check takes O(n) time and constant space.”
# 3️⃣ Difference between iterating a string vs a list?
# Similarity:

# Both are iterable

# Both support indexing and loops

# Key Differences:
# Aspect	String	List
# Mutability	❌ Immutable	✅ Mutable
# Modify element	❌ Not allowed	✅ Allowed
# Use case	Text processing	Data storage

# Example:

# lst = [1, 2, 3]
# lst[0] = 10   # ✅ works

# s = "abc"
# s[0] = "x"    # ❌ error


# 💬 Interview answer:

# “Iteration is similar, but strings are immutable while lists are mutable.”

# 4️⃣ Can we solve palindrome using two pointers?

# YES — and this is a strong interview approach.

# 🧠 Idea:

# One pointer at start

# One pointer at end

# Move inward

# 🧪 Python Code:
# s = "madam"

# left = 0
# right = len(s) - 1
# is_palindrome = True

# while left < right:
#     if s[left] != s[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1

# print(is_palindrome)

# Complexity:

# Time: O(n)

# Space: O(1)

# 💬 Interview answer:

# “Yes, using two pointers starting from both ends and moving inward.”