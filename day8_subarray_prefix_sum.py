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