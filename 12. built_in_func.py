#   built in fucntions

# absoulute function 
  
num = -19772
print(abs(num))

# bool function
num = 9378348
print(bool(num)) #true

#  dir func

print(dir("hello"))

# [ '__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#   '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
#   '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
#   '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
#   'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
#   'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
#   'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
#   'swapcase', 'title', 'translate', 'upper', 'zfill'
# ]

#  it gives all the method that can be applied on that parameter of dir


print(help("hello".upper))


s="hello"

print(s.upper())


print(s + str(100))

print(200 + int("100"))