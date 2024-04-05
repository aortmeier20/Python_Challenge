#S


import csv
file_path = "PyBank/Resources/budget_data.csv"



#create variables
total_months = 0
sum_balance = 0
changes = []
average_change = 0
total_change = 0
current_profit_loss = 0
previous_profit_loss = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

#open the file
with open(file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    next(csv_file) #skips a row in the file ( first row =header row_)
    for row in csv_file: 
        #add to total months
        total_months += 1
        #set current profit loss for change
        current_profit_loss = int(row[1])
        if total_months >= 0:
        #define columns
            Date = row[0]
            profit_loss = row[1]
        #calculate net total
            sum_balance += int(profit_loss)
        #calculate change
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            total_change += change
            previous_profit_loss = current_profit_loss
        #calculate greatest increase
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = Date
        #calculate greatest decrease
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = Date
    average_change = total_change/len(changes)



# print to terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${sum_balance}')
print(f'Average Change: ${round(average_change, 2)}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')


#print the results to file
out_file_path = "PyBank/analysis/financial_analysis_results.txt"
with open(out_file_path, 'w') as file_out:
    file_out.write('Financial Analysis\n')
    file_out.write('----------------------------\n')
    file_out.write(f'Total Months: {total_months}\n')
    file_out.write(f'Total: ${sum_balance}\n')
    file_out.write(f'Average Change: ${round(average_change, 2)}\n')
    file_out.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    file_out.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')

#E
