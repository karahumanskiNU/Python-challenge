# import os and csv
import os, csv

# link CSV file
csvfile =os.path.join("Resources","election_data.csv")

votes =[]
candidate =[]
#make with block to open csv
with open(csvfile, "r") as election_text:
    #make a csvfile reader 
    election_reader = csv.reader(election_text)
    #skip the header
    header = next(election_reader)

    # for loop to loop through all data and add info to lists
    for row in election_reader:
       votes.append(row)
       total_votes = len(votes)
       candidate.append(row[2])

#Count the votes for each canadite in the canadite list    
khan_votes = candidate.count('Khan') 
li_votes = candidate.count('Li')
otooley_votes = candidate.count("O'Tooley") 
correy_votes = candidate.count('Correy')

#Calculate the percent of total votes each candidate recieved
khan_percent = round(khan_votes/total_votes*100)
li_percent = round(li_votes/total_votes*100)
otooley_percent = round(otooley_votes/total_votes*100)
correy_percent = round(correy_votes/total_votes*100)

#Make dictionary with canidate as key and amount of votes as value
vote_dict = {"Li": li_votes, "Khan":khan_votes, "O'Tooley":otooley_votes, "Correy":correy_votes}
winner = max(vote_dict, key=vote_dict.get)

#Make a new list which lists each candidates name once
candidate_new = list(set(candidate))


#Print results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"{candidate_new[0]}: {otooley_percent:.3f}% ({otooley_votes})")
print(f"{candidate_new[1]}: {khan_percent:.3f}% ({khan_votes})")
print(f"{candidate_new[2]}: {li_percent:.3f}% ({li_votes})")
print(f"{candidate_new[3]}: {correy_percent:.3f}% ({correy_votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#link output file
output_file = os.path.join("analysis","output.txt")
#with block to open output file for writing and enter info
with open(output_file, "w", newline= "") as csvfile:
   csvwriter = csv.writer(csvfile)
   csvwriter.writerow(["Election Results"]) 
   csvwriter.writerow(["----------------------------"])
   csvwriter.writerow([f"Total Votes: {total_votes}"])
   csvwriter.writerow(["----------------------------"])
   csvwriter.writerow([f"{candidate_new[0]}: {otooley_percent:.3f}% ({otooley_votes})"])
   csvwriter.writerow([f"{candidate_new[1]}: {khan_percent:.3f}% ({khan_votes})"])
   csvwriter.writerow([f"{candidate_new[2]}: {li_percent:.3f}% ({li_votes})"])
   csvwriter.writerow([f"{candidate_new[3]}: {correy_percent:.3f}% ({correy_votes})"])
   csvwriter.writerow(["----------------------------"])
   csvwriter.writerow([f"Winner: {winner}"])
   csvwriter.writerow(["----------------------------"])