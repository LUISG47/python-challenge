# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/luisgalindez/Documents/python-challenge/Pybank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

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
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    #first_row = next(reader)
    #dates = first_row[0]

    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months = total_months + 1

        # Track the net change
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
        
        profit_losses_count = prof_loss
        #dates.append(date)

# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0

# Generate the output summary


# Print the output

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase[0]} (${increase[1]})")
print(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
