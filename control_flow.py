# Syntax if variable - condition age:

# weather = "rainy"
#
# if weather == "sunny": # this this condition is true the next line would execute
#     print("take the umbrella ") # this line needs to be inside the if code block - intended
# elif weather != "sunny": # conditions True or False
#     print("the weather is not rainy, Enjoy as much as you can ")
# else:
#     print("Thank you for shopping please visit again")
# # Let's use our ticket age criteria
#
# age = 18
#
# if age <= 18: # checking the condition according to the age given
#     print(" you are not eligible to watch this movie, please select under 18 rated movie")

# For Loops and While loops
# Loops help us Iterate through our data, such as Lists, Dict, sets etc.

# shopping_list = ["eggs", "apples", "milk", "bread", "butter", 1, 2, 3, 4, 5, 6, 7, 9]
#                #    0        1        2       3         4
# # print(shopping_list[0])
# # print(shopping_list[1])
# # print(shopping_list[2])
# # print(shopping_list[3])
# # print(shopping_list[4])
# # Let's see you can we get it done with for loop by iterating through our list
# # first iteration:
# for items in shopping_list:
#     print(items)

# # Second Iterations with if conditions and control the flow of our program
# shopping_list = ["eggs", "apples", "milk", "bread", "butter", 1, 2, 3, 4, 5, 6, 7, 9]
# for items in shopping_list:
#     if items == "butter": # if this condition is true
#         break # stop the loop as soon as the above condition is True
#     print(items)


# Third Iterations with dict
student_data = {
    "student_name": "James",  # srting
    "course": "DevOps",  # sting
    "course_topics": 4,  # int
    "topic_names": ["Business Week", "Python", "Virtualisation with Vagrant", "AWS cloud"]  # List
}
# print(student_data)
# Lets iterate through our dict
# for data in student_data.values():
#     if data == "James": # if the condition is True the loops exits
#         print(data)
# In any case for loop would iterate through the data until the last item of condition is True

# While Loops is essentially used to monitor the data
# # First Iteration of while loop
# num = 0
#
# while num < 10: # while num value was less than 10
#     print(f"it's working -> {num}")
#     num += 1 # adding 1 into num value each time it iterates through

# Second Iteration Iteration
# num = 0
# while num < 10:
#     print(f"it's working {num}")
#     if num == 5: # as soon as this condition is True it would exit
#         break
#     num += 1

# Let's see how can we interact with our user in the Third Iteration
# prompt the user to input age and restrict to enter in digits only
# check if the data is in digits display it back to the user if not in digits prompt the user with message to enter in digits

user_prompt = True

while user_prompt:
    age = input(" Please enter you age ? ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer in digit ")

# Final Iteration
user_prompt = True

while user_prompt:
    age = input(" Please enter you age ? ")
    if age.isdigit() and int(age) < 177: #
        user_prompt = False
    else:
        print("Please provide your answer in digit, below 117")
print(f"your age is {age}")
