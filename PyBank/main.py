import os
import csv

data_path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

months = []
ProfitLosses =[]

with open(data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        ProfitLosses.append(int(row[1]))
    
    total_months = len(months)
        
total_ProfitLosses = 0
greatest_increase = 0
greatest_decrease = 0
Pre_ProfitLoss = ProfitLosses[0]

for r in range(len(ProfitLosses)): 
    total_ProfitLosses += ProfitLosses[r]
    ProfitLosses_change = ProfitLosses[r] - Pre_ProfitLoss
    Pre_ProfitLoss = ProfitLosses[r]
    
    if(ProfitLosses_change > greatest_increase):
        greatest_increase = ProfitLosses_change
        greatest_increase_date = months[r]

    if(ProfitLosses_change < greatest_decrease):
        greatest_decrease = ProfitLosses_change
        greatest_decrease_date = months[r]
            
total_change = ProfitLosses[len(ProfitLosses)-1] - ProfitLosses[0]
average_change = round(total_change/(total_months-1), 2)
    
    
output_path = os.path.join("..", "PyBank", "Results.txt")
with open(output_path, "w") as textfile:
    textfile.writelines("Financial Analysis\n")
    textfile.writelines("-----------------------------\n")
    textfile.writelines("Total Months: " + str(total_months) + "\n")
    textfile.writelines("Total " + str(total_ProfitLosses) + "\n")
    textfile.writelines("Average Change: " + str(average_change) + "\n")
    textfile.writelines("Greatest Increase in Profits: " + greatest_increase_date + " $ " + str(greatest_increase) + "\n")
    textfile.writelines("Greatest Decrease in Profits: " + greatest_decrease_date + " $ " + str(greatest_decrease) + "\n")
    
with open(output_path, "r") as readfile:
    print(readfile.read())
        