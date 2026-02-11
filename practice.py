# Average oa All SubArrays of Size K
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
window_sum = sum(arr[:k])
result = [window_sum / k]

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    result.append(window_sum / k)

print(result)

word = "reviver"
is_palindrome = True

for i in range(len(word)//2):
    if word[i] == word[-i -1]:
        pass
    else:
        is_palindrome = False
        break
print(is_palindrome)

# count vowels
s = "educationeefdewasxscsfuiouiuhj"
vowels = "aeiou"
count = 0

for t in s:
    if t in vowels:
        count+=1
print(count)

# # ✅ Problem 3: Reverse Words in a String
import string
s = "learn python daily"
words = s.split()
print(words)
words.reverse()
# result = " ".join(words)
result = " ".join(s.split()[::-1])
print(result)

# Problem 4: First Non-Repeating Character
# Input: "aabbcdde"
# Output: "c"

s =  "aabbcdde"

for t in s:
    if s.count(t) == 1:
        print(t)
        print(s.index(t))
        break
# Problem 5: Remove Duplicate Characters
# Input: "programming"
# Output: "progamin"
s = "programming"
seen = set()
result = ""
for ch in word:
    if ch not in seen:
        seen.add(ch)
        result += ch
print(result)

# Problem 4: Capitalize Each Word
# Input: "learn python daily"
# Output: "Learn Python Daily"

Input = "learn python daily"
input_split = Input.split()
result = ""
for w in input_split:
    output = w.capitalize()
    result += output + " "
print(result)

# Problem 5: Check Rotation
# Input: "abcd", "cdab"
# Output: True

s1 = "abcd"
s2 = "cdab"

if s2 in (s1+s2):
    print(True)
else:
    print(False)