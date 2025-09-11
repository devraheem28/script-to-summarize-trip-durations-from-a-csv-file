import csv
from datetime import datetime 
#ask the user for CSV name
filename=input("enter csv file name:")
durations=[] #list to store trip durations
with open(filename,"r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader: #go through each row in the file one by one
        start=row[0]
        end=row[1]
        start_time=datetime.strptime(start.strip(), "%Y-%m-%d %H:%M:%S")
        end_time=datetime.strptime(end.strip(), "%Y-%m-%d %H:%M:%S")
        #this will calculate trip duration in minutes
        duration=(end_time - start_time).total_seconds() / 60
        durations.append(duration) #store the trip duration in the list
#now calculate summary
total_trips=len(durations)
total_time=sum(durations)
average_time=total_time/total_trips if total_trips > 0 else 0
#now show results
print("Trip Summary")
print("Total trips:",total_trips)
print("Total time(minutes):",total_time)
print("Average trip time(minutes)",average_time)




