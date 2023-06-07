#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:45:09 2023

@author: tarcisio
"""

#%% import the data csv 

import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

url = 'https://ws.mapserver.transports.gouv.qc.ca/swtq?service=wfs&version=2.0.0&request=getfeature&typename=ms:circulation_routier&outfile=DebitCirculation&outputformat=csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(url)

# Now you can work with the DataFrame as needed
print(df.head())  # Print the first few rows of the DataFrame

#%% download only the files xls in the section and donnees columns 

# Create new columns for extracted URLs
df['extracted_url_section'] = np.nan
df['extracted_url_donnees'] = np.nan

# Function to extract URLs from HTML using BeautifulSoup
def extract_urls(html):
    if isinstance(html, float):
        return []
    soup = BeautifulSoup(str(html), 'html.parser')
    urls = []
    for a in soup.find_all('a'):
        url = a['href']
        if url.endswith('.xlsx'):
            urls.append(url)
    return urls

# Iterate over each row and extract URLs based on conditions
for index, row in df.iterrows():
    section_urls = extract_urls(row['url_index_section'])
    donnees_urls = extract_urls(row['url_index_donnees'])
    if section_urls:
        df.at[index, 'extracted_url_section'] = ', '.join(section_urls)
    if donnees_urls:
        df.at[index, 'extracted_url_donnees'] = ', '.join(donnees_urls)

# Print the updated DataFrame
print(df)

#%% filter for rows that have values in the two new columns ()


# Create a filter based on non-empty values in the specified columns
filter = df['extracted_url_section'].notna() | df['extracted_url_donnees'].notna()

# Apply the filter to select the rows with non-empty values
filtered_df = df[filter]

# Print the filtered DataFrame
print(filtered_df)

#%% check duplicates
# Check for duplicate values in 'num_sectn_trafc' column
duplicates = df['num_sectn_trafc'].duplicated()

# Count the number of duplicates
num_duplicates = duplicates.sum()

# Print the count of duplicates
print("Number of duplicates in 'num_sectn_trafc' column:", num_duplicates)

#%% DOWNLOAD THE FILES

import requests
import os

# Create a folder for the downloaded files
# Specify the relative path to the folder
relative_folder_path = 'debit_circulation_quebec'

# Get the current working directory
current_dir = os.getcwd()

# Create the full path for the new folder
new_folder_path = os.path.join(current_dir, relative_folder_path)

# Create the new folder
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# Function to download a file from a URL
def download_file(url, folder):
  pathts.get(url)
    filename = url.split('/')[-1]
    file_path = os.path.join(download_folder, folder, filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)

# Function to extract URLs from HTML using BeautifulSoup
def extract_urls(html):
    if isinstance(html, float):
        return []
    soup = BeautifulSoup(str(html), 'html.parser')
    urls = []
    for a in soup.find_all('a'):
        url = a['href']
        if url.endswith('.xlsx'):
            urls.append(url)
    return urls

# Counter variables
total_folders_created = 0
current_folders_created = 0

# Iterate over each row and download files based on extracted URLs
for index, row in df.iterrows():
    num_sectn_trafc = str(row['num_sectn_trafc'])
    section_urls = extract_urls(row['url_index_section'])
    donnees_urls = extract_urls(row['url_index_donnees'])
    
    # Create a folder for the current 'num_sectn_trafc' if it doesn't already exist
    folder_path = os.path.join(download_folder, num_sectn_trafc)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        total_folders_created += 1
        current_folders_created += 1
    
    # Download files from 'extracted_url_section' URLs
    section_folder_path = os.path.join(folder_path, 'extracted_url_section')
    if section_urls:
        if not os.path.exists(section_folder_path):
            os.makedirs(section_folder_path)
            current_folders_created += 1
        for url in section_urls:
            download_file(url, os.path.join(num_sectn_trafc, 'extracted_url_section'))
    
    # Download files from 'extracted_url_donnees' URLs
    donnees_folder_path = os.path.join(folder_path, 'extracted_url_donnees')
    if donnees_urls:
        if not os.path.exists(donnees_folder_path):
            os.makedirs(donnees_folder_path)
            current_folders_created += 1
        for url in donnees_urls:
            download_file(url, os.path.join(num_sectn_trafc, 'extracted_url_donnees'))

    # Print the number of new folders created for the current 'num_sectn_trafc'
    print(f"For num_sectn_trafc '{num_sectn_trafc}', {current_folders_created} new folders were created.")
    current_folders_created = 0

# Print the total number of new folders created
print(f"Total number of new folders created: {total_folders_created}")

# Print a message after the download is complete
print("File download complete.")

#%% confirme if downloaded all files
import os

directory = '/path/debit_circulation_quebec/'
# Get a list of all items in the directory
items = os.listdir(directory)

# Count the number of directories
num_folders = sum(os.path.isdir(os.path.join(directory, item)) for item in items)

# Print the number of folders
print(f"The '{directory}' directory has {num_folders} folders.")



        
        
        
        
        
        
        
