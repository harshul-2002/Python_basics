

#  try and error are used in section of program where an error can be raised 

#  for example lets   preint a name without intitializinf it 

try:
    if name == "harsh":
        print(f"hello {name}")
except:
    print("you did not defined the name") 

name = "harsh"           
