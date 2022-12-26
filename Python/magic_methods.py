class magic_methods:
    
    def __new__(cls, x): # called before __init__ and is used to control the creation of a new instance
        print("__new__")
        inst = object.__new__(cls)
        return inst
    
    def __init__(self, x): # called on instantiation of class and is used to control the initialization of a new instance
        self.x = x
        print("__init__")
        
        
    # __int__ int(magic_methods)
    # __float__ float(magic_methods)
    # __complex__ complex(magic_methods)
    # __oct__ oct(magic_methods)
    # __hex__ hex(magic_methods)
    # __index__ list[:magic_methods] used when object is in a slice expression
    def __str__(self): # used when converting class to string str(magic_methods)
        return "string"
    # __repr__ repr(magic_methods)
    # __len__ len(magic_methods)
    # __unicode__ unicode(magic_methods)
    # __format__ string.format(magic_methods)
    # __hash__ hash(magic_methods)
    # __nonzero__ bool(magic_methods)
    # __dir__ dir(magic_methods)
    # __sizeof__ sys.getsizeof(magic_methods)
    
    # __pos__ +magic_methods
    # __abs__ abs(magic_methods)
    # __invert__ ~magic_methods
    # __round__ round(magic_methods)
    # __floor__ math.floor(magic_methods)
    # __ceil__ math.ceil(magic_methods)
    # __trunc__ math.trunc(magic_methods)
    def __neg__(self): # used when class is negative -magic_methods
        return -5
    #__contains__ magic_methods in magic_methods
    
    # __sub__ magic_methods - magic_methods
    # __mul__ magic_methods * magic_methods
    # __floordiv__ magic_methods // magic_methods
    # __truediv__ magic_methods / magic_methods
    # __mod__ magic_methods % magic_methods
    # __power__ magic_methods ** magic_methods
    def __add__(self, other): # used when + operator is used on class magic_methods + magic_methods
        if type(other) is magic_methods:
            return self.x + other.x
        return self.x
    # __iadd__ magic_methods += magic_methods
    # __isub__ magic_methods -= magic_methods
    # __imul__ magic_methods *= magic_methods
    # __ifloordiv__ magic_methods //= magic_methods
    # __idiv__ magic_methods /= magic_methods
    # __imod__ magic_methods %= magic_methods
    # __ipow__ magic_methods **= magic_methods
    # __ilshift__ magic_methods <<= magic_methods
    # __irshift__ magic_methods >>= magic_methods
    # __iand__ magic_methods &= magic_methods
    # __ior__ magic_methods |= magic_methods
    # __ixor__ magic_methods ^= magic_methods
    
    # __lt__ magic_methods < magic_methods
    # __gt__ magic_methods > magic_methods
    # __le__ magic_methods <= magic_methods
    # __eq__ magic_methods == magic_methods
    # __ne__ magic_methods != magic_methods
    def __ge__(self, other): # used when >= operator is used on class magic_methods >= magic_methods
        if type(other) is magic_methods:
            return self.x >= other.x
    
    def __getattr__(self, attr): # called when trying to access an attribute that does not exist
        print("Attribute does not exist")
    
    def __getitem__(self, index): # gets item at class index magic_methods[i]
        return index
    
    def __setitem__(self, index, item): # sets item at class index magic_methods[i] = x
        self.x = item
        
    def __enter__(self): # called when with magic_method()) as x starts
        print("entered")
        
    def __exit__(self, exc_type, exc_val, exc_tb): # called when with magic_method()) as x exits
        print("exited")
        
    def __call__(self, x):
        return self.x + x
    
    def __del__(self):
        print("__del__")
        
magic = magic_methods(5)
magic2 = magic_methods(10)
print(str(magic)) # string
print(magic + magic2) # 15
print(magic + 2) # 5
print(magic >= magic2) # False
print(-magic) # -5
magic.totallyRealAttribute
print(magic[3]) # 3
with magic_methods(7) as method:
    ...
print(magic(1)) # 6