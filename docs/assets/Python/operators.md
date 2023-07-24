---
layout: script
language: Python
---

`is` is used to check if two variables are the same object. Often used to check if a variable is `None`.

```python
import math
print('# is #')# is #

# immutable
a = 100
b = 100
print(a is b) # True

# mutable
a = [100, 200, 300]
b = [100, 200, 300]
print(a is b) # False # a is not b 
print(a == b) # True  # but a is equal to b 

# is not #
a = 100
b = a
print(a is not b) # False
```

`and` can be used to make sure a variable has a valid value before performing a operation. Valid value meaning not 0, an empty list, or None.

```python
print('# and #')# and #

a = True
b = False
print(a and b) # False
a = 10
b = 5
print(a and b) # 5
# and operator returns a if it is false otherwise it returns b

# and short circuits
True and print("short circuit") # short circuit
False and print("short circuit") #
try:
    a = 10
    b = 0
    c = a/b
except Exception as e:
    print(e) # division by zero
    a = 10
    b = 0
    c = b and a/b # since b is 0 (which is false) the and operator short circuits and returns 0 
    print(c) # 0
```

`or` can be used as a back up value if the first value is `False` (0, empty list, or None).

```python
print('# or #')# or #

a = True
b = False
print(a or b) # True
lang = None or 'Python'
print(lang) # Python
lang = 'Java' or 'Python'
print(lang) # Java

print('# floor and modulo #')# floor and modulo #

# floor
print(101/4) # 25.25
print(101//4) # 25

print(10/3) # 3.333
print(10//3) # 3
print(math.floor(3.3)) # floor rounds down so 3.3 becomes 3 # 3

print(-10/3) # -3.33
print(-10//3) # -4
print(math.floor(-3.3)) # floor rounds down so -3.3 becomes -4 # -4
```

Modulo is used to get the reminder of a division operation.

```python
# modulo

print(10 % 4) # 2

print(2451 % 1) # 0
print(2451 % 10) # 1
print(2451 % 100) # 51

seconds = 100000
print("Days: "+str(int(seconds/60/60/24))) # 1
print("Hours: "+str(int(seconds/60/60)%24)) # 3
print("Minutes: "+str(int(seconds/60)%60)) # 46
print("Seconds: "+str(seconds%60)) # 40

# tilde

print(~5) # -6

# it is the same as -x -1

numbers = [1,2,3,4,5]
for i in range(len(numbers)):
    temp = numbers[i]
    numbers[i] = numbers[~i]
    numbers[~i] = temp

```