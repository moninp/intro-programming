# =============================================================================
# Homework 8: Python to R -- Translation and Fluency Practice
#
# Submit this file with your solutions filled in below each problem.
# Do not delete the problem statements.
#
# Instructions:
# - Write clear, readable R.
# - Test your code with the provided data and additional test cases.
# - For questions that ask for an explanation, write a short explanation in a
#   comment immediately below the relevant code.
# - When asked to predict output, make your prediction in a comment first.
# - Your code should run from top to bottom without requiring manual input.
#
# A note on this assignment: the underlying concepts here are all things
# you already know well from Python. The goal tonight is reps, not
# difficulty -- lots of short, focused exercises so that R syntax starts
# to feel automatic rather than something you have to consciously
# translate every time. Work through every sub-problem, even the ones
# that feel almost too easy; that repetition is the point.
# =============================================================================

# =============================================================================
# Problem 1 -- Finance: Daily Stock Returns
# =============================================================================

# A small trading desk recorded the closing price of a stock for eight
# consecutive trading days. You will practice creating vectors, checking
# their types, and performing basic vectorized arithmetic -- the same
# operations you would do with a NumPy array in Python.

prices <- c(101.2, 102.5, 100.8, 103.1, 104.0, 103.5, 105.2, 106.0)

# 1a. Confirm that `prices` is a numeric vector by checking its class()
#     and length(). Store the class in answer_1a_class and the length
#     in answer_1a_length.

answer_1a_class <- NULL
answer_1a_length <- NULL

# 1b. Without using diff(), compute the day-over-day price change for
#     days 2 through 8 (i.e., prices[2] - prices[1], prices[3] -
#     prices[2], and so on). Do this with a single vectorized
#     expression, not a loop. Store the result (a vector of length 7)
#     in daily_change.
#
# Hint: prices[2:8] - prices[1:7]

daily_change <- NULL

# 1c. Using daily_change, compute the number of days with a positive
#     price change. Store this count in answer_1c.

answer_1c <- NULL

# 1d. Compute the average daily change using mean(). Store it in
#     answer_1d.

answer_1d <- NULL

# 1e. A colleague suggests the price on day 5 might be a data entry
#     error and should be excluded from the mean. Create a new vector
#     prices_fixed that is identical to prices but with day 5 replaced
#     by NA. Then compute the mean of prices_fixed, first without
#     removing NA, then again removing NA. Store the two results in
#     answer_1e_with_na and answer_1e_without_na.

prices_fixed <- NULL
answer_1e_with_na <- NULL
answer_1e_without_na <- NULL

# =============================================================================
# Problem 2 -- Epidemiology: Daily Case Counts
# =============================================================================

# A small clinic reports new daily case counts over a two-week period.
# This problem practices logical filtering, basic statistics, and
# writing your first R function.

case_counts <- c(3, 5, 2, 8, 6, 4, 9, 11, 7, 3, 2, 6, 10, 8)

# 2a. How many days had more than 5 new cases? Store the count in
#     answer_2a. Do not use a loop.

answer_2a <- NULL

# 2b. Extract the subset of case_counts that is greater than 5 into a
#     new vector called high_days.

high_days <- NULL

# 2c. Write a function called pct_above_threshold that takes two
#     arguments, values and threshold, and returns the percentage
#     (0-100) of elements in values strictly greater than threshold.
#     Test it on case_counts with a threshold of 5; the result should
#     match answer_2a divided by length(case_counts), times 100.

pct_above_threshold <- function(values, threshold) {
  # TODO: implement this function
}

answer_2c_test <- NULL  # call pct_above_threshold(case_counts, 5) here

# 2d. Using a for loop (intentionally, for practice -- we will compare
#     this to a vectorized approach in 2e), compute the cumulative sum
#     of case_counts: a vector of the same length where element i is
#     the sum of all case counts up through day i. Store the result in
#     cumulative_loop.

cumulative_loop <- numeric(length(case_counts))
# TODO: fill in cumulative_loop using a for loop

# 2e. Now compute the same cumulative sum using R's built-in
#     cumsum() function, storing the result in cumulative_builtin.
#     Confirm the two approaches produce identical results using
#     identical().

cumulative_builtin <- NULL
answer_2e_identical <- NULL

# =============================================================================
# Problem 3 -- Physics: Measurement Error in a Pendulum Experiment
# =============================================================================

# A student measures the period of a pendulum (in seconds) across 10
# trials, expecting some measurement error around the true value. This
# problem practices lists, type checking, and writing a slightly more
# involved function.

trial_periods <- c(2.01, 1.98, 2.05, 1.99, 2.10, 2.02, 1.97, 2.03, 2.08, 2.00)

# 3a. Store trial_periods, the number of trials, and a short character
#     description of the experiment ("Pendulum period measurement") all
#     together in a single list called experiment. Use named elements:
#     periods, n_trials, description.

experiment <- NULL

# 3b. Using $ notation, extract the periods from experiment and
#     confirm (with a logical comparison, not just visually) that they
#     are identical to the original trial_periods vector. Store the
#     TRUE/FALSE result in answer_3b.

answer_3b <- NULL

# 3c. Write a function called summarize_measurements that takes a
#     numeric vector x and returns a named list with three elements:
#     mean_value (the mean of x), sd_value (the standard deviation of
#     x, using sd()), and range_value (a vector of length 2: the min
#     and max of x). Test it on trial_periods and store the result in
#     answer_3c.

summarize_measurements <- function(x) {
  # TODO: implement this function
}

answer_3c <- NULL

# 3d. Using your function from 3c, determine whether any individual
#     trial in trial_periods falls more than 2 standard deviations
#     from the mean (a common, if simplistic, outlier rule). Store a
#     logical vector (one TRUE/FALSE per trial) in answer_3d.
#
# Hint: abs(trial_periods - mean_value) > 2 * sd_value

answer_3d <- NULL

# =============================================================================
# Problem 4 -- Biology: A Small Dataset of Measurements
# =============================================================================

# A biology lab recorded the species and body length (in cm) of six
# captured specimens. This problem practices creating a data frame,
# inspecting it, and performing basic logical filtering -- the R
# analogue of everyday pandas DataFrame work.

specimens <- data.frame(
  species = c("frog", "frog", "lizard", "lizard", "lizard", "frog"),
  length_cm = c(4.2, 3.9, 7.1, 6.8, 7.5, 4.0)
)

# 4a. Use str() and summary() to inspect specimens (just run these --
#     no need to store output, but include the calls in your script so
#     the output appears when the file is run).

# 4b. Extract all rows where species is "lizard" into a new data frame
#     called lizards.

lizards <- NULL

# 4c. Compute the mean length_cm for lizards and for frogs separately,
#     without using group_by()/dplyr (we have not covered the
#     tidyverse yet -- use logical filtering as in 4b). Store the two
#     means in answer_4c_lizard_mean and answer_4c_frog_mean.

answer_4c_lizard_mean <- NULL
answer_4c_frog_mean <- NULL

# 4d. Add a new column to specimens called length_mm that is
#     length_cm converted to millimeters (1 cm = 10 mm).

# TODO: add the length_mm column to specimens

# 4e. Using logical filtering on the ORIGINAL specimens data frame
#     (now including length_mm), extract the single row corresponding
#     to the longest specimen (by length_cm). Store the result in
#     longest_specimen. Do not hard-code which row it is; your code
#     should work even if the data changed.
#
# Hint: specimens[specimens$length_cm == max(specimens$length_cm), ]

longest_specimen <- NULL

# =============================================================================
# Problem 5 -- Climate: Daily Temperature Readings
# =============================================================================

# A weather station recorded daily high temperatures (in Fahrenheit)
# for two weeks. This problem is a cumulative review: vectors, NA
# handling, functions, loops, and vectorization, all in one place.

daily_high_f <- c(72, 75, NA, 78, 80, 77, 74, 73, 76, 79, 81, NA, 75, 74)

# 5a. How many missing values (NA) are present in daily_high_f? Store
#     the count in answer_5a. (Hint: sum(is.na(...)))

answer_5a <- NULL

# 5b. Write a function called f_to_c that converts a Fahrenheit
#     temperature (or vector of temperatures) to Celsius, using the
#     formula C = (F - 32) * 5/9. Your function should work correctly
#     on a vector that includes NA values (NA should propagate, not
#     cause an error).

f_to_c <- function(f) {
  # TODO: implement this function
}

answer_5b_test <- NULL  # call f_to_c(daily_high_f) and store the result here

# 5c. Compute the mean daily high temperature in Celsius, correctly
#     ignoring missing values. Store the result in answer_5c.

answer_5c <- NULL

# 5d. Using a for loop, count how many non-missing days had a high
#     temperature (in Fahrenheit) above 76. Store the count in
#     answer_5d_loop. Then compute the same count using a single
#     vectorized expression (no loop) and store it in
#     answer_5d_vectorized. Confirm the two match.
#
# Hint: remember that comparisons involving NA produce NA, not FALSE --
# you may need is.na() or na.rm-style handling to get this right.

answer_5d_loop <- 0
# TODO: fill in using a for loop

answer_5d_vectorized <- NULL

answer_5d_match <- NULL  # TRUE/FALSE comparing the two counts

# =============================================================================
# Problem 6 -- Synthesis: Translate a Complete Python Analysis
# =============================================================================

# Below is a complete Python analysis using NumPy. Your job is to
# translate it into R, reproducing the same computation, not just
# matching the output superficially. This problem combines nearly
# everything from Problems 1-5: vectors, NA-style handling, logical
# filtering, grouping by a label, and functions.
#
# Python (for reference -- do not run this, it is not R):
#
#   import numpy as np
#
#   rng = np.random.default_rng(123)
#   measurements = rng.normal(loc=50, scale=5, size=24)
#   shift = np.repeat(["morning", "afternoon", "night"], 8)
#
#   def summarize(values):
#       return {
#           "mean": values.mean(),
#           "sd": values.std(ddof=1),
#           "n": len(values),
#       }
#
#   for s in ["morning", "afternoon", "night"]:
#       subset = measurements[shift == s]
#       print(s, summarize(subset))

# 6a. Translate the random generation step. Use set.seed(123) and
#     rnorm() to create a vector measurements of 24 values drawn from
#     a normal distribution with mean 50 and standard deviation 5.

set.seed(123)
measurements <- NULL

# 6b. Translate the `shift` label vector using rep(). Be careful to
#     choose each= or times= correctly so that the first 8
#     measurements are labeled "morning", the next 8 "afternoon", and
#     the last 8 "night".

shift <- NULL

# 6c. Write an R function called summarize_shift that takes a numeric
#     vector values and returns a named list with elements mean, sd,
#     and n -- the R translation of the Python summarize() function.
#     (Use R's built-in sd(), which by default matches NumPy's
#     std(ddof=1).)

summarize_shift <- function(values) {
  # TODO: implement this function
}

# 6d. For each of "morning", "afternoon", and "night", extract the
#     matching subset of measurements (using logical filtering on
#     shift) and apply summarize_shift(). Print the result for each
#     shift using a for loop, matching the structure of the Python
#     for-loop above.

# TODO: write the for loop

# 6e. In a comment below, write 3-5 sentences comparing the Python and
#     R versions of this analysis. Specifically address:
#       - Which parts translated almost line-for-line?
#       - Which parts required a different idiom (not just different
#         syntax, but a genuinely different way of expressing the same
#         idea)?
#       - Where, if anywhere, did R's vector-first design make the
#         problem easier or harder than the Python/NumPy version?

# TODO: write your comparison here as a comment

# =============================================================================
# Problem 7 -- Challenge (Optional)
# =============================================================================

# This problem is optional and intended for students who want
# additional practice. It is not required for full credit.

# 7a. Write a function called moving_average that takes a numeric
#     vector x and an integer window, and returns a vector of the same
#     length as x where element i is the mean of x[(i - window + 1):i]
#     for i >= window, and NA for i < window (not enough prior values
#     to compute a full window). Do not use any package beyond base R.
#
# Test your function on daily_high_f (Problem 5) with window = 3, and
# note that your function should correctly propagate NA when the
# window includes a missing value from the original data.

moving_average <- function(x, window) {
  # TODO: implement this function
}

answer_7a_test <- NULL  # call moving_average(daily_high_f, 3) here

"
Expected time: 3-5 hours for students still building R fluency.

Main concepts practiced:

- Creating and inspecting vectors, lists, and data frames
- Vectorized arithmetic and comparisons
- Logical filtering on vectors and data frames
- NA-aware computation (sum, mean, custom functions)
- Writing and testing simple R functions
- for loops versus vectorized/built-in alternatives (cumsum, etc.)
- rep() with each= versus times=
- Translating a complete small Python/NumPy analysis into R
"