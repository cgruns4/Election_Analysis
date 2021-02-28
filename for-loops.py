# numbers = [0, 1, 2, 3, 4]

# for num in range(5):
#     print(num)

# for i in range(len(numbers)):
#     print(numbers[i])

# counties_tuple = ("Arapahoe","Denver","Jefferson")

# for i in range(len(counties_tuple)):
#     print(counties_tuple[i])


#Dictionary = ["key":value,"key":value,"key": value]
counties_dict = {"Arapahoe": 422829,"Denver": 463353,"Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict.keys():
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

#--------------------

#for key, value in dictionary_name.items()
    #retrieve(key, value)
# for key, value in counties_dict.items():
#     print(key, value)

# #same as previous subsituting county & voters for key & value
# for county, voters in counties_dict.items():
#     print(county, voters)


# for county, voters in counties_dict.items():
#     print(county, "county has", voters, "registered voters")

#print using f string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")
    

