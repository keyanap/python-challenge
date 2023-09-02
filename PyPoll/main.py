import os
import csv

election_data_csv = "election_data.csv"

ballot_id =[]
county =[]
candidate =[]

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= " ,")

    ballot_id.append = (row[0])
    county.append = (row[1])
    candidate.append = (row[2])

    # ignore header
    import statistics
   
print("Election Results")
print("Total Votes: " + ballot_id.count)
print("Charles Casper Stockham:" + "(" + candidate.count(Charles Casper Stockham) + ")")
print("Diana DeGette: " + "(" + candidate.count(Diana DeGette)+ ")")
print("Raymon Anthony Doane: " + "(" + candidate.count(Raymon Anthony Doane) + ")")
print("Winner:" + statistics.mode(row[2]))
# percentage for votes 
    