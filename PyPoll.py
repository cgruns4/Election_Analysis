#The data we need to retreive.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#Add dependencies
import os
import csv

# Assign a variable for the file to load and the path.
# file_to_load = os.path.join('C:/Users/chris/CU-Repositories/Election_Analysis/Resources/election_results.csv')
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to load a file from a path.
# file_to_save = os.path.join('C:/Users/chris/CU-Repositories/Election_Analysis/analysis', 'C:/Users/chris/CU-Repositories/Election_Analysis/Resources/election_analysis.txt')
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize vote counter
total_votes = 0    

# Declare new empty list (before with open statements)
candidate_options = []
# Declare new empty dictionary (before with open statements)
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     # Write some data to the file.\n is new line
#     txt_file.write("Counties in the Election\nArapahoe\nDenver\nJefferson")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.      
    file_reader = csv.reader(election_data)

    # # Print first item in each row in the CSV file.
    # for row in file_reader:
    #     print(row[0])

    #Read the header row - dont count in analysis.
    headers = next(file_reader)

    # Print each row in the CSV file. Alternative: total_votes = total_votes + 1
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]    

        # If the candidate does not match any existing candidate...(adding if to only list candidate once)
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name) 
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.   
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.

# To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    # Print the total votes.
    # print(total_votes)
    # Print the candidate list.
    # print(candidate_votes)

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to terminal

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
