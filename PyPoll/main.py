import os
import csv

total_votes = 0
candidatelist = []
votecountlist = []
vote_percentlist = []

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidatelist:
            candidatelist.append(candidate)
            votecountlist.append(1)
        else:
            index_candidate = candidatelist.index(candidate)
            votecountlist[index_candidate] += 1

result = []
win_count = 0
for candidate in candidatelist:
    votecount = votecountlist[candidatelist.index(candidate)]
    vote_percent = (votecount/total_votes)*100

    if votecount > win_count:
        win_count = votecount
        winner = candidate
        
    result.append(f"{candidate}: {vote_percent:.3f}% ({votecount})")
                  

output_path = os.path.join("..", "PyPoll", "Results.text")
with open(output_path, "w") as textfile:
    textfile.writelines("Election Results\n")
    textfile.writelines("------------------------\n")
    textfile.writelines("Total Votes: " + str(total_votes) + "\n")
    textfile.writelines("------------------------\n")
    
    for r in range(len(result)):
        textfile.writelines(result[r] + "\n")
    
    textfile.writelines("------------------------\n")
    textfile.writelines("winner: " + winner + "\n")
    textfile.writelines("------------------------\n")
    
with open(output_path, "r") as readfile:
    print(readfile.read())
