


# placeholders

name= "jake"
sentence = "is 10 yr old"
print(name+" "+sentence)

#  the above example is for simple string

#  now if we proceed using placeholders we  use  %s sign for string and  %d for integers
# for eg

place_holder =" %s %s is 10 yr old"
print(place_holder % ("harsh" , "kumar"))

# now for integer

integer_holder =" %s %s is %d yr old"
print(integer_holder % ("varun","punia",20))

# format string

name="jayant aggarwal"
print(f"Hello mr. {name}")

# example 2 

a,b = 31,49
print(f"the sum of a & b is {a+b}")





