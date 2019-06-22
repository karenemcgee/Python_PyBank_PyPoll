
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
        minPLchangeMonth = months[i]
        maxPLchange = max(PLchange)
        maxPLchangeMonth = months[i]
    #CANT FIGURE OUT HOW TO MAKE MONTHS WORK HERE...
    
    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {totalmonths}')
    print(f'Total: ${netPL}')
    print(f'Average Change: ${avgPLchange}')
    print(f'Greatest Increase in Profits: {maxPLchangeMonth} ${maxPLchange}')
    print(f'Greatest Decrease in Profits: {minPLchangeMonth} ${minPLchange}')
    

TotalMonths = [totalmonths]
NetProfitLoss = [netPL]
AverageProfitLoss = [avgPLchange]
Maximum = [maxPLchange]
Minimum = [minPLchange]

summary = zip(TotalMonths, NetProfitLoss, AverageProfitLoss, Maximum, Minimum)

output_file = os.path.join("PyBank", "PyBankCSV.csv")
with open(output_file, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Total Months", "Net Profit/Loss", "Average Profit/Loss", "Greatest Profit Increase", "Greatest Profit Decrease"])
    writer.writerows(summary)

output_file = os.path.join("PyBank", "PyBankResults.txt")
with open(output_file, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow([f'Financial Analysis'])
    csvwriter.writerow([f'----------------------------'])
    csvwriter.writerow([f'Total Months: {totalmonths}'])
    csvwriter.writerow([f'Total: ${netPL}'])
    csvwriter.writerow([f'Average Change: ${avgPLchange}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {maxPLchangeMonth} ${maxPLchange}'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {minPLchangeMonth} ${minPLchange}'])