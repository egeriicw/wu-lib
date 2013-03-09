from weather import Weather

class WeatherManager:

    def __init__(self):
        self.weather = Weather()
        self.weather.setLocalNOAAWeather('724050-13743-2011')
        self.weather.getData()

    # run through checks of various data sources.
    # Check for json data file
    # Check various db bindings (mysql, mongodb, etc.)
    # IF nothing found, then download, process, and store in 
    # json and db.

def main():
    print "...Weather Manager Main..."
    manager = WeatherManager()

if __name__ == "__main__":
    main()

