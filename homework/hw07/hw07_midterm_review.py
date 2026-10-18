"""
Homework: Midterm Review

This assignment reviews all topics covered on the midterm:
data types, data structures, control flow, functions, NumPy, pandas,
and Git/version control.

Instructions:
- Write clear, readable Python.
- Test your code with the provided data and additional test cases of your own.
- For questions that ask for an explanation, write a short explanation in a
  comment or string immediately below the relevant code.
- When asked to predict output, make your prediction in a comment BEFORE
  running the code.
- Your code should run from top to bottom without requiring manual input.
- Problem 7 (Git) does not require code in this file; follow the instructions
  and answer the questions in comments.
"""

import numpy as np
import pandas as pd


# =============================================================================
# Problem 1 — Data Types and Basic Operations
# =============================================================================

# 1a. Predict the value and type of each expression BEFORE running the code.
# Write your predictions as comments next to each line.

expr_1 = 7 / 2          # predicted value: ____, predicted type: ____
expr_2 = 7 // 2         # predicted value: ____, predicted type: ____
expr_3 = 7 % 2          # predicted value: ____, predicted type: ____
expr_4 = int("42")      # predicted value: ____, predicted type: ____
expr_5 = float("42")    # predicted value: ____, predicted type: ____
expr_6 = bool(0)        # predicted value: ____, predicted type: ____
expr_7 = "3" + "4"      # predicted value: ____, predicted type: ____

for val in [expr_1, expr_2, expr_3, expr_4, expr_5, expr_6, expr_7]:
    print(val, type(val))


# 1b. Explain in 1-2 sentences why 0.1 + 0.2 does not exactly equal 0.3 in
# Python, and write a function `approximately_equal(a, b, tol)` that returns
# True when the absolute difference between a and b is no greater than tol.

def approximately_equal(a, b, tol):
    pass  # Replace with your code

# Test:
print(approximately_equal(0.1 + 0.2, 0.3, 1e-12))

# Answer (1-2 sentences):
#


# =============================================================================
# Problem 2 — Data Structures
# =============================================================================

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 45,
    "pears": 20,
}

# 2a. Add a new item "grapes" with a count of 60 to the dictionary.

# Your code here


# 2b. Update the count of "bananas" by adding 15 more to the existing value.

# Your code here


# 2c. Write a function `total_inventory(inventory_dict)` that returns the
# total count of all items, using a for loop (do not use the built-in sum()).

def total_inventory(inventory_dict):
    pass  # Replace with your code

print(total_inventory(inventory))


# 2d. Write a function `items_below_threshold(inventory_dict, threshold)` that
# returns a list of item names whose count is strictly less than the
# threshold.

def items_below_threshold(inventory_dict, threshold):
    pass  # Replace with your code

print(items_below_threshold(inventory, 40))


# 2e. The following code is supposed to remove duplicate values from a list
# while preserving order, but it has a bug. Identify and fix it.

def unique_in_order(items):
    seen = []
    result = []
    for item in items:
        if item in result:
            result.append(item)
    return result

# Fixed version:
def unique_in_order_fixed(items):
    pass  # Replace with your code

print(unique_in_order_fixed([3, 3, 1, 2, 1, 4, 2]))


# 2f. EXPLANATION: You need to store student IDs mapped to names, and need
# to look up names by ID frequently. Explain why a dictionary is a better
# choice than a list of tuples for this task. (2-3 sentences)

# Answer:
#


# =============================================================================
# Problem 3 — Control Flow
# =============================================================================

readings = [12, 45, 67, 23, 89, 34, 56, 78, 90, 15]

# 3a. Using a for loop and an accumulator, count how many readings are
# greater than 50. Do not use any built-in filtering functions.

count_above_50 = None  # Replace with your code


# 3b. Using a while loop, find the index of the first reading greater than
# 80. If none exist, the result should be -1.

first_index_above_80 = None  # Replace with your code


# 3c. The following function is supposed to classify a temperature in
# Celsius but has a bug. Find and fix it.

def classify_temp(temp_c):
    if temp_c < 0:
        return "freezing"
    if temp_c < 15:
        return "freezing"
    elif temp_c < 25:
        return "mild"
    else:
        return "hot"

# Fixed version:
def classify_temp_fixed(temp_c):
    pass  # Replace with your code

# Test cases (should return "freezing", "mild", "hot" respectively):
print(classify_temp_fixed(-5))
print(classify_temp_fixed(20))
print(classify_temp_fixed(30))


# 3d. Write a nested loop that, given a 2D list (list of lists) of numbers,
# returns the sum of only the EVEN numbers across the entire structure.

def sum_even_nested(matrix):
    pass  # Replace with your code

test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_even_nested(test_matrix))  # should be 2 + 4 + 6 + 8 = 20


# =============================================================================
# Problem 4 — Functions
# =============================================================================

# 4a. Write a function `find_max_min(numbers)` that returns a tuple
# (max_value, min_value) WITHOUT using the built-in max() or min() functions.

def find_max_min(numbers):
    pass  # Replace with your code

print(find_max_min([4, 1, 9, 2, 7]))  # should be (9, 1)


# 4b. Write a function `make_multiplier(n)` that returns a NEW function. The
# returned function should take one argument x and return x * n.
# (This tests closures.)

def make_multiplier(n):
    pass  # Replace with your code

times3 = make_multiplier(3)
print(times3(10))  # should be 30


# 4c. Predict the output of the following code BEFORE running it. Then run
# it to check your prediction.

def update_value():
    value = value + 1
    return value

value = 5
# result = update_value()   # What happens if you uncomment this line?

# Prediction (comment):
#


# 4d. Write a function `safe_divide(a, b, default=0)` that returns a / b,
# but returns `default` instead if b is zero (avoiding a ZeroDivisionError).

def safe_divide(a, b, default=0):
    pass  # Replace with your code

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # 0
print(safe_divide(10, 0, -1)) # -1


# =============================================================================
# Problem 5 — NumPy: Array Creation, Indexing, and Slicing
# =============================================================================

data = np.array([12, 45, 7, 23, 89, 34, 56, 78, 90, 15])

# 5a. Create a new array containing only the values greater than 30, using
# boolean indexing (no loops).

above_30 = None  # Replace with your code


# 5b. Create a new array containing only the EVEN values in `data`, using
# boolean indexing (no loops).
# Hint: use the % operator inside the boolean condition.

even_values = None  # Replace with your code


# 5c. Use slicing (no loops) to extract every other element of `data`,
# starting from the first element.

every_other = None  # Replace with your code


# 5d. Create a 2D array from this nested list, then report its shape.

grid_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
grid = None       # Convert to a NumPy array
grid_shape = None # Report its shape


# 5e. Using indexing (not slicing), extract the single value in `grid` at
# row index 1, column index 2. (It should be 7.)

single_value = None  # Replace with your code


# 5f. Use slicing to extract the first two rows and the last two columns of
# `grid` as a sub-array.

sub_array = None  # Replace with your code


# =============================================================================
# Problem 6 — NumPy: Elementwise Operations and Aggregation
# =============================================================================

# 6a. Using elementwise operations (no loops), create an array called
# `scaled` that is `data` with every value multiplied by 2 and then
# increased by 1.

scaled = None  # Replace with your code


# 6b. Calculate the sum of each row and the sum of each column of `grid`
# using np.sum() with the appropriate axis argument.

row_sums = None     # one value per row
col_sums = None     # one value per column


# 6c. Calculate the mean, maximum, and standard deviation of all values in
# `data` using NumPy's built-in functions (no loops).

data_mean = None
data_max = None
data_std = None


# 6d. Predict the output of the following code BEFORE running it. Then run
# it to check your prediction. (This tests broadcasting with mismatched
# shapes, which should raise an error -- or will it?)

arr_a = np.array([1, 2, 3])
arr_b = np.array([10, 20, 30, 40])
# result = arr_a + arr_b   # What happens if you uncomment this line?

# Prediction (comment):
#


# 6e. EXPLANATION: In 1-2 sentences, explain why `arr1 + arr2` behaves
# differently for two NumPy arrays than `list1 + list2` behaves for two
# Python lists.

# Answer:
#


# =============================================================================
# Problem 7 — Pandas: Series, DataFrames, and Selection
# =============================================================================

students = pd.DataFrame({
    "name": ["Ana", "Ben", "Cho", "Dee", "Eli"],
    "score": [88, 72, 95, 60, 83],
    "section": ["A", "B", "A", "B", "A"],
})

# 7a. Select just the "score" column as a Series. Store it in `scores_series`.
# Then verify its type using type().

scores_series = None


# 7b. Select the "name" and "score" columns together as a DataFrame. Store
# it in `name_score_df`. Then verify its type using type().

name_score_df = None


# 7c. Use boolean filtering to create a DataFrame `passing` containing only
# students with a score of 70 or higher.

passing = None


# 7d. Add a new column "passed" that is True when score >= 70 and False
# otherwise, using a vectorized expression (no loop or .apply()).

# Your code here (modify `students` in place)


# 7e. Use .loc to select the "name" column for only the rows where
# "section" is "A". Store the result in `section_a_names`.

section_a_names = None


# =============================================================================
# Problem 8 — Pandas: Groupby, Missing Data, and Merging
# =============================================================================

# 8a. Use groupby to calculate the mean score for each section. Store the
# result in `section_means`.

section_means = None


# 8b. Use groupby to calculate BOTH the count and the mean score for each
# section in a single call. Store the result in `section_summary`.
# Hint: look into .agg() with a list of function names.

section_summary = None


# 8c. There is a new student, "Fay", with no recorded score (missing value,
# represented as None/NaN) in section "B". Add this row to `students` using
# pd.concat() with a small one-row DataFrame.

# Your code here


# 8d. Count how many missing values exist in the "score" column after
# adding Fay. Store the result in `num_missing`.

num_missing = None


# 8e. EXPLANATION: Suppose you wanted to fill Fay's missing score with 0
# instead of leaving it as NaN. In 1-2 sentences, explain why this might
# give a misleading impression if you then compute the class average.

# Answer:
#


# 8f. Create a second small DataFrame called `advisors` that maps each
# section to an advisor's name:
# {"section": ["A", "B"], "advisor": ["Dr. Lee", "Dr. Patel"]}
# Then merge it with `students` on the "section" column, using a left
# merge, and store the result in `students_with_advisors`.

advisors = None
students_with_advisors = None


# =============================================================================
# Problem 9 — Git and Version Control (No Code Required)
# =============================================================================

# 9a. Suppose you have just finished writing this homework file for the
# first time, and your Math5200 folder is already a Git repository
# (git init has already been run). List, in order, the Git commands you
# would type to stage and commit this file with the message
# "Complete midterm review homework".

# Answer (write the commands as comments):
#
#
#

# 9b. You realize you want to see the history of commits you've made so far
# in this repository, in a compact, one-line-per-commit format. What command
# would you run?

# Answer:
#

# 9c. EXPLANATION: Why is "fix stuff" a poor commit message compared to
# "Fix off-by-one error in sum_even_nested loop bounds"? Write 1-2 sentences.

# Answer:
#
