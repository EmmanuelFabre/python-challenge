#allows us to create file paths across operating systems
import os
#module for reading csv file
import csv

import collections

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

#########################


path_1 = Path('/Users/emmanuelfabre/Desktop/pythonstuff/Assignment3/03_python_homework_Instructions_PyPoll_Resources_election_data.csv')

def election(electionCsv):
	with open(electionCsv, "r") as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ',')
		next(csvreader)

		# declaring list
		votes = []	

		for row in csvreader:
			votes.append(str(row[2]))	# add to list

		total_votes = len(votes)		# length of list
	
		counter=collections.Counter(votes)
		#print(counter)					# debug statement

		#set variables using collections library
		Khan = counter['Khan']
		Correy = counter['Correy']
		Li = counter['Li']
		OTooley = counter['O\'Tooley']

		# percentage of votes per candidate, rounded to one decimal place
		Khan_percentage = round((Khan/total_votes)* 100)
		Correy_percentage = round((Correy/total_votes)* 100)
		Li_percentage = round((Li/total_votes)* 100)
		OTooley_percentage = round((OTooley/total_votes)* 100)


		with open("elec_results.txt", "w") as text_file:

			# print to terminal
			print("Election Results")
			print("_______________________")
			print("Total Votes: " + str(total_votes))
			print("___________________________")
			print("Khan: " + str(Khan_percentage) + "%" + " " + "(" + str(Khan) + ")")
			print("Correy: " + str(Correy_percentage) + "%" + " " + "(" + str(Correy) + ")")
			print("Li: " + str(Li_percentage) + "%" + " " + "(" + str(Li) + ")")
			print("O'Tooley: " + str(OTooley_percentage) + "%" + " " + "(" + str(OTooley) + ")")

			# print to txt file 'elec_results.txt'
			print("Election Results", file= text_file)
			print("_______________________", file= text_file)
			print("Total Votes: " + str(total_votes), file= text_file)
			print("___________________________", file= text_file)
			print("Khan: " + str(Khan_percentage) + "%" + " " + "(" + str(Khan) + ")", file= text_file)
			print("Correy: " + str(Correy_percentage) + "%" + " " + "(" + str(Correy) + ")", file= text_file)
			print("Li: " + str(Li_percentage) + "%" + " " + "(" + str(Li) + ")", file= text_file)
			print("O'Tooley: " + str(OTooley_percentage) + "%" + " " + "(" + str(OTooley) + ")", file= text_file)

election(path_1)