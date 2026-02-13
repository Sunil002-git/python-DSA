# Brute Force
arr = [1,1,1]
k = 2

count = 0

for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        if current_sum == k:
            count+=1
print(count)
# Practice 1 — Count Subarrays With Sum = K
arr = [1,1,1]
k = 2

prefix_sum = 0
count = 0
prefix_map = {0:1}

for num in arr:
    prefix_sum += num
    diff = prefix_sum - k

    if diff in prefix_map:
        count += prefix_map[diff]
    
    prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
print(count)

arr = [1, 2, 3]
k = 3

prefix_sum = 0
prefix_map = {0:1}
count = 0

for num in arr:
    prefix_sum += num
    diff = prefix_sum - k
    if diff in prefix_map:
        count += prefix_map[diff]

    prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
print(count)

# Practice 2 — Works With Negative Numbers
arr = [1, -1, 0]
k = 0
prefix_sum = 0
prefix_map = {0:1}
count = 0

for num in arr:
    prefix_sum += num
    diff = prefix_sum - k
    if diff in prefix_map:
        count += prefix_map[diff]
    prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
print(count)

# Practice 3 — Longest Subarray With Sum = K
arr = [1, -1, 5, -2, 3]
k = 3

prefix_sum = 0
first_index = {0: -1}
max_len = 0

for i , num in enumerate(arr):
    prefix_sum += num
    diff = prefix_sum - k

    if (diff) in first_index:
        max_len = max(max_len, i - first_index[diff])
    
    if prefix_sum not in first_index:
        first_index[prefix_sum] = i
print(max_len)
# Practice 4 — Check If Subarray With Sum = K Exists

arr = [10, 2, -2, -20, 10]
k = -10
total = 0
seen = {0}

for num in arr:
    total += num
    diff = total - k
    if diff in seen:
        exists = True
        break
    seen.add(num)
print(exists)

# Total so far = ?
# I need = total - ?
# Store = sum / index / count ?

# For “Count”
# map[0] = 1
# if total-k in map:
#     count += map[total-k]

# For “Longest”
# store first index only
# length = i - old_index

# For “Exists”
# use set
# if total-k in set: True

# LEVEL 1 — Basic (Warm Up)
# Subarray Sum Equals K (Count)
arr = [1,2,3]
k=3
# Find: Number of subarrays
count = 0
prefix_sum = 0
prefix_map = {0:1}

for num in arr:
    prefix_sum += num
    diff = prefix_sum - k
    if diff in prefix_map:
        count += prefix_map[diff]
    prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
print(count)
# 2️⃣ Check If Subarray With Sum = K Exists

arr =  [4,2,-3,1,6]
k=0
seen = {0}
# Find: True/False
sub_sum = 0
for num in arr:
    sub_sum += num
    diff = sub_sum - k
    if diff in seen:
        exists = True
        break
    seen.add(num)
print(exists)

# LEVEL 2 — Intermediate
# 3️⃣ Longest Subarray With Sum = K

arr = [1,-1,5,-2,3]
k=3
# Find: Length

# 💡 Hint: Store first index of each prefix sum.
max_len = 0
first_index = {0:-1}
total = 0
for i,num in enumerate(arr):
    total += num
    diff = total - k
    if diff in first_index:
        max_len = max(max_len , i - first_index[diff])
    
    if total not in first_index:
        first_index[total] = i
print(max_len)

# 4️⃣ Count Subarrays With Sum = 0

# Input: [0,0,0]
# Find: Count

# 💡 Hint: Many prefix sums repeat.
arr = [0,0,0]
k = 0
count = 0
prefix_map = {0:1}
prefix_sum = 0

for n in arr:
    prefix_sum += n
    diff = n - k
    if diff in prefix_map:
        count += prefix_map[diff]
    
    prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
print(count)

# Count Subarrays With Sum Divisible by K

# Input: [4,5,0,-2,-3,1], k=5

# 💡 Hint: Use prefix % k.
arr = [4,5,0,-2,-3,1]
k=5
count = 0
prefix_map = {0:1}
prefix_sum = 0
for n in arr:
    prefix_sum += n
    div = prefix_sum % k
    
    count += prefix_map.get(div, 0)
    prefix_map[div] = prefix_map.get(div, 0) + 1
print(count)
# If two prefix sums have the same remainder mod k, their difference is divisible by k.

# 🟠 LEVEL 3 — Tricky
# 6️⃣ Maximum Length Subarray With Equal 0s and 1s
# Input: [0,1,0,1,1,1,0]
# 💡 Hint: Replace 0 → -1 first.

# 7️⃣ Find Subarray With Given Sum (Print Indices)
# Input: [10,2,-2,-20,10], k=-10
# 💡 Hint: Store prefix sum → index.
arr = [10,2,-2,-20,10]
k = -10
prefix_map = {0:-1} 
prefix_sum = 0
for i,n in enumerate(arr):
    prefix_sum += n
    if (prefix_sum - k) in prefix_map:
        start = prefix_map[prefix_sum - k] + 1
        end = i
        print(start, end)
        print(arr[start:end+1])
        break
    if prefix_sum not in prefix_map:
        prefix_map[prefix_sum] = i



# 🔴 LEVEL 4 — Challenge
# 8️⃣ Count Subarrays With Sum in Range [L, R]
# Input: [1,2,3,4], L=3, R=6
# 💡 Hint: Use prefix + counting.



# 1) Why prefix sum instead of sliding window?

# Sliding window works when the window sum changes monotonically as you move pointers (usually when all numbers are non-negative and you’re looking for exact sum or ≤/≥ constraints).

# Here the condition is:
# subarray sum % k == 0 (divisible by k)

# With divisibility (and also with negatives), moving left/right doesn’t give a predictable “sum gets bigger/smaller” behavior. You can’t decide “shrink or expand” based on current sum.
# So sliding window can miss answers.

# Prefix sum + remainders works because:

# Let prefix[i] be sum up to i

# Subarray sum (l..r) = prefix[r] - prefix[l-1]

# If (prefix[r] - prefix[l-1]) % k == 0 ⇒ prefix[r] % k == prefix[l-1] % k
# So we just count equal remainders.

# 2) Why initialize {0:1}?

# prefix_map = {0:1} means:

# “We have seen remainder 0 once before starting (empty prefix).”

# This is needed to count subarrays that start at index 0.

# Example: arr = [5], k=5

# prefix_sum = 5, remainder = 0

# We should count subarray [5] as valid.
# If {0:1} isn’t there, you’d miss it.

# In general: whenever current prefix remainder is 0, it forms a valid subarray from start.

# 3) What happens with negative numbers?

# Negatives break many sliding-window approaches (no monotonic property).

# Prefix remainder method still works with negatives because the math property is always true:
# (a - b) % k == 0 ⇔ a%k == b%k.

# In Python, prefix_sum % k is already in 0..k-1 even if prefix_sum is negative, so it’s safe.

# (If you were in languages where % can be negative, you’d normalize with:)

# rem = ((prefix_sum % k) + k) % k