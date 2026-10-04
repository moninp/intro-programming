"""
Homework 5: Forensic Genealogy - The Great Donut Heist

Submit this file with your solutions filled in below each problem.
Do not delete the problem statements.

Instructions:
- Write clear, readable Python code.
- Test your code with the provided data.
- For questions that ask for an explanation, write a short explanation in a
  comment or string immediately below the relevant code.
- Your code should run from top to bottom without requiring manual input.
"""

import numpy as np

# =============================================================================
# Problem 0 — Introduction to Forensic Genealogy and DNA Profiling
# =============================================================================

"""
THE GREAT DONUT HEIST

Early Tuesday morning, Principal Monin discovered a crime most heinous: 
someone had broken into the faculty lounge and stolen his entire collection of 
artisanal donuts from The Salty Bakery. These weren't ordinary donuts—
they were maple-bacon-bourbon glazed masterpieces, worth at least $47.

The thief was sloppy. They left behind:
1. Donut crumbs on the counter
2. A single hair on the evidence envelope
3. Fingerprints on the donut box (too smudged to use)

The campus has 8 suspects, all of whom have been suspiciously cheerful that 
morning and smell faintly of maple. Your job: use DNA evidence and numpy (of course!) to 
find the culprit.

 ═══════════════════════════════════════════════════════════════════════════
DNA PROFILING SIMPLIFIED
═══════════════════════════════════════════════════════════════════════════

DNA analysis for identification works by comparing specific genetic markers 
that vary between individuals. We'll use a simplified model:

- We examine 15 genetic markers (locations on DNA)
- Each marker has 2 alleles (one inherited from each parent)
- Alleles are represented as integers (12, 15, 18, etc.)
- A person's profile is a 15x2 array

Example:
    Person A: [[12, 15], [18, 18], [14, 16], ...]
              Marker 1   Marker 2   Marker 3
              
When both alleles are the same (like [18, 18]), the marker is "homozygous."
When different ([12, 15]), it's "heterozygous."

Real forensics uses similar principles—comparing Short Tandem Repeats (STRs) 
or Single Nucleotide Polymorphisms (SNPs)—but with more sophisticated analysis.
"""

# No code required for Problem 0—just understand the setup.


# =============================================================================
# Problem 1 — DNA Profile Analysis and Comparison
# =============================================================================

"""
You've extracted DNA from the crime scene and collected profiles from 5 suspects.
First, you need to organize the data and calculate basic similarity metrics.
"""

# Crime scene DNA profile (15 markers, provided as flat list for practice)
# That is, the first two numbers are the alleles for marker 1, the next two for marker 2, etc.
crime_scene_flat = [
    14, 17, 16, 19, 13, 15, 20, 22, 12, 14,
    18, 18, 15, 16, 21, 24, 11, 13, 19, 21,
    17, 17, 14, 15, 13, 16, 22, 23, 16, 18
]

# 1a. Convert the flat list to a (15, 2) numpy array
# Hint: Use np.array() and .reshape()
crime_scene_profile = None

print(f"Crime scene profile shape: {crime_scene_profile.shape if crime_scene_profile is not None else 'Not computed'}")


# 1b. Count how many markers are homozygous (both alleles identical)
# Hint: Compare first column with second column using Boolean indexing, then sum
num_homozygous = None

print(f"Crime scene homozygous markers: {num_homozygous if num_homozygous is not None else 'Not computed'}")


# Suspect profiles (5 suspects × 15 markers × 2 alleles)
suspects = np.array([
    # Suspect A
    [[14, 16], [16, 18], [13, 14], [20, 21], [12, 13],
     [18, 19], [15, 17], [21, 23], [11, 12], [19, 20],
     [17, 18], [14, 16], [13, 15], [22, 24], [16, 17]],
    
    # Suspect B  
    [[13, 15], [17, 19], [14, 15], [19, 21], [11, 13],
     [17, 18], [16, 17], [22, 24], [12, 14], [20, 22],
     [16, 17], [15, 16], [14, 16], [21, 23], [17, 18]],
    
    # Suspect C
    [[14, 17], [16, 19], [13, 15], [20, 22], [12, 14],
     [18, 18], [15, 16], [21, 24], [11, 13], [19, 21],
     [17, 17], [14, 15], [13, 16], [22, 23], [16, 18]],
    
    # Suspect D
    [[15, 17], [17, 20], [12, 14], [21, 23], [13, 15],
     [19, 20], [14, 16], [20, 22], [10, 12], [18, 20],
     [18, 19], [13, 15], [12, 14], [23, 25], [15, 17]],
    
    # Suspect E
    [[13, 16], [15, 18], [14, 16], [19, 20], [11, 12],
     [17, 19], [15, 17], [21, 22], [12, 13], [19, 21],
     [16, 18], [14, 15], [13, 15], [22, 24], [17, 19]]
])

suspect_names = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']

print(f"\nSuspect database shape: {suspects.shape}")


# 1c. Calculate genetic distance using sum of absolute differences
# For each suspect, calculate: sum of |suspect_allele - crime_allele| over all alleles
# Store results in distances array
distances = np.zeros(5)

for i in range(5):
    # Your code here
    # Hint: np.abs(suspects[i] - crime_scene_profile), then np.sum()
    pass

print(f"\nGenetic distances (lower = more similar):")
for i, name in enumerate(suspect_names):
    dist = distances[i] if distances[i] != 0 else 'Not computed'
    print(f"  {name}: {dist}")


# 1d. Find suspect with minimum distance
closest_idx = None  # Use np.argmin()
closest_name = None  # suspect_names[closest_idx]

print(f"\nSuspect with smallest genetic distance: {closest_name if closest_name else 'Not computed'}")


# 1e. Calculate homozygosity for each suspect
# Count how many markers are homozygous for each suspect
suspect_homozygosity = np.zeros(5, dtype=int)

for i in range(5):
    # Your code here
    # Hint: Similar to 1b, but for suspects[i]
    pass

print(f"\nHomozygous markers per suspect:")
for i, name in enumerate(suspect_names):
    print(f"  {name}: {suspect_homozygosity[i]}")

print(f"\nCrime scene homozygous markers: {num_homozygous}")


# 1f. EXPLANATION: Why might the closest match not be the culprit?
# Give at least 2 reasons.

"""
YOUR EXPLANATION HERE:


"""


# =============================================================================
# Problem 2 — Multiple Metrics and Statistical Analysis
# =============================================================================

"""
Genetic distance alone might not be enough. Different metrics can reveal 
different aspects of similarity. You'll calculate alternative measures and 
use statistical analysis to strengthen your conclusion.
"""

# 2a. Calculate "match rate" - what proportion of alleles match exactly?
# For each suspect, count how many individual alleles (out of 30 total) match 
# any allele in the crime scene profile at the same marker

match_rates = np.zeros(5)

for i in range(5):
    matches = 0
    for marker in range(15):
        # Check if suspect's alleles match either crime scene allele at this marker
        suspect_alleles = suspects[i, marker]
        crime_alleles = crime_scene_profile[marker]
        
        # Your code here: count matches
        # Hint: Check if suspect_alleles[0] equals crime_alleles[0] or crime_alleles[1]
        #       Also check if suspect_alleles[1] equals crime_alleles[0] or crime_alleles[1]
        pass
    
    match_rates[i] = matches / 30.0  # 30 total alleles (15 markers × 2)

print("\n2a. Match rates (proportion of alleles matching):")
for i, name in enumerate(suspect_names):
    rate = match_rates[i] if match_rates[i] != 0 else 'Not computed'
    print(f"  {name}: {rate:.3f}" if isinstance(rate, float) else f"  {name}: {rate}")


# 2b. Calculate correlation coefficient between profiles
# Flatten each profile to 1D and compute correlation with crime scene
# This measures how profiles co-vary

crime_flat = crime_scene_profile.flatten()
correlations = np.zeros(5)

for i in range(5):
    suspect_flat = suspects[i].flatten()
    
    # Your code here: calculate correlation
    # Hint: Use np.corrcoef(crime_flat, suspect_flat)
    # This returns a 2×2 matrix; you want the off-diagonal element
    pass

print("\n2b. Correlation coefficients (higher = more similar):")
for i, name in enumerate(suspect_names):
    corr = correlations[i] if correlations[i] != 0 else 'Not computed'
    print(f"  {name}: {corr:.4f}" if isinstance(corr, float) else f"  {name}: {corr}")


# 2c. Identify "shared rare alleles"
# Some alleles are rare in the population. If crime scene and suspect both 
# have rare alleles, that's stronger evidence.
# Define "rare" as alleles that appear less than or equal to 2 times across all suspects

# First, find all alleles and their frequencies
all_suspect_alleles = suspects.flatten()
unique_alleles, counts = np.unique(all_suspect_alleles, return_counts=True)

# Find rare alleles (appearing <=2 times)
rare_alleles = unique_alleles[counts <= 2]

print(f"\n2c. Rare alleles (appearing <=2 times): {rare_alleles}")

# Count shared rare alleles between crime scene and each suspect
shared_rare_counts = np.zeros(5, dtype=int)

for i in range(5):
    # Your code here: count how many rare alleles are shared
    # Hint: Check if alleles in suspects[i] are in rare_alleles AND in crime_scene_profile
    pass

print("\nShared rare alleles with crime scene:")
for i, name in enumerate(suspect_names):
    print(f"  {name}: {shared_rare_counts[i]}")


# 2d. Statistical significance - Random match probability
# Calculate the probability that a random person would match this well

# Assume each allele has frequency 0.1 in population (simplified)
# Probability of matching at one marker = (0.1)^2 = 0.01
# With 15 markers, probability of matching purely by chance:

P_random_match = 0.01 ** 15

print(f"\n2d. Probability of random match: {P_random_match:.2e}")

# For each suspect, calculate probability of their match given their distance
# Simplification: P(match | distance d) ≈ 0.01^(15 - d/2)
# where d is genetic distance

match_probabilities = np.zeros(5)

for i in range(5):
    # Your code here
    # Use: match_probabilities[i] = 0.01 ** max(0, 15 - distances[i]/2)
    pass

print("\nMatch probabilities for each suspect:")
for i, name in enumerate(suspect_names):
    prob = match_probabilities[i] if match_probabilities[i] != 0 else 'Not computed'
    if isinstance(prob, float):
        print(f"  {name}: {prob:.2e}")
    else:
        print(f"  {name}: {prob}")


# 2e. Create a summary score combining multiple metrics
# Weight different metrics to create overall similarity score
# Higher score = more likely to be the culprit

summary_scores = np.zeros(5)

for i in range(5):
    # Normalize and combine metrics
    # Lower distance is better (invert it)
    # Higher match rate is better
    # Higher correlation is better
    # More shared rare alleles is better
    
    # Your code here - suggested formula:
    # score = (1 / (1 + distances[i])) * match_rates[i] * (1 + correlations[i]) * (1 + shared_rare_counts[i])
    pass

print("\n2e. Summary scores (higher = more suspicious):")
for i, name in enumerate(suspect_names):
    score = summary_scores[i] if summary_scores[i] != 0 else 'Not computed'
    if isinstance(score, float):
        print(f"  {name}: {score:.4f}")
    else:
        print(f"  {name}: {score}")


# 2f. EXPLANATION: Broadcasting
# In your calculations, you used operations like suspects[i] - crime_scene_profile.
# Explain what numpy broadcasting is (looking it up if necessary) and why it makes this code work.

"""
YOUR EXPLANATION HERE:


"""


# =============================================================================
# Problem 3 — Final Analysis and Determination
# =============================================================================

"""
Now synthesize all evidence to make your determination. You should consider:
- Genetic distance (Problem 1c)
- Match rate (Problem 2a)  
- Correlation (Problem 2b)
- Shared rare alleles (Problem 2c)
- Summary score (Problem 2e)
- Homozygosity pattern (Problem 1e vs 1b)
"""

# 3a. Create a comprehensive report
# Print a formatted summary of all metrics for all suspects

print("\n" + "="*70)
print("COMPREHENSIVE FORENSIC ANALYSIS - THE GREAT DONUT HEIST")
print("="*70)

# Your code here: print a well-formatted table showing all metrics
# You can use formatted strings like:
# print(f"{'Suspect':<10} {'Distance':>10} {'Match Rate':>12} {'Correlation':>12} {'Rare Alleles':>12} {'Summary':>12}")

pass


# 3b. Identify the most likely culprit based on ALL evidence
# Don't just pick the person with lowest distance. Consider all metrics

prime_suspect = None  # Name of person you believe is guilty

# Your reasoning code here - you might check:
# - Who has highest summary score?
# - Is there a clear outlier?
# - Do multiple metrics agree?

pass

print(f"\n{'='*70}")
print(f"DETERMINATION")
print(f"{'='*70}")
print(f"\nBased on comprehensive DNA analysis, the culprit is: {prime_suspect if prime_suspect else 'UNDETERMINED'}")


# 3c. Justify your conclusion
# Explain WHY you chose this person. Reference specific metrics and values.

"""
YOUR JUSTIFICATION HERE (3-5 sentences):





"""


# 3d. Alternative hypothesis
# Is there a second suspect who could plausibly be guilty? Why or why not?

"""
YOUR ANALYSIS HERE (2-3 sentences):



"""


# 3e. EXPLANATION: Limitations of DNA evidence
# Even with a strong match, what are 2-3 limitations or concerns about 
# using DNA evidence to identify someone?

"""
YOUR EXPLANATION HERE:




"""
