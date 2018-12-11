
#allows us to create file paths across operating systems
import os

#module for reading csv file
import csv

#encode path
from pathlib import Path

#pandas
#import pandas as pd

path = Path('/Users/emmanuelfabre/Desktop/03_python_homework_Instructions_PyBank_Resources_budget_data.csv')

#function gettotals
def get_months(BudgetCsv):
	with open(BudgetCsv, "r") as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ',')
		next(csvreader)
		#make list out of rows
		row_count = list(csvreader)	
		#count rows in csv
		months = len(row_count)
	
		print("The total number of months included is: " + str(months))



def sum_pnl(BudgetCsv):
	with open(BudgetCsv, "r") as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ',')
		next(csvreader)

		pnl_count = 0
		for row in csvreader:
			pnl_count += int(row[1])	#neg nums seen as string unless converted to int
		print("The total net amount of Profit/Losses is: " + str(pnl_count))			
									#prints out pnl col. If you indent it once more..
									#it's in the for loop, and will print after each..
									#addition. 



get_months(path)
sum_pnl(path)





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



