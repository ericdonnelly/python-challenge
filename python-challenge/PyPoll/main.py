 #import dependencies
import os
import csv

#define csv path
csvpath = os.path.join('Resources', 'electiondata.csv')

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # as the csv file contains a header, read the header row first
    csv_header = next(csvreader)   
#store lists
    voter_id_list = []
    county_list = []
    name_list = []
    khan_list = []
    correy_list = []
    li_list =[]
    otooley_list = []
#set initial variables to zero
    row_count = 0
#loop through data
    for row in csv.reader(csvfile):
#append the voter id list
        voter_id_list.append(row[0])
#append the county list
        county_list.append(row[1])
#append the candidate list
        name_list.append(row[2])
#determine number of rows
        row_count += 1
#append candidate votes to their corresponding list
        if (row[2] == "Khan"):
            khan_list.append(row[2])
        elif (row[2] == "Correy"):
            correy_list.append(row[2])
        elif (row[2] == "Li"):
            li_list.append(row[2])
        else:
            otooley_list.append(row[2])

#define totals
vote_total = len(voter_id_list)
khan_total = len(khan_list)
correy_total = len(correy_list)
li_total = len(li_list)
otooley_total = len(otooley_list)

# calculate percentage of votes for each candidate
khan_percent = khan_total / vote_total
correy_percent = correy_total / vote_total
li_percent = li_total / vote_total
otooley_percent = otooley_total / vote_total

#determine winner
if khan_total > correy_total and li_total and otooley_total:
    winner = "Khan"
elif correy_total > khan_total and li_total and otooley_total:
    winner = "Correy"
elif li_total > khan_total and correy_total and otooley_total:
    winner = "Li"
else:
    winner = "O'Tooley"

# print data
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {vote_total}")
print(f"---------------------------")
print(f"Khan: {khan_percent:.3%}({khan_total})")
print(f"Correy: {correy_percent:.3%}({correy_total})")
print(f"Li: {li_percent:.3%}({li_total})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_total})")
print(f"---------------------------")
print(f"Winner: {winner}")
print(f"---------------------------")

# determine file path to write to
output_file = os.path.join('Analysis', 'ElectionResults.text')

# write file
with open(output_file, 'w',) as txtfile:

# data written
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {vote_total}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {khan_percent:.3%}({khan_total})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_total})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_total})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_total})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"---------------------------\n")