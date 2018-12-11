
#allows us to create file paths across operating systems
import os

#module for reading csv file
import csv

#encode path
from pathlib import Path

#pandas
#import pandas as pd

path = Path('/Users/emmanuelfabre/Desktop/03_python_homework_Instructions_PyBank_Resources_budget_data.csv')


with open(path, newline='') as csvfile:
	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	print(csvreader)

		#Add function to print out file and see if it prints out correctly
	for row in csvreader:
		print(row)


BudgetDataCsv = os.path.join('/Users/emmanuelfabre/Desktop/03_python_homework_Instructions_PyBank_Resources_budget_data.csv')

#function gettotals
def getTotals(BudgetCsv):
	with open(BudgetCsv, "r") as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ",")
		next(csvreader)
		#make list out of rows
		row_count = list(csvreader)	
		#count rows in csv
		months = len(row_count)
	
	#TotalNet = sum(int(BudgetDataCsv[1]))	#or budgetdatacsv, budgetdata?
				#google sum(int) in csv col
		print(months)


getTotals(BudgetDataCsv)



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



