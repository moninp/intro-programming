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
# Use a for loop and an accumulator variable.
# Store the result in `total_cases`.

total_cases = None

# 1d. Calculate the average daily case count.
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
# Problem 2 — Finance: Stock Price Analysis
# =============================================================================

# You are tracking stock prices for a small portfolio.

# 2a. Create a dictionary mapping stock ticker symbols to their current prices.
# Use this data:
#
#   AAPL: 178.50
#   GOOGL: 142.25
#   MSFT: 420.80
#   TSLA: 242.15
#   NVDA: 495.30
#
# Store the result in `stock_prices`.

stock_prices = {}

# 2b. The price of TSLA has increased to 255.40. Update the dictionary.

# Your code here

# 2c. Add a new stock to the portfolio: AMZN at 178.25.

# Your code here

# 2d. Find all stocks with prices above $200.
# Store the ticker symbols in a list called `expensive_stocks`.
#
# Hint: Iterate through the dictionary items.

expensive_stocks = []

# 2e. Calculate the total value if you own 10 shares of each stock.
# Store the result in `portfolio_value`.

portfolio_value = None

# 2f. The prices were from Monday. Here are Tuesday's prices:

tuesday_prices = {
    "AAPL": 182.30,
    "GOOGL": 139.50,
    "MSFT": 425.60,
    "TSLA": 248.90,
    "NVDA": 501.75,
    "AMZN": 175.80
}

# Calculate the change (Tuesday - Monday) for each stock.
# Store the results in a dictionary called `price_changes`.
#
# Hint: Iterate through tuesday_prices. For each ticker, calculate
# tuesday_prices[ticker] - stock_prices[ticker]

price_changes = {}

# 2g. You have two separate portfolios with different stocks:

portfolio_a = {"AAPL", "GOOGL", "MSFT", "NVDA"}
portfolio_b = {"MSFT", "TSLA", "NVDA", "AMZN", "META"}

# Find:
# - Stocks that appear in BOTH portfolios (intersection)
# - Stocks that appear in EITHER portfolio (union)
# - Stocks in portfolio A but NOT in portfolio B (difference)
#
# Store results in `common_stocks`, `all_stocks`, and `only_in_a`.
#
# Hint: Use set operations: & for intersection, | for union, - for difference

common_stocks = None
all_stocks = None
only_in_a = None

# 2h. Algorithm comparison: Suppose you want to find which stocks from a
# watchlist appear in your portfolio.
#
# Here are two approaches:

def find_matches_v1(watchlist, portfolio):
    """Use nested loops - checks each watchlist item against each portfolio item."""
    matches = []
    for stock in watchlist:
        for held_stock in portfolio:
            if stock == held_stock and stock not in matches:
                matches.append(stock)
    return matches

def find_matches_v2(watchlist, portfolio):
    """Convert portfolio to a set for fast lookup."""
    portfolio_set = set(portfolio)
    matches = []
    for stock in watchlist:
        if stock in portfolio_set:
            matches.append(stock)
    return matches

# Test both functions with:
watchlist = ["AAPL", "GOOGL", "META", "NFLX", "NVDA"]
portfolio = ["AAPL", "GOOGL", "MSFT", "NVDA"]

result_v1 = find_matches_v1(watchlist, portfolio)
result_v2 = find_matches_v2(watchlist, portfolio)

print("2h v1:", result_v1)
print("2h v2:", result_v2)

# In a comment, explain: For a watchlist with n stocks and a portfolio with m stocks,
# approximately how many comparisons does each algorithm perform?
# Which algorithm is more efficient for large portfolios?
#
# Answer:
#

# =============================================================================
# Problem 3 — Biology: DNA Sequence Analysis
# =============================================================================

# DNA sequences consist of four nucleotides: A (adenine), T (thymine),
# G (guanine), and C (cytosine).

dna_sequence = "ATCGATCGATCGTAGCTAGCTAGCTAAGCTTAGCCGATCG"

# 3a. Find the length of the DNA sequence.
# Store the result in `sequence_length`.

sequence_length = None

# 3b. Extract the first 10 nucleotides (positions 0-9).
# Store the result in `first_ten`.

first_ten = None

# 3c. Count how many times each nucleotide appears in the sequence.
# Store the results in a dictionary called `nucleotide_counts`.
#
# For example: {"A": 12, "T": 10, "G": 9, "C": 10}
#
# Hint: Initialize an empty dictionary. For each character in the sequence:
#   - If character not in dictionary, set its count to 0
#   - Increment the count by 1

nucleotide_counts = {}

# 3d. Calculate the GC content of the sequence.
# GC content is the percentage of nucleotides that are G or C.
#
# Formula: GC content = (count of G + count of C) / total length * 100
#
# Store the result in `gc_content`.

gc_content = None

# 3e. Find the position of the first occurrence of the codon "TAG".
# A codon is a sequence of three nucleotides.
#
# Store the starting position in `tag_position`.
# If "TAG" is not found, store -1.
#
# Hint: Use a for loop with range(len(dna_sequence) - 2) and check
# if dna_sequence[i:i+3] equals "TAG"

tag_position = None

# 3f. In genetics, the complement of a DNA sequence is found by replacing:
#   A ↔ T
#   G ↔ C
#
# Create the complement of the sequence.
# Store the result in `complement`.
#
# Hints:
# - Strings are immutable, so you cannot change characters directly
# - Build a new string by iterating through the original
# - Use a dictionary to map each nucleotide to its complement:
#   complement_map = {"A": "T", "T": "A", "G": "C", "C": "G"}
# - For each character, append complement_map[character] to your result string

complement_map = {"A": "T", "T": "A", "G": "C", "C": "G"}
complement = ""

# 3g. The reverse complement is the complement sequence read backwards.
# This is important in DNA analysis because the two strands of DNA run in
# opposite directions.
#
# Create the reverse complement of the original sequence.
# Store the result in `reverse_complement`.
#
# Hint: You already have `complement`. Now reverse it using string slicing.

reverse_complement = None

# 3h. Sometimes DNA sequences are stored with lowercase letters and spaces.
# Clean and analyze this sequence:

raw_sequence = "atcg atcg   ATCG tagc TAGC"

# Clean the sequence by:
# 1. Converting to uppercase
# 2. Removing all spaces
#
# Store the cleaned sequence in `cleaned_sequence`.
#
# Then count the nucleotides in the cleaned sequence.
# Store the result in `cleaned_counts`.
#
# Hint: Use .upper() and .replace(" ", "")

cleaned_sequence = None
cleaned_counts = {}

# =============================================================================
# Problem 4 — Synthesis: Multi-Domain Data Processing
# =============================================================================

# This problem combines concepts from all previous problems.

# 4a. You have daily case counts by region:

regional_data = [
    ("North", 45),
    ("South", 67),
    ("East", 52),
    ("West", 71),
    ("North", 48),
    ("South", 73),
    ("East", 58),
    ("West", 69),
]

# Calculate the total cases for each region.
# Store the result in `regional_totals` (a dictionary).

regional_totals = {}

# 4b. You have stock prices over three days for multiple stocks.
# The data is stored as a list of (day, ticker, price) tuples:

price_history = [
    (1, "AAPL", 178.50),
    (1, "GOOGL", 142.25),
    (1, "MSFT", 420.80),
    (2, "AAPL", 182.30),
    (2, "GOOGL", 139.50),
    (2, "MSFT", 425.60),
    (3, "AAPL", 179.80),
    (3, "GOOGL", 141.00),
    (3, "MSFT", 422.15),
]

# Calculate the average price for each stock across all three days.
# Store the result in `average_prices` (a dictionary).
#
# Hints:
# - You'll need to track both the sum and count for each stock
# - Use two dictionaries: one for sums, one for counts
# - Or use a dictionary where values are lists: [sum, count]

average_prices = {}

# 4c. You have DNA sequences from multiple samples, some of which may be invalid.
# Invalid sequences contain characters other than A, T, G, C.

samples = [
    "ATCGATCG",
    "GCTAGCTA",
    "ATXGATCG",  # Invalid: contains X
    "TAGCTAGC",
    "ATCG123",   # Invalid: contains numbers
    "GCGCGCGC",
]

# Filter the samples to keep only valid sequences.
# A sequence is valid if it contains only the characters A, T, G, C.
# Store the valid sequences in `valid_samples` (a list).
#
# Hint: For each sample, check if every character is in the set {"A", "T", "G", "C"}
# You can use a loop with a flag variable, or use the all() function:
#   all(char in {"A", "T", "G", "C"} for char in sample)

valid_samples = []

# 4d. Calculate the average GC content across all valid samples.
# Store the result in `average_gc_content`.
#
# Hints:
# - For each valid sample, calculate its GC content
# - Sum all the GC contents
# - Divide by the number of valid samples

average_gc_content = None

# 4e. You have nested data: each region reports cases by age group.

nested_data = [
    ("North", {"0-17": 12, "18-64": 28, "65+": 5}),
    ("South", {"0-17": 18, "18-64": 42, "65+": 7}),
    ("East", {"0-17": 15, "18-64": 32, "65+": 5}),
    ("West", {"0-17": 20, "18-64": 45, "65+": 6}),
]

# Calculate the total cases for each age group across all regions.
# Store the result in `age_group_totals` (a dictionary).
#
# For example: {"0-17": 65, "18-64": 147, "65+": 23}
#
# Hints:
# - Initialize age_group_totals = {"0-17": 0, "18-64": 0, "65+": 0}
# - For each (region, age_dict) pair, iterate through the age_dict
# - Add each age group's count to the corresponding total

age_group_totals = {"0-17": 0, "18-64": 0, "65+": 0}

# 4f. Reflection: In 3-4 sentences, describe the most important algorithmic
# pattern you used repeatedly in this homework. How did choosing appropriate
# data structures (lists, dictionaries, sets) make the problems easier to solve?
#
# Answer:
#

# =============================================================================
# Problem 5 — Challenge (Optional)
# =============================================================================

# This problem is optional but recommended for students who want extra practice.

# 5a. Implement a function that finds the longest streak of consecutive days
# with increasing case counts.

def longest_increasing_streak(counts):
    """
    Find the length of the longest streak of consecutive increasing values.
    
    For example:
    [1, 2, 3, 2, 3, 4, 5] → 4 (the streak 2, 3, 4, 5)
    [5, 4, 3, 2, 1] → 1 (no increasing streaks)
    [1, 2, 1, 2, 3, 4] → 4 (the streak 1, 2, 3, 4)
    
    Args:
        counts: list of numbers
    
    Returns:
        length of longest increasing streak
    """
    # Your code here
    pass

# Test your function
test_cases_5a = [45, 52, 48, 67, 71, 89, 103, 98, 87, 92]
print("5a:", longest_increasing_streak(test_cases_5a))

# 5b. Implement a function that finds all codons (3-letter sequences) that
# appear more than once in a DNA sequence.

def find_repeated_codons(sequence):
    """
    Find all 3-letter subsequences that appear more than once.
    
    For example:
    "ATCGATCG" → ["ATC", "TCG"] (both appear twice)
    
    Args:
        sequence: DNA sequence string
    
    Returns:
        list of codons that appear more than once
    """
    # Your code here
    pass

# Test your function
test_seq_5b = "ATCGATCGATCGTAGCTAGC"
print("5b:", find_repeated_codons(test_seq_5b))

"""
Expected time: 3-5 hours for students new to programming.

Main concepts practiced:
- List indexing and slicing
- Accumulator pattern (counting, summing)
- Dictionaries for aggregation and lookup
- Set operations
- String processing
- Nested data structures
- Algorithm design and efficiency
- Data validation and edge cases
"""