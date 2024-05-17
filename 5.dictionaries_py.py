# lets take   example  why wee need dictionaries

marks_list = ['rachel',12,'varun',19,'sujal',8]
print(marks_list)
# now if  we want to print name and marks of 2nd student

print(marks_list[1])

# we can see it is only giving 12 by which one cannot identify the student

# so here the concept of dictionaries

marks_dict = {'varun':20 , 'harsh':22 , 'jayant':21}
print(marks_dict)
# now we can get the marks by name
print(marks_dict['varun'])

# to update any value
marks_dict['varun']=29
print(marks_dict['varun'])


# length of dictioanry
print(len(marks_dict))

#  to delete any entry
del marks_dict['varun']
print(marks_dict)
print(len(marks_dict))
