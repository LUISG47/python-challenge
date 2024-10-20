# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/luisgalindez/Documents/python-challenge/Pybank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("/Users/luisgalindez/Documents/python-challenge/Pybank/analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
profit_losses_count = None
increase = ('', 0)
decrease = ('', 0)
changes = []
dates = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    # Extract first row to avoid appending to net_change_list
    header = next(reader)

    # Track the total and net change
    # Process each row of data
    for row in reader:

        # Track the amount of total of months to be computed
        total_months = total_months + 1

        # ----------------------------------------------------------------------------------------------
        # Track the net change of profit and losses within each period and append it 
        # to a list to get all the monthly changues in profit and losses to calculate the average later
        # ----------------------------------------------------------------------------------------------
        prof_loss = int(row[1])
        total_net = total_net + prof_loss

        if profit_losses_count is not None:
            change = prof_loss - profit_losses_count
            changes.append(change)
        
        # Calculate the greatest increase in profits (month and amount)
            if change > increase[1]:
                increase = (row[0], change)
            
        # Calculate the greatest decrease in losses (month and amount)
            if change < decrease[1]:
                decrease = (row[0], change)
        
        #update the current profit/lose amount to be computed on the next iteration
        profit_losses_count = prof_loss

# Calculate the average net change across the months in the list collected in the changues list
average_change = sum(changes) / len(changes) if changes else 0

# Generate the output summary
# Print the summary of the desired results to the terminal

print("----------------------------")
print("                            ")
print("Financial Analysis")
print("                            ")
print("----------------------------")
print("                            ")
print(f"Total Months: {total_months}")
print("                            ")
print(f"Total: ${total_net}")
print("                            ")
print(f"Average Change: ${average_change:.2f}") # the .2f is to show only 2 decimals on the result
print("                            ")
print(f"Greatest Increase in Profits: {increase[0]} (${increase[1]})")
print("                            ")
print(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})")
print("                            ")
print("----------------------------")

# Write the results to the desired putput txt file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"----------------------------------------------------\n\n")
    txt_file.write(f"Financial Analysis\n\n")
    txt_file.write(f"----------------------------------------------------\n\n")
    txt_file.write(f"Total Months: {total_months} \n\n")
    txt_file.write(f"Total: ${total_net} \n\n")
    txt_file.write(f"Average Change: ${average_change:.2f} \n\n")
    txt_file.write(f"----------------------------------------------------\n\n")
    txt_file.write(f"Greatest Increase in Profits: {increase[0]} (${increase[1]}) \n\n")
    txt_file.write(f"Greatest Increase in Profits: {increase[0]} (${increase[1]}) \n\n")
    txt_file.write(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]}) \n\n")
