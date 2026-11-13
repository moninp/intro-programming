# =============================================================================
# Lecture 10: Statistical Computing, Simulation, and Modeling
# Live Coding Script (Stub)
#
# This file is worked through live in class. Each section below
# corresponds to an Exercise/Your Turn in class.qmd with the same number.
# Run this file top to bottom as the lecture progresses; do not skip
# sections, since later exercises depend on objects defined earlier.
# =============================================================================


# =============================================================================
# Shared Setup: A Financial Risk Data-Generating Process
# =============================================================================
#
# Throughout today's lecture, we treat daily stock returns as random
# draws from a known probability distribution. In reality we never
# know the true data-generating process -- but by ASSUMING one here,
# we can check how well our statistical tools recover the truth we
# built in ourselves.

true_mean_return <- 0.001   # 0.1% average daily return
true_sd_return <- 0.02      # 2% daily volatility


# =============================================================================
# Exercise 1: Randomness and Reproducibility
# =============================================================================

# ---- Your Turn 1.1: Pseudorandom Generation and Seeds ----
#
# (a) Set the seed to 2026 and draw 5 values from rnorm() using
#     true_mean_return and true_sd_return.
# (b) Run the exact same two lines again. Confirm the results are
#     identical.
# (c) Change the seed to 2027 and rerun. Confirm the results differ.

# TODO: work this out live in class
# PAUSE: ask students to predict whether (b) will match (a) exactly,
#        before running it


# ---- Your Turn 1.2: Independent Repetitions ----
#
# (a) Set a seed of your choice. Draw a single sample of 30 daily
#     returns using true_mean_return and true_sd_return.
# (b) Compute the sample mean. How close is it to true_mean_return?
# (c) Without changing the seed, draw a SECOND sample of 30 (just
#     call rnorm() again) and compute its mean. Compare to (b).

# TODO: work this out live in class


# =============================================================================
# Exercise 2: Monte Carlo Reasoning
# =============================================================================

# ---- Your Turn 2.1: A Monte Carlo Approximation ----
#
# We want to estimate P(daily return < -3%), assuming returns are
# Normal(true_mean_return, true_sd_return).
#
# (a) Compute the EXACT answer using pnorm().
# (b) Set a seed, simulate 100,000 draws from the same distribution,
#     and compute the PROPORTION of simulated draws below -0.03.
# (c) Compare (a) and (b). How close are they?

# TODO: work this out live in class


# ---- Your Turn 2.2: Convergence with Simulation Size ----
#
# For each simulation size in c(10, 100, 1000, 10000, 100000):
#   (a) Simulate that many draws from Normal(true_mean_return,
#       true_sd_return) (use a fresh seed each time, or just let the
#       global RNG state continue -- either is fine for this
#       demonstration).
#   (b) Compute the proportion below -0.03.
#   (c) Store the results and compare to the exact value from 2.1.
#
# Use a for loop or sapply() -- your choice.

sim_sizes <- c(10, 100, 1000, 10000, 100000)

# TODO: work this out live in class



# =============================================================================
# Exercise 3: Sampling Distributions
# =============================================================================

# ---- Your Turn 3.1: The Sampling Distribution of the Mean ----
#
# (a) Set a seed. Using a for loop (or sapply()), simulate 5000 sample
#     means, each computed from a fresh sample of n = 30 draws from
#     Normal(true_mean_return, true_sd_return). Store the 5000 means
#     in a vector called sample_means.
# (b) Plot a histogram of sample_means using hist().
# (c) Compute the mean and standard deviation of sample_means. Compare
#     the mean to true_mean_return, and the standard deviation to the
#     theoretical standard error true_sd_return / sqrt(30).

n_sims <- 5000
sample_means <- numeric(n_sims)

# TODO: work this out live in class


# ---- Your Turn 3.2: Effect of Sample Size on Variance ----
#
# Repeat Exercise 3.1, but with n = 100 instead of n = 30. Store the
# result in sample_means_n100. Compare sd(sample_means) (from 3.1,
# n = 30) to sd(sample_means_n100). By roughly what factor should the
# standard deviation shrink, given the change in sample size? Confirm
# this matches what you observe.

# TODO: work this out live in class


# =============================================================================
# Exercise 4: Statistical Inference via Simulation
# =============================================================================

# ---- Your Turn 4.1: Confidence Interval Coverage ----
#
# (a) Write a function called one_ci() with no arguments that: draws
#     a sample of n = 30 from Normal(true_mean_return,
#     true_sd_return), computes the sample mean and standard error,
#     and returns a named vector c(lower = ..., upper = ...) for a
#     95% confidence interval (mean +/- 1.96 * se).
# (b) Set a seed. Call one_ci() 2000 times (sapply() works well here),
#     and for each resulting interval, check whether true_mean_return
#     falls between lower and upper.
# (c) Compute the proportion of intervals that contain
#     true_mean_return. This proportion is the empirical COVERAGE of
#     your confidence interval procedure. How close is it to 0.95?

one_ci <- function() {
  # TODO: implement this function
}

# TODO: work this out live in class


# ---- Your Turn 4.2: Statistical Power ----
#
# (a) Simulate 2000 samples of n = 30 under the NULL hypothesis that
#     the true mean is 0 (not true_mean_return). For each sample, run
#     t.test(sample_data, mu = 0) and record whether the p-value is
#     below 0.05. The proportion of rejections estimates your TYPE I
#     ERROR rate; it should be close to 0.05.
# (b) Now simulate 2000 samples of n = 30 under a TRUE ALTERNATIVE
#     where the real mean is 0.005 (a small but genuine effect),
#     still testing against mu = 0. The proportion of rejections now
#     estimates your POWER to detect this effect size at n = 30.
# (c) Repeat (b) with n = 200 instead of n = 30. How does power
#     change?

# TODO: work this out live in class


# =============================================================================
# Exercise 5: Regression
# =============================================================================

# ---- Your Turn 5.1: Fitting a Simple Linear Model ----
#
# A hypothesis: a stock's daily return is related to overall market
# return that day (a simplified one-factor model).
#
# (a) Set a seed. Simulate 100 days of market_return ~
#     Normal(0.0005, 0.01).
# (b) Simulate stock_return = 0.0002 + 1.2 * market_return + noise,
#     where noise ~ Normal(0, 0.01) (so the "true" relationship has
#     intercept 0.0002 and slope 1.2 -- this is the stock's true
#     "beta").
# (c) Combine market_return and stock_return into a data frame.
# (d) Fit model <- lm(stock_return ~ market_return, data = ...), and
#     print summary(model). How close is the estimated slope to the
#     true value of 1.2 you built into the simulation?

# TODO: work this out live in class


# ---- Your Turn 5.2: Residuals and Model Assumptions ----
#
# Using the model from 5.1:
#   (a) Extract the fitted values and residuals.
#   (b) Plot residuals against fitted values using plot(). Add a
#       horizontal reference line at 0 with abline(h = 0, col = "red").
#   (c) Discuss: does the scatter of residuals look patternless (a
#       good sign), or is there visible structure?

# TODO: work this out live in class


# =============================================================================
# Exercise 6: Major Investigation -- Simulation as a Statistical Laboratory
# =============================================================================

# ---- Your Turn 6.1: Confidence Interval Coverage Under Non-Normal Returns ----
#
# Real financial returns often have heavier tails than a normal
# distribution (more extreme outliers than a Normal model predicts).
# We investigate whether this breaks our confidence interval coverage
# from Exercise 4.1.
#
# (a) Write a function one_ci_t() that is identical to one_ci() from
#     4.1, EXCEPT the sample is drawn using
#     true_mean_return + true_sd_return * rt(n, df = 3)
#     instead of rnorm(). (rt() with a small degrees-of-freedom
#     parameter produces a heavy-tailed, outlier-prone distribution;
#     multiplying by true_sd_return and adding true_mean_return gives
#     it roughly the same scale and center as our normal case, though
#     NOTE: for df = 3, rt() has a larger true variance than a
#     standard normal, which is itself worth discussing.)
# (b) Run the same coverage simulation as 4.1 (2000 repetitions, n =
#     30), but using one_ci_t() instead of one_ci().
# (c) Compare the empirical coverage to the normal case from 4.1 and
#     to the nominal target of 0.95. Discuss what this tells you
#     about the reliability of a "mean +/- 1.96 * se" interval when
#     the true data-generating process has heavy tails.

one_ci_t <- function() {
  # TODO: implement this function
}

# TODO: work this out live in class
