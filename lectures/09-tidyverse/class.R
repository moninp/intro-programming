
---

# class.R

```r
# =============================================================================
# Lecture 9: Data Wrangling, Validation, and Tidy Data
# Live Coding Script (Stub)
#
# This file is worked through live in class. Each section below
# corresponds to an Exercise/Your Turn in class.qmd with the same number.
# Run this file top to bottom as the lecture progresses; do not skip
# sections, since later exercises depend on objects defined earlier.
# =============================================================================

library(tidyverse)

# =============================================================================
# Shared Data for Today's Lecture: A Small Infectious Disease Dataset
# =============================================================================
#
# These objects are used throughout all five exercises. Run this block
# first and do not modify it, so results stay comparable across
# exercises.

daily_cases <- tibble(
  region = rep(c("North", "South", "East", "West"), each = 5),
  date = rep(as.Date("2026-01-01") + 0:4, times = 4),
  new_cases = c(
    12, 15, 9, 20, 18,    # North
    8, 10, 7, 11, 9,      # South
    30, 28, 35, 40, 38,   # East
    5, 6, 4, 7, 6         # West
  )
)

population <- tibble(
  region = c("North", "South", "East", "West"),
  population = c(1200000, 900000, 2500000, 400000)
)

geography <- tibble(
  region = c("North", "South", "East", "West"),
  country = c("Numeria", "Numeria", "Grapheria", "Grapheria")
)

population_wide <- tibble(
  region = c("North", "South", "East", "West"),
  pop_2024 = c(1150000, 880000, 2420000, 390000),
  pop_2025 = c(1180000, 890000, 2460000, 395000),
  pop_2026 = c(1200000, 900000, 2500000, 400000)
)

# A deliberately "messy" table for Exercise 4.2: multiple variant
# surveillance records per region, with no unique key, used to
# demonstrate many-to-many join duplication.
variant_surveillance <- tibble(
  region = c("North", "North", "South", "South", "East", "West"),
  variant = c("Alpha", "Beta", "Alpha", "Gamma", "Beta", "Alpha"),
  sample_count = c(5, 3, 4, 2, 6, 1)
)

# =============================================================================
# Exercise 1: Tidy Data and Tibbles
# =============================================================================

# ---- Your Turn 1.1: tibble() versus data.frame() ----
#
# Create the same small table two ways: as a data.frame() and as a
# tibble(). Print both. Then check is.data.frame() on the tibble.

# TODO: work this out live in class
# PAUSE: ask students what differences they notice in the printed output

# ---- Your Turn 1.2: What Makes Data "Tidy"? ----
#
# You are given a "wide" table with one column per day:
#
#   wide_cases <- tibble(
#     region = c("North", "South"),
#     cases_day1 = c(12, 8),
#     cases_day2 = c(15, 10)
#   )
#
# (a) Identify which of the three tidy data rules this table
#     violates, and why.
# (b) Use pivot_longer() to reshape it into a long, tidy table with
#     columns region, day, cases.

wide_cases <- tibble(
  region = c("North", "South"),
  cases_day1 = c(12, 8),
  cases_day2 = c(15, 10)
)

# TODO: work this out live in class

# =============================================================================
# Exercise 2: dplyr Verbs
# =============================================================================

# ---- Your Turn 2.1: select() and filter() ----
#
# Using daily_cases:
#   (a) select() only the region, date, and new_cases columns
#       (daily_cases already has only these columns, so demonstrate
#       select() by reordering them: date, region, new_cases).
#   (b) filter() to keep only rows where new_cases > 15.

# TODO: work this out live in class
# PAUSE: ask students to predict how many rows survive the filter
#        before running it

# ---- Your Turn 2.2: mutate() and arrange() ----
#
# Using daily_cases joined to population (you may do a quick
# inner_join() here as a preview of Exercise 4):
#   (a) Create a new column cases_per_10k = new_cases / population * 10000.
#   (b) Arrange the result in descending order of cases_per_10k.
#   (c) Which region-date combination has the highest rate?

# TODO: work this out live in class

# ---- Your Turn 2.3: group_by() and summarise() ----
#
# Using daily_cases:
#   (a) Group by region and compute total_cases = sum(new_cases) and
#       n_days = n() (the number of rows per group).
#   (b) VALIDATE: confirm that the sum of total_cases across all
#       regions equals sum(daily_cases$new_cases).

# TODO: work this out live in class
# PAUSE: this validation step is not optional -- make sure it runs

# =============================================================================
# Exercise 3: Reshaping with tidyr
# =============================================================================

# ---- Your Turn 3.1: pivot_longer() ----
#
# Using population_wide:
#   (a) Pivot the pop_2024, pop_2025, pop_2026 columns into a long
#       format with columns region, year, population. (Hint: use
#       cols = starts_with("pop_").)
#   (b) VALIDATE: the resulting table should have
#       nrow(population_wide) * 3 rows. Check this with nrow().

# TODO: work this out live in class

# ---- Your Turn 3.2: pivot_wider() ----
#
# Using daily_cases:
#   (a) Group by region and date, summarise total new_cases (there is
#       only one row per region-date already, but practice the
#       pattern anyway).
#   (b) pivot_wider() so each date becomes its own column, with
#       region as rows.
#   (c) VALIDATE: the number of columns should equal 1 (for region)
#       plus the number of distinct dates.

# TODO: work this out live in class
# PAUSE: ask students to predict ncol() of the result before checking

# =============================================================================
# Exercise 4: Joins
# =============================================================================

# ---- Your Turn 4.1: Keys and inner_join() ----
#
# (a) Confirm that "region" is a valid key: check that it is unique
#     in population using anyDuplicated(population$region) == 0.
# (b) inner_join() daily_cases to population by "region".
# (c) VALIDATE: the joined table should have the same number of rows
#     as daily_cases, since every region in daily_cases has a match
#     in population (a many-to-one relationship).

# TODO: work this out live in class

# ---- Your Turn 4.2: Many-to-Many Joins and Unexpected Duplication ----
#
# (a) Check whether "region" is unique in variant_surveillance using
#     anyDuplicated(). What do you find?
# (b) inner_join() daily_cases to variant_surveillance by "region".
# (c) VALIDATE: compare nrow() of the result to nrow(daily_cases).
#     What happened, and why?
# (d) Discuss: is this duplication ever desirable? When would it
#     signal a mistake?

# TODO: work this out live in class
# PAUSE: have students predict nrow() of the joined result BEFORE
#        running it -- most will underestimate it

# =============================================================================
# Exercise 5: Major Investigation -- Building a Validated Analysis Dataset
# =============================================================================

# ---- Your Turn 5.1: Combine Cases, Population, and Geography ----
#
# (a) Build analysis_data by inner_join()-ing daily_cases to
#     population by "region", then inner_join()-ing the result to
#     geography by "region".
# (b) Add a derived column cases_per_10k.
# (c) Group by country and date, and summarise total new_cases and
#     total population-weighted cases_per_10k (sum of new_cases
#     divided by sum of population, times 10000) for each country-date
#     combination.
#
# VALIDATE at each step:
#   - nrow(analysis_data) should equal nrow(daily_cases), since every
#     region has exactly one population row and one geography row
#     (both many-to-one relationships).
#   - sum of new_cases in analysis_data should equal
#     sum(daily_cases$new_cases).
#   - no NA values should appear in population or country columns
#     after the joins.
#   - cases_per_10k values should all be positive and of a
#     plausible magnitude (not in the millions, for example).

# TODO: work this out live in class
# PAUSE: walk through each validation check explicitly and discuss
#        what a failure would have meant