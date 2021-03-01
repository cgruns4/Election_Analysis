# Election_Analysis

## Project Overview
A Colorado Board of Elections has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.2, Visual Studio Code 1.53.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election
- The breakdown of votes per county are:
    - Jefferson: 10.5% (total county votes were: 38,855)
    - Denver: 82.8% (total county votes were: 306,055)
    - Arapahoe: 6.7% (total county votes were: 24,801)
    - Denver recorded the largest number of votes

![ElectionText](https://user-images.githubusercontent.com/71041680/109440903-ba0e7e00-7a01-11eb-8b8f-3afa96a3ee29.png)


- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana Degette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

- The winner of the election was:
    - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Election Audit Summary
   The code created for this analysis could be used as a template for analyzing any other election, 
   with just some slight modifications.  It would be necessary to link the code to the the datafile of the next election for analysis,
   and the code would need some slight adjusting if the new election data file is not stored in the exact same format (ballot id, county, candidate). 
   Additionally, in order to use this script for a broader, country-wide election, there would be the need to change logic to pull data at the state level.
   
   Examples of code that would require modification to utilize in other elections: 
   
   ![CodeSnip](https://user-images.githubusercontent.com/71041680/109441039-27221380-7a02-11eb-8519-19ee023a48eb.png)

   ![CodeSnip2](https://user-images.githubusercontent.com/71041680/109441108-59337580-7a02-11eb-9a8a-54d9764c97b7.png)

