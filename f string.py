# voting_data = []
# voting_data.append ({"county":"Arapahoe","registered_voters": 422829})
# voting_data.append ({"country":"Denver","regist4ered_voters": 463353})
# voting_data.append ({"county":"Jefferson","registered_voters": 432438})

# #ORIGINAL LONGER PRINT CODE
# # my_votes = int(input("How many votes did you get in the election? "))
# # total_votes = int(input("What is the total votes in the election? "))
# # percentage_votes = (my_votes / total_votes) * 100
# # print("I received " + str(percentage_votes)+"% of the total votes.")

# #UPDATED CODE USING F STRING
# my_votes = int(input("How many votes did you get in the election?"))
# total_votes = int(input("What is the total votes in the election?"))
# print(f"I received {my_votes / total_votes *100}% of the total votes")

#--------------------------------

# counties_dict = {"Arapahoe": 422829,"Denver": 463353,"Jefferson": 432438}

# candidate_votes = int(input("How many votes did you get in the election?"))
# total_votes = int(input("What is the total votes in the election?"))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes.  "
#     f"The total number of votes in the election was {total_votes:,}.  "
#     #:.2f formats the return percentage to 2 decimal places
#     f"You received {candidate_votes / total_votes *100:.2f}% of the total votes")

# print(message_to_candidate)

#--------------------------------

counties_dict = {"Arapahoe": 422829,"Denver": 463353,"Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")


