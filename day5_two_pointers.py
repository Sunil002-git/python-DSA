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
    	
