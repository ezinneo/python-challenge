#Import OS
import os

#Import csv and match
import csv
import math

#Get location of csv, name the file path/ location
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
print(csvpath)

#Open the csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    print(csv_reader)

    #Set up variable
    total_votes = 0
    candidate_names = set() #To store unique names of candidates
    candidate_votes = {} #Dictionary to store vote counts for each candidate


    #Read the first row and skip and skip if it is a header
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    next(csv_reader)
#Loops for calculations
    for row in csv_reader:
        #calculate total votes
        total_votes += 1

        #find the candidate names and add to the set
        candidate_name = row[2]
        candidate_names.add(candidate_name)
        #Calculate vote percentages
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

#Sort name in chronological order
sorted_names = sorted(candidate_names)
       
#Calculate percentage of votes for each candidate
percentage_votes = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes/ total_votes) * 100
    percentage_votes[candidate] = percentage

#find winner
winner = max(candidate_votes, key =candidate_votes.get)

#Print statements
print("Total Votes:", total_votes)

print("Candidate Names, Percentage of Votes and Total Number of votes per candidate:")
for candidate, percentage in percentage_votes.items():
    print(candidate, ":", round(percentage), "%" )

for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes")

print("Winner:", winner)
