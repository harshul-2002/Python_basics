# 1. Create a list of names and print the second item.
# 2. Create a list of sports and then replace the second item with another sport.
# 3. Create a list containing numbers and delete the fifth number from the array.
# 4. Create two lists of numbers and merge them.
# 5. Create a list of numbers and find the length, minimum, and maximum.
# 6. Create a dictionary of students and scores and print out a student’s score.
# 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
# 8. Create a dictionary of names and ages and then print out all the keys and values
# 9. Create a tuple of your favorite movies
# 10. Create a tuple and print all the items from the first to third index

# solutions

# Exercise #1
names = ["Avi", "Jim", "Jill"]
print(names[1])
 
# Exercise #2
sports = ["Baseball", "Basketball", "Cricket"]
sports[1] = "Football"
 
# Exercise #3
nums = [1,2,3,4,5,6,7]
del nums[4]
 
# Exercise #4
nums1 = [1,2,3]
nums2 = [4,5,6]
nums3 = nums1 + nums2
 
#Exercise #5
nums = [9,3,15,18,98,1]
print(max(nums))
print(min(nums))
print(len(nums))
 
#Exercise #6
students = {"Avi": 94, "Jack":88, "Jill":84}
print(students["Avi"])
 
#Exercise #7
data = {"Rachel": 17, "Rahul": 61, "Anna": 15}
del data["Rahul"]
 

#  ///////////////////////////////////////////////////////////

#Exercise #8   # doubttttttt
data = {"Rachel": 17, "Rahul": 61, "Anna": 15}
print(data.keys())
print(data.values())

# ///////////////////////////////////////////////////////////////////////////
 
#Exercise #9
movies = ("Inception", "The Imitation Game", "The Secret Life of Walter Mitty")
print(movies)
 
#Exercise #10
data = (1,2,3)
print(data[0:2])