import csv

total_votes = 0
candidates = {}
total_votes_percent = 0
winner = ""

with open('Resources/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        
        candidate = row[2]
        total_votes += 1

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
    for x in candidates:
        total_votes_percent = "{0:.3f}".format(candidates[x]/total_votes*100)
        file.write(f'\n{x}: {total_votes_percent}% ({candidates[x]})')
    file.write(f'''
-------------------------
Winner: {winner}
-------------------------''')

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