"""
Homework 2: Strings, Data Structures, and Control Flow

Submit this file with your solutions filled in below each problem.
Do not delete the problem statements.

Instructions:
- Write clear, readable Python.
- Unless a problem explicitly asks you to use a particular function or
  data structure, you may use basic Python tools and the standard library.
- For questions that ask for an explanation, write a short explanation in
  a comment immediately below the relevant code.
- When a problem asks you to predict an answer before executing code,
  make your prediction first and then use Python to check it.
- Your code should run from top to bottom without requiring manual input.
- Do not define your own functions unless a problem explicitly asks you to.
"""

# =============================================================================
# Problem 1 — Strings, indexing, and slicing
# =============================================================================

# Consider the string:
#
#     course = "Mathematical Computing"
#
# 1a. Before running any code, predict the result of each expression:
#
#     len(course)       = __________
#     course[0]         = __________
#     course[5]         = __________
#     course[-1]        = __________
#     course[0:12]      = __________
#     course[13:]       = __________
#
# Then use Python to check your answers.

course = "Mathematical Computing"

print("1a:", len(course))
print("1a:", course[0])
print("1a:", course[5])
print("1a:", course[-1])
print("1a:", course[0:12])
print("1a:", course[13:])


# 1b. Use slicing to extract the word "Computing" from course.
# Store it in `word_1b`.

word_1b = None


# 1c. Use indexing or slicing to reverse the string.
# Store the result in `reverse_1c`.
#
# Hint: Python allows a slice to have a step.

reverse_1c = None


# 1d. In one or two sentences, explain the difference between an index and
# a slice.
#
# Answer:
#


# =============================================================================
# Problem 2 — String processing
# =============================================================================

# Consider the following sentence:
#
sentence = "Python and R are useful for mathematical and statistical computing."

# 2a. Convert sentence to lowercase and store it in `lower_sentence`.

lower_sentence = None


# 2b. Count how many times the letter "a" appears in the lowercase sentence.
# Store the result in `number_of_a`.

number_of_a = None


# 2c. Split the sentence into individual words using the string `split()`
# method. Store the resulting list in `words_2c`.

words_2c = None


# 2d. How many words are in the sentence? Store the answer in `number_of_words`.

number_of_words = None


# 2e. Print the results from 2a–2d.

print("2e:", lower_sentence)
print("2e:", number_of_a)
print("2e:", words_2c)
print("2e:", number_of_words)


# =============================================================================
# Problem 3 — Lists and mutability
# =============================================================================

# Consider the list:
#
scores = [72, 85, 91, 68, 94]

# 3a. Predict the result of each expression:
#
#     scores[0]       = __________
#     scores[-1]      = __________
#     scores[1:4]     = __________
#     len(scores)     = __________
#
# Then check your predictions with Python.

print("3a:", scores[0])
print("3a:", scores[-1])
print("3a:", scores[1:4])
print("3a:", len(scores))


# 3b. Change the first score from 72 to 75.
# Then append the score 88 to the list.

# Your code here:


# 3c. Sort the scores from smallest to largest.
# Then print the resulting list.

# Your code here:


# 3d. Explain briefly why a list is a useful data structure for this example.
# Mention at least TWO operations that are useful when working with a list.
#
# Answer:
#


# =============================================================================
# Problem 4 — Dictionaries
# =============================================================================

# A dictionary is useful when information is naturally organized as
# key-value pairs.
#
# Consider:
#
student = {
    "name": "Ada",
    "program": "Mathematics and Statistics",
    "year": 1,
    "credits": 12,
}

# 4a. Retrieve Ada's name, program, and number of credits.
# Store them in the variables below.

student_name = None
student_program = None
student_credits = None


# 4b. Add a new key-value pair indicating that Ada's favorite programming
# language is Python.
#
# Your code here:


# 4c. Change the value associated with "credits" from 12 to 15.

# Your code here:


# 4d. Print the final dictionary.

print("4d:", student)


# 4e. In one or two sentences, explain why a dictionary is more natural than
# a list for storing information such as a student's name, program, and year.
#
# Answer:
#


# =============================================================================
# Problem 5 — Sets and membership
# =============================================================================

# The following list contains repeated values:
#
departments = [
    "math", "statistics", "math", "computer science",
    "statistics", "math", "physics"
]

# 5a. Use a set to determine the distinct departments.
# Store the result in `unique_departments`.

unique_departments = None


# 5b. Determine how many distinct departments there are.
# Store the result in `number_of_departments`.

number_of_departments = None


# 5c. Use the `in` operator to determine whether "physics" and "economics"
# occur in the set.
#
# Store the results in `has_physics` and `has_economics`.

has_physics = None
has_economics = None


# 5d. Print your results.

print("5d:", unique_departments)
print("5d:", number_of_departments)
print("5d:", has_physics, has_economics)


# 5e. What is one important difference between a set and a list?
#
# Answer:
#


# =============================================================================
# Problem 6 — Boolean logic and conditional statements
# =============================================================================

# Suppose a student passes an assignment if the score is at least 70.
#
score = 83

# 6a. Write a Boolean expression that determines whether the student passes.
# Store it in `passes`.

passes = None


# 6b. Write an if/else statement that prints:
#
#     "Pass"
#
# if the student passes and
#
#     "Does not pass"
#
# otherwise.

# Your code here:


# 6c. Now suppose that a score of 90 or higher receives an "A", a score of
# 80–89 receives a "B", a score of 70–79 receives a "C", and anything below
# 70 receives an "F".
#
# Use an if/elif/else statement to assign the appropriate letter grade to
# `letter_grade`.

letter_grade = None


# 6d. Test your code by changing score to several different values.
# You do not need to preserve those test values in your submitted answer.
#
# Briefly explain why the order of the conditions in an if/elif/else statement
# matters.
#
# Answer:
#


# =============================================================================
# Problem 7 — for loops and accumulation
# =============================================================================

# Consider the list:
#
temperatures = [68, 71, 73, 70, 75, 77, 74]

# 7a. Use a for loop to calculate the sum of the temperatures.
# Store the result in `temperature_sum`.

temperature_sum = 0

# Your code here:


# 7b. Use a for loop to count how many temperatures are at least 75 degrees.
# Store the result in `number_at_least_75`.

number_at_least_75 = 0

# Your code here:


# 7c. Calculate the average temperature using your answer from 7a.
# Store it in `average_temperature`.

average_temperature = None


# 7d. Print your results.

print("7d:", temperature_sum)
print("7d:", number_at_least_75)
print("7d:", average_temperature)


# =============================================================================
# Problem 8 — Filtering data with a loop
# =============================================================================

# Consider the following transaction amounts:
#
transactions = [12.50, 87.25, 4.99, 125.00, 63.75, 210.50, 18.00, 91.25]

# 8a. Create an empty list called `large_transactions`.
#
# Then use a for loop and an if statement to add every transaction greater
# than $80 to the list.
#
# Do NOT use a list comprehension for this problem.

large_transactions = []

# Your code here:


# 8b. Print the resulting list.

print("8b:", large_transactions)


# 8c. How many large transactions are there?
# Store the answer in `number_of_large_transactions`.

number_of_large_transactions = None


# 8d. Calculate the total value of the large transactions.
# Store it in `total_large_transactions`.

total_large_transactions = None


# =============================================================================
# Problem 9 — Tracing a loop
# =============================================================================

# Consider this program:
#
#     total = 0
#     for x in [2, 4, 6]:
#         total = total + x
#
# 9a. Before running the code, trace the value of total after each iteration.
#
# Before the loop: total = ______
# After x = 2:     total = ______
# After x = 4:     total = ______
# After x = 6:     total = ______
#
# 9b. Now run the program and verify your answer.

total = 0

for x in [2, 4, 6]:
    total = total + x

print("9b:", total)


# 9c. In your own words, explain what an "accumulator" is in a loop.
#
# Answer:
#


# =============================================================================
# Problem 10 — Algorithms and efficiency
# =============================================================================

# Suppose you have a list containing n numbers and want to determine whether
# the value 100 appears in the list.
#
# 10a. Describe, in plain English, a simple algorithm that checks the list
# from beginning to end until it finds 100 or reaches the end of the list.
#
# Answer:
#


# 10b. In the worst case, approximately how many list elements must this
# algorithm inspect if the list contains n elements?
#
# Answer:
#


# 10c. Now suppose you have a sorted list and use a method that repeatedly
# cuts the remaining search interval approximately in half.
#
# Without implementing the algorithm, explain why this approach can require
# dramatically fewer checks for a very large list.
#
# Answer:
#


# 10d. Which of the following best describes the main idea of computational
# complexity?
#
# A. How many seconds a particular computer takes to run a program.
# B. How the amount of computational work grows as the size of the problem
#    grows.
# C. How many lines of Python code are in a program.
# D. How much memory a computer has.
#
# Store the correct letter in `answer_10d`.

answer_10d = None


# =============================================================================
# Problem 11 — Choosing the right data structure
# =============================================================================

# For each situation below, choose the most natural Python data structure:
#
#     list, tuple, dictionary, or set
#
# 11a. A collection of exam scores that you expect to modify:
#
answer_11a = None


# 11b. A fixed geographic coordinate consisting of latitude and longitude:
#
answer_11b = None


# 11c. A mapping from a student's ID number to the student's name:
#
answer_11c = None


# 11d. A collection of unique course subject codes where you mainly care
# about whether a particular code is present:
#
answer_11d = None


# 11e. Briefly explain ONE of your choices above. Your explanation should
# refer to the operations you expect to perform on the data.
#
# Answer:
#


# =============================================================================
# Problem 12 — Short reflection: from problem to algorithm
# =============================================================================

# In 4–6 sentences, explain the following:
#
# Why is choosing a data structure part of solving a computational problem,
# rather than merely a programming-language detail? Give a concrete example
# from this homework or from a problem you might encounter in data analysis.
#
# Answer:
#
