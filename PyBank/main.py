import csv

total_months = 0
total_profit = 0
profit_change = 0
previous_profit = 0
profit_list = []
profit_average = 0

with open('Resources/budget_data.csv') as csvfile:
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
        
    profit_average = "{0:.2f}".format(sum(profit_list)/len(profit_list))


    #print(profit_average)

    print(f'''    Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${profit_average}
Greatest Increase in Profits: 
Greatest Decrease in Profits:     ''')