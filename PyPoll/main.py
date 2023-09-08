#dependencies
import os
import csv

#path
election_data_csv = "election_data.csv"

#variables
ballot_id =[]
county =[]
candidate =[]

#open and read csv
with open(election_data_csv) as csvfile:
    #read header row first
    csvreader = csv.reader(csvfile, delimiter= ",")
    header=next(csvreader)
    #read through each row after header
    for row in csvreader:
        candidate.append (row[2])

    import statistics
#number of candiate votes and percentage of votes
charlespercentage =candidate.count("Charles Casper Stockham")/len(candidate)*100
dianapercentage = candidate.count("Diana DeGette")/len(candidate)*100
raymonpercentage = candidate.count("Raymon Anthony Doane")/(len(candidate))*100

#print results in terminal
print("Election Results")
print("------------------")
print("Total Votes: ", len(candidate))
print("Charles Casper Stockham:", round(charlespercentage,3),"%" + "(", candidate.count("Charles Casper Stockham"), ")")
print("Diana DeGette: ", round(dianapercentage,3),"%" + "(", candidate.count("Diana DeGette"), ")")
print("Raymon Anthony Doane: ", round(raymonpercentage,3),"%" + "(", candidate.count("Raymon Anthony Doane"), ")")
print("Winner:" + statistics.mode(candidate))

#export results into text file
electionresults = os.path.join("Analysis", "Election Results.txt")
with open (electionresults,"w") as electiondata:
    
    output = (f"Election Results\n"
    f"------------------\n"
    f"Total Votes: {len(candidate)}\n"
    f"Charles Casper Stockham: {round(charlespercentage,3)}% '('{candidate.count('Charles Casper Stockham')}')'\n"
    f"Diana DeGette: {round(dianapercentage,3)}% '(' {candidate.count('Diana DeGette')}')'\n"
    f"Raymon Anthony Doane: {round(raymonpercentage,3)} % '('{candidate.count('Raymon Anthony Doane')}')'\n"
    f"Winner: {statistics.mode(candidate)}")

    electiondata.write(output)