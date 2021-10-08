# In this challenge, you are tasked with creating a Python script for analysing
# the financial records of your company. You will give a set of financial data called
# budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)



# Your task is to create a Python script that analyses the records to calculate each of the following:
    #       1-The total number of months included in the dataset
    #       2-The net total amount of "Profit/Losses" over the entire period
    #       3-The average of the changes in "Profit/Losses" over the entire period
    #       4-The greatest increase in profits (date and amount) over the entire period
    #       5-The greatest decrease in losses (date and amount) over the entire period

# import library
import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

# declare variables
Totalmonths = 0
NetTot_revenue = 0
profit_previous_month = 0
Total_change_profit = 0
date = []
monthly_change = []


# read the file
with open(budget_data_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next (csv_reader)

# 1-The total number of months included in the dataset	
    
    for row in csv_reader:
        Totalmonths += 1

# 2-The net total amount of "Profit/Losses" over the entire period
        NetTot_revenue += int(row[1])
        
print("Total number of months: ", Totalmonths)   
print("Net total amount of Profit/Losses:" + str(NetTot_revenue))
#  3-The average of the changes in "Profit/Losses" over the entire period

monthly_profit = int(row[1])
                
monthly_change_profits = monthly_profit - profit_previous_month

monthly_change.append(monthly_change_profits)

Total_change_profit = Total_change_profit + monthly_change_profits
profit_previous_month = monthly_change

average_change_profits = (Total_change_profit/Totalmonths)
 

print("Average_change_profits:" + "$" + str(round(average_change_profits)))

#   4-The greatest increase in profits (date and amount) over the entire period

greatest_increase = max(monthly_change)
    
#5-The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(monthly_change)

print (greatest_increase)
print (greatest_decrease)

output_file = os.path.join(".", "analysis", "results.txt")
with open(output_file, "w",) as textfile:

    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------\n")
    textfile.write("Total months:" + str(Totalmonths) + "\n")
    textfile.write("Total:" + "$" + str(NetTot_revenue) + "\n")

    # textfile.write("Average_change_profits:" + "$" + str(round(average_change_profits)) + "\n")
    # textfile.write("Greatest_increase in profits:", str(greatest_increase) + "\n")
    # textfile.write("Greatest_decrease in profits:", str(greatest_increase) + "\n")