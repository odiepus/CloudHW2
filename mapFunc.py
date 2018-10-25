import csv
import sys


# i is for testing 
i = 0

#Dictionary to contain a tuple for a key and an int for the value
#the tuple will be the crimetype and the month number in string 
#the value will be the count of occurences of the key
entries = {}

#get file name for input file to use
#not sure if we need to use a looping std reader for 
#multiple files
for line in sys.stdin:
        csv_f = open(line.rstrip(), 'r')
        #using csv module we will create our dictionary and count 
        #the number of occurances while iterating thru the rows.
        reader = csv.DictReader(csv_f)
        for row in reader:
            info = () #temp tuple to hold our key 
            info = (row['Crime Type'], row['Date'][0:2])
        
            #if the key is not already in the dictionary then add it and give it a count of 1
            #else increment the count by one
            if info not in entries:
                entries[info] = 1
            else:
                entries[info] += 1
            
            #code below is for testing only
            #laptop takes too long to process all entries 
            #for all files
            #comment it out when out of testing
#            i = i + 1
#            if(i > 200):
#                break

#this part will print out the keys and count of each key
#from here it goes to reduce
for key,count in entries.items():
    print key, "\t", count

