print(ord('s'))
print(ord('u'))
print(ord('n'))
print(ord('i'))
print(ord('l'))

print(chr(65))
print(chr(97))
print(chr(115))
print(chr(126))

# ✅ 3️⃣ Why ASCII Is Important in DSA

# ASCII helps you in:

# ✔️ Character comparisons
# ✔️ Sorting strings
# ✔️ Encryption
# ✔️ Hashing
# ✔️ Case conversion
# ✔️ Frequency arrays
# 1. Compare Characters
print('a' > 'A')
print(ord('a'))
print(ord('A'))

# 2. Convert Lowercase <-> Uppercase (Without built in)
ch = 'a'
upper = chr(ord(ch) - 32)
print(upper)
# upper to lower
ch = 'A'
lower = chr(ord(ch) + 32)
print(lower)

# Frequency Array Using ASCII (Very Important)
# Example: Count lowercase letters.

s = "banana"

freq = [0]*26

for ch in s:
    index = ord(ch) - ord('a')
    freq[index] += 1

print(freq)

# Check If Character Is Alphabet / Digit 
# Without using .isalpha()

ch = 'G'

if ord('A') <= ord(ch) <= ord('Z') or ord('a') <= ord(ch) <= ord('z'):
    print("Alphabet")

ch = '5'
if ord('0') <= ord(ch) <= ord('9'):
    print("Digit")

# ASCII vs Unicode (Don’t Worry Much Now)

# ASCII: 0–127 (English only)
# Unicode: All languages (Python uses Unicode)

# But in DSA, mostly ASCII is enough.
# Easy Way to Remember
# 'A' -> 65
# 'a' -> 97
# '0' -> 48
s = "aB3cD@e"

freq = [0]*26

for ch in s:
    if 'a' <= ch <= 'z':
        index = ord(ch) - ord('a')
        freq[index] += 1

print(freq)