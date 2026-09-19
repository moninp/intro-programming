"""
Homework 3: Functions and Python Fundamentals Review

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
# Problem 1 — Seismology: Earthquake Magnitude Analysis
# =============================================================================

# Seismologists monitor earthquake activity to understand tectonic patterns and
# assess seismic hazards. Earthquake magnitude measures the energy released,
# with each whole number increase representing roughly 32 times more energy.
# In this problem, you'll analyze earthquake magnitude data from a seismic
# monitoring station over two weeks. You'll practice working with lists,
# basic control flow, and writing simple functions to process seismic data.
# Understanding earthquake patterns helps scientists predict future seismic
# activity and inform building codes in earthquake-prone regions.

# Earthquake magnitudes (Richter scale) recorded over 14 days
# Magnitude 0-2: micro, 2-4: minor, 4-5: light, 5-6: moderate, 6-7: strong, 7+: major
earthquake_magnitudes = [2.1, 3.4, 1.8, 2.9, 4.2, 3.7, 2.3, 
                         1.9, 3.1, 2.6, 5.1, 3.8, 2.4, 3.2]

# 1a. Without using any built-in functions like sum(), max(), or min(), write
# a for loop that counts how many earthquakes had a magnitude of 3.0 or greater.
# Store the result in significant_count.

significant_count = None

# 1b. Without using built-in functions, write a for loop that calculates the
# total sum of all earthquake magnitudes. Then calculate the mean (average)
# magnitude. Store the sum in total_magnitude and the mean in mean_magnitude.

total_magnitude = None
mean_magnitude = None

# 1c. Write a function called calculate_mean_magnitude() that takes a list of 
# magnitudes as a parameter and returns the mean. The function should work for
# any list of numbers, not just earthquake data. Use a for loop inside your function.
# Then, use your function to verify your answer from 1b.

def calculate_mean_magnitude(magnitudes):
    """Calculate the mean magnitude from a list of earthquake magnitudes."""
    pass  # Replace with your code

mean_magnitude_func = None  # Call your function here

# 1d. Write a function called find_magnitude_range() that takes a list of 
# earthquake magnitudes and returns both the minimum and maximum magnitudes as a 
# tuple (min, max). Do NOT use the built-in min() or max() functions.
# Hint: Initialize both min and max with the first element, then loop through
# the remaining elements comparing each one.

def find_magnitude_range(magnitudes):
    """Find minimum and maximum earthquake magnitudes."""
    pass  # Replace with your code

min_magnitude, max_magnitude = None, None  # Call your function here

# 1e. A seismic cluster is defined as 4 or more consecutive days with at least
# one earthquake of magnitude 2.5 or higher per day. Write a function called
# detect_seismic_cluster() that takes a list of daily magnitudes and a threshold
# magnitude, and returns True if there's a seismic cluster (4+ consecutive days
# at or above threshold), False otherwise.
# Hint: Use a counter to track consecutive days at/above threshold.

def detect_seismic_cluster(magnitudes, threshold=2.5):
    """Detect if there's a seismic cluster (4+ consecutive days above threshold)."""
    pass  # Replace with your code

has_cluster = None  # Call your function with the earthquake_magnitudes data

# 1f. Data types and type conversion: The earthquake_magnitudes list contains 
# float values. Create a new list called magnitudes_rounded that contains all 
# magnitudes rounded to the nearest integer (as int type, not float). 
# Use a for loop and the round() and int() functions.

magnitudes_rounded = None

# 1g. Create a function called classify_earthquake() that takes a magnitude
# and returns a classification string:
# - 'micro' if magnitude < 2.0
# - 'minor' if magnitude >= 2.0 and < 4.0
# - 'light' if magnitude >= 4.0 and < 5.0
# - 'moderate' if magnitude >= 5.0 and < 6.0
# - 'strong' if magnitude >= 6.0 and < 7.0
# - 'major' if magnitude >= 7.0
# Use if/elif/else statements.

def classify_earthquake(magnitude):
    """Classify earthquake by magnitude."""
    pass  # Replace with your code

# Test your function
test_classification = None  # classify_earthquake(4.2) should return 'light'

# 1h. Boolean logic: Create a list called above_average that contains True for 
# earthquakes where the magnitude was above the mean, and False otherwise. 
# Use a for loop and your calculated mean_magnitude from earlier.

above_average = None

# 1i. Using your classify_earthquake() function, create a list called 
# earthquake_categories that contains the classification string for each
# earthquake in the dataset. Use a for loop.

earthquake_categories = None

# 1j. EXPLANATION QUESTION: In your detect_seismic_cluster() function, you used a
# default parameter value (threshold=2.5). Write a 2-3 sentence explanation
# below describing what default parameters are and why they're useful.

"""
YOUR EXPLANATION HERE:

"""

# =============================================================================
# Problem 2 — Pharmacology: Drug Dosage Calculator
# =============================================================================

# Pharmacologists must carefully calculate drug dosages based on patient 
# characteristics like weight, age, and kidney function. Incorrect dosages can
# be ineffective or dangerous. In this problem, you'll work with patient data
# stored in dictionaries and write functions to calculate appropriate drug
# doses. This type of calculation is crucial in clinical settings where
# personalized medicine requires adjusting treatments for individual patients.
# You'll practice working with dictionaries, conditional logic, and functions
# with multiple parameters.

# Patient data: dictionary where keys are patient IDs, values are dictionaries
# containing patient information
patients = {
    'P001': {'name': 'Alice Chen', 'weight_kg': 68, 'age': 45, 'kidney_function': 'normal'},
    'P002': {'name': 'Bob Martinez', 'weight_kg': 82, 'age': 67, 'kidney_function': 'reduced'},
    'P003': {'name': 'Carol Singh', 'weight_kg': 58, 'age': 34, 'kidney_function': 'normal'},
    'P004': {'name': 'David Kim', 'weight_kg': 95, 'age': 71, 'kidney_function': 'reduced'},
    'P005': {'name': 'Emma Wilson', 'weight_kg': 72, 'age': 52, 'kidney_function': 'normal'}
}

# 2a. Access the dictionary for patient 'P003' and extract their weight.
# Store the weight in p003_weight.

p003_weight = None

# 2b. Use a for loop to create a new dictionary called patient_names where
# the keys are patient IDs and the values are just the patient names.
# Example: {'P001': 'Alice Chen', 'P002': 'Bob Martinez', ...}

patient_names = None

# 2c. Write a function called calculate_basic_dose() that takes a weight in kg
# as a parameter and returns the drug dose in mg. The basic formula is:
# dose (mg) = 5 mg/kg × weight (kg)
# For example, a 70 kg patient would get 5 × 70 = 350 mg.

def calculate_basic_dose(weight_kg):
    """Calculate basic drug dose based on weight."""
    pass  # Replace with your code

# Test your function with a 70 kg patient
test_dose = None  # Should be 350

# 2d. Write a function called calculate_adjusted_dose() that takes three 
# parameters: weight_kg, age, and kidney_function. The function should:
# 1. Start with the basic dose (5 mg/kg × weight)
# 2. If age > 65, reduce dose by 25% (multiply by 0.75)
# 3. If kidney_function is 'reduced', reduce dose by another 30% (multiply by 0.7)
# 4. Return the final adjusted dose rounded to 1 decimal place
# Hint: Apply adjustments sequentially - age first, then kidney function.

def calculate_adjusted_dose(weight_kg, age, kidney_function):
    """Calculate adjusted drug dose based on weight, age, and kidney function."""
    pass  # Replace with your code

# 2e. Using your calculate_adjusted_dose() function, create a new dictionary
# called patient_doses where keys are patient IDs and values are the
# calculated doses for each patient. Use a for loop.

patient_doses = None

# 2f. Use a while loop to find the first patient (in order of the dictionary)
# whose dose is greater than 300 mg. Store the patient ID in first_high_dose.
# Hint: You can iterate through dictionary keys using list(patients.keys())[index]
# or convert the keys to a list first.

first_high_dose = None

# 2g. Conditional logic: Write a function called dose_category() that takes a
# dose in mg and returns a string category:
# - 'low' if dose < 200
# - 'medium' if dose >= 200 and < 350
# - 'high' if dose >= 350
# Use if/elif/else statements.

def dose_category(dose_mg):
    """Categorize dose as low, medium, or high."""
    pass  # Replace with your code

# 2h. Create a set (not a list) containing all the unique dose categories
# for your patients. Use your dose_category() function and the patient_doses
# dictionary. Store the result in unique_categories.

unique_categories = None

# 2i. EXPLANATION QUESTION: Why is a set more appropriate than a list for
# storing unique categories in part 2h? Write 2-3 sentences explaining the
# difference between sets and lists in Python.

"""
YOUR EXPLANATION HERE:

"""

# =============================================================================
# Problem 3 — Astronomy: Stellar Classification
# =============================================================================

# Astronomers classify stars based on their properties like temperature, 
# luminosity, and mass. The Hertzsprung-Russell diagram is a fundamental tool
# that plots stellar temperature against luminosity, revealing patterns that
# help us understand stellar evolution. In this problem, you'll work with data
# from multiple stars, using tuples to represent immutable stellar properties
# and writing functions to classify stars. This illustrates how astronomers
# process observational data to categorize the billions of stars in our galaxy
# and beyond, helping us understand how stars are born, live, and die.

# Star data: each tuple contains (star_name, temperature_K, luminosity_solar, mass_solar)
# Temperature is in Kelvin, luminosity is relative to Sun (Sun = 1.0),
# mass is relative to Sun (Sun = 1.0)
stars = [
    ('Sirius', 9940, 25.4, 2.02),
    ('Betelgeuse', 3500, 126000, 16.5),
    ('Proxima Centauri', 3042, 0.0017, 0.12),
    ('Rigel', 11000, 120000, 21.0),
    ('Barnard\'s Star', 3134, 0.0004, 0.14),
    ('Vega', 9602, 40.12, 2.14),
    ('Antares', 3660, 57500, 12.4),
    ('Alpha Centauri A', 5790, 1.519, 1.08)
]

# 3a. Tuples are immutable. Access the temperature of the third star 
# (Proxima Centauri) using indexing. Remember that tuple elements can also
# be accessed by index, and that the star tuple itself is at index 2 in the list.
# Store the temperature in proxima_temp.

proxima_temp = None

# 3b. Use tuple unpacking in a for loop to create a list of just the star names.
# Tuple unpacking allows you to write: name, temp, lum, mass = star_tuple
# Store the result in star_names.

star_names = None

# 3c. Write a function called get_star_property() that takes two parameters:
# a star tuple and a property name (string: 'name', 'temperature', 'luminosity', 
# or 'mass'), and returns the corresponding value.
# Hint: Use if/elif statements to check which property is requested.

def get_star_property(star_tuple, property_name):
    """Extract a specific property from a star tuple."""
    pass  # Replace with your code

# Test: Should return 9940
sirius_temp = None  # get_star_property(stars[0], 'temperature')

# 3d. Write a function called classify_by_temperature() that takes a temperature
# in Kelvin and returns a classification string:
# - 'O' if temp >= 30000
# - 'B' if temp >= 10000
# - 'A' if temp >= 7500
# - 'F' if temp >= 6000
# - 'G' if temp >= 5200
# - 'K' if temp >= 3700
# - 'M' if temp < 3700
# This is a simplified version of stellar spectral classification.

def classify_by_temperature(temperature_K):
    """Classify star by temperature (simplified spectral type)."""
    pass  # Replace with your code

# 3e. Write a function called classify_by_luminosity() that takes a luminosity
# value (relative to Sun) and returns a classification:
# - 'supergiant' if luminosity > 10000
# - 'giant' if luminosity > 100
# - 'main sequence' if luminosity >= 0.01
# - 'subdwarf' if luminosity < 0.01

def classify_by_luminosity(luminosity_solar):
    """Classify star by luminosity."""
    pass  # Replace with your code

# 3f. Write a function called get_full_classification() that takes a star tuple
# and returns a dictionary with the classification results. The function should:
# 1. Call classify_by_temperature() with the star's temperature
# 2. Call classify_by_luminosity() with the star's luminosity
# 3. Return a dictionary with keys 'spectral_type' and 'luminosity_class'
# This demonstrates functions calling other functions.

def get_full_classification(star_tuple):
    """Get complete classification for a star."""
    pass  # Replace with your code

# Test with Sirius
sirius_classification = None  # Should be {'spectral_type': 'A', 'luminosity_class': 'main sequence'}

# 3g. Use a for loop to create a list of tuples called hot_stars containing
# only stars with temperature > 5000K. Each tuple should contain (name, temperature).
# Hint: Use conditional logic inside your loop.

hot_stars = None

# 3h. Create a dictionary called star_classifications where keys are star names
# and values are the full classification dictionaries (from get_full_classification).
# Use a for loop and tuple unpacking.

star_classifications = None

# 3i. Object exploration: Use dir() on one of the star tuples to see what 
# attributes and methods tuples have. Then determine which of the following
# are methods (callable) and which are properties: 'count', 'index', '__len__'.
# Store your findings as a dictionary where keys are the attribute names and
# values are True (if callable) or False (if not callable).
# Hint: Use callable() to test each one.

star_tuple = stars[0]
attribute_types = {
    'count': None,      # Is tuple.count callable?
    'index': None,      # Is tuple.index callable?
    '__len__': None     # Is tuple.__len__ callable?
}

# 3j. EXPLANATION QUESTION: Why do you think astronomers might use tuples
# rather than lists to store star data (name, temperature, luminosity, mass)?
# Write 2-3 sentences about immutability and when it's appropriate.

"""
YOUR EXPLANATION HERE:

"""

# =============================================================================
# Problem 4 — Synthesis: Marine Biology Population Dynamics
# =============================================================================

# Marine biologists study how fish populations change over time due to
# reproduction, mortality, and fishing. In this synthesis problem, you'll
# simulate a simplified population model that tracks multiple fish species
# in a marine reserve. This problem combines all the concepts you've learned:
# functions, dictionaries, lists, loops, conditionals, and data types.
# Understanding population dynamics is critical for sustainable fisheries
# management and marine conservation. Your code will simulate how populations
# grow or decline under different conditions, helping identify sustainable
# fishing quotas.

# Initial population data: dictionary where keys are species names,
# values are dictionaries with population parameters
populations = {
    'Blue Tang': {'count': 1200, 'growth_rate': 0.15, 'fishing_quota': 50},
    'Yellowfin Tuna': {'count': 450, 'growth_rate': 0.08, 'fishing_quota': 40},
    'Clownfish': {'count': 3500, 'growth_rate': 0.22, 'fishing_quota': 0},  # Protected species
    'Red Snapper': {'count': 890, 'growth_rate': 0.12, 'fishing_quota': 80}
}

# 4a. Write a function called simulate_year() that takes a species' current count,
# growth_rate, and fishing_quota, and returns the population after one year.
# The calculation is:
# 1. Natural growth: new_pop = count × (1 + growth_rate)
# 2. Subtract fishing quota: new_pop = new_pop - fishing_quota
# 3. Population cannot go below 0
# Return the result as an integer (use int() to round down).

def simulate_year(count, growth_rate, fishing_quota):
    """Simulate one year of population change."""
    pass  # Replace with your code

# Test: Blue Tang starting at 1200, growth 0.15, quota 50 should give:
# 1200 × 1.15 - 50 = 1330
test_population = None

# 4b. Write a function called simulate_multiple_years() that takes a species'
# starting count, growth_rate, fishing_quota, and number of years, and returns
# a list of population counts for each year (including year 0).
# Use a for loop and call simulate_year() each iteration.
# Example: for 3 years, return a list of 4 values [year0, year1, year2, year3]

def simulate_multiple_years(count, growth_rate, fishing_quota, years):
    """Simulate population over multiple years."""
    pass  # Replace with your code

# Test with Blue Tang over 5 years
blue_tang_trajectory = None

# 4c. Write a function called check_sustainability() that takes the same
# parameters as simulate_multiple_years() and returns True if the population
# is sustainable (doesn't decline by more than 20% over the period), False otherwise.
# Hint: Compare the final population to the initial population.

def check_sustainability(count, growth_rate, fishing_quota, years):
    """Check if current fishing quota is sustainable."""
    pass  # Replace with your code

# 4d. Create a dictionary called sustainability_report where keys are species
# names and values are True/False indicating if current fishing quotas are
# sustainable over 10 years. Use a for loop and your check_sustainability function.

sustainability_report = None

# 4e. Write a function called find_max_quota() that takes a species' starting count,
# growth_rate, and number of years, and returns the maximum fishing quota that
# keeps the population stable (doesn't decline). Use a while loop that starts
# with quota=0 and increments by 5 until the population starts declining.
# Return the last quota that maintained or increased the population.
# Hint: This might take several iterations to get right!

def find_max_quota(count, growth_rate, years=10):
    """Find maximum sustainable fishing quota."""
    pass  # Replace with your code

# Find max sustainable quota for Yellowfin Tuna
tuna_max_quota = None

# 4f. Create a report: Use nested for loops and string formatting to create a
# multi-line string report. For each species, show:
# - Species name
# - Starting population
# - Population after 10 years (with current quota)
# - Sustainability status
# Store the result in population_report.
# Hint: Use \n for newlines and f-strings for formatting.

population_report = None
# Your report should look something like:
# Blue Tang: 1200 → 1500 (Sustainable)
# Yellowfin Tuna: 450 → 380 (Unsustainable)
# ...

# 4g. Variable scope challenge: Look at this code and predict what will be
# printed BEFORE running it. Write your prediction in a comment, then test.

x = 10

def outer_function():
    x = 20
    
    def inner_function():
        x = 30
        return x
    
    return x + inner_function()

result = outer_function()
print(f"Result: {result}, Global x: {x}")

# YOUR PREDICTION:
# Result will be: ???
# Global x will be: ???

# 4h. EXPLANATION QUESTION: In marine biology, why is it important to model
# population dynamics before setting fishing quotas? Also, explain how the
# growth_rate parameter in our model relates to a fish species' biological
# reproduction rate. Write 3-4 sentences.

"""
YOUR EXPLANATION HERE:

"""

# =============================================================================
# Problem 5 — Challenge (Optional)
# =============================================================================

# This problem is optional and more challenging. It's designed for students
# who finish the main problems early and want extra practice.

# DNA sequences can be represented as strings of nucleotides (A, T, G, C).
# A reading frame is a way of dividing DNA into consecutive triplets (codons).
# There are three possible reading frames depending on where you start.

dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

# 5a. Write a function called get_codons() that takes a DNA sequence string
# and a frame number (0, 1, or 2), and returns a list of codon strings.
# Frame 0 starts at position 0, frame 1 at position 1, frame 2 at position 2.
# Only include complete codons (length 3).
# Example: "ATGGCC" in frame 0 gives ["ATG", "GCC"]
# Example: "ATGGCC" in frame 1 gives ["TGG"]

def get_codons(sequence, frame=0):
    """Extract codons from DNA sequence in specified reading frame."""
    pass  # Replace with your code

# 5b. Write a function called find_start_codons() that takes a DNA sequence
# and returns a list of all positions where the start codon "ATG" appears.
# Use a while loop to search through the sequence.

def find_start_codons(sequence):
    """Find all positions of start codon ATG."""
    pass  # Replace with your code

# 5c. The stop codons are "TAA", "TAG", and "TGA". Write a function called
# find_orfs() that takes a DNA sequence and returns a list of potential genes
# (Open Reading Frames). An ORF starts with "ATG" and ends with a stop codon,
# and must be in the same reading frame.
# This is quite challenging! Break it down into steps:
# 1. Find all start positions
# 2. For each start, extract codons in that frame
# 3. Look for stop codons
# 4. If found, save the sequence from start to stop
# Return a list of tuples: (start_pos, end_pos, sequence)

def find_orfs(sequence):
    """Find Open Reading Frames (start codon to stop codon)."""
    pass  # Replace with your code

orfs = None  # Call your function