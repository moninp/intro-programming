"""
Lecture 5: Data Analysis with Pandas - Class Exercises
MATH 5200 - Computing Using R & Python

This file contains starter code for in-class exercises using Chicago Divvy bike-share data.
Complete the sections marked "Your code here" during class.

Instructions:
- Work through each section as directed by the instructor
- Test your code frequently
- Ask questions when you get stuck
- Save your work regularly

Dataset: Chicago Divvy bike-share system, May 2024
Central Question: How do members and casual riders use the bike-share system differently?
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Setup: Create Sample Divvy Data
# =============================================================================

# For demonstration purposes, we'll create a small sample dataset
# In practice, you would load the full May 2024 dataset (609K rows)

sample_data = {
    'ride_id': ['ABC123', 'DEF456', 'GHI789', 'JKL012', 'MNO345'],
    'rideable_type': ['classic_bike', 'electric_bike', 'electric_bike', 'classic_bike', 'electric_bike'],
    'started_at': ['2024-05-01 08:00:00', '2024-05-01 09:15:00', '2024-05-01 12:30:00', 
                   '2024-05-01 17:45:00', '2024-05-01 19:00:00'],
    'ended_at': ['2024-05-01 08:25:00', '2024-05-01 09:45:00', '2024-05-01 13:00:00',
                 '2024-05-01 18:05:00', '2024-05-01 19:35:00'],
    'start_station_name': ['Clark St & Elm St', 'Broadway & Barry Ave', None, 
                           'Michigan Ave & Oak St', None],
    'start_station_id': ['TA1307000039', 'TA1307000060', None, 'TA1307000011', None],
    'end_station_name': ['Wells St & Elm St', None, 'Sedgwick St & North Ave',
                         'State St & Pearson St', 'Sheridan Rd & Lawrence Ave'],
    'end_station_id': ['TA1307000039', None, 'TA1307000038', 'TA1307000061', 'TA1307000041'],
    'start_lat': [41.903, 41.938, 41.912, 41.901, 41.910],
    'start_lng': [-87.631, -87.647, -87.638, -87.624, -87.655],
    'end_lat': [41.903, 41.945, 41.912, 41.898, 41.969],
    'end_lng': [-87.634, -87.652, -87.641, -87.628, -87.655],
    'member_casual': ['member', 'casual', 'member', 'casual', 'member']
}

df = pd.DataFrame(sample_data)
print(f"Sample dataset created: {len(df)} rows, {len(df.columns)} columns")


# =============================================================================
# Exercise 1.2: Load and Inspect the Data
# =============================================================================

# Display the first few rows
# Your code here


# Check the shape (rows, columns)
# Your code here


# Display column names and data types
# Your code here


# Get basic information
# Your code here



# =============================================================================
# Exercise 1.3: Explore the Data Structure
# =============================================================================

# How many unique ride_ids are there?
# Your code here


# What percentage of rides are by members vs casual riders?
# Your code here


# How many unique start stations are there?
# Your code here


# Which columns have missing values?
# Your code here


# What's the pattern of missingness? 
# (Hint: look at missing station names by bike type)
# Your code here



# =============================================================================
# Exercise 2.1: DateTime Conversions and Extraction
# =============================================================================

# Convert started_at and ended_at to datetime if not already done
# Your code here


# Extract the month from started_at
# Your code here


# Extract the day name (Monday, Tuesday, etc.)
# Your code here


# Calculate trip duration in minutes
# Hint: (ended_at - started_at).dt.total_seconds() / 60
# Your code here


# Find the average trip duration
# Your code here



# =============================================================================
# Exercise 2.2: Identify Data Quality Issues
# =============================================================================

# Find trips with duration less than 1 minute
# Your code here


# Find trips with duration greater than 8 hours (480 minutes)
# Your code here


# Check if any start coordinates are (0, 0) - likely invalid
# Your code here


# Verify all latitudes are in reasonable range for Chicago
# (approximately 41.6 to 42.1)
# Your code here


# Check for missing end coordinates
# Your code here



# =============================================================================
# Exercise 3.1: Create Additional Variables
# =============================================================================

# Create a 'month_name' column
# Your code here


# Create an 'is_rush_hour' column (True for 7-9am or 4-6pm)
# Your code here


# Create a 'has_station_info' column indicating if both 
# start and end station names are present
# Your code here


# Create a 'bike_category' column that groups bike types
# into 'Classic' vs 'Electric' (combining electric_bike and electric_scooter)
# Your code here



# =============================================================================
# Exercise 3.2: Investigate Missing Data Patterns
# =============================================================================

# What percentage of trips have BOTH start and end station info missing?
# Your code here


# For trips with missing station names, do we still have coordinates?
# Your code here


# Compare average trip duration for trips WITH station info
# vs trips WITHOUT station info
# Your code here


# Create a strategy: For trips with missing station names,
# should we drop them, fill with "Unknown", or keep as-is?
# Write your reasoning in a comment
# Your code here



# =============================================================================
# Exercise 4.1: Perform Grouped Analyses
# =============================================================================

# Calculate average duration by time_of_day
# Your code here


# Find the most popular start station for members vs casual riders
# Your code here


# Compare weekend vs weekday average durations
# Your code here


# Find which hour of the day has the most trips
# Your code here


# Calculate the percentage of trips that are on classic bikes
# for members vs casual riders
# Your code here



# =============================================================================
# Exercise 4.2: Create Pivot Tables
# =============================================================================

# Create a pivot table showing COUNT of trips by:
# - rows: day_of_week (0=Monday, 6=Sunday)
# - columns: member_casual
# Your code here


# Create a pivot table showing MEAN duration by:
# - rows: time_of_day
# - columns: rideable_type
# Your code here


# Create a pivot table showing trip counts by:
# - rows: rideable_type
# - columns: is_weekend
# Your code here



# =============================================================================
# Exercise 5.1: Create Visualizations
# =============================================================================

# Create a bar plot showing trip count by hour of day
# Your code here


# Create a bar plot comparing bike type preferences
# between members and casual riders
# Your code here


# Create a line plot showing average duration by day of week
# Your code here



# =============================================================================
# End of Class Exercises
# =============================================================================

print("\nClass exercises complete!")
print("Save this file and commit to your Git repository.")
print("\nNext steps:")
print("1. Try loading the full May 2024 Divvy dataset (609K rows)")
print("2. Explore additional questions about bike-share usage patterns")
print("3. Create more sophisticated visualizations")
