DOMAIN = 'box1'
from Tree import DecisionTree
import pandas as pd
from datetime import date
from datetime import datetime


def setup(hass, config):
    """Setup our skeleton component."""
    #States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('box1.box1', 'Works!')
    model = Tree.DecisionTree()
    name = DB.getmodelname() #STAVROS CHECK HERE

    today = date.today()
    today = today.strftime("%d%m%Y")

    if (name == null || today - DB.getTrainDay() >= 7):
         model.train_all('CSV_txt.txt')
    else:
        model.load(name) #STAVROS CHECK HERE

    def isHoliday(): #currently only recognizes december 25th as a holiday.
        day = date.today()
        day = day.strftime("%d%m")
        if (day == "2512"):
            return 1
        else:
            return 0

    # Listener to handle fired events
    def handle_event(event):
        today = date.today()
        today = today.strftime("%d%m%Y")
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        user = "user1"
        weekday =  today.weekday()
        holiday = isHoliday()
        location = getStatus("stavrosIphone") #Derik or Patrick please check. This should return a 1 or 0 (integers) if stavroses Iphone is connected
        if (location == 0):
			# getTraffic() returns the amount of above average seconds for the commute
            ETA = Traffic.getTraffic("homeAddress", "SchoolAddress") 
            current_time = current_time + ETA

        action = event.event_type + event.gata #this is merging two data types. I don't know if it is necessary to string parse them
        time,action = model.predict(user,action,today,current_time,location,holiday,weekday)
        schedual(action,time) #Derick, please put add your schedualling function. The action is already parsed correctly. Please spell check me too. Thanks.
        DB.save(user,action,today,current_time,location,holiday,weekday) #Stavros check here

    # Listen for when example_component_my_cool_event is fired
    hass.bus.listen('example_component_my_cool_event', handle_event)


    return True
