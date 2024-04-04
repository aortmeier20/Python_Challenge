import csv
file_path = "PyBank/Resources/budget_data.csv"

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
