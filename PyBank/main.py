#dependencies
import os
import csv

#path
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#variables
date = []
total_months = 0
total_net = 0
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]
avg_change = 0

#open and read csv
with open(budget_data_csv) as csvfile:
    #read header row first
    csvreader = csv.reader(csvfile, delimiter= ",")
    header=next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    #read through each row after header
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1])-previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]
        date.append (row[0])
        
        #greatest increase and decrease
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    #average change in total net
    avg_change = sum(net_change_list)/len(net_change_list)

#print results in terminal
print("Financial Analysis")
print("-------------------------")
print("Total Months: ", total_months)
print("Total: " + "$", total_net)
print("Average Change:" + "$", (round(avg_change,2)))
print("Greatest Increase in Profits:" + greatest_increase[0] + "(" + "$", greatest_increase[1], ")")
print("Greatest Decrease in Profits:" + greatest_decrease[0]+ "(" + "$", greatest_decrease[1], ")")

#export results into text file
profitanalysis = os.path.join("Analysis", "Profit Analysis.txt")
with open (profitanalysis,"w") as profitdata:
    
    output = (f"Profit Analysis\n"
    f"----------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_net}\n"
    f"Average Change: ${round(avg_change,2)}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}")

    profitdata.write(output)