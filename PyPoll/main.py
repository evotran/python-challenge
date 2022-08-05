import os
import csv
from pathlib import Path

total_votes = 0 
stockham_votes = 0
degette_votes = 0
doane_votes = 0

election_data_csv = os.path.join('Resources', 'election_data.csv')
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        total_votes +=1
        if row[2] == "Charles Casper Stockham": 
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane_votes +=1
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [stockham_votes, degette_votes, doane_votes]

dict_candidates_and_votes = dict(zip(candidates,votes))
winner = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

stockham_percent = (stockham_votes/total_votes) * 100
degette_percent = (degette_votes/total_votes)* 100
doane_percent = (doane_votes/total_votes) * 100
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

output_file = Path("Analysis", "results.txt")
with open(output_file,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")