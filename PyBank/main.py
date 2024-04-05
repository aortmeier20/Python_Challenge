#S


import csv
file_path = "PyBank/Resources/budget_data.csv"

#The total number of months included in the dataset - Done

#The net total amount of "Profit/Losses" over the entire period - Done

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period




#create variables
total_months = 0
sum_balance = 0
changes = []
average_change = 0
total_change = 0
current_profit_loss = 0
previous_profit_loss = 0

#open the file
with open(file_path) as text:
    csv_file = csv.reader(text)
    next(csv_file) #skips a row in the file ( first row =header row_)
    for row in csv_file: 
        #add to total months
        total_months += 1
        current_profit_loss = int(row[1])
        if total_months >= 0:
            #set rows
            Date = row[0]
            profit_loss = row[1]
            #calculate net total
            sum_balance += int(profit_loss)
        #calculate change
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            total_change += change
            previous_profit_loss = current_profit_loss
    average_change = total_change/len(changes)
    #greatest increase and greatest decrease
    greatest_increase = max(changes)
    #greatest_increase_date = Date[changes.index(greatest_increase)]
    greatest_decrease = min(changes)
    #greatest_decrease_date = Date[changes.index(greatest_decrease)]


# print to terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: {sum_balance}')
print(f'Average Change: {average_change}')
print(f'Greatest Increase in Profits: ${greatest_increase}')
print(f'Greatest Decrease in Profits: ${greatest_decrease}')


#print the results to file
out_file_path = "PyBank/analysis/financial_analysis_results.txt"
with open(out_file_path, 'w') as file_out:
    file_out.write('Financial Analysis\n')
    file_out.write('----------------------------\n')
    file_out.write(f'Total Months: {total_months}\n')
    file_out.write(f'Total: {sum_balance}\n')
    file_out.write(f'Average Change: {average_change}\n')
    file_out.write(f'Greatest Increase in Profits: ${greatest_increase}\n')
    file_out.write(f'Greatest Decrease in Profits: ${greatest_decrease}\n')

#E
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)