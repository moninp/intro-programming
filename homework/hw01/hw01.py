"""
Homework 1: Foundations, State, Binary Representation, and Floating-Point Error

Submit this file with your solutions filled in below each problem.
Do not delete the problem statements.

Instructions:
- Write clear, readable Python.
- Unless a problem explicitly asks you to use a particular function, you may use
  basic Python tools and the standard library.
- For questions that ask for an explanation, write a short explanation in a
  comment or string immediately below the relevant code.
- When a question asks you to predict an answer before executing code, make your
  prediction first and then use Python to check it.
- Your code should run from top to bottom without requiring manual input.
"""

# =============================================================================
# Problem 1 — Expressions, types, and mathematical notation
# =============================================================================

# 1a. Evaluate the mathematical expression
#
#       (3 + 5)^2 / 4
#
# using Python. Store the result in `answer_1a`.
#
# Be careful: Python uses ** for exponentiation.

answer_1a = None


# 1b. What is the type of `answer_1a`? Store the type in `type_1b`.
#
# Before running the code, predict the answer in a comment.

type_1b = None


# 1c. Write Python code that evaluates
#
#       1 + 2 * 3^2
#
# using the appropriate Python operator for exponentiation.
#
# Store the result in `answer_1c`.

answer_1c = None


# 1d. In one or two sentences, explain why the result of 1c is not the same
# as if Python evaluated the expression strictly from left to right.
#
# Answer:
#


# =============================================================================
# Problem 2 — Program state and reassignment
# =============================================================================

# Consider the following program:
#
# x = 10
# y = x + 5
# x = 2
# y = y + x
#
# 2a. Before running the code, trace the state after each line.
#
# Fill in the table in the comments.
#
# After line 1: x = ___, y = ___
# After line 2: x = ___, y = ___
# After line 3: x = ___, y = ___
# After line 4: x = ___, y = ___


# 2b. Now run the program and print the final values of x and y.

x = 10
y = x + 5
x = 2
y = y + x

print("2b:", x, y)


# 2c. Explain briefly why changing x on line 3 does not change the value that
# y received on line 2.
#
# Answer:
#


# =============================================================================
# Problem 3 — Types and conversion
# =============================================================================

# 3a. Predict the value and type of each expression before executing it.
#
# Expression                 Predicted value       Predicted type
# ----------------------------------------------------------------
# 7 / 2                      __________             __________
# 7 // 2                     __________             __________
# 7 % 2                      __________             __________
# int("17")                  __________             __________
# float("17")                __________             __________
# bool(0)                    __________             __________
# bool(1)                    __________             __________
#
# Then write Python code that checks your predictions.

expressions_3a = [
    7 / 2,
    7 // 2,
    7 % 2,
    int("17"),
    float("17"),
    bool(0),
    bool(1),
]

for value in expressions_3a:
    print("3a:", value, type(value))


# 3b. Convert the string "3.14159" to a floating-point number and store it
# in `pi_approx`.

pi_approx = None


# 3c. Convert the integer 12 to a floating-point number and store it in
# `twelve_float`.

twelve_float = None


# =============================================================================
# Problem 4 — Binary representation
# =============================================================================

# 4a. Convert each decimal integer to binary by hand first.
#
# Decimal       Binary
# -----------------------
# 5             __________
# 13            __________
# 42            __________
# 100           __________
#
# Then use Python's bin() to check your answers.

for n in [5, 13, 42, 100]:
    print("4a:", n, bin(n))


# 4b. Convert each binary number to decimal by hand first.
#
# Binary        Decimal
# -----------------------
# 1011          __________
# 11010         __________
# 1000001       __________
#
# Then use int(binary_string, 2) to check your answers.

for s in ["1011", "11010", "1000001"]:
    print("4b:", s, int(s, 2))


# 4c. Explain briefly what each digit in a binary number represents.
# For example, explain the place values in 10110.
#
# Answer:
#


# =============================================================================
# Problem 5 — Fixed-width integers and Python's int
# =============================================================================

# Suppose a computer uses an unsigned 8-bit integer.
#
# 5a. What are the smallest and largest values that can be represented?
#
# Minimum: __________
# Maximum: __________
#
# Explain your answer briefly.
#
# Answer:
#


# 5b. Suppose instead that an 8-bit signed integer uses two's complement.
#
# What are the smallest and largest values that can be represented?
#
# Minimum: __________
# Maximum: __________
#
# Answer:
#


# 5c. Python integers do not normally overflow when you add two large integers.
# Demonstrate this by calculating 2**100 and then adding 1.
#
# Store the result in `large_integer`.

large_integer = None


# 5d. Why does this not mean that Python integers have unlimited computational
# resources?
#
# Answer:
#


# =============================================================================
# Problem 6 — Floating-point representation and precision
# =============================================================================

import sys

# 6a. Print the following attributes of sys.float_info:
#
#   max
#   min
#   eps
#   max_exp
#   min_exp
#
# You may print the entire object if you prefer, but identify the requested
# quantities clearly.

print("6a:", "max =", sys.float_info.max)
print("6a:", "min =", sys.float_info.min)
print("6a:", "eps =", sys.float_info.epsilon)
print("6a:", "max_exp =", sys.float_info.max_exp)
print("6a:", "min_exp =", sys.float_info.min_exp)


# 6b. In your own words, what does sys.float_info.epsilon tell you?
#
# Answer:
#


# 6c. Compute:
#
#     0.1 + 0.2
#
# and compare it with 0.3.

sum_06 = 0.1 + 0.2
print("6c:", sum_06)
print("6c:", sum_06 == 0.3)


# 6d. Explain why Python can produce False in the equality comparison above
# even though mathematically 0.1 + 0.2 = 0.3.
#
# Answer:
#


# =============================================================================
# Problem 7 — Absolute and relative error
# =============================================================================

# Suppose the exact value of a quantity is 1/3 and our approximation is
# 0.3333.
#
# 7a. Calculate the absolute error:
#
#       |approximation - exact|
#
# Store the result in `absolute_error`.

exact = 1 / 3
approximation = 0.3333

absolute_error = None


# 7b. Calculate the relative error:
#
#       |approximation - exact| / |exact|
#
# Store the result in `relative_error`.

relative_error = None


# 7c. Print both errors.

print("7c:", "absolute error =", absolute_error)
print("7c:", "relative error =", relative_error)


# 7d. In one or two sentences, explain the difference between absolute and
# relative error.
#
# Answer:
#


# =============================================================================
# Problem 8 — Reliable floating-point comparisons and cancellation
# =============================================================================

# 8a. Write a function `approximately_equal(a, b, tol)` that returns True when
# the absolute difference between a and b is no greater than tol.
#
# For example:
#
#     approximately_equal(0.1 + 0.2, 0.3, 1e-12)
#
# should return True.

def approximately_equal(a, b, tol):
    pass


# 8b. Test your function on:
#
#     0.1 + 0.2  versus  0.3
#
# using a tolerance of 1e-12.

print("8b:", approximately_equal(0.1 + 0.2, 0.3, 1e-12))


# 8c. Consider the mathematically equivalent expressions
#
#     sqrt(x + 1) - sqrt(x)
#
# and
#
#     1 / (sqrt(x + 1) + sqrt(x)).
#
# For x = 10**16, calculate both expressions.
#
# Hint: import sqrt from math.

from math import sqrt

x = 10**16

expression_a = None
expression_b = None

print("8c:", expression_a)
print("8c:", expression_b)


# 8d. The two expressions are mathematically equal. Compare their numerical
# results. What does this example suggest about the relationship between
# mathematical equivalence and numerical reliability?
#
# Answer:
#


# =============================================================================
# Problem 9 — Short reflection: What is computation?
# =============================================================================

# In 3–5 sentences, answer the following:
#
# What is the difference between solving a mathematical problem and solving a
# computational problem? Your answer should mention at least TWO of the
# following:
#
#   - representation
#   - algorithms
#   - finite precision
#   - testing
#   - validation
#   - reproducibility
#
# Answer:
#
