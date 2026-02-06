# 1️⃣ Count Word Frequency
s = "learn python learn dsa"
words = s.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print(freq)

# 2️⃣ Find the Most Frequent Character
s = "success"
freq = {}
most_freq_char = ""
most_freq = 0
for w in s:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
for w in freq:
    if freq[w] > most_freq:
        most_freq = freq[w]
        most_freq_char = w

print(f"{most_freq_char} : {most_freq}")

# 3️⃣ Check if Two Strings Are Anagrams (basic)
s1 = "listen"
s2 = "silent"

freq1 = {}
freq2 = {}
is_anagrams = True

for w in s1:
    if w in freq1:
        freq1[w] += 1
    else:
        freq1[w] = 1

for w in s2:
    if w in freq2:
        freq2[w] += 1
    else:
        freq2[w] = 1  
print(freq1)
print(freq2)
if freq1 == freq2:
    print(is_anagrams)
else:
    print(is_anagrams = "False")
# for ch in s1:
#     if freq1[ch] == freq2:
#         print(True)
#     else:
#         print(False)

# 4️⃣ Find First Repeating Element

arr = [10, 5, 3, 4, 3, 5, 6]
seen = set()

for n in arr:
    if n in seen:
        print(n)
        break
    seen.add(n)

# 5️⃣ Check if Array Has Unique Elements
arr = [1, 2, 3, 4]
seen = set()
is_unique = True
for n in arr:
    if n not in seen:
        seen.add(n)
if len(seen) == len(arr):
    print(is_unique)
else:
    print(False)
# 6️⃣ Find Pair With Given Sum (Two Sum variation)
arr = [8, 7, 2, 5, 3, 1]
target = 10
var = {}
for i,n in enumerate(arr):
    rem = target - n
    if rem in var:
        print(var[rem], i)
        break
    var[n] = 1
# 7️⃣ First Non-Repeating Character
s = "aabbccd"
fir_non_rep = {}

for w in s:
    if w in fir_non_rep:
        fir_non_rep[w] += 1
    else:
        fir_non_rep[w] = 1
for w in fir_non_rep:
    if fir_non_rep[w] == 1:
        print(w)
        break
# 8️⃣ Count Frequency of Numbers
arr = [1, 2, 2, 3, 1, 1]
count_freq = {}

for i in arr:
    if i in count_freq:
        count_freq[i] += 1
    else:
        count_freq[i] = 1
print(count_freq)