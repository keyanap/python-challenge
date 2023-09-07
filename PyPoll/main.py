import os
import csv

election_data_csv = "election_data.csv"

ballot_id =[]
county =[]
candidate =[]

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header=next(csvreader)
    for row in csvreader:
        candidate.append (row[2])

    import statistics
charlespercentage =candidate.count("Charles Casper Stockham")/len(candidate)*100
dianapercentage = candidate.count("Diana DeGette")/len(candidate)*100
raymonpercentage = candidate.count("Raymon Anthony Doane")/len(candidate)*100

print("Election Results")
print("Total Votes: ", len(candidate))
print("Charles Casper Stockham:", charlespercentage,"%" + "(", candidate.count("Charles Casper Stockham"), ")")
print("Diana DeGette: ", dianapercentage,"%" + "(", candidate.count("Diana DeGette"), ")")
print("Raymon Anthony Doane: ", raymonpercentage,"%" + "(", candidate.count("Raymon Anthony Doane"), ")")
print("Winner:" + statistics.mode(candidate))

electionresults = os.path.join("Analysis", "Election Results.txt")
with open (electionresults,"w") as electiondata:
    
    output = (f"Election Results\n"
    f"Total Votes: {len(candidate)}\n"
    f"Charles Casper Stockham: {charlespercentage}% '('{candidate.count('Charles Casper Stockham')}')'\n"
    f"Diana DeGette: {dianapercentage}% '(' {candidate.count('Diana DeGette')}')'\n"
    f"Raymon Anthony Doane: {raymonpercentage} % '('{candidate.count('Raymon Anthony Doane')}')'\n"
    f"Winner: {statistics.mode(candidate)}")

    electiondata.write(output)