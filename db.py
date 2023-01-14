from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

startDate = date.today() # date is in "yyyy-mm-dd"

# prompt user for latest possible meeting date
endDate = date(2023, 12, 30)  # placeholder

# init db
db = {}
availabilityNum = {}

# populate db with days and hour intervals
for single_date in daterange(startDate, endDate):
    hourIntervalDict = {}
    for hourInterval in range(0, 24):
        hourIntervalDict[hourInterval] = []
        db[single_date] = hourIntervalDict

def fillAvailability(name, date, startTime, endTime):
    for time in range(startTime, endTime + 1):
        db[date][time].append(name)
        if str(date) + str(time) not in availabilityNum:
            availabilityNum[str(date) + str(time)] = 0
        availabilityNum[str(date) + str(time)] += 1
        

fillAvailability("kelvin", startDate, 0, 23)
fillAvailability("kelvin", startDate, 0, 23)

sortHighestAvail = dict(sorted(availabilityNum.items(), key= lambda item: item[1]))

# print(sortHighestAvail) # shows list of date-times where most people are available
# print(availabilityNum["2023-01-1423"]) # shows number of people avail at a particular date-time




