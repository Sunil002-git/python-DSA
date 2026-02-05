#min value
# arr = [100, 200, 300, 400, 500]
# min_val = float('inf')

# for x in arr:
#   if x < min_val :
#     min_val = x
        
# print(min_val)

arr = [10, 5, 20, 8]

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(second)
print(largest)
arr = [10, 5, 20, 8]


# time : O(n)
# space : O(1)

# Remove Duplicates (preserve Order)
 
arr = [1,2,2,3,1,4]
seen = set()
result = []

for num in arr:
    if num not in seen:
        result.append(num)
        seen.add(num)
print(result)
print(seen)
# time : O(n)
# space : O(n)

# Problem 3: Left Rotate Array by 1
arr = [1,2,3,4,5]
first = arr[0]

for i in range(len(arr)-1):
    arr[i] = arr[i]+1
arr[-1] = first
print(arr)

# last = arr[-1]
# for i in range(len(arr)-1, 0, -1):
#     print (arr[i])
#     # print(arr[i-1])
#     arr[i] = arr[i-1]
# arr[0] = last
# print(arr)

# time : O(n)
# space : O(1)
# ⏱️ PART 3 — Interview Questions to Answer (15 min)

# Answer aloud:

# Why not sort for second largest?
# I'm Avoiding sort to keep it O(1)
# with sorting : 
# arr = [1,4,6,7,9,8]
# arr.sort()
# second_largest = arr[-2]
# print(second_largest)

# What happens if array has all same values?
# The results will be same for some and not possible for some ex: second largest
# Time & space complexity of each problem?
# Mentioned above
# Can you do remove duplicates without set? (Think!)
# arr = [1, 2, 2, 3, 1, 4]
# result = []

# for i in arr:
#   if i not in result:
#     result.append(i)
        
# print(result)

# Pattern : Simple Traversal + extensions
# use : Visit all elements
# When : Find something special in an array 
# Template: for i in range(len(arr))
# Mistake :     Nested Loops