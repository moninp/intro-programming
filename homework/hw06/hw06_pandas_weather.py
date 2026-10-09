"""
PANDAS HOMEWORK: A MONTH OF WEATHER ACROSS U.S. CITIES
=====================================================

Estimated time: 3-5 hours
Libraries: pandas, NumPy, matplotlib
Tested with: pandas 3.0.6

Purpose
-------
Practice the core ideas from the pandas "10 minutes to pandas" guide:
Series and DataFrames, selection, missing values, new columns, merging,
groupby, lambda functions, dates, plotting, and CSV import/export.

How to use this file
--------------------
1. Read the short explanations before each section.
2. Fill in every TODO. Do not simply copy outputs from the prompt.
3. Run the script regularly. Inspect small results with print().
4. Answer the interpretation questions in comments where indicated.
5. Keep your code readable; short explanatory comments are welcome.

The data are fictional but designed to look like plausible weather observations.
The setup section creates two CSV files in the current working directory:
    weather_raw.csv
    city_info.csv
Do not edit the setup section. The rest of the assignment reads those files.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# SETUP: CREATE SMALL, REPRODUCIBLE FICTIONAL DATA
# ---------------------------------------------------------------------------
# This is provided so that everyone starts with exactly the same data.
# The setup also demonstrates constructing DataFrames from dictionaries.
# You do not need to understand every line yet; revisit it after the assignment.

dates = pd.date_range("2026-09-01", periods=14, freq="D")
cities = ["Washington, DC", "Chicago", "Denver", "Seattle", "Atlanta", "Phoenix"]

# Each row below corresponds to one city; each value corresponds to a date.
highs_by_city = {
    "Washington, DC": [84, 86, 83, 79, 77, 82, 85, 87, 81, 78, 80, 84, 82, 79],
    "Chicago":        [76, 78, 75, 73, 71, 74, 77, 79, 76, 72, 70, 74, 75, 73],
    "Denver":         [81, 83, 80, 78, 76, 79, 82, 84, 81, 77, 75, 78, 80, 79],
    "Seattle":        [69, 71, 68, 67, 66, 70, 72, 73, 71, 68, 67, 69, 70, 68],
    "Atlanta":        [88, 90, 87, 85, 83, 86, 89, 91, 88, 84, 82, 85, 87, 86],
    "Phoenix":        [101, 103, 100, 98, 96, 99, 102, 104, 101, 97, 95, 98, 100, 99],
}
lows_by_city = {
    "Washington, DC": [68, 70, 67, 63, 61, 65, 68, 70, 66, 62, 64, 67, 66, 63],
    "Chicago":        [59, 61, 58, 56, 54, 57, 60, 62, 59, 55, 53, 56, 58, 56],
    "Denver":         [52, 54, 51, 49, 47, 50, 53, 55, 52, 48, 46, 49, 51, 50],
    "Seattle":        [54, 55, 53, 52, 51, 54, 56, 57, 55, 52, 51, 53, 54, 52],
    "Atlanta":        [70, 72, 69, 67, 65, 68, 71, 73, 70, 66, 64, 67, 69, 68],
    "Phoenix":        [78, 80, 77, 75, 73, 76, 79, 81, 78, 74, 72, 75, 77, 76],
}
rain_by_city = {
    "Washington, DC": [0.00, 0.00, 0.18, 0.42, 0.05, 0.00, 0.00, 0.00, 0.10, 0.35, 0.00, 0.00, 0.02, 0.00],
    "Chicago":        [0.12, np.nan, 0.00, 0.00, 0.30, 0.04, 0.00, 0.00, 0.00, 0.08, 0.00, 0.22, 0.00, 0.00],
    "Denver":         [0.00, 0.00, 0.00, 0.03, 0.16, 0.00, 0.00, 0.00, 0.00, np.nan, 0.00, 0.00, 0.05, 0.00],
    "Seattle":        [0.20, 0.15, 0.32, 0.05, 0.00, 0.00, 0.00, 0.00, 0.08, 0.12, 0.25, 0.00, np.nan, 0.10],
    "Atlanta":        [0.00, 0.00, 0.00, 0.14, 0.40, 0.05, 0.00, 0.00, 0.00, 0.26, 0.00, 0.00, 0.10, 0.00],
    "Phoenix":        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
}

weather_rows = []
for city in cities:
    for i, date in enumerate(dates):
        weather_rows.append(
            {
                "date": date.strftime("%Y-%m-%d"),
                "city": city,
                "high_temp": highs_by_city[city][i],
                "low_temp": lows_by_city[city][i],
                "precipitation": rain_by_city[city][i],
            }
        )

weather_seed = pd.DataFrame(weather_rows)
# A few temperature readings are missing too, to make missing-data work realistic.
weather_seed.loc[(weather_seed["city"] == "Chicago") & (weather_seed["date"] == "2026-09-06"), "high_temp"] = np.nan
weather_seed.loc[(weather_seed["city"] == "Seattle") & (weather_seed["date"] == "2026-09-10"), "low_temp"] = np.nan
weather_seed.to_csv("weather_raw.csv", index=False)

city_info_seed = pd.DataFrame(
    {
        "city": cities,
        "region": ["South", "Midwest", "Mountain West", "Pacific Northwest", "South", "Southwest"],
        "elevation_ft": [25, 594, 5280, 175, 1050, 1086],
        "timezone": ["Eastern", "Central", "Mountain", "Pacific", "Eastern", "Mountain"],
    }
)
city_info_seed.to_csv("city_info.csv", index=False)


# ---------------------------------------------------------------------------
# PART 1. LOAD, INSPECT, AND CREATE PANDAS OBJECTS (about 25 minutes)
# ---------------------------------------------------------------------------
# A Series is a one-dimensional labeled object. A DataFrame is a two-dimensional
# labeled table. They resemble NumPy arrays, but carry index/column labels.

# TODO 1A: Read weather_raw.csv into a DataFrame named weather.
# Hint: pd.read_csv("weather_raw.csv")
weather = None  # replace this line

# TODO 1B: Read city_info.csv into a DataFrame named city_info.
city_info = None  # replace this line

# TODO 1C: Print the first 8 rows of weather, its shape, and its column names.
# Then use .info() and .isna().sum() to inspect data types and missing values.
# Remember: .info() prints information and returns None.
print("\n--- PART 1: INSPECT THE DATA ---")
# YOUR CODE HERE


# TODO 1D: Create a Series named sample_temps from this dictionary:
# {"Monday": 72, "Tuesday": 75, "Wednesday": 70}
# Print the Series and its type.
# YOUR CODE HERE


# TODO 1E: Create a small DataFrame named weekend_plan from a dictionary of lists:
# day = ["Saturday", "Sunday"]
# activity = ["hiking", "reading"]
# hours_outside = [3, 0]
# Print it. What are its row index and column labels?
# YOUR CODE HERE

# Interpretation 1: In one or two sentences, explain one important difference
# between a Series and a DataFrame. Put your answer in a comment here.


# ---------------------------------------------------------------------------
# PART 2. SELECTING DATA: [] AND .loc (about 35 minutes)
# ---------------------------------------------------------------------------
# In pandas, [] is an indexing operator. The object inside [] determines what
# is selected. For example, weather["city"] selects one column as a Series,
# while weather[["city", "high_temp"]] selects multiple columns as a DataFrame.
#
# .loc selects by LABEL: weather.loc[row_label, column_label].
# .iloc selects by INTEGER POSITION. You may use it as a comparison, but focus
# on [] and .loc in this assignment.

print("\n--- PART 2: SELECTING DATA ---")

# TODO 2A: Select the high_temp column as a Series; print its type.
# YOUR CODE HERE

# TODO 2B: Select date, city, and high_temp as a DataFrame.
# Print its type and the first five rows.
# YOUR CODE HERE

# TODO 2C: Use a Boolean mask to show all Washington, DC observations with
# high_temp >= 84. Print only date, high_temp, and precipitation.
# YOUR CODE HERE

# TODO 2D: Use .loc with a row label and column labels to select a small subset.
# First, reset or inspect the index so you know what the row labels are.
# For example, select rows 0 through 4 and columns city and high_temp.
# Note: .loc label slices include the endpoint when the labels are present.
# YOUR CODE HERE

# TODO 2E: Use .iloc to select the first 3 rows and first 2 columns.
# In a comment, explain how this differs from .loc.
# YOUR CODE HERE

# TODO 2F: Select just the precipitation column, then select it as a one-column
# DataFrame. Use print(type(...)) to compare the two objects.
# YOUR CODE HERE

# Interpretation 2: Explain what each pair of brackets does in
# weather[["city", "high_temp"]]. Which brackets perform selection, and which
# brackets construct the list of column names?


# ---------------------------------------------------------------------------
# PART 3. MISSING VALUES AND NEW COLUMNS (about 35 minutes)
# ---------------------------------------------------------------------------
# Missing numeric data are commonly represented by NaN. Pandas has methods such
# as isna(), dropna(), fillna(), and notna(). Choose a missing-data treatment
# based on the meaning of the variable and the question being asked.

print("\n--- PART 3: MISSING VALUES AND NEW COLUMNS ---")

# TODO 3A: Count missing values in each column. Then print just the rows where
# precipitation is missing.
# YOUR CODE HERE

# TODO 3B: Create a DataFrame called complete_temps by dropping rows where
# either high_temp or low_temp is missing. Do not drop rows just because
# precipitation is missing. How many rows remain?
# YOUR CODE HERE

# TODO 3C: Make a copy of weather called weather_work. Fill missing precipitation
# values with 0, but do NOT fill missing temperatures with 0. Explain in a
# comment why blindly replacing every missing value with zero would be risky.
# YOUR CODE HERE

# TODO 3D: Add a column temp_range equal to high_temp - low_temp.
# Add a column rainy equal to True when precipitation is at least 0.10 inches,
# and False otherwise. Use a vectorized expression rather than a loop.
# YOUR CODE HERE

# TODO 3E: Add a column hot_day that is True when high_temp >= 90.
# How many hot-day observations are there? Hint: a Boolean Series can be summed.
# YOUR CODE HERE

# TODO 3F: Create a column temp_category using a lambda function and .apply():
# "cool" if high_temp < 70, "mild" if high_temp < 85, and "hot" otherwise.
# Missing high temperatures should remain missing. You may use .apply() on
# the high_temp Series, or define a small helper function instead.
# YOUR CODE HERE

# Interpretation 3: Why might a missing precipitation value be treated
# differently from a missing temperature? State the assumption you make if
# you replace missing precipitation with 0.


# ---------------------------------------------------------------------------
# PART 4. MERGING TWO DATAFRAMES (about 30 minutes)
# ---------------------------------------------------------------------------
# We have one row per city-day in weather_work and one row per city in city_info.
# A merge matches rows whose key columns have the same value. Here, "city" is
# the shared key. This is similar to looking up each city's region and elevation
# and attaching those details to every weather observation for that city.
#
# A left merge keeps every row from the left-hand table and adds matching
# columns from the right-hand table. The "validate" argument checks the expected
# relationship: many weather rows can match one city_info row ("many_to_one").

print("\n--- PART 4: MERGING ---")

# TODO 4A: Merge weather_work (left) with city_info (right) on "city" using
# how="left" and validate="many_to_one". Name the result weather_full.
# YOUR CODE HERE

# TODO 4B: Print the first 6 rows of weather_full, its shape, and the columns.
# Check that the number of rows has not increased.
# YOUR CODE HERE

# TODO 4C: Use value_counts() or nunique() to check that every city in weather
# has city information. Print the unique regions in weather_full.
# YOUR CODE HERE

# Interpretation 4: In plain English, describe what "left merge on city" does.
# What might go wrong if city_info had two rows for Chicago?


# ---------------------------------------------------------------------------
# PART 5. GROUPBY: SUMMARIZE SUBSETS OF THE DATA (about 45 minutes)
# ---------------------------------------------------------------------------
# groupby("city") divides the rows into groups with the same city. Selecting
# ["high_temp"] then chooses the high_temp Series within each group. Calling
# .mean() calculates a mean separately for each group.
#
# Thus: weather_full.groupby("city")["high_temp"].mean()
# is like calculating high_temp.mean(), but separately for each city.

print("\n--- PART 5: GROUPBY ---")

# TODO 5A: Calculate mean high temperature by city, sorted from warmest to coolest.
# YOUR CODE HERE

# TODO 5B: Calculate mean high_temp and mean precipitation by region. You may use
# groupby("region")[["high_temp", "precipitation"]].mean().
# YOUR CODE HERE

# TODO 5C: For each city, calculate the number of observations, mean high_temp,
# and maximum precipitation. Use .groupby() and .agg().
# Hint: .agg(["count", "mean", "max"]) on selected columns is one approach.
# YOUR CODE HERE

# TODO 5D: Count rainy days by city. Use groupby plus a Boolean column or a
# conditional expression. Be explicit about whether a missing precipitation
# value counts as a rainy day under your chosen treatment.
# YOUR CODE HERE

# TODO 5E: Use groupby("region")["city"].nunique() to count distinct cities
# represented in each region.
# YOUR CODE HERE

# TODO 5F: In one expression, calculate the mean temperature range by region.
# YOUR CODE HERE

# Interpretation 5: Explain the pieces in
# weather_full.groupby("city")["high_temp"].mean()
# In particular, what does groupby do, what does ["high_temp"] select, and
# what does mean() do?


# ---------------------------------------------------------------------------
# PART 6. DATES AND A SHORT TIME-SERIES EXERCISE (about 35 minutes)
# ---------------------------------------------------------------------------
# The CSV stores dates as text by default. Convert the date column to pandas'
# datetime dtype before doing date-based operations. Dates are not just strings:
# a datetime dtype makes chronological filtering and plotting easier.

print("\n--- PART 6: DATES ---")

# TODO 6A: Convert weather_full["date"] to datetime using pd.to_datetime().
# Check the dtype.
# YOUR CODE HERE

# TODO 6B: Filter to observations from September 5 through September 10, 2026,
# inclusive. Save as date_window and print date, city, and high_temp.
# Hint: compare the datetime column with pd.Timestamp("2026-09-05") and
# pd.Timestamp("2026-09-10").
# YOUR CODE HERE

# TODO 6C: Select Washington, DC observations and sort them by date.
# Print date and high_temp. Why is sorting useful for a time-series table?
# YOUR CODE HERE

# Interpretation 6: Why is it useful to convert dates from strings to a
# datetime dtype, even if the strings look like dates?


# ---------------------------------------------------------------------------
# PART 7. PLOTS (about 25 minutes)
# ---------------------------------------------------------------------------
# A plot can reveal patterns that are hard to see in a table. Label axes and
# give each plot a title. These plots need not be fancy.

print("\n--- PART 7: PLOTS ---")

# TODO 7A: Make a bar chart of average high temperature by city.
# Include axis labels and a title; rotate city labels if needed.
# YOUR CODE HERE

# TODO 7B: Make a line plot of high_temp over time for Washington, DC.
# Sort by date first. Include axis labels, a title, and markers.
# YOUR CODE HERE

# TODO 7C: Optional challenge: plot high temperatures over time for three cities
# on the same axes, with a legend. Do not worry about this if you are short on time.
# YOUR CODE HERE

# Interpretation 7: Which plot is better for comparing typical temperatures
# across cities? Which is better for seeing how one city's temperature changes?


# ---------------------------------------------------------------------------
# PART 8. EXPORT, RELOAD, AND WRAP-UP (about 15 minutes)
# ---------------------------------------------------------------------------
# to_csv() exports a DataFrame. read_csv() imports it again. index=False avoids
# writing the DataFrame's row labels as an extra column unless you explicitly
# want to preserve them.

print("\n--- PART 8: EXPORT AND RELOAD ---")

# TODO 8A: Export weather_full to "weather_enriched.csv" without writing the
# DataFrame index.
# YOUR CODE HERE

# TODO 8B: Read "weather_enriched.csv" back into a DataFrame named reloaded.
# Parse the date column during import using parse_dates=["date"].
# YOUR CODE HERE

# TODO 8C: Print reloaded.head(), reloaded.shape, and reloaded.dtypes.
# Confirm that the shape matches weather_full and that date is a datetime dtype.
# YOUR CODE HERE

# FINAL CHECK: Write 3–5 sentences in comments:
#   1. What is one pandas operation you expect to use in another course?
#   2. What is one distinction you now understand better (e.g., Series vs
#      DataFrame, .loc vs .iloc, or merge vs groupby)?
#   3. What is one question about pandas you still have?

print("\nAssignment script reached the end. Review your outputs and written answers.")
