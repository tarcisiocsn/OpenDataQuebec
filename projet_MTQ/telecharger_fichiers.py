#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:45:09 2023

@author: tarcisio
"""

#%% import the data csv 

import pandas as pd
from bs4 import BeautifulSoup

url = 'https://ws.mapserver.transports.gouv.qc.ca/swtq?service=wfs&version=2.0.0&request=getfeature&typename=ms:circulation_routier&outfile=DebitCirculation&outputformat=csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(url)

# Now you can work with the DataFrame as needed
print(df.head())  # Print the first few rows of the DataFrame

#%% download only the files xls in the last column 
# Function to extract .xlsx URLs from the <a> tags
def extract_xlsx_urls(row):
    url_section = row['url_index_section']
    if isinstance(url_section, float):  # Check if it's a float
        return []  # Return an empty list if it's a float
    soup = BeautifulSoup(url_section, 'html.parser')
    xlsx_urls = []
    for a in soup.find_all('a'):
        href = a.get('href')
        if href.endswith('.xlsx'):
            xlsx_urls.append(href)
    return xlsx_urls

# Apply the function to each row of the DataFrame 
df['xlsx_urls'] = df.apply(extract_xlsx_urls, axis=1)

#filter rows where "O" is present in index_sectn OR index_donnees OR contains .xlsx URLs

filtered_df = df[(df['index_sectn'].str.contains('O')) |
                 (df['index_donnees'].str.contains('O')) |
                 (df['xlsx_urls'].apply(lambda x: any(url.endswith('.xlsx') for url in x) if len(x) > 0 else False))]


# Print the filtered DataFrame
print(filtered_df)


#%% Non data
filtered_non_df = df[(df['index_sectn'].str.contains('N')) &
                 (df['index_donnees'].str.contains('N')) &
                 (df['xlsx_urls'].apply(lambda x: not any(url.endswith('.xlsx') for url in x) if len(x) > 0 else True))]

#%% Non data but agregees

filtered_non_df = df[(df['index_sectn'].str.contains('N')) |
                     (df['index_sectn'].str.contains('N')) |
                 (df['index_donnees'].str.contains('N')) |
                 (df['xlsx_urls'].apply(lambda x: not any(url.endswith('.xlsx') for url in x) if len(x) > 0 else True))]