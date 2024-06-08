# Define a list of fruits
fruit_list = ["apple", "mango", "avocado", "banana"]
# Print the list of fruits
print(fruit_list)
# Print the last item in the list of fruits
print(fruit_list[-1])

# Define a list of odd numbers
odd_numbers = [3, 5, 7, 9, 11]
# Print the list of odd numbers
print(odd_numbers)
# Print the type of the list of odd numbers
print(type(odd_numbers))

# Define a list of team mates
teammates_list = ["Nick", "John", "Max"]
# Print the list of team mates
print(teammates_list)

#nested list containing three students scores
scores = [
    [90,90,90],
    [80,80,80],
    [70,70,70]
]

#empty list to store average scores
avg_score=[]

#iteration over each inner list
for score in scores:
    total=sum(score) #sum of score for student
    avg=total/len(score) #average of score for student
    avg_score.append(avg) #append average to list of average scores 

#loop to print scores for each student
#enumerate takes an iterable ie avg_score and returns a pair of values i.e index starting from 1 and an item from the iterable
for i,j in enumerate(avg_score,start=1): #i holds the index, j holds the average score 
    print(f"Average score for student {i} is {j}")

# Define a list of numbers
numbers_list = [4, 3, 7, 1, 5]
# Print the list of numbers
print(numbers_list)

# Sort the list of numbers in ascending order
numbers_list.sort()
# Print the sorted list of numbers
print(numbers_list)

# Sort the list of numbers in descending order
numbers_list.sort(reverse=True)
# Print the sorted list of numbers in descending order
print(numbers_list)

# Print the length of the list of numbers
print(len(numbers_list))
