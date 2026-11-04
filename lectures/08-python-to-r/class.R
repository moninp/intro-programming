
# =============================================================================
# Lecture 8: Python to R -- Two Languages, One Computational Model
# Live Coding Script (Stub)
#
# This file is worked through live in class. Each section below
# corresponds to an Exercise/Your Turn in class.qmd with the same number.
# Run this file top to bottom as the lecture progresses; do not skip
# sections, since later exercises often depend on objects defined
# earlier.
# =============================================================================


# =============================================================================
# Exercise 1: R as a Computational Language
# =============================================================================

# ---- Your Turn 1.1: Objects and Assignment ----
#
# In Python you would write:
#   x = 10
#   y = "hello"
#   print(type(x), type(y))
#
# In R, create an object x holding the number 10 and an object y
# holding the string "hello", using the <- assignment operator.
# Then use class() to check the type of each (R's version of
# Python's type()).

x <- 10
y <- "hello"

# ---- Your Turn 1.2: Vectors -- The Atomic Unit of R ----
#
# In Python:
#   scores = [85, 92, 78, 95]
#
# Create an R vector called scores holding the same four values,
# using c(). Then check its length() and class().

scores <- c(85,92,78,95)

scores_ <- c(85,92,78,95,"phil")

# note that scores_ runs without an error, but produces elements that are character type


# ---- Your Turn 1.3: Vectorized Comparisons and Logical Filtering ----
#
# Using the scores vector from 1.2:
#   (a) Compute a logical vector indicating which scores are above 90.
#   (b) Use that logical vector to extract only the scores above 90.
#
# In Python/NumPy this would be:
#   scores[scores > 90]

scores <- c(85, 92, 78, 95)
scores > 90

scores[scores > 90]


# =============================================================================
# Exercise 2: R Data Structures
# =============================================================================

# ---- Your Turn 2.1: Atomic Vector Types ----
#
# Create four objects, one of each atomic type:
#   a logical value, an integer (using the L suffix), a double, and
#   a character string. Confirm each type with class().

alogical <- TRUE
aninteger <- 13L
adouble = 3.14
achar <- "math5200"


# ---- Your Turn 2.2: Missing Values -- NA ----
#
# Create a numeric vector containing 1, 2, NA, and 4.
#   (a) Compute sum() on it directly -- what happens?
#   (b) Compute sum() again, this time removing NA values.

p = c(1,2,NA,4)
sum(p)
# NA
sum(p, na.rm=T)
# 7




# ---- Your Turn 2.3: Lists ----
#
# Create a list called person with three named elements:
#   name  -- a character string
#   age   -- a number
#   languages -- a character vector of more than one language
#
# Then access each element using the $ operator, e.g. person$name.

person = list(name = 'Portia', age = 23, languages=c('French','English','Twi') )

print(person$name)

# ---- Your Turn 2.4: Data Frames ----
#
# Create a data frame called df with two columns:
#   name  -- c("Ada", "Grace", "Alan")
#   score -- c(92, 88, 95)
#
# Inspect it with str() and summary().

df <- data.frame( name = c('Ada','Grace','Alan'),
                  score = c(92,88,95)
                  )

str(df)

summary(df)

# ---- Your Turn 2.5: Logical Filtering of Data Frames ----
#
# Using the df object from 2.4, extract only the rows where score
# is greater than 90. Recall the bracket syntax: df[condition, ]

# Several ways
df[ df$score > 90 , ]

df[ df['score'] > 90 , ]

df[ df[2] > 90 , ]


# =============================================================================
# Exercise 3: Functions and Iteration
# =============================================================================

# ---- Your Turn 3.1: Writing Functions in R ----
#
# Write a function called cube that takes a single argument x and
# returns x raised to the third power. Test it on a few values.

cube <- function(x){
  return(x^3)
}


# ---- Your Turn 3.2: for Loops ----
#
# Using a for loop, print the cube (using your cube() function from
# 3.1) of each integer from 1 to 5.
#
# Reminder: R's 1:5 includes both endpoints.

for (it in 1:5){
  print(cube(it))
}



# ---- Your Turn 3.3: while Loops ----
#
# Using a while loop, print successive powers of 2 (2, 4, 8, 16, ...)
# as long as the value stays below 100.

n = 1
while (2^n < 100){
  print(2^n)
  n <- n+1
}





# ---- Your Turn 3.4: Vectorization Instead of Loops ----
#
# Given values <- c(1, 2, 3, 4, 5):
#   (a) Compute the cube of every element using a for loop, storing
#       results in a pre-allocated vector.
#   (b) Compute the same result using direct vectorized arithmetic.
#   (c) Confirm both approaches give identical results using
#       identical() or all.equal().

values <- c(1, 2, 3, 4, 5)

values^3

cubed_values = numeric(length(values))
for (i in seq_along(values)){
  cubed_values[i] = values[i]^3
}

cubed_values = numeric(length(values))
for (i in values){
  cubed_values[i] = values[i]^3
}

# ---- Your Turn 3.5: Scope ----
#
# Write a function called make_local that creates a variable inside
# its body and returns it. Call the function, store the result, and
# then try to print the internal variable directly from the top
# level. Confirm this raises an error, and discuss why.

# TODO: work this out live in class
# NOTE: this is expected to raise an error -- that is the point


# =============================================================================
# Exercise 4: Major Exercise -- Translate Python to R
# =============================================================================

# ---- Your Turn 4.1: Simulate a Stochastic Process and Summarize by Group ----
#
# Python equivalent (for reference, already solved in a previous
# lecture):
#
#   import numpy as np
#   rng = np.random.default_rng(42)
#   values = rng.normal(loc=0, scale=1, size=20)
#   groups = np.repeat(["A", "B"], 10)
#
#   for g in ["A", "B"]:
#       print(g, values[groups == g].mean())
#
# Translate this to R:
#   (a) Set a random seed with set.seed(42) for reproducibility.
#   (b) Generate 20 draws from a standard normal distribution using
#       rnorm().
#   (c) Create a character vector "groups" with 10 "A" labels
#       followed by 10 "B" labels (hint: rep()).
#   (d) For each group, compute the mean of the values belonging to
#       that group using logical filtering.
#
# As you go, note explicitly: which parts translated almost
# directly, and which parts required a different approach in R?

set.seed(42)

sample = rnorm(mean=0, sd=1, n=20)

groups = c(rep('A',10), rep('B',10))

# If we want the mean of the entries in sample that correspond to entries in groups
# equal to "A" or "B"

# Extract a logical vector indicating when groups is equal to "A":
gA <-  ( groups == "A" )

# Then, use this to index into sample, and compute the mean
mean_A <- mean(sample[gA])

# Then we can do the same for "B", this time directly
mean_B <- mean(sample[groups == 'B'])



# ---- Your Turn 4.2 (Optional, Time Permitting): Write a Reusable Function ----
#
# Generalize your solution from 4.1 into a function group_mean(values,
# groups) that returns a named numeric vector of group means for any
# values/groups vectors of matching length. Test it on the data from
# 4.1, then test it again on a new simulated dataset with three
# groups instead of two.

# TODO: work this out live in class
