# Variable length parameters
def languages(**kwargs):
    for item in kwargs:
        print(item) # functional # object_oriented
        print(kwargs[item]) # F# # java
        
languages(functional = 'F#', object_oriented = 'java')
language = {'functional': 'F#', 'object_oriented': 'java'}
languages(**language) # Same output as previous line