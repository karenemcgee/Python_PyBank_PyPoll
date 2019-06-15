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

voterID = []
county = []
candidate = []

mydir = os.getcwd()
pypoll_csv = os.path.join("Resources", "PyPollSmall.csv")

with open(pypoll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    #THIS PART WORKS
    #for row in csvreader:
        voterID.append(int(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))

        for i in voterID:
            totalvotes = len(voterID)
    print(f'The total number of votes is {totalvotes}.')

    def unique(list1):
        unique_list = []
        list_set = set(list1)
        unique_list = (list(list_set))
        for x in unique_list:
            print x
    list1 = candidate
    print(f'The candidates are {list1}')
