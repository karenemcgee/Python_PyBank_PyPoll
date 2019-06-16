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


import os
import csv
import pandas as pd

mydir = os.getcwd()
pypoll_csv = os.path.join("Resources", "PyPollSmall.csv")

with open(pypoll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    voterID = []
    county = []
    candidate = []

    #THIS PART WORKS
    for row in csvreader:
        voterID.append(int(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))

        #TOTAL VOTES
        for i in voterID:
            totalvotes = len(voterID)

        #LIST OF CANDIDATES
        candidatelist = set(candidate)
        
        #VOTE PERCENTAGES
        liVotePercent = ((candidate.count('Li')) / totalvotes) * 100
        khanVotePercent = ((candidate.count('Khan')) / totalvotes) * 100
        correyVotePercent = ((candidate.count('Correy')) / totalvotes) * 100
    
    print(f'The total number of votes is {totalvotes}.')
    print(f'These are the candidates: {candidatelist}')
    print(f"Li's votes are {liVotePercent}")
    print(f"Khan's votes are {khanVotePercent}")
    print(f"Correy's votes are {correyVotePercent}")
    ########################################################
    