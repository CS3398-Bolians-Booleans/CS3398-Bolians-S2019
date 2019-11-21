# USAGE
# Traffic.getTime()


class Traffic: 
    averageTime = 2150
    currentTime = 2520
	googlePayload = '{ "destination_addresses" : [ "New York, NY, USA" ], "origin_addresses" : [ "Washington, DC, USA" ], "rows" : [ { "elements" : [ { "distance" : { "text" : "225 mi", "value" : 361715 }, "duration" : { "text" : "3 hours 49 mins", "value" : 13725 }, "status" : "OK" } ] } ], "status" : "OK" }'

	
    # This method returns traffic time in seconds
    def getTime(self): 
        # TODO: deserialize payload => get travel time (rows.elements.duration.value)





        # Output to a text file
        # file = open("trafficTime.txt","w")
        # file.write(str(Austin.getTime()))
        # file.close()
        return self.currentTime - self.averageTime









Austin = Traffic();
print ("Expected time in traffic (seconds) ", Austin.getTime())

