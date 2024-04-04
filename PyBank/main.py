import csv
file_path = "PyBank/Resources/budget_data.csv"

#The total number of months included in the dataset - Done

#The net total amount of "Profit/Losses" over the entire period - Done

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period





total_months = 0
sum_balance = 0

#open the file
with open(file_path) as text:
    csv_file = csv.reader(text)
    next(csv_file) #skips a row in the file ( first row =header row_)
    for row in csv_file:
        
        if total_months >= 0:
            Date = row[0]
            profit_loss = row[1]
            sum_balance += int(profit_loss)
        total_months = total_months + 1

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: {sum_balance}')


#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)