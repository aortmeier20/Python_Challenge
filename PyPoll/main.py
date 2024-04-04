#
#1. The total number of votes cast - done*
#2. A complete list of candidates who received votes - done*
#3. The percentage of votes each candidate won - done*
#4. The total number of votes each candidate won - done*
#5. The winner of the election based on popular vote - done*

#S
#create variables

import csv
election_file_path = "PyPoll/Resources/election_data.csv"

total_votes = 0
candidates = []
candidate_votes = []
#open the file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file) #skips a row in the file ( first row =header row_)
    #read a row in the file
    for row in csv_file:
        #add to total votes
        total_votes += 1
        #Ballot ID,County,Candidate
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        #check if candidate exists
        if candidate not in candidates:
            # add to list if they haven't been added
            candidates.append(candidate) 
            candidate_votes.append(1) # add the first vote
        else: # candidate is in list
            candidate_id = candidates.index(candidate)
            candidate_votes[candidate_id] +=1

#done reading the file

#find the winner
winning_candidate = ""
winning_candidate_votes = 0
for candidate in candidates: 
     current_votes= candidate_votes[candidates.index(candidate)]
     if  current_votes > winning_candidate_votes:
          winning_candidate = candidate
          winning_candidate_votes = current_votes

     

          
#print the results to screen
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for candidate in candidates:
        current_candidate_votes = candidate_votes[candidates.index(candidate)]
        current_vote_pct = (current_candidate_votes/total_votes) *100
        print(f'{candidate}: {round(current_vote_pct,3)}% ({current_candidate_votes})')
print('-------------------------')
print(f'Winner: {winning_candidate}')
print('-------------------------')


#print the results to file





#E

# Example Output
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------