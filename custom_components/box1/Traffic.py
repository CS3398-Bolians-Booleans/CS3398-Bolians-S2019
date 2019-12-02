# 2019 Nov
# Author Sherwin Massoudian

# Usage:
# Traffic.getTraffic()

# Gets current travel time - average
# example: 
# 410

import random

class Traffic: 
    response = { "destination_addresses" : [ "San Marcos, TX, USA" ], "origin_addresses" : [ "Austin, TX, USA" ], "rows" : [ { "elements" : [ { "distance" : { "text" : "40 mi", "value" : 64373.8 }, "duration" : { "text" : "0 hours 45 mins", "value" : 2700 }, "status" : "OK" } ] } ], "status" : "OK" }
	
	
    # This method returns traffic time in seconds
    def getTraffic(self, homeAddress, SchoolAddress): 
        
		# Get travel time from payload
		rowArr = self.response['rows']
        rows = rowArr[0]
        elementArr = rows['elements']
        elements = elementArr[0]
        duration = elements['duration']
        currentTravelTime = duration['value']
		
		# Backup
		travelTime = random.randrange(2500, 3100)
        averageTime = self.getAvg();
        
        return travelTime - averageTime
    
	# This method returns the average traffic time
    def getAvg(self): 
        SanMarcos2Austin = 2420
        return SanMarcos2Austin
	
	# Method to print the traffic time to file
	# def printTime(self):
        # Output to a text file
        # file = open("trafficTime.txt","w")
        # file.write(str(Austin.getTime()))
        # file.close()

# Sample usage
Austin = Traffic()
print ("Expected time in traffic:", Austin.getTraffic(),"seconds")
