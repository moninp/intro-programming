# =============================================================================
# Homework 9: Data Wrangling, Validation, and Tidy Data
#
# Submit this file with your solutions filled in below each problem.
# Do not delete the problem statements.
#
# Instructions:
# - Write clear, readable R using the tidyverse (dplyr, tidyr).
# - Use the native pipe |> throughout, as we did in class.
# - Test your code with the provided data and additional test cases.
# - For questions that ask for an explanation, write a short explanation
#   in a comment immediately below the relevant code.
# - After every join or reshape, you MUST include a validation check
#   (row count, uniqueness, missing values, or a known total) as a
#   comment or as executed code. This is not optional -- it is graded.
# - Your code should run from top to bottom without requiring manual input.
#
# A note on this assignment: in class we worked with a single small
# infectious disease example. Tonight's assignment uses several
# different domains and several related tables per problem, so you get
# real practice deciding WHICH join to use, WHICH shape the data needs
# to be in, and HOW to validate that your transformation did what you
# intended -- not just reproducing a pattern you already saw in class.
# =============================================================================

library(tidyverse)

# =============================================================================
# Problem 1 -- Finance: Combining Daily Prices with Security Metadata
# =============================================================================

# Two "files" (represented here as inline tibbles) describe a small set
# of securities: one with daily closing prices, one with static
# metadata about each security (sector and exchange).

daily_prices <- tibble(
  ticker = rep(c("AXN", "BLT", "CGR", "DWN"), each = 4),
  date = rep(as.Date("2026-02-01") + 0:3, times = 4),
  close = c(
    101.2, 102.5, 100.8, 103.1,   # AXN
    54.0, 53.5, 55.1, 54.8,       # BLT
    220.5, 222.0, 219.8, 223.4,   # CGR
    12.1, 12.3, 12.0, 12.5        # DWN
  )
)

security_info <- tibble(
  ticker = c("AXN", "BLT", "CGR", "DWN"),
  sector = c("Tech", "Energy", "Tech", "Materials"),
  exchange = c("NASDAQ", "NYSE", "NASDAQ", "NYSE")
)

# 1a. Confirm that `ticker` is a valid, unique key in security_info
#     using anyDuplicated(). Store the result (0 means unique) in
#     answer_1a.

answer_1a <- NULL

# 1b. Join daily_prices to security_info using an appropriate join so
#     that every row of daily_prices is retained, with sector and
#     exchange attached. Store the result in prices_with_info.
#
# VALIDATE: nrow(prices_with_info) should equal nrow(daily_prices).
# Store the TRUE/FALSE result of this check in answer_1b_valid.

prices_with_info <- NULL
answer_1b_valid <- NULL

# 1c. Using prices_with_info, compute the average closing price by
#     sector using group_by() and summarise(). Store the result in
#     sector_avg.
#
# VALIDATE: the number of rows in sector_avg should equal the number
# of distinct sectors in security_info. Store this check in
# answer_1c_valid.

sector_avg <- NULL
answer_1c_valid <- NULL

# 1d. Using mutate(), add a column daily_return to prices_with_info
#     representing the day-over-day percentage return for each
#     ticker: (close - lag(close)) / lag(close) * 100, computed
#     SEPARATELY within each ticker (hint: group_by(ticker) before
#     mutate(), then consider ungroup() afterward). The first day for
#     each ticker should have an NA return, since there is no prior
#     day to compare to.

prices_with_info <- NULL  # reassign, adding the daily_return column

# 1e. VALIDATE: confirm that the number of NA values in daily_return
#     equals the number of distinct tickers (since each ticker's first
#     day should be NA, and no other NAs should be introduced). Store
#     the TRUE/FALSE result in answer_1e_valid.

answer_1e_valid <- NULL

# =============================================================================
# Problem 2 -- Climate: Reshaping Station Data
# =============================================================================

# A climate monitoring network reports monthly average temperatures
# (Fahrenheit) for three stations, recorded in wide format (one column
# per month) -- a common way data arrives from an external data
# provider, but not a tidy shape for analysis.

station_temps_wide <- tibble(
  station = c("STN_A", "STN_B", "STN_C"),
  jan = c(28.5, 35.2, 41.0),
  feb = c(31.0, 37.8, 43.5),
  mar = c(38.2, 44.0, 49.1)
)

# 2a. Identify, in a comment, which of the three tidy data rules
#     station_temps_wide violates, and why.

# 2b. Use pivot_longer() to reshape station_temps_wide into a tidy
#     long-format tibble with columns station, month, temp_f. Store
#     the result in station_temps_long.
#
# VALIDATE: nrow(station_temps_long) should equal
# nrow(station_temps_wide) * 3 (one row per station per month). Store
# this check in answer_2b_valid.

station_temps_long <- NULL
answer_2b_valid <- NULL

# 2c. Add a column temp_c to station_temps_long converting temp_f to
#     Celsius using mutate() (formula: (temp_f - 32) * 5/9).

station_temps_long <- NULL  # reassign, adding temp_c

# 2d. Use pivot_wider() to convert station_temps_long back into a wide
#     format, but this time with one column per STATION (not per
#     month) and one row per month, showing temp_c values.
#
# VALIDATE: the resulting table should have as many rows as there are
# distinct months (3) and as many columns as 1 (for month) plus the
# number of distinct stations (3), i.e., 4 columns total. Store a
# TRUE/FALSE check of the column count in answer_2d_valid.

station_temps_rewide <- NULL
answer_2d_valid <- NULL

# =============================================================================
# Problem 3 -- Infectious Disease: A Three-Table Join with a Deliberate Trap
# =============================================================================

# Three related tables: weekly case counts by clinic, a clinic-to-region
# lookup, and a table of lab test results PER CLINIC VISIT (note: a
# clinic may have multiple lab results per week, which will matter).

weekly_cases <- tibble(
  clinic_id = rep(c("C1", "C2", "C3"), each = 3),
  week = rep(1:3, times = 3),
  new_cases = c(5, 8, 6, 3, 4, 2, 10, 12, 9)
)

clinic_region <- tibble(
  clinic_id = c("C1", "C2", "C3"),
  region = c("North", "North", "South")
)

lab_results <- tibble(
  clinic_id = c("C1", "C1", "C1", "C2", "C3", "C3", "C3", "C3"),
  test_type = c("PCR", "PCR", "Rapid", "PCR", "PCR", "Rapid", "Rapid", "PCR"),
  positive_count = c(4, 1, 2, 3, 9, 1, 0, 8)
)

# 3a. Check whether clinic_id is a unique key in clinic_region AND in
#     lab_results, using anyDuplicated() on each. Store the two
#     results in answer_3a_region and answer_3a_lab. Based on these
#     results, is clinic_id a safe (many-to-one) or risky
#     (many-to-many) join key for each table, relative to
#     weekly_cases? Answer in a comment.

answer_3a_region <- NULL
answer_3a_lab <- NULL

# 3b. Join weekly_cases to clinic_region (a safe, many-to-one join).
#     Store the result in cases_with_region.
#
# VALIDATE: nrow(cases_with_region) should equal nrow(weekly_cases).
# Store this check in answer_3b_valid.

cases_with_region <- NULL
answer_3b_valid <- NULL

# 3c. Now join cases_with_region to lab_results by clinic_id. Store
#     the result in cases_with_labs.
#
# VALIDATE: compare nrow(cases_with_labs) to nrow(cases_with_region).
# In a comment, explain WHY the row count changed (or did not), using
# the many-to-many reasoning from class. Store the two row counts in
# answer_3c_before and answer_3c_after.

cases_with_labs <- NULL
answer_3c_before <- NULL
answer_3c_after <- NULL

# 3d. A colleague argues that cases_with_labs is now unsuitable for
#     computing total weekly cases per region, because summing
#     new_cases directly on this table would overcount. In a comment,
#     explain why the colleague is right, and then write CORRECT code
#     that computes total new_cases per region per week (hint: you may
#     want to go back to cases_with_region, not cases_with_labs, for
#     this particular calculation).

region_week_totals <- NULL

# VALIDATE: sum(region_week_totals$total_cases) should equal
# sum(weekly_cases$new_cases). Store this check in answer_3d_valid.

answer_3d_valid <- NULL

# =============================================================================
# Problem 4 -- Biology: Filtering, Deriving, and Grouped Summaries
# =============================================================================

# A field study recorded body measurements for captured specimens
# across two sites and two sampling visits.

specimens <- tibble(
  specimen_id = 1:12,
  site = rep(c("Site_A", "Site_B"), times = 6),
  visit = rep(c(1, 1, 1, 2, 2, 2), times = 2),
  species = rep(c("vole", "shrew", "vole", "shrew", "vole", "shrew"), times = 2),
  mass_g = c(22.1, 11.4, 23.5, 10.8, 21.9, 12.0,
             24.0, 10.5, 22.8, 11.9, 23.2, 10.2)
)

# 4a. Use filter() and select() to produce a tibble called
#     voles_only containing only rows where species is "vole", with
#     only the columns specimen_id, site, visit, mass_g.

voles_only <- NULL

# 4b. Using group_by() and summarise() on the full specimens tibble
#     (not voles_only), compute the mean mass_g and the number of
#     specimens (n()) for every combination of site, visit, and
#     species. Store the result in mass_summary.
#
# VALIDATE: the number of rows in mass_summary should equal the number
# of distinct (site, visit, species) combinations actually present in
# specimens. Use n_distinct() appropriately, or compare row counts
# directly, and store the TRUE/FALSE result in answer_4b_valid.
#
# Hint: you may compute this by checking that
# nrow(mass_summary) == nrow(distinct(specimens, site, visit, species))

mass_summary <- NULL
answer_4b_valid <- NULL

# 4c. Using mutate() on the full specimens tibble, add a column
#     mass_category that is "light" if mass_g < 15 and "heavy"
#     otherwise. (Hint: use ifelse() or dplyr's case_when().) Store
#     the updated tibble in specimens (reassign).

specimens <- NULL  # reassign, adding mass_category

# 4d. Using group_by() and summarise(), compute how many specimens
#     fall into each combination of species and mass_category. Store
#     the result in category_counts.
#
# VALIDATE: the sum of the n column (or count column, whatever you
# name it) in category_counts should equal nrow(specimens) (12).
# Store this check in answer_4d_valid.

category_counts <- NULL
answer_4d_valid <- NULL

# =============================================================================
# Problem 5 -- Synthesis: A Four-Table Economic Analysis Dataset
# =============================================================================

# This problem combines everything: reshaping, multiple joins (both
# safe and risky), derived variables, and a full validation sequence,
# using a slightly larger example than anything seen in class.
#
# Four related tables describe a small set of countries:
#   - gdp_wide: GDP (in billions USD) by country, wide by year
#   - population: current population by country
#   - region_lookup: which region each country belongs to
#   - trade_events: a log of trade agreements signed by country
#     (NOTE: some countries have signed multiple agreements, and this
#     table is deliberately NOT one-row-per-country)

gdp_wide <- tibble(
  country = c("Numeria", "Grapheria", "Vectoria", "Scalaria"),
  gdp_2023 = c(820, 410, 1500, 95),
  gdp_2024 = c(850, 430, 1540, 98),
  gdp_2025 = c(880, 445, 1600, 101)
)

population <- tibble(
  country = c("Numeria", "Grapheria", "Vectoria", "Scalaria"),
  population_millions = c(12.5, 8.2, 45.0, 3.1)
)

region_lookup <- tibble(
  country = c("Numeria", "Grapheria", "Vectoria", "Scalaria"),
  region = c("Northland", "Northland", "Southland", "Southland")
)

trade_events <- tibble(
  country = c("Numeria", "Numeria", "Grapheria", "Vectoria", "Vectoria", "Vectoria"),
  agreement = c("TA-1", "TA-2", "TA-1", "TA-3", "TA-4", "TA-5")
)

# 5a. Reshape gdp_wide into a long-format tibble called gdp_long with
#     columns country, year, gdp_billion. (Hint: use
#     starts_with("gdp_") inside pivot_longer(), and consider how to
#     clean up the "year" column afterward so it contains just the
#     numeric year rather than "gdp_2023", etc. -- you may use
#     str_remove() from stringr, part of the tidyverse, e.g.
#     str_remove(year, "gdp_"), or names_prefix inside pivot_longer().)
#
# VALIDATE: nrow(gdp_long) should equal nrow(gdp_wide) * 3. Store this
# check in answer_5a_valid.

gdp_long <- NULL
answer_5a_valid <- NULL

# 5b. Check whether "country" is a unique key in population AND in
#     region_lookup (both should be unique -- confirm this with
#     anyDuplicated()). Then join gdp_long to population and to
#     region_lookup (two safe, many-to-one joins). Store the result in
#     analysis_data.
#
# VALIDATE: nrow(analysis_data) should equal nrow(gdp_long). Store
# this check in answer_5b_valid.

analysis_data <- NULL
answer_5b_valid <- NULL

# 5c. Add a derived column gdp_per_capita to analysis_data: GDP in
#     billions divided by population in millions, times 1000 (to
#     express GDP per capita in thousands of USD per person, given the
#     units provided).

analysis_data <- NULL  # reassign, adding gdp_per_capita

# 5d. Now check whether "country" is a unique key in trade_events
#     (hint: it is not). If you were to inner_join() analysis_data to
#     trade_events by country, would this be a safe many-to-one join
#     or a risky many-to-many join FROM analysis_data's perspective?
#     Answer in a comment, then perform the join anyway (we want to
#     see the duplication happen), storing the result in
#     analysis_with_trade.
#
# VALIDATE: compare nrow(analysis_with_trade) to nrow(analysis_data).
# Store both counts in answer_5d_before and answer_5d_after, and
# explain in a comment whether this duplication is a problem for this
# particular dataset, or intentional/acceptable.

analysis_with_trade <- NULL
answer_5d_before <- NULL
answer_5d_after <- NULL

# 5e. Using analysis_data (NOT analysis_with_trade, to avoid the
#     duplication problem), compute the average gdp_per_capita by
#     region and year using group_by() and summarise(). Store the
#     result in region_year_summary.
#
# VALIDATE: write and execute at least ONE validation check of your
# own design for region_year_summary (row count, range check, or a
# known relationship), and explain in a comment what it confirms.

region_year_summary <- NULL

"
Expected time: 4-6 hours.

Main concepts practiced:

- dplyr core verbs: select(), filter(), mutate(), arrange(), group_by(),
  summarise()
- tidyr reshaping: pivot_longer(), pivot_wider()
- Choosing between inner_join()/left_join() based on desired behavior
  for unmatched rows
- Diagnosing many-to-one versus many-to-many join relationships using
  anyDuplicated()
- Validating every major transformation: row counts, uniqueness,
  missing values, known totals
- Writing fully reproducible, pipe-based (|>) R code
"