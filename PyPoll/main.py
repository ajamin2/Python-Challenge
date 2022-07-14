# Import modules
import os
import csv

# Set path for file
PyPollcsv = os.path.join("Resources", "election_data.csv")
PyPollcsv = r'/Users/anishachaudhari/data_science/Python-Challenge/PyPoll/Resources/election_data.csv'

# Lists to store data
num_votes = []
candidates = []
percent_votes = []

# Set variables
total_votes = 0

# Open csv file
with open(PyPollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# Skip the header
    csvheader = next(csvreader)
    for row in csvreader:

# Total number of votes cast
        total_votes = total_votes + 1

# Complete list of candidates who received votes
# Append candidate names
        name_candidate = row[2]

# Conditional for if candidate does not match a candidate
        if name_candidate not in candidates:
            candidates.append(name_candidate)
            index = candidates.index(row[2])
            num_votes.append(1)

        else:
            index = candidates.index(row[2])
            num_votes[index] +=1

# Percentage of votes each candidate won
# Total number of votes each candidate wone
        for votes in num_votes:
            percentage = (votes/total_votes) * 100
            percentage = round(percentage)
            percentage = "%.3f%%" % percentage
            percent_votes.append(percentage)

# Winner of election based on popular vote
        winner = max(num_votes)
        index = num_votes.index(winner)
        winning_candidate = candidates[index]

# Print results in terminal

    print("Election Results")
    print("---------------------------------------------------------")
    print("Total Votes:" + str(total_votes))
    print("---------------------------------------------------------")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    print("---------------------------------------------------------")
    print(f"Winner: {winning_candidate}")

# Forward results to .txt file
# Create path to output file
    results = os.path.join("Output", "results.txt")
    results = r'/Users/anishachaudhari/data_science/Python-Challenge/PyPoll/Analysis/results.txt'

    with open(results, 'w') as txt:

# Print results in .txt file
        txt.write("Election Results" + "\n")
        txt.write("Total Votes: " + str(total_votes) + "\n")
        for i in range(len(candidates)):
            txt.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})" + "\n")
        txt.write("Winner: " + str(winning_candidate) + "\n")



 
