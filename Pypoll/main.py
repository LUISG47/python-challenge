# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/luisgalindez/Documents/python-challenge/Pypoll/Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("/Users/luisgalindez/Documents/python-challenge/Pypoll/analysis/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}
results = []

# Winning Candidate and Winning Count Tracker
candidate_win = 0
count_win= 0
percentage_win = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row

        total_votes = total_votes + 1
        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal) [This part was printed with the resume at the end of the code]
    

    # Write the total vote count to the text file
    txt_file.write(f"----------------------------------------------------\n\n")
    txt_file.write(f"Election Results\n\n")
    txt_file.write(f"----------------------------------------------------\n\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"----------------------------------------------------\n\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates:


        # Get the vote count and calculate the percentage
        votes = candidates[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > count_win:
            count_win = votes
            candidate_win = candidate
            percentage_win = vote_percentage

        # Print and save each candidate's vote count and percentage
        
        results.append((candidate, vote_percentage, votes))
        print(". ")

    print("                            ")
    print("Election Results")
    print("                            ")
    print("----------------------------")
    print("                            ")
    print(f"Total Votes: {total_votes}")
    print("                            ")
    print("----------------------------")
    
    print("                            ")
    for candidate, vote_percentage, votes in results:
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    

    print("                            ")
    print("----------------------------")
    # Generate and print the winning candidate summary
    print(f"\nWinner: {candidate_win}")
    print("                            ")
    print("----------------------------")
    print("                            ")
    print(f"Winning Vote Count: {count_win}")
    print(f"Winning Percentage:{percentage_win:.2f}")
    print("                            ")
    print("----------------------------")

    # Save the winning candidate summary to the text file
    
    for candidate, vote_percentage, votes in results:
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n\n")
    txt_file.write(f"----------------------------------------------------\n\n")
    txt_file.write(f"Winner: {candidate_win}\n\n")
    txt_file.write(f"----------------------------------------------------\n\n")
    txt_file.write(f"Winning Vote Count: {count_win}\n")
    txt_file.write(f"Winning Percentage: {percentage_win:.3f}%\n")
