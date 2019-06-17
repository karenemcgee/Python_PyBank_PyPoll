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
import csv
import os

pypoll_csv = "Resources/PyPoll.csv"
data_file_pd = pd.read_csv(pypoll_csv)

candidatesList = data_file_pd["Candidate"].value_counts().keys().tolist()
candidatesVotes = data_file_pd["Candidate"].value_counts().tolist()
totalVotes = sum(candidatesVotes)
candidatesPercent = [x / totalVotes for x in candidatesVotes]
candidatesPercent2 = [x * 100 for x in candidatesPercent]
maxVotesAmt = max(candidatesVotes)

talliesDF = pd.DataFrame({"Candidates": candidatesList, 
                          "Votes": candidatesVotes,
                          "Percent": candidatesPercent2})

winner = talliesDF.iloc[talliesDF.Votes.argmax(), 0]

print(f'ELECTION RESULTS')
print(f'-------------------------')
print(f'Total Votes: {totalVotes}')
print(f'-------------------------')
print(talliesDF)
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

mydir = os.getcwd()
output_path = os.path.join("PyPoll", "PyPollResults.txt")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow([f'ELECTION RESULTS'])
    csvwriter.writerow([f'-------------------------'])
    csvwriter.writerow([f'Total Votes: {totalVotes}'])
    csvwriter.writerow([f'-------------------------'])
    csvwriter.writerow([talliesDF])
    csvwriter.writerow([f'-------------------------'])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow([f'-------------------------'])

talliesDF.to_csv('../python-challenge/PyPoll/PyPollCSV.csv', index=False)