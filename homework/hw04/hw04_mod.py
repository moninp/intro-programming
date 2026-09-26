"""
Homework 4: Command Line, Git, and NumPy Arrays

Submit this file with your solutions filled in below each problem.
Do not delete the problem statements.

Instructions:
- Complete Problem 0 (Command Line & Git Setup) before starting the NumPy exercises.
- Write clear, readable Python code for Problems 1-4.
- Test your code with the provided data.
- Use git to commit your work after completing each NumPy problem (Problems 1-4).
- Your code should run from top to bottom without requiring manual input.
"""

# =============================================================================
# Problem 0 — Command Line & Git Setup (Not Graded - But Required!)
# =============================================================================

"""
IMPORTANT: Complete this section BEFORE starting the NumPy exercises.
This section teaches essential command line and version control skills.

═══════════════════════════════════════════════════════════════════════════
PART A: COMMAND LINE BASICS
═══════════════════════════════════════════════════════════════════════════

The command line (also called terminal, shell, or console) is a text-based
interface for interacting with your computer. While it may seem old-fashioned,
it's incredibly powerful for programming, data science, and automation.

STEP 1: Open Your Terminal
---------------------------
**macOS/Linux**: 
  - macOS: Open "Terminal" from Applications > Utilities
  - Linux: Open "Terminal" (keyboard shortcut: Ctrl+Alt+T on most systems)

**Windows**: 
  - Recommended: Open "PowerShell" (search for it in Start menu)
  - Alternative: Use "Git Bash" if you have Git installed (provides Unix-like commands)
  
  Note: PowerShell and Git Bash use slightly different commands. This guide shows
  both when they differ. If using PowerShell, follow PowerShell commands; if using
  Git Bash, follow macOS/Linux commands.

STEP 2: Determine Your Current Location
----------------------------------------
When you open a terminal, you start in a default directory (folder). Let's find
out where you are.

Command to show current directory:
  - macOS/Linux/Git Bash:  pwd    (print working directory)
  - PowerShell:            pwd    (works the same!)

Type the command and press Enter. You'll see a path like:
  - macOS: /Users/yourname
  - Linux: /home/yourname  
  - Windows PowerShell: C:\Users\yourname
  - Windows Git Bash: /c/Users/yourname

TASK: Write down your default starting directory below (as a comment):
"""

# My default terminal directory: 

"""
STEP 3: List Files in Current Directory
----------------------------------------
Let's see what files and folders are in your current location.

Commands to list files:
  - macOS/Linux/Git Bash:  ls           (list)
  - PowerShell:            dir  or  ls  (both work!)

To see hidden files (those starting with . like .gitignore):
  - macOS/Linux/Git Bash:  ls -a   (the -a flag means "all")
  - PowerShell:            ls -Force

Try both commands (with and without showing hidden files) and observe the difference.

STEP 4: Navigate to Your Documents Folder
------------------------------------------
Let's navigate to your Documents directory where you have (or will create) your
Math5200 folder.

Commands to change directory:
  - macOS/Linux/Git Bash:  cd Documents
  - PowerShell:            cd Documents  (same!)

After running this command, verify you're in the right place by running pwd again.

If you get an error like "no such file or directory":
  - You might be in a different location than expected
  - Try: cd ~/Documents (the ~ means your home directory)
  - On Windows PowerShell: cd ~\Documents

STEP 5: Create Math5200 Folder (if needed)
-------------------------------------------
If you don't already have a Math5200 folder, create it now.

Commands to make a directory:
  - macOS/Linux/Git Bash:  mkdir Math5200
  - PowerShell:            mkdir Math5200  (same!)

Then navigate into it:
  - All systems:  cd Math5200

STEP 6: Practice Navigation
----------------------------
Let's practice moving up and down the directory tree.

Command to go UP one directory level:
  - All systems:  cd ..   (two dots mean "parent directory")

Try this:
  1. From Math5200, type: cd ..
  2. You should be back in Documents. Verify with pwd.
  3. List files with ls (or dir) to confirm you see Math5200 folder.
  4. Navigate back: cd Math5200

Command to go directly to your home directory:
  - macOS/Linux/Git Bash:  cd ~
  - PowerShell:            cd ~  (same!)

TASK: Starting from Math5200, navigate to your home directory, then list all
      files including hidden ones. Describe what you find (write as comment below):
"""

# What I found in my home directory:
# (List 3-5 interesting files or folders you see, including any hidden files)

"""
═══════════════════════════════════════════════════════════════════════════
PART B: GIT SETUP
═══════════════════════════════════════════════════════════════════════════

Git is a version control system that tracks changes to your files over time.
It's like a sophisticated "undo" system that lets you:
  - Save snapshots of your work at different points
  - See what changed between versions
  - Collaborate with others
  - Recover old versions if you make mistakes

You'll use Git throughout your programming career, so it's crucial to learn it now.

STEP 1: Ensure You're in Math5200 Directory
--------------------------------------------
Before initializing Git, make sure you're in your Math5200 folder.

Commands:
  - Check current location: pwd
  - If not in Math5200: cd ~/Documents/Math5200  (macOS/Linux/Git Bash)
                        cd ~\Documents\Math5200   (PowerShell)

STEP 2: Initialize Git Repository
----------------------------------
This creates a new Git repository in your Math5200 folder.

Command (all systems):
  git init

You should see a message like: "Initialized empty Git repository in ..."

This creates a hidden .git folder that stores all version control information.

STEP 3: Verify .git Folder Exists
----------------------------------
Let's confirm the .git folder was created.

Commands to list hidden files:
  - macOS/Linux/Git Bash:  ls -a
  - PowerShell:            ls -Force

You should see a .git entry in the list. This folder contains all Git data.

WARNING: Never manually edit files in the .git folder! Git manages this automatically.

STEP 4: Create .gitignore File
-------------------------------
A .gitignore file tells Git which files to ignore. We'll ignore Python cache files
because:
  1. They're automatically generated when you run Python code
  2. They're not human-readable source code
  3. They can be different on different computers
  4. They're not needed to run your code (Python recreates them)
  5. They clutter your repository with unnecessary files

We'll use a command-line text editor to create this file.

For macOS/Linux/Git Bash - Using nano:
  1. Type: nano .gitignore
  2. In the editor, type these two lines:
       __pycache__/
       *.pyc
  3. Press Ctrl+O (letter O, not zero) to save
  4. Press Enter to confirm filename
  5. Press Ctrl+X to exit

For Windows PowerShell - Using notepad:
  1. Type: notepad .gitignore
  2. When notepad opens, type these two lines:
       __pycache__/
       *.pyc
  3. Click File > Save
  4. Close notepad

Alternative for PowerShell (using echo):
  1. Type: echo "__pycache__/" > .gitignore
  2. Type: echo "*.pyc" >> .gitignore
  (Note: > creates file, >> appends to file)

STEP 5: Verify .gitignore Was Created
--------------------------------------
Check that the file exists and has correct content.

Commands:
  - macOS/Linux/Git Bash:  cat .gitignore  (shows file contents)
  - PowerShell:            type .gitignore  or  cat .gitignore

You should see:
  __pycache__/
  *.pyc

EXPLANATION:
  - __pycache__/ means "ignore any folder named __pycache__"
  - *.pyc means "ignore any file ending in .pyc"
  - These are Python's compiled bytecode files, not source code

TASK: Why do we use .gitignore? Write your understanding below (2-3 sentences):
"""

# Why we use .gitignore:
# 

"""
STEP 6: Check Git Status
-------------------------
This shows what files Git sees and their status.

Command (all systems):
  git status

You should see:
  - "Untracked files" including .gitignore
  - Instructions about using "git add"

"Untracked" means Git sees the file but isn't tracking changes to it yet.

STEP 7: Stage Files for Commit
-------------------------------
"Staging" means preparing files to be committed (saved in Git's history).

Command to stage all files:
  git add .

The . means "current directory and everything in it"

Run git status again. Now .gitignore should be under "Changes to be committed"
in green (instead of red "Untracked files").

STEP 8: Make Initial Commit
----------------------------
A "commit" is a snapshot of your project at a point in time. Each commit needs
a message describing what changed.

Command:
  git commit -m "Initial commit"

The -m flag lets you provide the message directly. Always write descriptive messages!

You should see output like:
  [master (root-commit) abc1234] Initial commit
   1 file changed, 2 insertions(+)
   create mode 100644 .gitignore

STEP 9: View Commit History
----------------------------
Let's see the history of commits in this repository.

Commands:
  git log           (detailed view)
  git log --oneline  (compact view - one line per commit)

You should see your "Initial commit" with:
  - A commit hash (long string of letters/numbers)
  - Author information
  - Date and time
  - The commit message

Press 'q' to exit the log view if it doesn't return to command prompt automatically.

═══════════════════════════════════════════════════════════════════════════
GIT WORKFLOW FOR THIS ASSIGNMENT
═══════════════════════════════════════════════════════════════════════════

For this homework, you'll follow this workflow:

1. Complete Problem 1 (NumPy Exercise 1.3) in this file
2. Save the file
3. Run these Git commands:
     git add hw04.py
     git commit -m "Add solution to Problem 1"

4. Complete Problem 2 (NumPy Exercise 1.4)
5. Save the file
6. Run:
     git add hw04.py
     git commit -m "Add solution to Problem 2"

7. Repeat for Problems 3 and 4

8. At the end, run: git log --oneline

You should see 5 commits total:
  - Initial commit
  - Add solution to Problem 1
  - Add solution to Problem 2
  - Add solution to Problem 3
  - Add solution to Problem 4

TROUBLESHOOTING COMMON ISSUES
══════════════════════════════════════════════════════════════════════════

Lost in the file system?
  - Run pwd to see where you are
  - Run cd ~ to go home
  - Then navigate to Math5200: cd ~/Documents/Math5200

Git says "not a git repository"?
  - You're in the wrong folder
  - Navigate to Math5200 where you ran git init

Git asks for username and email?
  - Run these once (with your info):
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"

Can't see hidden files?
  - macOS/Linux/Git Bash: use ls -a
  - PowerShell: use ls -Force

Forgot a Git command?
  - git status: shows current state
  - git log: shows history
  - git help: shows available commands

File not found when trying to edit?
  - Make sure you're in the right directory (pwd)
  - Check if file exists (ls or dir)
  - Use full path if needed

PowerShell vs Git Bash confusion?
  - Most commands are the same (cd, pwd, mkdir, git)
  - Main difference: listing files (ls vs dir)
  - When in doubt, check online documentation

NOW YOU'RE READY! Proceed to Problem 1 below.
Remember to commit after each problem!
"""

# =============================================================================
# Problem 1 — Epidemiology: Outbreak Data Analysis (Array Indexing & Slicing)
# =============================================================================

"""
Epidemiologists track disease outbreaks across different geographic regions
and time periods to understand transmission patterns and guide public health
interventions. In this problem, you'll work with outbreak data from four
regions over 10 days, using NumPy array indexing and slicing to extract
specific subsets of data. Array indexing is crucial for accessing specific
data points, while slicing allows you to extract entire rows (regions), 
columns (days), or sub-arrays (specific regions over specific time periods).
Understanding these operations is fundamental to working with structured
numerical data in scientific computing.
"""

import numpy as np

# Outbreak data: 4 regions × 10 days
# Each row represents a region (A, B, C, D)
# Each column represents a day (0-9)
outbreak = np.array([
    [23, 29, 35, 41, 49, 58, 69, 81, 95, 112],   # Region A
    [15, 18, 22, 26, 31, 37, 44, 52, 62, 73],    # Region B
    [45, 56, 69, 85, 104, 127, 155, 189, 230, 280], # Region C
    [8, 9, 11, 13, 15, 18, 21, 25, 29, 34]       # Region D
])

# 1a. Extract all data for Region C (the third row, index 2)
# Hint: Use row indexing - remember Python uses 0-based indexing
region_c = None

# 1b. Get day 5 data for all regions (the sixth column, index 5)
# Hint: Use [:, column_index] to get all rows for a specific column
day_5 = None

# 1c. Get the last 3 days (days 7, 8, 9) for Region B (row index 1)
# Hint: Use negative indexing or slice notation like [-3:]
region_b_end = None

# 1d. Find all values where cases exceed 100
# Hint: Use boolean indexing - outbreak[condition] where condition is a comparison
high_outbreak = None

# 1e. Get the first week (days 0-6, inclusive) for regions A and C (rows 0 and 2)
# Hint: Use fancy indexing with a list of row indices, then slice columns
# Like: array[[row1, row2], start_col:end_col]
subset = None

# Print results (uncomment these after filling in your answers)
# print(f"Region C: {region_c}")
# print(f"Day 5 all regions: {day_5}")
# print(f"Region B last 3 days: {region_b_end}")
# print(f"High outbreak (>100 cases): {high_outbreak}")
# print(f"First week for regions A and C:\n{subset}")

"""
REMEMBER: After completing Problem 1, save this file and run:
  git add hw04.py
  git commit -m "Add solution to Problem 1"
"""

# =============================================================================
# Problem 2 — Epidemiology: Disease Growth Metrics (Elementwise Operations)
# =============================================================================

"""
Understanding how diseases spread requires calculating growth rates, doubling
times, and projections. These epidemiological metrics help public health
officials predict future case counts and evaluate intervention effectiveness.
In this problem, you'll use NumPy's elementwise operations to perform 
calculations across entire arrays efficiently, without writing explicit loops.
This vectorized approach is not only more concise but also significantly
faster than Python loops, especially with large datasets. You'll calculate
moving averages, growth factors, doubling times, projections, and cumulative
totals—all essential tools in epidemiological modeling.
"""

import numpy as np

# Daily confirmed cases over 14 days
cases = np.array([23, 29, 35, 41, 49, 58, 69, 81, 95, 112, 131, 154, 180, 211])

# 2a. Calculate 7-day moving averages
# We'll calculate the average for the first week and the second week
week1_avg = np.mean(cases[:7])  # Days 0-6
week2_avg = np.mean(cases[7:])  # Days 7-13
print(f"Week 1 average: {week1_avg:.1f}")
print(f"Week 2 average: {week2_avg:.1f}")

# 2b. Calculate daily growth factor (today's cases / yesterday's cases)
# Hint: Create two arrays - one shifted by one day - then divide elementwise
yesterday = cases[:-1]  # All but last day
today = cases[1:]       # All but first day
growth_factor = None    # Your code here: divide today by yesterday

# print(f"Daily growth factors: {growth_factor}")

# 2c. Estimate doubling time for each day
# Formula: doubling_time ≈ log(2) / log(growth_factor)
# Hint: Use np.log() for natural logarithm, np.log(2) for log of 2
doubling_times = None  # Your code here

# print(f"Doubling times (days): {doubling_times}")

# 2d. Project forward 7 days using average growth rate
# Start with last known value, multiply by average growth rate for each day
# Hint: avg_growth ** 7 gives growth over 7 days, then multiply by last_value
avg_growth = np.mean(growth_factor)
last_value = cases[-1]
projection = None  # Your code here: last_value * (avg_growth ** 7)

# print(f"7-day projection: {projection:.0f} cases")

# 2e. Calculate cumulative cases (running total)
# Hint: Use np.cumsum() which returns cumulative sum
cumulative = None  # Your code here

# print(f"Cumulative cases: {cumulative}")

"""
REMEMBER: After completing Problem 2, save this file and run:
  git add hw04.py
  git commit -m "Add solution to Problem 2"
"""

# =============================================================================
# Problem 3 — Epidemiology: Regional Outbreak Statistics (Array Aggregations)
# =============================================================================

"""
When analyzing multi-region outbreaks, epidemiologists need to compute
summary statistics both across time (for each region) and across space
(for each day). NumPy's aggregation functions with the `axis` parameter
make this straightforward. Understanding `axis=0` (aggregate across rows,
giving one result per column) versus `axis=1` (aggregate across columns,
giving one result per row) is crucial for working with multi-dimensional
data. In this problem, you'll calculate totals, averages, peaks, and
variability measures to characterize outbreak patterns across five regions
over 10 days.
"""

import numpy as np

# 5 regions × 10 days of case data
outbreak = np.array([
    [23, 29, 35, 41, 49, 58, 69, 81, 95, 112],   # Region A
    [15, 18, 22, 26, 31, 37, 44, 52, 62, 73],    # Region B
    [45, 56, 69, 85, 104, 127, 155, 189, 230, 280], # Region C
    [8, 9, 11, 13, 15, 18, 21, 25, 29, 34],      # Region D
    [67, 82, 100, 122, 148, 180, 219, 266, 323, 392] # Region E
])

# 3a. Calculate total cases across all regions and all days
# Hint: np.sum() with no axis argument sums everything
total = None

# 3b. Calculate total cases per region (sum across days)
# Hint: Use axis=1 to sum across columns, giving one value per row (region)
region_totals = None

# 3c. Calculate total cases per day (sum across regions)
# Hint: Use axis=0 to sum across rows, giving one value per column (day)
daily_totals = None

# 3d. Find average cases per region across all days
# Hint: Use np.mean() with axis=1
region_averages = None

# 3e. Find the peak (maximum) day for each region
# Hint: Use np.max() with axis=1
region_peaks = None

# 3f. Find which region had the worst single day overall
# This is provided as an example
worst_day_per_region = np.max(outbreak, axis=1)  # Max for each region
worst_region = None  # Your code here: use np.argmax() to find index of maximum

# print(f"Region with highest single-day cases: Region {chr(65 + worst_region)}")
# Note: chr(65) = 'A', chr(66) = 'B', etc., so chr(65 + index) converts index to letter

# 3g. Calculate standard deviation per region
# Hint: Use np.std() with axis=1
region_std = None

# Uncomment these print statements after filling in your answers:
# print(f"Total cases: {total}")
# print(f"Region totals: {region_totals}")
# print(f"Daily totals: {daily_totals}")
# print(f"Region averages: {region_averages}")
# print(f"Region peaks: {region_peaks}")
# print(f"Region std deviations: {region_std}")

"""
REMEMBER: After completing Problem 3, save this file and run:
  git add hw04.py
  git commit -m "Add solution to Problem 3"
"""

# =============================================================================
# Problem 4 — Epidemiology: Disease Modeling with Linear Algebra
# =============================================================================

"""
Mathematical epidemiology uses linear algebra to model disease transmission
through populations. The Next-Generation Matrix (NGM) approach calculates
the basic reproduction number (R₀), which represents the average number of
secondary infections caused by one infected individual in a fully susceptible
population. R₀ > 1 means the disease will spread; R₀ < 1 means it will die
out. The NGM is constructed from a contact matrix (who interacts with whom)
and transmission probabilities. Eigenvalues of this matrix reveal the disease's
growth potential, with the largest eigenvalue being R₀. This problem introduces
you to real epidemiological modeling using NumPy's linear algebra functions.
"""

import numpy as np

# Contact matrix: average daily contacts between age groups
# Rows and columns represent age groups: [0-20, 21-40, 41-60, 61+]
# Element [i,j] = average contacts per day between group i and group j
contact = np.array([
    [12, 4, 3, 1],   # 0-20 year olds have 12 contacts with their age group, 4 with 21-40, etc.
    [4, 10, 5, 2],   # 21-40 year olds
    [3, 5, 8, 3],    # 41-60 year olds
    [1, 2, 3, 6]     # 61+ year olds
])

# Transmission probability per contact (5% chance per contact)
transmission_prob = 0.05

# 4a. Create the Next-Generation Matrix (NGM)
# NGM = contact matrix × transmission probability
# Hint: Multiply the entire contact array by transmission_prob
NGM = None

# 4b. Calculate eigenvalues and eigenvectors
# Hint: Use np.linalg.eig() which returns (eigenvalues, eigenvectors)
eigenvalues = None
eigenvectors = None

# 4c. Find R₀ (the largest eigenvalue)
# Hint: Use np.max() on the eigenvalues array
R0 = None

# Uncomment these print statements after filling in your answers:
# print(f"Next-generation matrix:\n{NGM}")
# print(f"Eigenvalues: {eigenvalues}")
# print(f"R₀ = {R0:.3f}")
# print(f"Disease will {'spread' if R0 > 1 else 'die out'}")

# 4d. Model intervention (reduce all contacts by 50%)
contact_intervention = contact * 0.5
NGM_intervention = None  # Your code here: multiply contact_intervention by transmission_prob
eigenvalues_intervention, _ = None, None  # Your code here: use np.linalg.eig()
R0_intervention = None  # Your code here: find max eigenvalue

# Uncomment these print statements after filling in your answers:
# print(f"\nWith 50% contact reduction:")
# print(f"New R₀ = {R0_intervention:.3f}")
# print(f"Reduction: {(R0 - R0_intervention) / R0 * 100:.1f}%")

# 4e. Solve a linear system for equilibrium populations
# This is a simplified compartmental model
# We have a system of linear equations: Ax = b, solve for x
# Interpretation: At equilibrium, flow in = flow out for each compartment
A = np.array([
    [1, -0.5],    # Equation 1: x1 - 0.5*x2 = 100
    [-0.3, 1]     # Equation 2: -0.3*x1 + x2 = 50
])
b = np.array([100, 50])

# Solve the system Ax = b
# Hint: Use np.linalg.solve(A, b)
equilibrium = None

# print(f"\nEquilibrium populations: {equilibrium}")

"""
REMEMBER: After completing Problem 4, save this file and run:
  git add hw04.py
  git commit -m "Add solution to Problem 4"

Then run: git log --oneline
You should see 5 commits total (Initial commit + 4 problem commits)
"""