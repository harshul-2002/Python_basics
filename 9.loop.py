
#    for loops
list_1 = ['apple' , 'banana' , 'cherry' , 'berry' , 'orange']
tuple_1 = [10 , 23 , 34 , 56 , 69]

for items in list_1 :  # this will simply print  each item in the list
    print(items)

for values in tuple_1 :  # this will simply print  each value  in the tuple
    print(values)   

#  printing ranges using for in loops
    
for n in range(10,50):
    print(n)  

#  skiiping no. uisng range functions
for n in range(10,50,2):
    print(n)  

# for loop inside a for loop for example print multiply of no bet between 0 -5 and 0-3
for i in range (0,5):
    for j in range(0,3):   
        print(i*j) 

#  ///////////////           while loops in python       ///////////////////////////
        
c = 0
while c < 10 :
    print(f"the value of  c is {c}")
    c = c+1
    print(f"the value after increment is {c}")

print(f"while loop is completed and the final value of c is {c}")


#   //////////////////   control statements     ////////////////////
c = 0
while  c<10 :
    c = c+1
    if c==8:
        print(f" inside break c is {c}")
        break
    elif c==6:
         continue  #as we can  see  at c==6 the print statemnt is skipped
         print(f" inside continue c is {c}")
    elif c==4:
         pass   
         print(f"values inside pass is {c}")
    else:
        print(f"this is inside else when c is not 8 and it is  {c}")
        













