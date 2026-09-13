"""
Homework 2: Data Structures, Algorithms, and Control Flow

Submit this file with your solutions filled in below each problem.
Do not delete the problem statements.

Instructions:
- Write clear, readable Python.
- Test your code with the provided data and additional test cases.
- For questions that ask for an explanation, write a short explanation in a
  comment or string immediately below the relevant code.
- When asked to predict output, make your prediction in a comment first.
- Your code should run from top to bottom without requiring manual input.
"""

# =============================================================================
# Problem 1 — Epidemiology: Disease Case Tracking
# =============================================================================

# You are analyzing daily COVID-19 case counts from a small region over two weeks.

daily_cases = [45, 52, 48, 67, 71, 89, 103, 98, 87, 92, 78, 68, 71, 64]

# 1a. Use list indexing to find the number of cases on day 7 (remember: zero-indexed).
# Store the result in `cases_day_7`.

cases_day_7 = None

# 1b. Use list slicing to extract cases from days 5 through 10 (inclusive).
# Store the result in `cases_week2_start`.

cases_week2_start = None

# 1c. Calculate the total number of cases over the 14-day period.
# Use a for loop and an accumulator variable (do not use the built-in sum() function).
# Store the result in `total_cases`.

total_cases = None

# 1d. Calculate the average daily case count (do not use the built-in sum() function).
# Store the result in `average_cases`.

average_cases = None

# 1e. Count how many days had more than 70 cases.
# Use a for loop with a conditional.
# Store the result in `high_case_days`.

high_case_days = None

# 1f. Find the maximum number of cases in a single day.
# Do NOT use Python's built-in max() function.
# Instead, implement the algorithm: start with the first value as current max,
# then iterate through remaining values, updating when you find a larger value.
# Store the result in `max_cases`.

max_cases = None

# 1g. The data also includes the day of the week for each count.
# Here is the same data with day names:

cases_with_days = [
    ("Mon", 45), ("Tue", 52), ("Wed", 48), ("Thu", 67), ("Fri", 71),
    ("Sat", 89), ("Sun", 103), ("Mon", 98), ("Tue", 87), ("Wed", 92),
    ("Thu", 78), ("Fri", 68), ("Sat", 71), ("Sun", 64)
]

# Find which day of the week had the highest case count in this sample.
# Store the day name in `highest_day` and the count in `highest_count`.
#
# Hint: Iterate through the list of tuples, unpacking each as (day, count).

highest_day = None
highest_count = None

# 1h. Calculate the total cases for each day of the week across both weeks.
# Store the results in a dictionary where keys are day names and values are totals.
#
# For example, if Monday appears twice with counts 45 and 98, the dictionary
# should have {"Mon": 143, ...}
#
# Store the result in `cases_by_weekday`.
#
# Hint: Initialize an empty dictionary. For each (day, count) pair:
#   - If day is not in dictionary, add it with count as value
#   - If day is already in dictionary, add count to existing value

cases_by_weekday = {}

# 1i. Explain in 2-3 sentences why a dictionary is a better choice than a list
# for storing the weekday totals in 1h.
#
# Answer:
#

# =============================================================================
# Problem 2 — "Your Turn" from Exercise 2.1 in class notes
# =============================================================================

text = "The Quick BROWN fox!"

# 1. Convert to lowercase

# 2. Remove the exclamation mark

# 3. Check if it contains "brown"

# 4. Split into words

# 5. Reverse the entire string

# Your code here

# =============================================================================
# Problem 3 — "Your Turn" from Exercise 2.2 in class notes
# =============================================================================

text = "the quick brown fox jumps over the lazy dog and the fox runs"

# Try to use dictionaries to answer the following questions about the text.

# 1. Split the text into words

# 2. Count how many times each word appears

# 3. Find the word(s) that appear most frequently

# Your code here


# =============================================================================
# Problem 4 — "Your Turn" from Exercise 2.3 in class notes
# =============================================================================

text1 = "the quick brown fox"
text2 = "the lazy dog"

# Try to use sets to answer the following questions about the two texts.

# 1. Find letters that appear in both texts

# 2. Find letters that appear in text1 but not text2

# 3. Count how many distinct letters appear across both texts

# Your code here


# =============================================================================
# Problem 5 — "Practice Exercise" #2 in class notes on Text Analysis
# =============================================================================

text = """
Python is a programming language. Python is widely used
for data analysis, scientific computing, and statistics.
Data science relies heavily on Python libraries.
"""

# 1. Count how many times each word appears (case-insensitive)

# 2. Find the longest word

# 3. Determine the average word length

# 4. Find words that appear exactly once

# Your code here

# =============================================================================
# Problem 6 — "Practice Exercise" #3 in class notes on Data Cleaning
# =============================================================================


observations = [
    ("Monday", 15.2),
    ("Tuesday", None),
    ("Wednesday", 14.8),
    ("Thursday", -999),
    ("Friday", 16.5),
    ("Saturday", 150.0),
    ("Sunday", 14.1)
]

# Treat None and -999 as missing data
# Treat values outside [-50, 50] as measurement errors

# 1. Create a new list containing only valid observations

# 2. Calculate statistics (mean, min, max) on valid data

# 3. Report which days had invalid data

# Your code here