 #import dependencies
import os
import csv

#define csv path
csvpath = os.path.join('Resources', 'budgetdata.csv')

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # as the csv file contains a header, read the header row first
    csv_header = next(csvreader)   
#store lists
    profitlosses = []
    changes = []
    months = []
#set initial variables to zero
    net_total = 0
    row_count = 0
#loop through data
    for row in csv.reader(csvfile):
#append the profit/losses list
        profitlosses.append(row[1])
#append the months list
        months.append(row[0])
#determine the net total of profit/losses over the entire period
        net_total += int(row[1])
#determine row count
        row_count += 1
#determine number of months
        month_count = len(months)
#zip function used to determine initial and subsequent value in profit/losses column
    for initial_value, next_value in zip(profitlosses, profitlosses[1:]):
#calculate the changes
        changes.append(int(initial_value) - int(next_value))
#calculate average change
        total_change = sum(changes)
        average_change = -(total_change / len(changes))
#determine greatest increase or decrease in profits over the entire period
        greatest_increase = -(min(changes))
        greatest_decrease = -(max(changes))

#print data
print("Financial Analysis")
print("------------------------")
print(f"Total months: {month_count}")
print(f"Total volume: {net_total}")
print(f"Average monthly change: {average_change}")
print(f"Greatest increase: {greatest_increase}")
print(f"Greatest decrease: {greatest_decrease}")

# determine file path to write to
output_file = os.path.join('Analysis', 'FinancialAnalysis.text')

# write file
with open(output_file, 'w',) as txtfile:

# data written
    txtfile.write(f"FinancialAnalysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total months: {month_count}\n")
    txtfile.write(f"Net total: {net_total}\n")
    txtfile.write(f"Average Monthly Change: {average_change}\n")
    txtfile.write(f"Greatest Increase: {greatest_increase}\n")
    txtfile.write(f"Greatest Decrease: {greatest_decrease}\n")
    txtfile.write(f"---------------------------\n")