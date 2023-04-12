import csv

total_months = 0
total_profit = 0
profit_change = 0
previous_profit = 0
profit_list = []
profit_average = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open('Resources/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:

        month = str(row[0])
        profit = int(row[1])

        total_months += 1
        total_profit += profit

        profit_change = profit - previous_profit
        previous_profit = profit
        if profit_change != profit:
            profit_list.append(profit_change)
        
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            greatest_increase_month = month
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_month = month
        
    profit_average = "{0:.2f}".format(sum(profit_list)/len(profit_list))

with open('analysis/analysis_output.txt', 'w') as file:
    file.write(f'''    Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${profit_average}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})''')

print(f'''    Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${profit_average}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})''')