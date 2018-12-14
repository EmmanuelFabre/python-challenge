#allows us to create file paths across operating systems
import os
#module for reading csv file
import csv

import collections
#encode path
from pathlib import Path

path = Path('/Users/emmanuelfabre/Desktop/pythonstuff/Assignment3/03_python_homework_Instructions_PyPoll_Resources_election_data.csv')

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

election(path)