import sys
#dict to contain the tuple(key) and the 
#sum of all counts(value)
entries = {}

#for each entry received
for line in sys.stdin:
    #strip the entry of added \n's etc

    print line
    line = line.strip()

    #split the line into key and val(count)
    key, count = line.split("\t", 1)
   
    #check if key is in the dict 
    if key not in entries:
        #if key not in dict then add it and set the count
        entries[key] = count
    else: #else pull up the entry and add the count to the value it has already
        entries[key] += count

#print each entry and its full count 
for key,count in entries.items():
    print key, "\t", count


