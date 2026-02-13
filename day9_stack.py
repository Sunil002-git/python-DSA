# Stack : Last in First Out
s = "()[]{}"
stack = []

pairs = {')' : '(', ']' : '[', '}' : '{'}

for ch in s:
    if ch in pairs.values():
        stack.append(ch)
    else :
        if not stack or stack[-1] != pairs[ch]:
            print(False)
            break
        stack.pop()
print(not stack)

s = "([])"
match = {')' : '(', ']' : '[', '}' : '{'}
stack = []

for ch in s:
    if ch in match.values():
        stack.append(ch)
    else:
        if not stack or stack[-1] != match[ch]:
            print(False)
            break
        stack.pop()
else: 
    print (not stack)
print("sunil")

s= "(()"
stack = []
pairs = {')' : '('}

for ch in s:
    if ch in pairs.values():
        stack.append(ch)
    else :
        if not stack or stack[-1] != pairs[ch]:
            print(False)
            break
        stack.pop()
else:
    print(not stack)

s = "(()())(())"

match = {')' : '('}

depth = 0
result = []
for ch in s:
    if ch in match.values():
        depth += 1
        if depth > 1:
            result.append(ch)
    else :
        if not result :
            print(False)
            break
        depth -= 1
        if depth > 0:
            result.append(ch)
print("".join(result))

# Practice Set 2 — Next Greater Element
arr = [4, 5, 2, 10, 8]
# brute force
n = len(arr)

result = [-1] * n

for i in range(n):
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            result[i] = arr[j]
            break
print(result)


# Practice Set 2 — Next Greater Element
# 3️⃣ Next Greater Element (Right Side)
arr = [4, 5, 2, 10, 8]
n = len(arr)
stack = [] # stores indices 
result = [-1] * n

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        result[idx] = arr[i]
    stack.append(i)
print(result)
# 4️⃣ Next Greater Element (Circular Array)
arr = [1 ,2 , 1]
n = len(arr)

result = [-1]*n
stack = []
for i in range(2 * n):
    curr = arr[i % n]
    while stack and curr > arr[stack[-1]]:
        idx = stack.pop()
        result[idx] = curr
    if i < n:
        stack.append(i)
print(result)
# Practice Set 3 — Stack for Evaluation
# Evaluate Postfix Expression
exp = ["2","1","+","3","*"]
# output : 9
stack = []

for i in exp:
    if i.isdigit():
        stack.append(int(i))
    else:
        b = stack.pop()
        a = stack.pop()
       
        if i == "+":
            stack.append(a + b)
        elif i == "-":
            stack.append(a - b)
        elif i == "*":
            stack.append(a*b)
        elif i == "/":
            stack.append(int(a/b))
print(stack[-1])

# Bonus (Optional but Good)
# 5️⃣ Min Stack (Design Problem)

# Design a stack that supports:

# push
# pop
# getMin() in O(1)
# This is a classic interview problem.

class MinStack:
    def  __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, x):
        self.stack.append(x)

        if not self.min_stack:
            self.min_stack.append(x)
        else :
            self.min_stack.append(min(x, self.min_stack[-1]))
    def pop(self):
        if not self.stack:
            raise IndexError("Pop from empty stack")
        self.min_stack.pop()
        return self.stack.pop()
    def top(self):
        if not self.stack:
            raise IndexError("Pop from empty stack")
        return self.stack[-1]
    def getMin(self):
        if not self.min_stack:
            raise IndexError('getMin from Empty stack')
        return self.min_stack[-1]

s = MinStack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)

print("Top:", s.top())
print("Min:" , s.getMin())
print("Pop" , s.pop())
print("Top:", s.top())
print("Min:" , s.getMin())

# Topic: Stack Practice

# Patterns:
# - Matching parentheses
# - Monotonic stack (next greater element)
# - Expression evaluation

# Mistakes:
# (popping empty stack / wrong order)

s = "{[()()]}"
match = {')':'(', '}':'{', ']':'['}
stack = []

for ch in s:
    if ch in match.values():
        stack.append(ch)
    else:
        if not stack or stack[-1] != match[ch]:
            print(False)
            break
        stack.pop()
else:
    print(not stack)

# Simplify Path (Unix Style) path = "/a/./b/../../c/" Return: "/c"
path = "/a/./b/../../c/"
path_split = path.split("/")

stack = []

for ch in path_split:
   
   if ch == "." or ch == "":
       continue
   elif ch == "..":
       if stack:
           stack.pop()
   else:
       stack.append(ch)

result = "/" + "/".join(stack)
print(result)

path = "/a/./b/../../c/"

parts = path.split("/")   # split by /
stack = []

for part in parts:

    if part == "" or part == ".":
        # ignore empty and current folder
        continue

    elif part == "..":
        # go back
        if stack:
            stack.pop()

    else:
        # normal folder
        stack.append(part)

# build result
result = "/" + "/".join(stack)

print(result)

# 3️⃣ Remove Adjacent Duplicates 
s = "abbaca"
# Return: "ca"
# Explanation: Remove "bb" Then remove "aa"
stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)
print("".join(stack))

