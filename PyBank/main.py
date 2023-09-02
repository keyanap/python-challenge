import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

date = []
profit = []

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= " ,")

    date.append = (row[0])
    profit.append = (row[1])

print("Financial Analysis")
print("Total Months: " + date.count)
print["Total: " + sum(row[1])]
print["Average Change: " + sum(row[1])/len(row[1])]
print("Greatest Increase in Profits: " + max(row[1]))
print("Greatest Decrease in Profits: " + max(row[1]))

# export results to a text file