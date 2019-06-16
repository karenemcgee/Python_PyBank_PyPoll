#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting 
#process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but 
#unfortunately, his concentration isn't what it used to be.)

#You will be give a set of poll data called election_data.csv. The dataset is composed of 
#three columns: Voter ID, County, and Candidate. Your task is to create a Python script that 
#analyzes the votes and calculates each of the following:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.

import pandas as pd
import os
import csv

#OPEN CSV
mydir = os.getcwd()
pypoll_csv = os.path.join("Resources", "PyPollSmall.csv")
data_file_pd = pd.read_csv(pypoll_csv)

#TOTAL NUMBER OF VOTES CAST
totalvotes = data_file_pd.shape[0]
print(f'The total number of votes was {totalvotes}.')

#LIST OF CANDIDATES AND VOTE TOTALS
candidatesList = data_file_pd["Candidate"].value_counts()
print(f'The following candidates received these votes: ')
print(f'{candidatesList}')

# mydir = os.getcwd()
# pypoll_csv = os.path.join("Resources", "PyPollSmall.csv")

# with open(pypoll_csv, newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ",")
#     next(csvreader, None)

#     voterID = []
#     county = []
#     candidates = []

#     #THIS PART WORKS
#     for row in csvreader:
#         voterID.append(int(row[0]))
#         county.append(str(row[1]))
#         candidates.append(str(row[2]))

#         #TOTAL VOTES
#         for i in voterID:
#             totalvotes = len(voterID)

#         #LIST OF CANDIDATES
#         candidateUnique = set(candidates)
#         candidateList = list(candidateUnique)

#     for candidate in candidateList:
#         print(f"{candidate}'s number of votes are {candidate.count(row[2])}")

#         #VOTE TOTALS
#         #liVotes = candidate.count('Li')
#         #khanVotes = candidate.count('Khan')
#         #correyVotes = candidate.count('Correy')
        
#         #VOTE PERCENTAGES
#         #liVotePercent = round(((liVotes / totalvotes) * 100),2)
#         #khanVotePercent = round(((khanVotes / totalvotes) * 100),2)
#         #correyVotePercent = round(((correyVotes / totalvotes) * 100),2)

#         #WINNER
#         #voteTotals = [liVotes, khanVotes, correyVotes]
#         #winner = max(voteTotals)
    
#     print(f'The total number of votes is {totalvotes}.')
#     print(f'These are the candidates: {candidateList}')
#     #print(f"Li's total number of votes is {liVotes} or {liVotePercent}%.")
#     #print(f"Khan's total number of votes is {khanVotes} or {khanVotePercent}%.")
#     #print(f"Correy's total number of votes is {correyVotes} or {correyVotePercent}%")
#     #print(f'The winner is {winner}!')
#     ########################################################
    