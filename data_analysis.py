# Author: @ Phillip Muza
# Date: 03/10/2024
# Title: Data analysis for MRI brain images

# Import necessary libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_dataframe(dataframe_path):
    #load dataframe
    df = pd.read_csv('registration/volumes.csv')

    # Extract the image ID from the path
    path_parts = os.path.abspath(dataframe_path).split(os.sep)
    filename = path_parts[-1]

    # Extract the animal ID from the filename
    animal_id = filename.split('_')[3]

    #Extract the week of imaging acquisition
    week_of_imaging = filename.split('_')[2]
    week_of_imaging = int(week_of_imaging.split('W')[1])

    # Create a new column with the subject ID
    df['animal_id'] = animal_id
    df['imaging_week'] = week_of_imaging

    return df

parent_dir = /path/to/directory
list_of_dataframes = []

for root, dirs, files in os.walk(parent_dir):
    full_path = os.path.abspath(root)
    if 'output_img.tif' in files:
        df = read_dataframe(full_path)
        list_of_dataframes.append(df)
    else:
        print(f"No 'output_img.tif' in: {full_path}")

# Combine all dataframes into a single dataframe
combined_df = pd.concat(list_of_dataframes, ignore_index=True)
print(f'Combined dataframe shape: {combined_df.shape}')

# Get the number of unique animals in the combined dataframe
num_unique_animals = len(combined_df['animal_id'].unique())
print(f'Number of unique animals: {num_unique_animals}')

# Get the number of unique weeks of imaging for each animal
unique_weeks_per_animal = combined_df.groupby('animal_id')['imaging_week'].nunique()
print(f'Unique weeks of imaging per animal: {unique_weeks_per_animal}')

# Read the structure file
structures_file = pd.read_csv('structures.csv')

# Merge the combined dataframe with the structures dataframe
merged_df = structures_file.merge(combined_df, left_on='name', right_on='structure_name', how='left')

# Save the combined dataframe to a CSV file
merged_df.to_csv('merged_dataframe.csv', index=False)

set_merged = set(merged_df['name'])
set_combined = set(combined_df['structure_name'])
only_in_merged = set_merged - set_combined
only_in_merged.to_csv('only_in_merged.csv', index=False)

print(f'Structures only in merged: {only_in_merged}')
print(f'Structures only in combined: {only_in_combined}')



