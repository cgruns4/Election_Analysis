#The data we need to retreive.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('C:/Users/chris/CU-Repositories/Election_Analysis/Resources/election_results.csv')
# file_to_load = os.path.join("Resources", "election_results.csv")


# Assign a variable to load a file from a path.
file_to_save = os.path.join('C:/Users/chris/CU-Repositories/Election_Analysis/analysis', 'C:/Users/chris/CU-Repositories/Election_Analysis/Resources/election_analysis.txt')
# file_to_save = os.path.join("analysis", "election_results.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     # Write some data to the file.\n is new line
#     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.      
    file_reader = csv.reader(election_data)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

    # # Print first item in each row in the CSV file.
    # for row in file_reader:
    #     print(row[0])

    # Print the header row.
    headers = next(file_reader)
    print(headers)
