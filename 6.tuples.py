# tuples in pyhton


#  tuples are immutable  mean they can be modified once they created
#  tuples are donated using closed paranthesis

fruit_tuple = ('oranges' , 'litchi' , 'dragon fruit' , 'apple' , 'pine apple' , 'strawberry')

print(fruit_tuple)

# now as  tuple are immmutable  if we  try to change an entry it will give an error

#                    for eg chnging litvchi into cherry

#                    fruit_tuple[1] = "cherry"

#                    and the error is      

#                    File "c:\Users\Harsh kumar\OneDrive\Desktop\PYTHON-P\6.tuples.py", line 15, in <module>
#                     fruit_tuple[1] = "cherry"
#                     ~~~~~~~~~~~^^^
#                    TypeError: 'tuple' object does not support item assignment



# accessing tuple values which is similar to lists

print(fruit_tuple[0])
print(fruit_tuple[1])
print(fruit_tuple[2])
print(fruit_tuple[0:2])
print(fruit_tuple[1:2])
print(fruit_tuple[0:3])

price_tuple = (12, 24, 56, 67, )

#  conactenation of two tuples
main_tuple = fruit_tuple + price_tuple
print(main_tuple)




