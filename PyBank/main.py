#allows us to create file paths across operating systems
import os
#module for reading csv file
import csv
#encode path
from pathlib import Path

path = Path('/Users/emmanuelfabre/Desktop/03_python_homework_Instructions_PyBank_Resources_budget_data.csv')

# analysis/PnL function
def analysis(BudgetCsv):

	with open(BudgetCsv, "r") as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ',')
		next(csvreader)

		# declaring variables (lists and ints)
		pnl = []
		pnl_change = []
		date = []
		avg_pnl_change = 0
		max_pnl_change = 0
		min_pnl_change = 0
		max_pnl_change_date = 0
		min_pnl_change_date = 0

		# adding values from each row to lists
		for row in csvreader:
			pnl.append(int(row[1]))
			date.append(row[0])
			#print(pnl)													# debug statement

		# for value in pnl list, add difference between current and previous value to pnl_change list
		for i in range(1, len(pnl)):						
			pnl_change.append(pnl[i] - pnl[i - 1])
			#print(pnl[i])												# debug statement
			#print("The sum of pnl change is " + str(sum(pnl_change)))	# debug statement

		max_pnl_change += max(pnl_change)										# max value in pnl_change list
		min_pnl_change += min(pnl_change)										# min value in pnl_change list
		max_pnl_change_date = str(date[pnl_change.index(max(pnl_change))])		# date of max value
		min_pnl_change_date = str(date[pnl_change.index(min(pnl_change))])		# date of min value
		avg_pnl_change += sum(pnl_change)/len(pnl_change)						# average change between months

		with open("Fin_Analysis.txt", "w") as text_file:

			print("Financial Analysis")
			print("_________________________________________________")
			print("Total Months: " + str(len(pnl)))
			print("Total: " + str(sum(pnl)))
			print("Average Change: $" + str(round(avg_pnl_change, 2)))
			print("Greatest Increase in Profits: " + str(max_pnl_change_date) + " $" + str(max_pnl_change))
			print("Greatest Decrease in Profits: " + str(min_pnl_change_date) + " $" + str(min_pnl_change))

			print("Financial Analysis", file= text_file)
			print("_________________________________________________", file= text_file)
			print("Total Months: " + str(len(pnl)), file= text_file)
			print("Total: " + str(sum(pnl)), file= text_file)
			print("Average Change: $" + str(round(avg_pnl_change, 2)), file= text_file)
			print("Greatest Increase in Profits: " + str(max_pnl_change_date) + " $" + str(max_pnl_change), file= text_file)
			print("Greatest Decrease in Profits: " + str(min_pnl_change_date) + " $" + str(min_pnl_change), file= text_file)

analysis(path)