import requests
import json
import sys
import csv
import StringIO

class WeatherData:

    def __init__(self, line):
        print "WeatherData loaded."
        self.month = ""
        self.day = ""
        self.year = ""
        self.hour = ""
        self.minute = ""
        
        # Temperature Data

        # Dry bulb air temperature
        self.tempDBRAW = ""
        self.tempDBF = ""
        self.tempDBC = ""

        # Wet bulb air temperature
        self.tempWBRAW = ""
        self.tempWBF = ""
        self.tempWBC = ""

        self.setWeatherData(line)

    def setDate(self, line):
        self.sourceFlag = line[27]

    def setWeatherData(self, line):
        # Set Month, Day, Year
        # File format: YYYYMMDD
        self.month = line[19:21] 
        self.day = line[21:23]
        self.year = line[15:19]
        
        # Set Hour, Minute
        # File format: HHMM in 24 hour clock
        self.hour = line[23:25]
        self.minute = line[25:27]

        # Set temperature data
        self.tempDBRAW = line[87:92]
        self.tempWBRAW = line[93:98]

        self.tempDBC = float(self.tempDBRAW[1:])/10.
        self.tempWBC = float(self.tempWBRAW[1:])/10.

        if self.tempDBRAW[0] == '-':
            self.tempDBC = self.tempDBC * -1.
        if self.tempWBRAW[0] == '-':
            self.tempWBC = self.tempWBC * -1.

        self.tempDBF = self.CtoF(self.tempDBC)
        self.tempWBF = self.CtoF(self.tempWBC)

    # Temperature Conversion Functions
    def FtoC(self, data):
        return (data - 32) / 1.8

    def CtoF(self, data):
        return (data * (9/5)) + 32
    
    def CtoK(self, data):
        # TODO
        return 0

    def KtoC(self, data):
        # TODO
        return 0

    def FtoR(self, data):
        # TODO
        return 0

    def RtoF(self, data):
        # TODO
        return 0

    def getWeatherData(self):
        return self.month, self.day, self.year

    def printWeatherData(self):
        print "Date: ", self.month + "/" + self.day + "/" + self.year + " " + self.hour + ":" + self.minute + "   DB_F: " + str(self.tempDBF) + "::DB_C: " + str(self.tempDBC) + ", WB_F: " + str(self.tempWBF) + "::WB_C: " + str(self.tempWBC)
            
        
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

        print "WeatherStation loaded..."
        
    def getStationName(self):
        return self.stationName

    def getStationUSAFIdentifier(self):
        return self.stationUSAFIdentifier

    def getStationWBANCode(self):
        return self.stationWBANCode

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
                        
            for line in infile:
                
                if setStation == True:
                    self.station.setWeatherStation(line)
                    setStation = False
                else:
                    self.data.append(WeatherData(line))
            self.station.getWeatherStation()
          
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
    authkey = ""
    tdata = {}
    
    weather = Weather()
    weather.setLocalNOAAWeather('724050-13743-2011')
    weather.getData()

if __name__ == "__main__":
    sys.exit(not main(sys.argv))
