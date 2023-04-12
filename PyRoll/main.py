import csv

#Set Initial Variables
total_votes = 0
candidates = {}
total_votes_percent = 0
winner = ""

with open('Resources/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Header Stored
    header = next(csvreader)
    for row in csvreader:
        
        candidate = row[2]
        total_votes += 1

        # Disctionary to assign candidate names as a key and vote count as a value
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
    winner = max(candidates, key=candidates.get)    
    
#Outputs
with open('analysis/analysis_output.txt', 'w') as file:
    file.write(f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------''')
    # Used a variable for each candidates info so that each candidate has their own line in the output
    for x in candidates:
        total_votes_percent = "{0:.3f}".format(candidates[x]/total_votes*100)
        file.write(f'\n{x}: {total_votes_percent}% ({candidates[x]})')
    file.write(f'''
-------------------------
Winner: {winner}
-------------------------''')

# repeated from above
print(f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------''')
for x in candidates:
    total_votes_percent = "{0:.3f}".format(candidates[x]/total_votes*100)
    print(f'{x}: {total_votes_percent}% ({candidates[x]})')
print(f'''-------------------------
Winner: {winner}
-------------------------''')