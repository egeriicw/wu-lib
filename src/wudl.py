import requests
import json
import sys

monthdays = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}

## Set parameters for GET request
#parameters = {'key1' : 'value1', 'key2' : 'value2'}

def main(arg):
    temp_data = []

    tdata = {}

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

    print json.dumps(json.loads(tdata['10/18/2010']))

    for m, d in monthdays.iteritems():
        print "Month: ", m, " Days: ", d
    
    return 0

def getWUTempHistory(key, mo, dy, yr):
    # Requests data from Weather Underground site
    # Returns json object

    url = 'http://api.wunderground.com/api/' + key + '/history_'+ yr + mo + dy + '/q/DCA.json'

    # Returns a json object
    r = requests.get(url)

    return r

if __name__ == "__main__":
    sys.exit(not main(sys.argv))
