import csv

import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")  


total_votes = 0
candidate_options= []
candidate_votes = {}
candidate_winner = ""
winning_count = 0
winning_percent = 0 

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    head = next(file_reader)

    for row in file_reader:

        total_votes += 1
        candidate_name = row [2]
        if candidate_name not in candidate_options:
            (candidate_options).append(candidate_name)
           
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] += 1
with open(file_to_save,"w") as txt_file:
    election_results= (
    f"\nElection Results\n"
    f"-----------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-----------\n")
    print(election_results, end=" ")
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        candidate_percent = float(votes)/float(total_votes)*100
        candidate_results = (
        f"{candidate_name}:{candidate_percent:.1f}% {votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)
        

        if (votes > winning_count) and (candidate_percent > winning_percent):
            winning_count = votes 
            winning_percent = candidate_percent
            candidate_winner = candidate_name       

    winning_candidate_summary = ( 
        f"--------------------\n"
        f"Winner: {candidate_winner}\n"
        f"Winning Vote count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percent:.1f}%\n"
        f"--------------------\n")

    print(winning_candidate_summary)           
    txt_file.write(winning_candidate_summary)



    