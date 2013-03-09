#! /usr/bin/env python

import requests
import json
import sys
import csv
import StringIO
import pandas as pd
import datetime as dt
from dateutil.parser import parse
import numpy as np


class WeatherData:

    def __init__(self, line):
        #print "WeatherData loaded."
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
        

        if self.tempDBRAW[1:] != '9999':

            self.tempDBC = float(self.tempDBRAW[1:])/10.
            
            if self.tempDBRAW[0] == '-':
                self.tempDBC = self.tempDBC * -1.
            self.tempDBF = self.CtoF(self.tempDBC)
        else:
            self.tempDBC = np.nan
            self.tempDBF = np.nan

        if self.tempWBRAW[1:] != '9999':
            self.tempWBC = float(self.tempWBRAW[1:])/10.
            if self.tempWBRAW[0] == '-':
                self.tempWBC = self.tempWBC * -1.
            self.tempWBF = self.CtoF(self.tempWBC)

        else:
            self.tempWBC = np.nan
            self.tempWBF = np.nan

        #print "DB: ", self.tempDBRAW, self.tempDBF
        #print "WB: ", self.tempWBRAW, self.tempWBF


    # Temperature Conversion Functions
    def FtoC(self, data):
        # Convert Fahrenheit to Celsius
        
        return (data - 32) / 1.8

    def CtoF(self, data):
        # Convert Celsius to Fahrenheit
        
        return (data * (9/5)) + 32
    
    def CtoK(self, data):
        # Convert Celsius to Kelvin

        # TODO
        return 0

    def KtoC(self, data):
        # Convert Kelvin to Celsius

        # TODO
        return 0

    def FtoR(self, data):
        # Convert Fahrenheit to Rankine

        #TODO
        return 0

    def RtoF(self, data):
        # Convert Rankine to Fahrenheit

        # TODO
        return 0

    def getWeatherData(self):
        return self.month, self.day, self.year

    def printWeatherData(self):
        print "Date: ", self.month + "/" + self.day + "/" + self.year + " " + self.hour + ":" + self.minute + "   DB_F: " + str(self.tempDBF) + "::DB_C: " + str(self.tempDBC) + ", WB_F: " + str(self.tempWBF) + "::WB_C: " + str(self.tempWBC)
            

    def getDateTime(self):
        return dt.datetime(int(self.year), int(self.month), int(self.day), int(self.hour), int(self.minute))
    
    def getDBTemperature(self):
        return self.tempDBF

        
    def throttle(self):
        # Throttling keeps Weather Underground API access within
        # free levels by scheduling how many times per minute and day
        # the API is called.
        #
        # Useful resource for scheduling:
        #   http://docs.python.org/2/library/sched.html
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
        print filename
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
        # Resources for FTP & gz decompression:
        #   http://www.blog.pythonlibrary.org/2012/07/19/python-101-downloading-a-file-with-ftplib/
        #   http://docs.python.org/2/library/zlib.html#module-zlib
        
  
    def setLocalWUWeather(self):
        # TODO
        print "...setLocalWUWeather()..."

    def setRemoteWUWeather(self, authkey=None):
        # TODO
        if authkey != "":
            print "...setRemoteWUWeather()..."
        else:
            print "Weather Underground Authentication Key Required."


    def toTimeSeries(self):
        # Returns PANDAS TimeSeries object

        tWeatherDatetime = []
        tWeatherTemperature = []

        for x in self.data:
            tWeatherDatetime.append(x.getDateTime())
            tWeatherTemperature.append(x.getDBTemperature())    


        #print tWeatherDatetime
        #print tWeatherTemperature        

        tsWeather = pd.Series(tWeatherTemperature, index=tWeatherDatetime)

        tsWeather.to_csv('../data/output/' + 'originaltest.csv', sep=',')

        # print tsWeather
        # First Date of timeseries
        #pd.to_datetime(str(tsWeather.index[0])).year
        # Last Date of timeseries
        #pd.to_datetime(str(tsWeather.index[-1])).year
        #print pd.to_datetime(str(tsWeather.index[0])).date, type(tsWeather[0])
        #print type(tsWeather)
        #print tsWeather.index.dtype

        # tsWeather.plot()

        #return tsWeather        

        # resampling
        f = lambda x: float(np.mean(x))

        # return resampled data
        return tsWeather.resample('30min', how=f, fill_method='ffill')

    def toCSV(self, data):
        data.to_csv('../data/output/' + 'resampletest.csv', sep=',')

def main(arg):
    authkey = ""
        
    weather = Weather()
    weather.setLocalNOAAWeather('724050-13743-2011')
    #weather.getData()
    newfile = weather.toTimeSeries()

    weather.toCSV(newfile)


if __name__ == "__main__":
    sys.exit(not main(sys.argv))
