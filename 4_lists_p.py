


#  lists in python

# the vanilla way to create a list of fruit itme is  simple by creatung each fruit by hand

f_1 ="apple"
f_2="pine"
# ....
# ....
f_n="last fruit in list"

# so this will take alot of time

#  no by using lists 

fruits= ["apple","pine apple","dragon fruit","kiwi","strawberry","cherry"]

print(fruits) 
# the will simple print the  square bracket along withnvalues 
#  lets see how can we access the values

# for item-1
print(fruits[0])

# for item-4
print(fruits[4])

# slicing in list
print(fruits[0:4])

#  now to add item in list simply use  .append
fruits.append("peaches")
print(fruits)

#  to change item
fruits[2]="grapes"
print(fruits)
#  we can see that dragon is chnged to grapes

# to delete item 
del fruits[0]
print(fruits)

# to find the length of list
print(len(fruits))

# we can also add/join lists together 
vegetable=['tomato','potato','onion','garlic']
wt=[1,2,3,4,5]
print(fruits + wt + vegetable)

# for repetiveness of list
print((fruits + wt + vegetable)*10)

# now to find max and min in alist we can simple use max and min function

find_max_min = [20,27,927,27828,2772,828292,2,4,5,67,2,2,-12,0,]

print(max(find_max_min))
print(min(find_max_min))





