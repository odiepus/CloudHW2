import re
import sys

#dict to contain the tuple(key) and the 
#sum of all counts(value)
entries = {}
crimeTypes = {}
monthString = ["Jan", "Feb", "Mar", "Apr", "May",  "Jun",   "Jul",  "Aug",  "Sep",   "Oct",   "Nov",   "Dec"]
columnHead = "Crime Type"
#for each entry received
for line in sys.stdin:
    #strip the entry of added \n's etc

    #print line
    line = line.strip()

    #split the line into key and val(count)
    key, count = line.split("\t", 1)
   
    #check if key is in the dict 
    if key not in entries:
        #if key not in dict then add it and set the count
        entries[key] = int(count)
    else: #else pull up the entry and add the count to the value it has already
        entries[key] += int(count)


#extract the crime type its month and count and put in dictionary
#each crime type will have a list of the number of said crime commited.
#the list index will be the month in which the count of said crime was commited.
for key, count in entries.items():
    months = [0 for x in range(13)]
    keyStr = re.sub("[()']", '', key)

    crimeNomenclature, month = keyStr.split(",", 1)

    if crimeNomenclature not in crimeTypes:
        months[int(month)] = count
        crimeTypes[crimeNomenclature] = months
    else:
        crimeTypes[crimeNomenclature][int(month)] = count

#print the header for the table
print "{:<40}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{}".format(columnHead, monthString[0],monthString[1],monthString[2],monthString[3],monthString[4],monthString[5],monthString[6],monthString[7],monthString[8],monthString[9],monthString[10],monthString[11]) 

#print each crime type and the monthly count
for key, value in crimeTypes.items():
    print "{:<40}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{:<6}{}".format(key,value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10],value[11],value[12],)
