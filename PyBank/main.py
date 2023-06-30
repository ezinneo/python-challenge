#Import OS
import os

#Import csv
import csv
import math

#Get location of csv, name of the file and location
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print(csvpath)

#To now open the file itself
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    print(csv_reader)

    #Set up variables to hold lists 
    total_months = 0
    total_profit_losses = 0
    changes_profit_loss = []
    dates = []
    

    # Getting the first profit/loss
    next(csv_reader) #next to get past header row
    second_row = next(csv_reader) #next to get to first data row
    previous_value = float(second_row[1]) # setting previous value with first profit/loss value
    csvfile.seek(0) # reset the row skip, so we can set the header again, since we need to start the loop from row 2 not row 3
    print(previous_value)

    #Read the header row first (but skip if it is a header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")


    #Loop through the rows
    for row in csv_reader:

        #Calculate the total number of months
        total_months += 1

        #Calculate the total Profit/Losses
        #collect the value for each row staring at Index 1
        # Add to previous value
        # Hold it in a variable
        value = float(row[1])
        total_profit_losses = total_profit_losses + value

        #Changes in Profit/ Losses over the period and then average of the changes
        changes = float(row[1]) - float(previous_value)
        previous_value = row[1]
        #changes_profit_loss.append((row[0], changes))
        changes_profit_loss.append(changes)
        #Collect the value for each row starting at index 0 (date)
        dates.append(row[0])

    # remove the first change, so we dont add 0 to the calculation
    changes_profit_loss.pop(0)

    #find highest number
    greatest_increase_profit = changes_profit_loss[0]
    greatest_decrease_profit = changes_profit_loss[0]
    for num in changes_profit_loss:
        if num > greatest_increase_profit:
            greatest_increase_profit = num
        if num < greatest_decrease_profit:
            greatest_decrease_profit= num

#Get corresponding date using Index
greatest_increase_index = changes_profit_loss.index(greatest_increase_profit)
greatest_increase_date = dates[greatest_increase_index + 1] #to account for skipping first row

greatest_decrease_index = changes_profit_loss.index(greatest_decrease_profit)
greatest_decrease_date = dates[greatest_decrease_index + 1] #to account for skipping first row

#Print statements
print("Total Months:", total_months)
print ("Total Profit/Losses: $", round(total_profit_losses))
print ("Average Change: $", round(math.fsum(changes_profit_loss)/len(changes_profit_loss),2))
print ("Greatest Increase in Profits: ", greatest_increase_date, "$", round(greatest_increase_profit))
print ("Greatest Decrease in Profits: ", greatest_decrease_date, "$", round(greatest_decrease_profit))

#Print the output (to text file)
output_file = os.path.join('.', 'analysis', 'budget_data.txt')
with open(output_file, "w") as file:
    file.write("Total Months: {total_months} \n")
    file.write("-------------------------\n")
    file.write(f"Total Profit/Losses:: {total_profit_losses}\n")
    file.write("-------------------------\n")
    file.write(f" Average Changes {round(math.fsum(changes_profit_loss)/len(changes_profit_loss),2)} \n")
    file.write("-------------------------\n")
    file.write(f"Greatest Increase in profits: {greatest_increase_date} {greatest_increase_profit} \n")
    file.write("-------------------------\n")
    file.write(f"Greatest Decrease in profits: {greatest_decrease_date} {greatest_decrease_profit} \n")

# Print a message to indicate the successful export of the results
print("Budget Data:", output_file)
