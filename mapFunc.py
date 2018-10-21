import csv

# i is for testing 
i = 0

#get file name for input file to use
#not sure if we need to use a looping std reader for 
#multiple files
csv_f = open(raw_input()) 

#Dictionary to contain a tuple for a key and an int for the value
#the tuple will be the crimetype and the month number in string 
#the value will be the count of occurences of the key
entries = {}

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
    #comment it out when out of testing
    i = i + 1
    if(i > 100):
        print i
        break

#this part will print out the keys and count of each key
#from here it goes to reduce
for key,count in entries.items():
    print key, "\t", count

csv_f.close()
