# Problem 1: Maximum Sum of Subarray of Size K
arr = [2, 6, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    max_sum = max(window_sum, max_sum)

print(max_sum)

arr = [1,4,2,10,23,3,1,0,20]
k = 4

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum  = window_sum + arr[i] - arr[i-k]
    max_sum = max(window_sum, max_sum)
print(max_sum)

# Average oa All SubArrays of Size K
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
window_sum = sum(arr[:k])
result = [window_sum / k]

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    result.append(window_sum / k)

print(result)

# Maximum Sum Subarray of Size k
# arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
# k = 3
arr = [3, 4, 1, 1, 6]
k = 2

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    max_sum = max(window_sum, max_sum)
print(max_sum)

# Practice Set 2 — Window + Count
# Count Subarrays of Size k With Sum > X
arr = [2, 1, 5, 1, 3, 2]
k = 3
x = 7
count = 0

window_sum = sum(arr[:k])
max_sum = window_sum
if window_sum > x:
    count += 1
for i in range(k, len(arr)):
    if window_sum > x:
        count += 1
    window_sum = window_sum + arr[i] - arr[i-k]
    max_sum = max(window_sum, max_sum)

print(count)

# 4️⃣ Find Maximum Average Subarray of Size k
arr = [1, 12, -5, -6, 50, 3]
k = 4
window_sum = sum(arr[:k])
result = [window_sum/k]

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    result.append(window_sum/k)
print(max(result))
# max_avg = window_sum / k

# for i in range(k, len(arr)):
#     window_sum = window_sum + arr[i] - arr[i-k]
#     max_avg = max(max_avg, window_sum / k)

# print(max_avg)

# Maximum Sum of k Consecutive Characters (ASCII)
s = "abcde"
k = 2
# output : 201   # 'de'
result = []
for i in s:
    print(ord(i))
    result.append(ord(i))

print(result)

window_sum = sum(result[:k])
max_sum = window_sum

for i in range(k, len(result)):
    window_sum = window_sum + result[i] - result[i-k]
    max_sum = max(window_sum, max_sum)
print(max_sum)

# Interview Thinking (Say This Aloud)

# For every problem, say:

# “I calculate the first window, then slide it by adding the next element and removing the previous one, which keeps the time complexity O(n).”
# 1️⃣ Why sliding window instead of nested loops?

# Answer:

# Sliding window avoids recalculating the same work again and again.
# Instead of using nested loops with O(n²) time, it reuses the previous window’s result and solves the problem in O(n) time.

# Strong one-liner:

# “Sliding window optimizes repeated subarray calculations.”

# 2️⃣ When does sliding window NOT work?

# Answer:

# Sliding window does not work when the window size is not controllable, the problem requires checking all combinations, or when elements cannot be added and removed incrementally.

# Examples:

# Finding all subsets

# Problems with non-linear conditions

# When shrinking/expanding window logic is unclear

# Interview closing line:

# “In such cases, brute force or other data structures are more suitable.”

# 3️⃣ Difference between two pointers and sliding window?

# Answer:

# Two pointers:

# A general technique using two indices

# Can move independently

# Used for symmetry, filtering, or comparisons

# Sliding window:

# A special case of two pointers

# Maintains a window of elements

# Reuses previous computation

# Strong interview sentence:

# “Sliding window is a specialized form of two pointers optimized for subarray or substring problems.”

# 4️⃣ Time & space complexity?

# Answer:

# Sliding window solutions run in O(n) time because each element enters and leaves the window once, and O(1) space because no extra data structures are required.

# If storing results:

# Space can become O(n) depending on output requirements.
# Interview Power Tip (Use This)

# End your explanation with:

# “This approach is optimal for this problem.”

# That signals confidence and maturity.