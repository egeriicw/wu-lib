import requests
import json
import sys
import csv

monthdays = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}

## Set parameters for GET request
#parameters = {'key1' : 'value1', 'key2' : 'value2'}

class WeatherData:

    def __init__(self, line):
        self.month = ""
        self.day = ""
        self.year = ""
        
        # Weather Data
        self.sourceFlag = ""

        self.setWeatherData(line)

    def setDate(self, line):
        self.sourceFlag = line[27]

    def setWeatherData(self, line):
        self.month = line[20:21] 
        self.day = line[22:23]
        self.year = line[16:19]

    def getWeatherData(self):
        return self.month, self.day, self.year

    def printWeatherData(self):
        print "Date: ", self.month + "/" + self.day + "/" + self.year
            
        
    def throttle(self):
        print "Throttling..."
        
class WeatherStation:
    def __init__(self):
        self.stationName = ""
        self.stationUSAFIdentifier = ""
        self.stationWBANCode = ""
        
        self.latitudeAngular = ""
        self.longitudeAngular = ""
        
        self.latitudeDegrees = ""
        self.latitudeHours = ""
        self.latitudeMin = ""
        self.latitudeSec = ""

        self.longitudeDegrees = ""
        self.longitudeHours = ""
        self.longitudeMin = ""
        self.longitudeSec = ""

    def getWeatherStation(self):
        print "Station Name: ", self.stationName
        print "Station USAF Identifier: ", self.stationUSAFIdentifier
        print "Station WBAN Code: ", self.stationWBANCode
        
    def setWeatherStation(self, line):
        # TODO
        print "...setWeatherStation()..."
        self.stationName = line[4:10]
        self.stationUSAFIdentifier = line[10:15]
        self.stationWBANCode = line[51:55]

class Weather:
    def __init__(self):
        self.station = WeatherStation()
        self.data = []
        self.setRemoteWUWeather("7d0d04e83a80b403")

    def getData(self):
        print "...getData()..."
        self.station.getWeatherStation()
        for data in self.data:
            data.printWeatherData()

    def toJSON(self):
        print "...toJSON..."

    def setLocalNOAAWeather(self, filename):
        # TODO
        setStation = True
        print "..setLocalNOAAWeather()..."
        with open('../data/input/' + filename, 'rb') as infile:
            lines = infile.read()
            
            for line in lines:
                
                print "Line: ", line
                if setStation == True:
                    self.station.setWeatherStation(line)
                    setStation = False
                else:
                    self.data.append(WeatherData(line))
            self.station.getWeatherStation()
            print "Data: ", self.data
        
    def setRemoteNOAAWeather(self):
        # TODO
        print "...setRemoteNOAAWeather()..."
  
    def setLocalWUWeather(self):
        # TODO
        print "...setLocalWUWeather()..."

    def setRemoteWUWeather(self, authkey=None):
        # TODO
        if authkey != "":
            print "...setRemoteWUWeather()..."
        else:
            print "Weather Underground Authentication Key Required."


def main(arg):
    temp_data = []
    authkey = '7d0d04e83a80b403' 
    tdata = {}
    
    weather = Weather()
    weather.setLocalNOAAWeather('724050-13743-2011')
    weather.getData()

    """
    print arg

    mo = '10'
    dy = '18'
    yr = '2010'

    # Save JSON object as text in a list
    temp_data = getWUTempHistory(authkey, '10', '18', '2010').text

    datetext = str(mo + "/" + dy + "/" + yr)
    print datetext

    tdata.update({datetext:temp_data})
    


    # json.loads converts a string to a json object.
    # json.dumps "prettifies" the json object into a useable form

    #test = json.dumps(json.loads(tdata['10/18/2010']), ensure_ascii=True)

    #writeJSON(test)

    #testy = readJSON()

    #print json.dumps(json.loads(testy))

    #for m, d in monthdays.iteritems():
    #    print "Month: ", m, " Days: ", d
    
    #return 0

#def getWUTempHistory(key, mo, dy, yr):
    # Requests data from Weather Underground site
    # Returns json object

#    url = 'http://api.wunderground.com/api/' + key + '/history_'+ yr + mo + dy + '/q/DCA.json'

    # Returns a json object
#    r = requests.get(url)

#    return r

def writeCSV(data):
    with open('../data/output/tempcsv.csv', 'wb') as outfile:
        writer = csv.writer(outfile, delimiter='\n')
        writer.writerow(data)

def writeJSON(data):
    with open('../data/output/tempdata.json', 'wb') as outfile:
        outfile.write(data)

def readJSON():
    with open('../data/output/tempdata.json', 'r') as infile:
        data = infile.read()
        return 
    """
if __name__ == "__main__":
    sys.exit(not main(sys.argv))
