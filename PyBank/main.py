#add os and csv
import os, csv

# link CSV file
csvfile = os.path.join("Resources", "budget_data.csv")

profit_change = 0
months= []
profit = []

# make with block to open the csv file
with open(csvfile, "r") as budgettext:
    #make CSV reader
    budgetreader = csv.reader(budgettext)
    #skip the header
    header = next(budgetreader)
    #read first row needed for average change
    row_1=next(budgetreader) 
    #add row 1 to lists
    profit.append(row_1[1])
    months.append(row_1[0])

    #for loop to go through rows of CSVfile
    for row in budgetreader:
       
        # add values to correct lists
       months.append(row[0])
       profit.append(row[1])
       value = int(row_1[1])

       #Find change 
       profit_change= int(row[1]) -value 

    #find total number of months  in month list
    num_months = len(months)
    
    #find total amount of the values in profit   
    profit = [int(num) for num in profit]
    total_amount = sum(profit)
    

#Calculate average change
aver_change =profit_change/num_months
#find greatest increase and the index of the greatest increase to search for the corresponding date
great_increase = max(profit)
great_index = (profit.index(max(profit)))

#determine month of greatest increase
great_inc_month = months[great_index]


#find greatest decrease and the index of the greatest decrease to search for the corresponding date
great_decrease = min(profit)
great_dec_index = (profit.index(min(profit)))
great_dec_month = months[great_dec_index]


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: $ {total_amount}")
print(f"Average Change: ${aver_change:.2f}")
print(f"Greatest Increase in Profits: {great_inc_month} (${great_increase})")
print(f"Greatest Decrease in Profits: {great_dec_month} (${great_decrease})")

#link output file
output_file = os.path.join("analysis","output.txt")
#with block to open output file for writing and enter info
with open(output_file, "w", newline= "") as csvfile:
   csvwriter = csv.writer(csvfile)
   csvwriter.writerow(["Financial Analysis"])
   csvwriter.writerow(["----------------------------"])
   csvwriter.writerow([f"Total Months: {num_months}"])
   csvwriter.writerow([f"Total: $ {total_amount}"])
   csvwriter.writerow([f"Average Change: ${aver_change:.2f}"]) 
   csvwriter.writerow([f"Greatest Increase in Profits: {great_inc_month} (${great_increase})"])
   csvwriter.writerow([f"Greatest Decrease in Profits: {great_dec_month} (${great_decrease})"])