

# the data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# create variable and set value of total_votes to 0
total_votes = 0

#Create Candidate list
candidate_options = []
#create candidate votes dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_votes = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        #add to the toal vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]
        #if candidate name does not match any in existing list
        if candidate_name not in candidate_options:
            #add candidate name to candidate_option list
            candidate_options.append(candidate_name)
            #begin tracking candidates vote count
            candidate_votes[candidate_name] = 0
            
        #increment candidate votes   
        candidate_votes[candidate_name] += 1
    
    #save the results to our text file
    with open(file_to_save, "w") as txt_file:
        
        #print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total votes: {total_votes:,}\n"
            f"-------------------------\n"
        )
        print(election_results, end="")
        txt_file.write(election_results)

        #loop through candidate_options dict
        for candidate_name in candidate_votes:
            #retrieve vote count for each candidate
            votes = candidate_votes[candidate_name]
            #calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            #format vote percentage to only 1 decimal place
            vote_percentage = round(vote_percentage, 1)
            
            #  To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
        
            #determine winning candidate
            #determine if votes are greater than winning vote count
            if (votes > winning_votes) and (vote_percentage > winning_percentage):
                #if true set the winning counts
                winning_votes = votes
                winning_percentage = vote_percentage
                #set the candidate to winning candidate
                winning_candidate = candidate_name

        #print the candidate name and the percentage of votes
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_votes:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

#print total vote value
#print(total_votes)
#print candidate_options list
#print(candidate_options)
#print the candidate vote dictionary
#print(candidate_votes)
        