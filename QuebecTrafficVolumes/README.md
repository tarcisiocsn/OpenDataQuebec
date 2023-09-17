## Data on OneDrive

* [folders_data_quebec](https://polymtlca0-my.sharepoint.com/:f:/g/personal/tarcisio_costa-de-souza-neto_polymtl_ca/Es42_1xrGx1EuIE6FHHBSBMBB05q0hX9axpftgjZcqmMaQ?e=L6TdUc) extracted by the python code. 

#### Python code for automatic download: 
File [telecharger_fichiers.py]. This code is used to download files from specific URLs and store them locally in corresponding folders. Here is a summary of the main steps:

1. Creating a download folder.
2. Define a function to download a file from a given URL.
3. Definition of a function to extract URLs from HTML code using BeautifulSoup.
4. Traverse each line of a dataframe called 'df'.
5. Extract section URLs and data URLs for each line.
6. Creation of a folder corresponding to the value of 'num_sectn_trafc' if it does not already exist.
7. Downloading files from section URLs to a specific subfolder.
8. Downloading files from data URLs to another specific subfolder.
9. Display of the number of new folders created for each 'num_sectn_trafc'.
10. Display of the total number of new folders created.
11. Display of a message indicating that the download of files is complete.

This summarizes the main steps of this code.

### Access the notebook file to get automatic analysis
