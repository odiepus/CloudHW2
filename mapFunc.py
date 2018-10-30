import csv

# i is for testing 
i = 0

#Dictionary to contain a tuple for a key and an int for the value
#the tuple will be the crimetype and the month number in string 
#the value will be the count of occurences of the key
entries = {}

#get file name for input file to use
#not sure if we need to use a looping std reader for 
#multiple files
with  open('./files.txt', 'r') as fp:

    for line in fp:
	csv_f = open(line.rstrip(), 'r')
	#using csv module we will create our dictionary and count 
	#the number of occurances while iterating thru the rows.
	reader = csv.DictReader(csv_f)

	for row in reader:

	    info = () #temp tuple to hold our key 
            crimeType = str(row['Crime Type'])
            month = str(row['Date'][0:2])
	    info = (crimeType, month)
            
            #print out the key and a count of 1 for reducer to take.
            #the reducer will be the one adding up all the occurances 
            #of the same crimetype and month
            print info, "\t", 1 
            

fp.close()
