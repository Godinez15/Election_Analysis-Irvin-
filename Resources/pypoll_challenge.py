#Add out dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load= os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes= 0

# Candidate Options and candidate votes
candidate_options=[]
candidate_votes={}

county_votes = {}
county_options = []

# Track the winning candidate, vote count, and percentage.
winning_candidate= ""
winning_count= 0
winning_percentage= 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)

    # Read the header row. 
    headers= next(file_reader)
 
    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.

        total_votes += 1

        #   Print candidate name from each row.
        candidate_name= row[2]

    # If the candidate does not match any existing candidate add it to the candidate list.

        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]= 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name]+= 1

        county_name= row[1]
        if county_name not in county_options:
        
            
            # If not, add it to the list of county names.

            # print('inside county_name if statement')
            county_options.append(county_name)
            #Begin tracking that candidate's vote count.
            county_votes[county_name]= 0
            
        # Add a vote to that candidate's count.
        county_votes[county_name]+= 1
        # print('outside of the county_name statement')

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Create a list for the counties.

    largest_turnout_county_name= " "

    # Declare a variable that represents the number of votes that a county 
    # received.  

    # row[1]

    #add an if statement to check if the county name has already been recorded.

    # if county_votes not in county_name:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    txt_file.write('\n')
    txt_file.write('County Results:\n')
    winning_county_vote_count = 0
    for county in county_votes:
        # Retrieve vote count and percentage.
        print('REALLY OBVIOUS')
        print(county_votes)
        print(county)
        votes= county_votes[county]
        

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Determine winning vote count, winning percentage, and county.
        if (votes > winning_county_vote_count) :
            winning_county_vote_count = votes
            largest_turnout_county_name= county
        # Print the winning countys' results to the terminal.
        county_results=(
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)

        # Save the county results to our text file.
        txt_file.write(county_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    
    txt_file.write('\n')

    winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {largest_turnout_county_name}\n"
    f"-------------------------\n")
    print(winning_county_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)

    for candidate in candidate_votes:

        # Retrieve vote count and percentage.
        votes= candidate_votes[candidate]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate= candidate

        candidate_results=(
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    # winning_county_summary = (
    # f"-------------------------\n"
    # f"Winner: {winning_county}\n"
    # f"Winning Vote Count: {winning_count:,}\n"
    # f"Winning Percentage: {winning_percentage:.1f}%\n"
    # f"-------------------------\n")
    # print(winning_county_summary)
    
    # # Save the winning county's results to the text file.
    # txt_file.write(winning_county_summary)