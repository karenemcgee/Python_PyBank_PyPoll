
#In this challenge, you are tasked with creating a Python script for analyzing the financial records 
#of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of 
#two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so 
#the records are simple.)

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

mydir = os.getcwd()
pybank_csv = os.path.join("Resources", "PyBank.csv")

with open(pybank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    months = []
    profitloss = []
    PLchange = []

    for row in csvreader:
        months.append(str(row[0]))
        profitloss.append(int(row[1]))
        
        totalmonths = len(months)
        netPL = sum(profitloss)
    
    for i in range(1, len(profitloss)):
        PLchange.append(profitloss[i] - profitloss[i-1])
        avgPLchange = round((sum(PLchange)/len(PLchange)),2)
        minPLchange = min(PLchange)
        maxPLchange = max(PLchange)
    
    print(f'The total number of months is {totalmonths}.')
    print(f'The net profit and loss is ${netPL}.')
    print(f'The average change in profit/loss is ${avgPLchange}.')
    print(f'The minimum change in profit/loss is ${minPLchange}.')
    print(f'The maximum change in profit/loss is ${maxPLchange}.')

TotalMonths = [totalmonths]
NetProfitLoss = [netPL]
AverageProfitLoss = [avgPLchange]
Maximum = [maxPLchange]
Minimum = [minPLchange]

summary = zip(TotalMonths, NetProfitLoss, AverageProfitLoss, Maximum, Minimum)

output_file = os.path.join("Resources", "PyBankFinal.csv")

with open(output_file, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Total Months", "Net Profit/Loss", "Average Profit/Loss", "Greatest Profit Increase", "Greatest Profit Decrease"])
    writer.writerows(summary)