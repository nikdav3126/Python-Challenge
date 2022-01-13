import os
import csv

csv_path = os.path.join('Resources','election_data.csv')

#Create List to Store Data
CandidateList = []
VoteTotal = []
Percent = []

#Set Variable Types
Vote = 0

with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        County = str(row[1])
        CandidateList.append(row[2])

        #Calculate number of votes
        Vote = Vote + 1

    print("---------------------")   
    print("Election Results")
    print("---------------------")
    print(f"Total Votes:  {str(Vote)}")
    print("---------------------")
    
    
    #At this point I ran into an issue trying to parse the candidates and the total number of votes they received
    #I thought a for loop would be helpful but I couldn't figure out how to set the variables within
    
