import csv
file_path = "PyBank/Resources/budget_data.csv"

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period





row_number = -1
sum_balance = -1
with open(file_path) as text:
    csv_file = csv.reader(text)

    for row in csv_file:
        
        if row_number > -1:
            Date = row[0]
            profit_loss = row[1]
            sum_balance += int(profit_loss)
        row_number = row_number + 1
print(row_number)
print(sum_balance)


#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)