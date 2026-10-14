"""
Homework 5: Real-World Data Analysis with NYC Yellow Taxi Data

Submit this file with your solutions filled in below each problem.
Do not delete the problem statements.

Instructions:
- Write clear, readable Python code following the patterns from class.
- Test your code with the provided data and additional test cases.
- For questions that ask for an explanation, write your reasoning in a
  comment or docstring immediately below the relevant code.
- When asked to make decisions about data cleaning, document your reasoning.
- Your code should run from top to bottom without requiring manual input.

Dataset:
You will work with two files:
1. yellow_tripdata_sample.parquet - 150,000 NYC taxi trips from January 2025
2. taxi_zones.csv - Lookup table mapping location IDs to borough/zone names

Data dictionary:
- VendorID: Taxi company (1 or 2)
- tpep_pickup_datetime: When passenger was picked up
- tpep_dropoff_datetime: When passenger was dropped off
- passenger_count: Number of passengers
- trip_distance: Trip distance in miles
- RatecodeID: Rate type (1=Standard, 2=JFK, 3=Newark, 4=Nassau/Westchester, 5=Negotiated, 6=Group)
- payment_type: How passenger paid (1=Credit card, 2=Cash, 3=No charge, 4=Dispute, 5=Unknown, 6=Voided)
- fare_amount: Base fare (time and distance)
- tip_amount: Tip amount (automatically populated for credit card tips)
- total_amount: Total charge to passenger

Note: Credit card tips are recorded, but cash tips are not captured in the data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Problem 1 — Data Loading and Initial Exploration
# =============================================================================

"""
You're starting a data analysis project for NYC's Taxi and Limousine Commission.
Before any analysis, you need to understand the structure and quality of your data.

Load the taxi trip data and perform initial exploration to understand what
you're working with.
"""

# 1a. Load the data from 'yellow_tripdata_sample.parquet'
#
# Store the DataFrame in a variable called 'taxi'
# Display the shape (rows, columns)

taxi = None

# 1b. Display the first 5 rows and examine the column names and data types
#
# What data types are the datetime columns? If they're not datetime type,
# you'll need to convert them in the next problem.

# Your code here

# 1c. Get basic summary statistics for numeric columns
#
# Use describe() to see count, mean, std, min, quartiles, max

# Your code here

# 1d. Check for missing values in each column
#
# Create a summary showing:
# - Column name
# - Number of missing values
# - Percentage of missing values
# Sort by number of missing values (descending)

missing_summary = None

# 1e. Identify which columns have missing data
#
# Based on your analysis, write a comment answering:
# - Which columns have missing values?
# - Which column has the most missing values?
# - Do you think these missing values are problematic? Why or why not?

# Your explanation here (3-4 sentences):
"""

"""

# =============================================================================
# Problem 2 — Data Cleaning and Quality Assessment
# =============================================================================

"""
Real-world data always has quality issues. Before analysis, you need to:
1. Identify implausible or invalid records
2. Decide how to handle them
3. Document your decisions

This is where your judgment as a data analyst matters.
"""

# 2a. Convert datetime columns if needed
#
# Ensure both datetime columns are proper datetime type
# If they're already datetime, this will confirm it

# Your code here

# 2b. Calculate trip duration in minutes
#
# Create a new column 'trip_minutes' 
# Formula: (dropoff_datetime - pickup_datetime) converted to minutes

taxi['trip_minutes'] = None

# 2c. Identify suspicious trips based on duration
#
# Find trips where:
# - Duration is negative (dropoff before pickup)
# - Duration is zero or very short (< 1 minute)
# - Duration is extremely long (> 3 hours = 180 minutes)
#
# For each category, count how many trips fall into it

negative_duration = None
very_short = None
very_long = None

print(f"Negative duration: {negative_duration}")
print(f"Very short (< 1 min): {very_short}")
print(f"Very long (> 180 min): {very_long}")

# 2d. Identify suspicious trips based on distance and fare
#
# Find trips where:
# - Distance is zero but fare is positive
# - Distance is negative
# - Fare amount is negative or zero

zero_distance_positive_fare = None
negative_distance = None
invalid_fare = None

# 2e. Calculate average speed and identify implausible speeds
#
# Create 'avg_speed_mph' column: distance / (duration_in_hours)
# Be careful with division by zero!
#
# Count trips with:
# - Speed > 100 mph (likely data error)
# - Speed > 60 mph (possible highway trip, but unusual in NYC)

taxi['avg_speed_mph'] = None

very_fast = None
fast = None

# 2f. Make cleaning decisions
#
# Based on your analysis above, create a cleaned dataset.
#
# Remove trips that are clearly data errors:
# - Negative or zero duration
# - Negative distance
# - Negative or zero fare_amount
# - Average speed > 100 mph
#
# Store the cleaned data in 'taxi_clean'
# Report how many rows were removed and what percentage

taxi_clean = None

rows_removed = None
pct_removed = None

print(f"Removed {rows_removed} rows ({pct_removed:.2f}%)")

# Write a comment explaining your reasoning:
"""
Why did you choose these criteria for removal?
Are there any borderline cases you decided to keep? Why?

Your explanation (3-4 sentences):

"""

# =============================================================================
# Problem 3 — Creating Analytical Variables
# =============================================================================

"""
Now that you have clean data, create variables that will help answer
questions about taxi usage patterns, tipping behavior, and operational
efficiency.
"""

# 3a. Extract time components from pickup datetime
#
# Create these new columns from tpep_pickup_datetime:
# - 'pickup_hour': hour of day (0-23)
# - 'pickup_day_name': day name (Monday, Tuesday, etc.)
# - 'pickup_date': just the date (no time)
# - 'is_weekend': True if Saturday or Sunday

taxi_clean['pickup_hour'] = None
taxi_clean['pickup_day_name'] = None
taxi_clean['pickup_date'] = None
taxi_clean['is_weekend'] = None

# 3b. Create time-of-day categories
#
# Create 'time_of_day' column with categories:
# - 'Early Morning' (midnight to 6am)
# - 'Morning Rush' (6am to 10am)  
# - 'Midday' (10am to 4pm)
# - 'Evening Rush' (4pm to 8pm)
# - 'Night' (8pm to midnight)
#
# Hint: Use pd.cut() with appropriate bins and labels

taxi_clean['time_of_day'] = None

# 3c. Create financial metrics
#
# Calculate:
# - 'tip_percentage': (tip_amount / fare_amount) * 100
# - 'fare_per_mile': fare_amount / trip_distance
# - 'revenue_per_minute': total_amount / trip_minutes
#
# Handle division by zero appropriately (set to NaN)

taxi_clean['tip_percentage'] = None
taxi_clean['fare_per_mile'] = None
taxi_clean['revenue_per_minute'] = None

# 3d. Create trip type indicators
#
# Based on RatecodeID, create 'trip_type' column:
# - 1 -> 'Standard'
# - 2 -> 'JFK Airport'
# - 3 -> 'Newark Airport'
# - 4 -> 'Nassau/Westchester'
# - 5 -> 'Negotiated'
# - 6 -> 'Group Ride'
#
# Hint: Use a dictionary with map() or replace()

rate_code_names = {
    1: 'Standard',
    2: 'JFK Airport',
    3: 'Newark Airport',
    4: 'Nassau/Westchester',
    5: 'Negotiated',
    6: 'Group Ride'
}

taxi_clean['trip_type'] = None

# 3e. Create payment type labels
#
# Create 'payment_method' column:
# - 1 -> 'Credit Card'
# - 2 -> 'Cash'
# - 3 -> 'No Charge'
# - 4 -> 'Dispute'
# - 5 -> 'Unknown'
# - 6 -> 'Voided'

payment_type_names = {
    1: 'Credit Card',
    2: 'Cash',
    3: 'No Charge',
    4: 'Dispute',
    5: 'Unknown',
    6: 'Voided'
}

taxi_clean['payment_method'] = None

# 3f. Create trip distance categories
#
# Create 'distance_category':
# - 'Very Short': 0-1 miles
# - 'Short': 1-3 miles
# - 'Medium': 3-7 miles
# - 'Long': 7-15 miles
# - 'Very Long': 15+ miles

taxi_clean['distance_category'] = None

# =============================================================================
# Problem 4 — Geographic Analysis with Merging
# =============================================================================

"""
The location IDs in the taxi data are meaningless without context.
You need to merge in the zone lookup table to understand WHERE trips
are happening.

The taxi_zones.csv file has these columns:
- LocationID: matches PULocationID and DOLocationID in taxi data
- Borough: Manhattan, Queens, Bronx, Brooklyn, Staten Island
- Zone: specific neighborhood/area name
"""

# 4a. Load the taxi zones lookup table
#
# Load from 'taxi_zones.csv'
# Display the first few rows to see the structure

zones = None

# 4b. Merge pickup location information
#
# Merge zones into taxi_clean to add pickup borough and zone
# Use left join (keep all taxi trips even if zone not found)
#
# Rename the merged columns to have 'pickup_' prefix:
# - 'pickup_borough'
# - 'pickup_zone'
#
# Hint: Merge twice - once for pickup, once for dropoff

# Your code here

# 4c. Merge dropoff location information
#
# Now merge zones again for dropoff locations
# Rename to have 'dropoff_' prefix:
# - 'dropoff_borough'  
# - 'dropoff_zone'

# Your code here

# 4d. Analyze trips by borough
#
# Create a summary showing for each pickup borough:
# - Number of trips
# - Average distance
# - Average duration
# - Average fare
# - Average tip percentage
#
# Sort by number of trips (descending)

borough_summary = None

# 4e. Identify most common pickup zones
#
# Find the top 10 pickup zones by number of trips
# For each zone, show:
# - Borough
# - Zone name
# - Number of trips

top_pickup_zones = None

# 4f. Analyze inter-borough vs intra-borough trips
#
# Create a column 'trip_pattern' that categorizes trips:
# - 'Within Manhattan': pickup and dropoff both in Manhattan
# - 'Within Other Borough': pickup and dropoff in same non-Manhattan borough
# - 'Manhattan to Other': pickup Manhattan, dropoff elsewhere
# - 'Other to Manhattan': pickup elsewhere, dropoff Manhattan
# - 'Between Boroughs': pickup and dropoff in different non-Manhattan boroughs
#
# Calculate the percentage of trips in each category

taxi_clean['trip_pattern'] = None

trip_pattern_summary = None

# =============================================================================
# Problem 5 — Synthesis: Tipping Behavior Analysis
# =============================================================================

"""
NYC taxi drivers rely heavily on tips. However, the data has an important
limitation: cash tips are not recorded, only credit card tips.

Use your pandas skills to answer: How do tipping patterns vary by payment
method, time, location, and trip characteristics?
"""

# 5a. Overall tipping rates by payment method
#
# For each payment method, calculate:
# - Number of trips
# - Percentage with positive tip (tip_amount > 0)
# - Average tip amount (for tips > 0)
# - Average tip percentage (for tips > 0)
#
# Based on the results, write a comment explaining why cash trips
# show zero tip amount

tipping_by_payment = None

# Your explanation:
"""

"""

# 5b. Tipping patterns by time of day
#
# For CREDIT CARD trips only, analyze how tip percentage varies by:
# - time_of_day categories
# - is_weekend
#
# Create a pivot table showing average tip percentage

# Filter to credit card only
cc_trips = None

tip_by_time_pivot = None

# 5c. Tipping patterns by pickup borough
#
# For credit card trips, compare average tip percentage across pickup boroughs
# Do riders from certain boroughs tip better?

tip_by_borough = None

# 5d. Relationship between trip characteristics and tips
#
# For credit card trips, create a grouped analysis showing:
# For each distance_category:
# - Average tip percentage
# - Average trip duration
# - Average fare amount
#
# Do people tip more on longer trips? Higher fares?

tip_by_distance = None

# 5e. Airport trips tipping analysis
#
# Compare tipping behavior for airport trips (JFK, Newark) vs standard trips
# For credit card trips only, compare:
# - Average tip percentage
# - Percentage of trips with tip > 20%
# - Percentage of trips with no tip

# Create an indicator for airport trips
taxi_clean['is_airport'] = None

airport_tip_comparison = None

# 5f. Visualize tipping patterns
#
# Create a bar plot showing average tip percentage by time_of_day
# Use only credit card trips
# Include a title and axis labels

# Your code here

# =============================================================================
# Problem 6 — Challenge: Rush Hour Economics (Optional)
# =============================================================================

"""
Taxi drivers often debate whether rush hour is more profitable than other times.
While there are more riders, trips may be shorter due to traffic, and time
spent per trip is higher.

Use your pandas skills to investigate: Is rush hour actually more profitable
for taxi drivers?
"""

# 6a. Define profitability metrics
#
# For this analysis, use these metrics:
# - Revenue per minute: total_amount / trip_minutes
# - Revenue per mile: total_amount / trip_distance
#
# Calculate the average of each metric for:
# - Morning Rush (6am-10am)
# - Evening Rush (4pm-8pm)
# - Midday (10am-4pm)
# - Other times
#
# Which time period has the highest revenue per minute?
# Which has the highest revenue per mile?

profitability_by_time = None

# 6b. Trip characteristics by time period
#
# Create a comprehensive comparison showing for each time_of_day:
# - Number of trips
# - Average distance
# - Average duration
# - Average speed
# - Average total amount
# - Revenue per minute
# - Revenue per mile
#
# Provide an interpretation: Is rush hour actually better for drivers?

comprehensive_time_analysis = None

# Your analysis (4-6 sentences):
"""

"""

# 6c. Manhattan vs Outer Boroughs profitability
#
# Compare the same metrics (revenue per minute, revenue per mile) between:
# - Trips that start in Manhattan
# - Trips that start in outer boroughs
#
# Do this separately for rush hour vs non-rush hour periods

# Create rush_hour indicator
taxi_clean['is_rush_hour'] = None

manhattan_outer_comparison = None

# 6d. Optimal trip characteristics
#
# Find the combination of characteristics that yields the highest revenue per minute:
# - Distance category
# - Time of day
# - Borough
#
# Use groupby with multiple variables and identify the top 10 combinations

optimal_trips = None