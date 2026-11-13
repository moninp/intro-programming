# =============================================================================
# Homework 10: Simulation as a Statistical Laboratory
#
# Submit this file with your solutions filled in below each problem.
# Do not delete the problem statements.
#
# Instructions:
# - Write clear, readable R.
# - ALWAYS call set.seed() before any simulation, and do not change the
#   seed values specified in each problem -- this lets your results be
#   checked against expected answers.
# - For questions that ask for an explanation or interpretation, write
#   a short explanation in a comment immediately below the relevant code.
# - When asked to predict a result, write your prediction in a comment
#   BEFORE running the code that reveals the answer.
# - Several problems ask you to produce a plot (histogram or scatter).
#   Use base R plotting (hist(), plot()) -- we have not yet covered
#   ggplot2, which is next lecture.
# - Your code should run from top to bottom without requiring manual input.
#
# A note on this assignment: every problem below follows the same basic
# pattern introduced in class: specify a data-generating process,
# simulate from it many times, compute a statistic each time, and look
# at the resulting distribution of that statistic. Once this pattern
# feels automatic, the specific statistical question almost doesn't
# matter -- the simulation workflow is the same every time.
# =============================================================================

# =============================================================================
# Problem 1 -- Epidemiology: Monte Carlo Estimation of an Outbreak Probability
# =============================================================================

# Suppose the number of new daily cases at a small clinic follows a
# Poisson distribution with rate (lambda) 6 cases per day. Public
# health officials want to know the probability that a given day sees
# MORE than 10 new cases (an "alert" day).

lambda_cases <- 6

# 1a. Compute the EXACT probability of an alert day (more than 10
#     cases) using ppois(). Recall that ppois(q, lambda) gives
#     P(X <= q), so you will need to adjust appropriately to get
#     P(X > 10). Store the result in answer_1a_exact.

answer_1a_exact <- NULL

# 1b. Set the seed to 10, then simulate 50,000 draws from
#     rpois(n, lambda = lambda_cases). Compute the proportion of
#     simulated days that are "alert" days (more than 10 cases). Store
#     this Monte Carlo estimate in answer_1b_mc.

set.seed(10)
answer_1b_mc <- NULL

# 1c. Compute the Monte Carlo standard error of your estimate from 1b,
#     using the formula sqrt(p_hat * (1 - p_hat) / n). Store it in
#     answer_1c_se.

answer_1c_se <- NULL

# 1d. Repeat the Monte Carlo estimate from 1b, but using only 500
#     simulated draws instead of 50,000 (use set.seed(10) again
#     immediately before this smaller simulation, so both estimates
#     start from a comparable, reproducible state). Store this
#     smaller-sample estimate in answer_1d_mc_small, and its standard
#     error (using the same formula as 1c) in answer_1d_se_small.
#
# In a comment, compare answer_1c_se to answer_1d_se_small. By roughly
# what factor should the standard error have changed, given the
# change in simulation size? Does the ratio you observe roughly match
# this prediction?

set.seed(10)
answer_1d_mc_small <- NULL
answer_1d_se_small <- NULL

# =============================================================================
# Problem 2 -- Finance: Sampling Distribution of a Portfolio Return
# =============================================================================

# A portfolio's daily return is modeled as Normal(mean = 0.0006,
# sd = 0.015). An analyst wants to understand how the AVERAGE return
# over a holding period behaves across many possible realizations of
# the market.

portfolio_mean <- 0.0006
portfolio_sd <- 0.015

# 2a. Set the seed to 20. Simulate 4000 independent "20-day holding
#     periods": for each, draw 20 daily returns and compute their
#     mean. Store the 4000 resulting period-average returns in a
#     vector called period_means_20.

set.seed(20)
period_means_20 <- NULL

# 2b. Produce a histogram of period_means_20 using hist(), with a
#     descriptive main title.

# 2c. Compute the mean and standard deviation of period_means_20.
#     Compare the standard deviation to the theoretical standard error
#     portfolio_sd / sqrt(20). Store the simulated SD in
#     answer_2c_sd_simulated and the theoretical SE in
#     answer_2c_se_theoretical.

answer_2c_sd_simulated <- NULL
answer_2c_se_theoretical <- NULL

# 2d. Repeat 2a, but for 60-day holding periods instead of 20-day
#     holding periods. Use set.seed(21) immediately before this
#     simulation. Store the result in period_means_60.
#
# VALIDATE / COMPARE: compute the ratio
# sd(period_means_60) / sd(period_means_20), and compare it to the
# theoretical ratio sqrt(20 / 60). Store both ratios in
# answer_2d_ratio_observed and answer_2d_ratio_theoretical.

set.seed(21)
period_means_60 <- NULL
answer_2d_ratio_observed <- NULL
answer_2d_ratio_theoretical <- NULL

# =============================================================================
# Problem 3 -- Physics: Confidence Interval Coverage for a Measured Constant
# =============================================================================

# A physics student measures a constant whose true value is 9.8 (think
# of this as a simplified stand-in for a measured quantity like a local
# gravitational acceleration), with each individual measurement subject
# to Normal(0, 0.3) measurement error. The student wants to know how
# well a standard 90% confidence interval performs.

true_value <- 9.8
measurement_sd <- 0.3

# 3a. Write a function called one_ci_90 that takes a single argument n
#     (the number of measurements per experiment) and:
#       - draws n measurements from Normal(true_value, measurement_sd)
#       - computes the sample mean and standard error
#       - returns a named vector c(lower = ..., upper = ...) for a 90%
#         confidence interval (mean +/- 1.645 * se)

one_ci_90 <- function(n) {
  # TODO: implement this function
}

# 3b. Set the seed to 30. Using sapply() (or a for loop), call
#     one_ci_90(n = 10) 3000 times, storing the resulting intervals.
#     Compute the empirical coverage (the proportion of intervals that
#     contain true_value). Store the coverage in answer_3b_coverage.

set.seed(30)
answer_3b_coverage <- NULL

# 3c. Repeat 3b exactly, but with n = 50 instead of n = 10. Use
#     set.seed(31) immediately before this simulation. Store the
#     coverage in answer_3c_coverage.
#
# In a comment, discuss: does coverage change meaningfully between
# n = 10 and n = 50? Should it, in principle, given that the
# confidence interval formula is designed to target 90% coverage
# regardless of n (assuming the normality assumption holds)?

set.seed(31)
answer_3c_coverage <- NULL

# 3d. Now investigate what happens if the measurement error is NOT
#     actually normal. Write a second function, one_ci_90_skewed, that
#     is identical to one_ci_90 EXCEPT the n measurements are generated
#     as:
#
#       true_value + (rexp(n, rate = 1) - 1) * measurement_sd
#
#     (This creates a skewed error distribution with approximately the
#     same mean and comparable scale to the normal case, since rexp(n,
#     rate=1) has mean 1 and sd 1, so subtracting 1 recenters it at 0.)
#
# Set the seed to 32. Run the same coverage simulation as 3b/3c (3000
# repetitions, n = 10) using one_ci_90_skewed(). Store the coverage in
# answer_3d_coverage.
#
# In a comment, compare answer_3d_coverage to answer_3b_coverage.
# Does skewness appear to hurt coverage at this small sample size?

one_ci_90_skewed <- function(n) {
  # TODO: implement this function
}

set.seed(32)
answer_3d_coverage <- NULL

# =============================================================================
# Problem 4 -- Weather: Power to Detect a Warming Trend
# =============================================================================

# A climate scientist wants to know how likely a simple statistical
# test is to detect a small warming trend, given noisy annual
# temperature data. Suppose baseline annual average temperature has
# mean 55 (degrees F) and sd 1.5, and we want to know the POWER to
# detect a true increase of 0.5 degrees, using a one-sample t-test
# against a null of 55.

baseline_mean <- 55
baseline_sd <- 1.5
true_increase <- 0.5

# 4a. Set the seed to 40. Simulate the TYPE I ERROR RATE of a t-test
#     with n = 15 years of data: repeat 3000 times, each time drawing
#     n = 15 values from Normal(baseline_mean, baseline_sd) (i.e.,
#     NO true increase), running t.test(x, mu = baseline_mean), and
#     recording whether the p-value is below 0.05. Store the proportion
#     of rejections (the Type I error rate) in answer_4a_type1.

set.seed(40)
answer_4a_type1 <- NULL

# 4b. Set the seed to 41. Simulate the POWER of the same test with
#     n = 15, but now drawing from Normal(baseline_mean + true_increase,
#     baseline_sd) (i.e., the true increase IS real). Store the
#     resulting power in answer_4b_power_n15.

set.seed(41)
answer_4b_power_n15 <- NULL

# 4c. Repeat 4b with n = 50 instead of n = 15. Use set.seed(42)
#     immediately before this simulation. Store the result in
#     answer_4c_power_n50.

set.seed(42)
answer_4c_power_n50 <- NULL

# 4d. Repeat 4b with n = 15, but with a LARGER true increase of 1.0
#     degree instead of 0.5. Use set.seed(43) immediately before this
#     simulation. Store the result in answer_4d_power_larger_effect.
#
# In a comment, rank answer_4b_power_n15, answer_4c_power_n50, and
# answer_4d_power_larger_effect from lowest to highest, and explain
# in one or two sentences WHY each change (more years of data, versus
# a bigger true effect) increased power.

set.seed(43)
answer_4d_power_larger_effect <- NULL

# =============================================================================
# Problem 5 -- Synthesis: Designing Your Own Simulation Study
# =============================================================================

# This problem asks you to design and run a small simulation study
# largely on your own, following the general pattern from Problems 1-4
# and from class.
#
# Setting: a biologist studies the body mass (in grams) of a small
# mammal species. Based on prior studies, the biologist believes body
# mass follows a Normal distribution with mean 18 and sd 2.5.

mammal_mean <- 18
mammal_sd <- 2.5

# 5a. Set the seed to 50. Investigate the BIAS of the sample standard
#     deviation as an estimator: simulate 3000 samples of size n = 5,
#     compute sd() for each sample, and compute the average of those
#     3000 sample standard deviations. Store this average in
#     answer_5a_mean_sd_n5. Compare it to mammal_sd -- is the sample sd
#     estimator noticeably biased at this very small sample size? Write
#     your conclusion in a comment.

set.seed(50)
answer_5a_mean_sd_n5 <- NULL

# 5b. Repeat 5a with n = 50 instead of n = 5. Use set.seed(51)
#     immediately before this simulation. Store the result in
#     answer_5b_mean_sd_n50. Does the bias (if any) you observed in 5a
#     appear to shrink at the larger sample size? Comment on your
#     finding.

set.seed(51)
answer_5b_mean_sd_n50 <- NULL

# 5c. Design and run ONE additional simulation investigation of your
#     own choosing, related to this mammal body mass example. Your
#     investigation must:
#       - specify a clear question (write it as a comment)
#       - use a seed of your choosing (document it)
#       - run at least 2000 repetitions
#       - produce a numeric result AND a plot (hist() or plot())
#       - include a 2-4 sentence interpretation, in a comment, of what
#         your simulation shows
#
# Some options to consider (you do not have to use one of these):
#   - investigate confidence interval coverage if sample size is very
#     small (e.g., n = 4)
#   - investigate how an outlier-contaminated sample (e.g., occasionally
#     drawing from a different, higher-mean distribution by mistake)
#     affects the sample mean's bias or variance
#   - investigate the power of a test to detect a small shift in mean
#     body mass between two populations

# TODO: design and implement your own simulation investigation here

