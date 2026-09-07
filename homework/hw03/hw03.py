"""
Homework 3: Functions, Modularity, and Version Control

Submit this file with your solutions filled in below each problem.
Do not delete the problem statements.

Instructions:
- Write clear, readable Python with descriptive function names.
- Include docstrings for all functions.
- Test your code with the provided data and additional test cases.
- For questions that ask for an explanation, write a short explanation in a
  comment or string immediately below the relevant code.
- Your code should run from top to bottom without requiring manual input.
"""

# =============================================================================
# Problem 1 — Climate Science: Temperature Analysis
# =============================================================================

# You are building a climate data analysis toolkit. Create functions to convert
# and analyze temperature data from weather stations around the world.

# 1a. Write a function to convert Celsius to Fahrenheit.
#
# Formula: F = C * 9/5 + 32
#
# Include a docstring with parameter and return descriptions.

def celsius_to_fahrenheit(celsius):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 1b. Write a function to convert Fahrenheit to Celsius.
#
# Formula: C = (F - 32) * 5/9

def fahrenheit_to_celsius(fahrenheit):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 1c. Write a function to convert Celsius to Kelvin.
#
# Formula: K = C + 273.15

def celsius_to_kelvin(celsius):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 1d. Write a function that calculates the temperature range (max - min)
# from a list of temperatures.

def temperature_range(temperatures):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 1e. Write a function that counts how many days exceed a threshold temperature.
#
# Parameters:
#   temperatures: list of daily temperatures
#   threshold: temperature threshold (default should be 30)
#   unit: "C" or "F" (default should be "C")

def count_days_above_threshold(temperatures, threshold=30, unit="C"):
    """
    # Your docstring here
    """
    # Your code here
    pass


# Test your functions
temperatures_c = [22, 25, 28, 31, 29, 27, 24]

print("1a:", celsius_to_fahrenheit(25))
print("1b:", fahrenheit_to_celsius(77))
print("1c:", celsius_to_kelvin(25))
print("1d:", temperature_range(temperatures_c))
print("1e:", count_days_above_threshold(temperatures_c))
print("1e (threshold=28):", count_days_above_threshold(temperatures_c, threshold=28))


# 1f. Explain in 2-3 sentences why using functions for these conversions is
# better than copying the conversion formula each time you need it.
#
# Answer:
#


# =============================================================================
# Problem 2 — Physics: Projectile Motion
# =============================================================================

# You are simulating projectile motion for a physics education app.
# All functions should be pure (no side effects).

# 2a. Write a function to calculate the horizontal distance traveled by a
# projectile given initial velocity and time.
#
# Formula: distance = velocity * time

def calculate_horizontal_distance(velocity, time):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 2b. Write a function to calculate the vertical position of a projectile
# at a given time, accounting for gravity.
#
# Formula: y = initial_height + initial_velocity * time - 0.5 * g * time^2
# where g = 9.8 m/s^2 (gravitational acceleration)
#
# Use g=9.8 as a default parameter.

def calculate_vertical_position(initial_height, initial_velocity, time, g=9.8):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 2c. Write a function to calculate both horizontal and vertical positions.
# This function should call the functions from 2a and 2b.
#
# Return both values as a tuple: (horizontal, vertical)

def calculate_position(h_velocity, v_velocity, initial_height, time, g=9.8):
    """
    # Your docstring here
    
    This function demonstrates function composition.
    """
    # Your code here
    # Hint: Use calculate_horizontal_distance and calculate_vertical_position
    pass


# Test your functions
print("\n2a:", calculate_horizontal_distance(10, 3))
print("2b:", calculate_vertical_position(5, 15, 2))
print("2c:", calculate_position(10, 15, 5, 2))


# 2d. These functions are "pure" functions. In 2-3 sentences, explain what
# makes a function pure and why pure functions are easier to test.
#
# Answer:
#


# =============================================================================
# Problem 3 — Biology: Protein Sequence Analysis
# =============================================================================

# You are analyzing protein sequences represented as strings of amino acid codes.
# Each amino acid is represented by a single letter (A, C, D, E, F, G, H, I, K,
# L, M, N, P, Q, R, S, T, V, W, Y).

# 3a. Write a function to calculate the length of a protein sequence.

def protein_length(sequence):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 3b. Write a function to count occurrences of a specific amino acid.

def count_amino_acid(sequence, amino_acid):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 3c. Write a function to calculate the percentage composition of an amino acid.
#
# Formula: (count of amino acid / total length) * 100

def amino_acid_percentage(sequence, amino_acid):
    """
    # Your docstring here
    
    This function should use count_amino_acid and protein_length.
    """
    # Your code here
    pass


# 3d. Write a function to find the most common amino acid in a sequence.
# Return both the amino acid and its count as a tuple.
#
# Hint: You can iterate through unique amino acids and count each.

def most_common_amino_acid(sequence):
    """
    # Your docstring here
    """
    # Your code here
    pass


# 3e. Write a function to validate a protein sequence.
# It should return True if all characters are valid amino acids, False otherwise.
#
# Valid amino acids: ACDEFGHIKLMNPQRSTVWY

def is_valid_protein(sequence):
    """
    # Your docstring here
    
    Raises:
        ValueError: if sequence is empty
    """
    # Your code here
    # Hint: Check if every character in sequence is in the valid set
    pass


# Test your functions
protein = "ACDEFGHIKLMNPQRSTVWY"
test_protein = "AACCGGTTAACCGGTT"

print("\n3a:", protein_length(protein))
print("3b:", count_amino_acid(test_protein, "A"))
print("3c:", amino_acid_percentage(test_protein, "A"))
print("3d:", most_common_amino_acid(test_protein))
print("3e:", is_valid_protein(test_protein))
print("3e (invalid):", is_valid_protein("AABBXX"))


# 3f. Add assertions to test your is_valid_protein function.
# Test at least 3 cases: valid sequence, invalid sequence, edge cases.

# Your test assertions here


# =============================================================================
# Problem 4 — Synthesis: Scientific Data Processing Module
# =============================================================================

# You are creating a reusable module for scientific data analysis.
# This problem combines concepts from all previous problems.

# 4a. Write a function to calculate the mean (average) of a list of values.

def calculate_mean(values):
    """
    # Your docstring here
    
    Parameters:
        values: list of numeric values (must be non-empty)
        
    Returns:
        float: arithmetic mean
        
    Raises:
        ValueError: if values is empty
    """
    # Your code here
    # Include input validation
    pass


# 4b. Write a function to calculate the standard deviation.
#
# Formula: std = sqrt(sum((x - mean)^2) / (n - 1))
#
# This function should use calculate_mean.

def calculate_std(values):
    """
    # Your docstring here
    
    Uses sample standard deviation (n-1 denominator).
    """
    # Your code here
    pass


# 4c. Write a function to calculate z-scores for a list of values.
#
# Z-score formula: z = (x - mean) / std
#
# Return a list of z-scores, one for each input value.
# This function should use calculate_mean and calculate_std.

def calculate_z_scores(values):
    """
    # Your docstring here
    
    Z-scores indicate how many standard deviations each value is from the mean.
    """
    # Your code here
    pass


# 4d. Write a function to identify outliers using z-scores.
# An outlier is typically defined as having |z-score| > 2.
#
# Return a list of tuples: (index, value, z_score) for outliers only.

def find_outliers(values, threshold=2.0):
    """
    # Your docstring here
    
    Parameters:
        values: list of numeric values
        threshold: z-score threshold for outlier detection (default 2.0)
    """
    # Your code here
    # Hint: Use calculate_z_scores
    pass


# Test your functions
test_data = [10, 12, 11, 13, 10, 12, 11, 100, 13, 12]

print("\n4a:", calculate_mean(test_data))
print("4b:", calculate_std(test_data))
print("4c:", calculate_z_scores([1, 2, 3, 4, 5]))
print("4d:", find_outliers(test_data))


# 4e. Organize the functions from 4a-4d as if they were in a module.
# Add section comments to group related functions.
#
# Write a comment below showing how you would organize these functions
# in a properly structured Python module file, including:
# - Module docstring
# - Import statements (if needed)
# - Sections for different types of functions
# - if __name__ == "__main__": block
#
# Answer (write as a multi-line comment):
"""


"""


# =============================================================================
# Problem 5 — Reflection: Git and Version Control
# =============================================================================

# 5a. You've just finished writing the calculate_mean function and tested it.
# Write the sequence of Git commands you would use to save this work.
#
# Answer (as a comment):
#


# 5b. You want to add a new feature: calculate_median function.
# Before starting, what Git command would you run to check the current
# state of your repository?
#
# Answer:
#


# 5c. You've modified 3 files: stats.py, test_stats.py, and README.md.
# You want to commit only stats.py and test_stats.py, not README.md.
# Write the Git commands to do this.
#
# Answer (as a comment):
#


# 5d. Explain in 2-3 sentences why version control is important for
# computational research projects.
#
# Answer:
#


# =============================================================================
# Problem 6 — Challenge (Optional)
# =============================================================================

# This problem is optional but recommended for students who want extra practice.

# 6a. Write a function that takes a list of functions and a value,
# and applies each function to the value in sequence.
#
# This is called function composition or pipelining.
#
# Example:
#   functions = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
#   apply_pipeline(5, functions) should compute ((5+1)*2)^2 = 144

def apply_pipeline(value, functions):
    """
    Apply a sequence of functions to a value.
    
    Parameters:
        value: initial value
        functions: list of functions, each taking one argument
        
    Returns:
        result after applying all functions in sequence
    """
    # Your code here
    pass


# Test the pipeline
def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x ** 2

pipeline = [add_one, double, square]
print("\n6a:", apply_pipeline(5, pipeline))


# 6b. Write a function decorator that prints the arguments and return value
# of any function it decorates.
#
# A decorator is a function that takes a function and returns a modified version.
# This is advanced but useful for debugging.

def debug_decorator(func):
    """
    Decorator that prints function calls and returns.
    
    This is an advanced concept - don't worry if it's challenging!
    """
    def wrapper(*args, **kwargs):
        # Print the function call
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Print the result
        print(f"{func.__name__} returned {result}")
        
        return result
    
    return wrapper


# Example usage (you don't need to modify this):
@debug_decorator
def add(a, b):
    return a + b

print("\n6b example:")
result = add(3, 5)


# 6c. Create a function that returns a function (a function factory).
# Write a function make_multiplier(n) that returns a function that multiplies
# its input by n.
#
# Example:
#   times_three = make_multiplier(3)
#   times_three(5) should return 15

def make_multiplier(n):
    """
    # Your docstring here
    
    This demonstrates closures and nested functions.
    """
    # Your code here
    pass


# Test make_multiplier
times_three = make_multiplier(3)
times_five = make_multiplier(5)

print("\n6c:", times_three(10))
print("6c:", times_five(10))
