# unpacking a function
nums = [0, 5, 7, 2]
print(nums) # [0, 5, 7, 2]
print(*nums) # 0 5 7 2

# arbitrary number of function parameters for non-key arguments and variable-length argument lists
def addition(*args):
    return sum(args)

print(addition(1, 2, 3, 4, 5)) # 15

def add(a, b):
    return a, b

nums = [2, 3]
print(add(*nums)) # 5

# Variable length parameters
def languages(**kwargs):
    for item in kwargs:
        print(item) # functional # object_oriented
        print(kwargs[item]) # F# # java
        
languages(functional = 'F#', object_oriented = 'java')
language = {'functional': 'F#', 'object_oriented': 'java'}
languages(**language)

nums = [5, 6]
def add(x, y):
    return x + y

print(add(*nums)) # 11

# Exponent
print(2**3) # 8