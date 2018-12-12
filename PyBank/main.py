
#allows us to create file paths across operating systems
import os

#module for reading csv file
import csv

#encode path
from pathlib import Path


path = Path('/Users/emmanuelfabre/Desktop/03_python_homework_Instructions_PyBank_Resources_budget_data.csv')


########################
#The average change in "Profit/Losses" between months over the entire period

#change in pnl function
def analysis(BudgetCsv):

	with open(BudgetCsv, "r") as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ',')
		next(csvreader)

		pnl = []
		pnl_change = []
		date = []
		avg_pnl_change = 0
		max_pnl_change = 0
		min_pnl_change = 0

		max_pnl_change_date = 0
		min_pnl_change_date = 0
		for row in csvreader:
			pnl.append(int(row[1]))
			date.append(row[0])
			#print(pnl)						#debug statement

		for i in range(1, len(pnl)):						
			pnl_change.append(pnl[i] - pnl[i - 1])
			#print(pnl[i])					#debug statement
			#print("The sum of pnl change is " + str(sum(pnl_change)))	#debug statement

		max_pnl_change += max(pnl_change)
		min_pnl_change += min(pnl_change)
		max_pnl_change_date = str(date[pnl_change.index(max(pnl_change))])
		min_pnl_change_date = str(date[pnl_change.index(min(pnl_change))])
		avg_pnl_change += sum(pnl_change)/len(pnl_change)

		print("The total number of months included is: " + str(len(pnl)))
		print("The total net amount of Profit/Losses is: " + str(sum(pnl)))
		print("The average change in 'Profit/Losses' between months is: $" + str(round(avg_pnl_change, 2)))
		print("The greatest increase in profits is: " + str(max_pnl_change_date) + " $" + str(max_pnl_change))
		print("The greatest decrease in profits is: " + str(min_pnl_change_date) + " $" + str(min_pnl_change))

analysis(path)

#############################
#Code below uses Pandas. 
#csvfile = "/Users/emmanuelfabre/Desktop/03_python_homework_Instructions_PyBank_Resources_budget_data.csv"
#
#csvfile_pd = pd.read_csv(csvfile)
#
#count_month = csvfile_pd.shape[0]
#print("The total count of months is: " + str(count_month))



#to check if correct file, use--csvfile_pd.head(). 
#total for single col
#pl_total = csvfile_pd["Profit/Losses"].sum
#print("The total net amount of Profit/Losses is: " + str(pl_total))


#Created develop branch (git checkout -b develop). Everything now pushes to develop
#branch. Eventually do pull request to merge with master.	



