#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:44:20 2023

@author: tarcisio
"""
# import functions
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# functions


def count_files(folder_path, subfolders, prefix, separator, suffix):
    # Initialize counters
    folder_count = 0
    file_count = 0

    # Iterate over subfolders
    for subfolder in subfolders:
        # Get the list of files in the subfolder
        files = os.listdir(os.path.join(folder_path, subfolder))

        # Check if the subfolder contains the specified files
        files_present = any(file.startswith(subfolder) and separator in file and suffix in file for file in files)

        # Increment counters
        if files_present:
            folder_count += 1
            file_count += sum(file.startswith(subfolder) and separator in file and suffix in file for file in files)

    return folder_count, file_count

def read_filtered_excel(filepath, sheet_name, filter_column, filter_values):
    try:
        xls = pd.ExcelFile(filepath)
        df = pd.read_excel(filepath, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error reading file: {filepath}")
        print(e)
        return None

    # Filter values in the specified column
    filtered_df = df[df[filter_column].isin(filter_values)]
    return filtered_df

# aggregated dataframe of all files filtered
def aggregate_filtered_data(folder_path, subfolders, filter_column, filter_values, sheet_name):
    # Initialize a list to store all filtered DataFrames
    aggregated_data_list = []

    # Iterate over subfolders
    for subfolder in subfolders:
        # Get the list of files in the subfolder
        files = os.listdir(os.path.join(folder_path, subfolder))

        # Iterate over files in the subfolder
        for file in files:
            # Check if it's an aggregated file
            if file.startswith(subfolder) and '_' in file:
                # Read the Excel file
                filepath = os.path.join(folder_path, subfolder, file)
                
                # Read the specified sheet with filter on the specified column
                filtered_df = read_filtered_excel(filepath, sheet_name, filter_column, filter_values)
                
                if filtered_df is not None:
                    # Append filtered data to the aggregated_data_list
                    aggregated_data_list.append(filtered_df)

    # Concatenate the list of DataFrames into a single DataFrame
    aggregated_data = pd.concat(aggregated_data_list, ignore_index=True)

    return aggregated_data

# read count_file
def read_count_file(folder_path, subfolders, include_entete=False):
    count_data_list = []

    for subfolder in subfolders:
        # Get the list of files in the subfolder
        files = os.listdir(os.path.join(folder_path, subfolder))

        for file in files:
            # Check if it's a count file
            if file.startswith(subfolder) and '-' in file and 'donnees' in file:
                filepath = os.path.join(folder_path, subfolder, file)
                try:
                    # Read the Excel file
                    xls = pd.ExcelFile(filepath)
                    sheet_names = xls.sheet_names

                    # Determine which sheet to read based on include_entete
                    sheet_index = 0 if include_entete else 1
                    count_df = pd.read_excel(xls, sheet_names[sheet_index], header=0)
                    count_data_list.append(count_df)
                except:
                    print(f"Error reading {file}")

    if count_data_list:
        count_data = pd.concat(count_data_list, ignore_index=True)
        return count_data
    else:
        return None
   
    # Dcustom_mean - section fact84
def custom_mean(series):
    return np.nanmean(series.values)

def count_filtered_data(folder_path, subfolders, filter_column, filter_values, sheet_name):
    # Initialize a list to store all filtered DataFrames
    count_data_list = []

    # Iterate over subfolders
    for subfolder in subfolders:
        # Get the list of files in the subfolder
        files = os.listdir(os.path.join(folder_path, subfolder))

        # Iterate over files in the subfolder
        for file in files:
            # Check if it's a count file
            if file.startswith(subfolder) and '-' in file and 'donnees' in file:
                # Read the Excel file
                filepath = os.path.join(folder_path, subfolder, file)
                
                # Read the specified sheet with filter on the specified column
                filtered_df = read_filtered_excel(filepath, sheet_name, filter_column, filter_values)
                
                if filtered_df is not None:
                    # Append filtered data to the count_data_list
                    count_data_list.append(filtered_df)

    # Concatenate the list of DataFrames into a single DataFrame
    count_data = pd.concat(count_data_list, ignore_index=True)

    return count_data

# plot fact84
import pandas as pd
import matplotlib.pyplot as plt

def plot_averages_by_month(dataframe_name):
    # Assuming you have the DataFrame with the given name available in the current scope
    data = globals()[dataframe_name]

    # Define the custom aggregation function
    def custom_mean(series):
        return series.mean()

    # Group by 'ANNEE' and 'MOIS' columns and apply custom aggregation function to all day columns
    averages_fact84 = data.groupby(['ANNEE', 'MOIS']).agg({
        'DIMANCHE': custom_mean,
        'LUNDI': custom_mean,
        'MARDI': custom_mean,
        'MERCREDI': custom_mean,
        'JEUDI': custom_mean,
        'VENDREDI': custom_mean,
        'SAMEDI': custom_mean,
        'MOYEN': custom_mean
    })

    # Extract 'ANNEE' and 'MOIS' from the index and add them as columns
    averages_fact84.reset_index(inplace=True)

    # Define the desired order of months
    month_order = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

    # Convert the 'MOIS' column to the ordered categorical data type
    averages_fact84['MOIS'] = pd.Categorical(averages_fact84['MOIS'], categories=month_order, ordered=True)

    # Sort the DataFrame by the 'MOIS' column
    averages_fact84 = averages_fact84.sort_values('MOIS')

    # Pivot the data to have days as columns and months as index
    pivot_table = averages_fact84.pivot(index='MOIS', columns='ANNEE')

    # Reorder the pivot table based on the month order
    pivot_table = pivot_table.reindex(month_order)

    # Get the unique years in the data
    years = pivot_table.columns.get_level_values('ANNEE').unique()

    # Calculate the number of subplots
    num_plots = len(pivot_table.columns.get_level_values(0).unique())
    num_rows = (num_plots - 1) // 3 + 1

    # Create the grid of subplots
    fig, axes = plt.subplots(num_rows, 3, figsize=(15, 5 * num_rows), sharex=True)

    # Flatten the axes array
    axes = axes.flatten()

    # Define line styles for highlighting
    highlight_styles = ['--', '--', '--']

    # Plot a single curve per year for each day
    for i, day in enumerate(pivot_table.columns.get_level_values(0).unique()):
        ax = axes[i]
        y_min = pivot_table[(day, years)].min().min()  # Automatic y_min
        y_max = pivot_table[(day, years)].max().max()  # Automatic y_max
        ax.set_ylim(y_min, y_max)
        for j, year in enumerate(years):
            line_style = highlight_styles[j % len(highlight_styles)] if year in [2020, 2021, 2022] else '-'
            line_alpha = 1.0 if year in [2020, 2021, 2022] else 0.5
            line_width = 2 if year in [2020, 2021, 2022] else 1
            ax.plot(pivot_table.index, pivot_table[(day, year)], label=f'{year}', linestyle=line_style, alpha=line_alpha)
        ax.set_ylabel('Mean')
        ax.set_title(f'Average Values by Year - {day}')
        ax.set_xticks(range(len(pivot_table.index)))  # Set x-ticks
        ax.set_xticklabels(pivot_table.index, rotation=45, ha='right')  # Set x-tick labels

        if i == 2 or i == 5:
            ax.legend(title='Year')
        else:
            ax.legend().set_visible(False)  # Hide legend for other subplots

        # Show x-axis labels for all subplots
        ax.set_xlabel('Months')

    # Hide unused subplots
    for j in range(num_plots, num_rows * 3):
        fig.delaxes(axes[j])

    # Adjust the spacing between subplots
    fig.tight_layout()

    # Display the plots
    plt.show()
