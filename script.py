import csv
import random
import webbrowser
import os
import numpy as np

# other functions
def numRows(data):
	for j in range(1,4):
		if len(data[j])==0:
			return(j)

# read the input file

print('Reading file sinfo.csv')
csvfile = open('sinfo.csv','rb')
csvreader = csv.reader(csvfile)
file = list(csvreader)

# display statistics
finished = [0.,0.,0.]
total = len(file)
for i in range(1,len(file)):
	for j in range(1,4):
		if len(file[i][j])>0:
			finished[j-1] = finished[j-1]+1
finished = np.divide(np.round(np.divide(finished, total) * 1000),10)
print('Completed: ' + str(finished[0]) + '% ' + str(finished[1]) + '% ' + str(finished[2]) + '%')
stop = raw_input("Waiting: [enter]")

# file[1:] are all the rows
order = range(1,len(file))
random.shuffle(order)
# pick a random row
for i in range(0,len(order)):
	row = order[i]
	# check how many entires it has
	curEnt = numRows(file[row]) 
	if curEnt < 2:
		# if less than 2, run the row
		print('Check participant #' + file[row][0])
		webbrowser.open('file://'+os.getcwd()+'/slow_gifs/'+file[row][0]+'.gif')
		quality = raw_input("Quality? [-1/0/1/e/c] ")
		if quality=='e':
			break
		if quality=='c':
			print('Current comment: ' + file[row][4])
			comment = raw_input("Comment: ")
			if len(comment)>0:
				file[row][4] = comment
			quality = raw_input("Quality? [-1/0/1/e] ")
		if quality=='e':
			break
		file[row][curEnt] = quality

print('Writing file sinfo.csv')
outfile = open('sinfo.csv','wb')
csvwriter = csv.writer(outfile)
csvwriter.writerows(file)
print('Ending')