
#In this challenge, you are tasked with creating a Python script for analyzing the financial records 
#of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

#In addition, your final script should both print the analysis to the terminal and export a text file 
#with the results (aka export csv)

import os
import csv

months = []
profitloss = []

mydir = os.getcwd()
pybank_csv = os.path.join("Resources", "PyBank.csv")

with open(pybank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    for row in csvreader:
        months.append(str(row[0]))
        profitloss.append(int(row[1]))
        totalmonths = len(months)
        netPL = sum(profitloss)
        average = netPL / len(profitloss)
        #################

    for i in profitloss:
        PLchange = (profitloss[i+1] - profitloss[i] for i in range(len(profitloss)-1))

    maxPLchange = max(PLchange)
    print(f'The maximum increase in profits is {maxPLchange}')

    
    for i in profitloss:
        PLchange = (profitloss[i+1] - profitloss[i] for i in range(len(profitloss)-1))

    minPLchange = min(PLchange)
    print(f'The maximum decrease in profits is {minPLchange}')

print(f'The total number of months is {totalmonths}')
print(f'The net profit and loss is {netPL}')
print(f'The average profit/loss is {average}')