#Dependencies
import csv

#Files to load and output
file_to_load = "budget_data.csv"
file_to_output = "analysis.txt"

#Track various revenue parameters
total_months = 0
initial_profit = 0
monthly_changes = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999999]
total_Profit_Losses= 0



#Read the csv and convert it into a list of dictionaries
with open (file_to_load) as Profit/Losses_data:
    reader = csv.DictReader(Profit/Losses_data)

    for row in reader:
        # Track the totals
        total_months = total_months + 1
        total_Profit_Losses = total_Profit_Losses + int(row["Profit/Losses"])

        # Track the changes in Profit/Losses
        profit_change = int(row["Profit/Losses"]) - initial_profit
        initial_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        monthly_changes = monthly_changes = [row["Date"]]
        
