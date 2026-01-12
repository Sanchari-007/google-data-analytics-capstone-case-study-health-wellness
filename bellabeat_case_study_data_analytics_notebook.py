
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""**STEPS ANALYSIS**"""

step_daily = pd.read_csv('/content/dailySteps_merged.csv')
step_hourly = pd.read_csv('/content/hourlySteps_merged.csv')

step_daily.head()

step_daily['ActivityDay'] = pd.to_datetime(step_daily['ActivityDay'])
step_daily['Day Of Week'] = step_daily['ActivityDay'].dt.day_name()
step_daily.head()

# Calculating the mean steps for each day of the week and reindex for proper order
daily_steps_avg = step_daily.groupby('Day Of Week')['StepTotal'].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

plt.figure(figsize=(8, 5))
sns.lineplot(x=daily_steps_avg.index, y=daily_steps_avg.values)
plt.title('Average Step Total per Day of Week')
plt.xlabel('Day Of Week')
plt.ylabel('Average Step Total')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print(step_daily.groupby('Day Of Week')['StepTotal'].mean())

step_hourly.head()

# Converting 'ActivityHour' to datetime objects, specifying the format to avoid warnings
step_hourly['ActivityHour'] = pd.to_datetime(step_hourly['ActivityHour'], format='%m/%d/%Y %I:%M:%S %p')
# Extracting the hour from 'ActivityHour'
step_hourly['Hour'] = step_hourly['ActivityHour'].dt.hour

# The mean steps per hour
hourly_steps_avg = step_hourly.groupby('Hour')['StepTotal'].mean()

plt.figure(figsize=(10, 5))
sns.lineplot(x=hourly_steps_avg.index, y=hourly_steps_avg.values)
plt.title('Average Step Total per Hour')
plt.xlabel('Hour Of Day')
plt.ylabel('Average Step Total')
plt.xticks(range(0, 24)) # Ensure all hours are shown on the x-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print(hourly_steps_avg)

"""**DISTANCE ANALYSIS**"""

heartrate = pd.read_csv('/content/heartrate_seconds_merged.csv')
calories = pd.read_csv('/content/dailyCalories_merged.csv')
intensities = pd.read_csv('/content/dailyIntensities_merged.csv')

intensities.head()

# Convert 'ActivityDay' to datetime objects if not already done
intensities['ActivityDay'] = pd.to_datetime(intensities['ActivityDay'])

# Calculate total distance for each day
intensities['TotalDistance'] = intensities['LightActiveDistance'] + \
                               intensities['ModeratelyActiveDistance'] + \
                               intensities['VeryActiveDistance']

# Calculate the average total distance per day
average_daily_distance = intensities.groupby('ActivityDay')['TotalDistance'].mean()

print("Average total distance covered per day:")
print(average_daily_distance.mean())

# Ensure 'ActivityDay' is datetime and extract 'Day Of Week'
intensities['ActivityDay'] = pd.to_datetime(intensities['ActivityDay'])
intensities['Day Of Week'] = intensities['ActivityDay'].dt.day_name()

# Calculate total distance for each day (moved from previous cell to ensure it's available)
intensities['TotalDistance'] = intensities['LightActiveDistance'] + \
                               intensities['ModeratelyActiveDistance'] + \
                               intensities['VeryActiveDistance']

# Calculate the mean total distance for each day of the week and reindex for proper order
daily_distance_avg = intensities.groupby('Day Of Week')['TotalDistance'].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# Create the plot
plt.figure(figsize=(10, 6))
sns.barplot(x=daily_distance_avg.index, y=daily_distance_avg.values)
plt.title('Average Total Distance per Day of Week')
plt.xlabel('Day Of Week')
plt.ylabel('Average Total Distance')
plt.show()

"""**CALORIES ANALYSIS**"""

calories.head()

# Convert 'ActivityDay' to datetime objects
calories['ActivityDay'] = pd.to_datetime(calories['ActivityDay'])

# Extract the day of the week
calories['Day Of Week'] = calories['ActivityDay'].dt.day_name()

# Calculate the mean calories burned per day of the week and reindex for proper order
daily_calories_avg = calories.groupby('Day Of Week')['Calories'].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

print("Average Calories Burned per Day of Week:")
print(daily_calories_avg)
print(daily_calories_avg.mean())

plt.figure(figsize=(10, 6))
sns.lineplot(x=daily_calories_avg.index, y=daily_calories_avg.values)
plt.title('Average Calories Burned per Day of Week')
plt.xlabel('Day Of Week')
plt.ylabel('Average Calories Burned')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

hourly_calories = pd.read_csv('/content/hourlyCalories_merged.csv')
hourly_calories.head()

# Convert 'ActivityHour' to datetime objects, specifying the format
hourly_calories['ActivityHour'] = pd.to_datetime(hourly_calories['ActivityHour'], format='%m/%d/%Y %I:%M:%S %p')

# Extract the hour from 'ActivityHour'
hourly_calories['Hour'] = hourly_calories['ActivityHour'].dt.hour

# Calculate the mean calories burned per hour
hourly_calories_avg = hourly_calories.groupby('Hour')['Calories'].mean()

# Create the line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly_calories_avg.index, y=hourly_calories_avg.values)
plt.title('Average Calories Burned per Hour')
plt.xlabel('Hour Of Day')
plt.ylabel('Average Calories Burned')
plt.xticks(range(0, 24)) # Ensure all hours are shown on the x-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

"""**PHYSICAL ACTIVITY**"""

hourly_intensities = pd.read_csv('/content/hourlyIntensities_merged.csv')
hourly_intensities['ActivityHour'] = pd.to_datetime(hourly_intensities['ActivityHour'], format='%m/%d/%Y %I:%M:%S %p')
hourly_intensities['Hour'] = hourly_intensities['ActivityHour'].dt.hour
hourly_intensities['TotalActiveMinutes'] = hourly_intensities['TotalIntensity']
hourly_active_minutes_avg = hourly_intensities.groupby('Hour')['TotalActiveMinutes'].mean()

print("Hourly Intensities (first 5 rows):")
print(hourly_intensities.head())
print("\nAverage Total Active Minutes per Hour:")
print(hourly_active_minutes_avg.head())

plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly_active_minutes_avg.index, y=hourly_active_minutes_avg.values)
plt.title('Average Total Active Minutes per Hour')
plt.xlabel('Hour Of Day')
plt.ylabel('Average Total Active Minutes')
plt.xticks(range(0, 24)) # Ensure all hours are shown on the x-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

daily_intensity_avg = intensities.groupby('Day Of Week')[['LightlyActiveMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'SedentaryMinutes']].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# Convert minutes to hours
daily_intensity_avg[['LightlyActiveMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'SedentaryMinutes']] = daily_intensity_avg[['LightlyActiveMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'SedentaryMinutes']] / 60

print("Average Daily Intensity Levels per Day of Week (in hours):")
print(daily_intensity_avg)

overall_avg_intensity = daily_intensity_avg[['LightlyActiveMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'SedentaryMinutes']].mean()
print("\nOverall Average Activity Levels (in hours):")
print(overall_avg_intensity)

plt.figure(figsize=(12, 7))
sns.lineplot(data=daily_intensity_avg)
plt.title('Average Daily Intensity Levels per Day of Week')
plt.xlabel('Day Of Week')
plt.ylabel('Average Hours')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Activity Level')
plt.show()

"""**HEART RATE ANALYSIS**"""

heartrate.head()

heartrate['Time'] = pd.to_datetime(heartrate['Time'], format='mixed', dayfirst=False)
heartrate['Date'] = heartrate['Time'].dt.date
daily_avg_heartrate = heartrate.groupby(['Id', 'Date'])['Value'].mean().reset_index()
daily_avg_heartrate['Day Of Week'] = pd.to_datetime(daily_avg_heartrate['Date']).dt.day_name()

print("First 5 rows of daily_avg_heartrate:")
print(daily_avg_heartrate.head())

daily_avg_heartrate_per_weekday = daily_avg_heartrate.groupby('Day Of Week')['Value'].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

plt.figure(figsize=(10, 6))
sns.lineplot(x=daily_avg_heartrate_per_weekday.index, y=daily_avg_heartrate_per_weekday.values)
plt.title('Average Heart Rate per Day of Week')
plt.xlabel('Day Of Week')
plt.ylabel('Average Heart Rate')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print("Average Heart Rate per Day of Week:")
print(daily_avg_heartrate_per_weekday)

"""**SLEEP ANALYSIS**"""

sleep_day = pd.read_csv('/content/sleepDay_merged.csv')
sleep_day.head()

sleep_day['SleepDay'] = pd.to_datetime(sleep_day['SleepDay'], format='%m/%d/%Y %I:%M:%S %p')
sleep_day['Day Of Week'] = sleep_day['SleepDay'].dt.day_name()

daily_sleep_avg = sleep_day.groupby('Day Of Week')[['TotalMinutesAsleep', 'TotalTimeInBed']].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# Convert minutes to hours
daily_sleep_avg[['TotalMinutesAsleep', 'TotalTimeInBed']] = daily_sleep_avg[['TotalMinutesAsleep', 'TotalTimeInBed']] / 60

# Rename columns for better legend labels
daily_sleep_avg = daily_sleep_avg.rename(columns={
    'TotalMinutesAsleep': 'Total Hours Asleep',
    'TotalTimeInBed': 'Total Time In Bed'
})

plt.figure(figsize=(10, 6))
sns.lineplot(data=daily_sleep_avg)
plt.title('Average Hours Asleep vs. Time In Bed per Day of Week')
plt.xlabel('Day Of Week')
plt.ylabel('Average Hours')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Metric')
plt.show()

print("Average Hours Asleep and Time In Bed per Day of Week:")
print(daily_sleep_avg)

"""**Weight Analysis**"""

weight = pd.read_csv('/content/weightLogInfo_merged.csv')
weight.head()

weight['Date'] = pd.to_datetime(weight['Date'], format='mixed', dayfirst=False)

# Create a mapping from original 'Id' to 'Customer X'
unique_ids = weight['Id'].unique()
id_to_customer = {id_val: f'Customer {i+1}' for i, id_val in enumerate(unique_ids)}
weight['Customer_Label'] = weight['Id'].map(id_to_customer)

plt.figure(figsize=(19, 7))
sns.lineplot(data=weight, x='Date', y='WeightKg', hue='Customer_Label', palette='tab10')
plt.title('Weight Trends of Each Customer Over Time')
plt.xlabel('Date')
plt.ylabel('Weight (Kg)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Customer', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

print("First 5 rows of weight data with converted Date and Customer Labels:")
print(weight.head())