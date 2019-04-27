import DataGrab
import argparse

countries = ["australia", "bahrain", "china", "azerbaijan", "spain", "monaco",
             "canada", "france", "austria", "great_britain", "germany", "hungary",
             "belgium", "italy", "singapore", "russia", "japan", "mexico",
             "united_states", "brazil", "abu_dhabi"]

def main(dataType, country, raceID):
    if dataType == 0:
        url = "https://www.formula1.com/en/results.html/2019/drivers.html"
        headers = ["Position", "First Name", "Last Name", "Nationality", "Car", "Points"]
        waitTime = 30
    elif dataType == 1:
        if country == None:
            print("no country specified")
            exit()
        url = "https://www.formula1.com/en/results.html/2019/races/{id}/{country}/race-result.html".format(id = raceID, country=country)
        headers = ["Position", "Number", "First Name", "Last Name", "Car", "Laps", "Time", "Points"]
        waitTime = 10
    else:
        print("Invalid flags")

    try:
        data = DataGrab.getdata(url)
    except IndexError:
        print("An error occured, are you sure this race has happened yet?")
        exit()
    DataGrab.display(data, headers, waitTime)


def getRaceID(country):
    raceID = 1000
    found = False
    if country == None:
        return None

    else:
        for i in range(len(countries)):
            if countries[i] == country:
                found = True
                raceID += i
    if found:
        return str(raceID)
    else:
        print("invalid country (for countries with multiple words, use an _, ie great_britain)")
        exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataType", help="selects data to view\nDriver Standings: 0\nRace Data: 1", type=int)
    parser.add_argument("country", help="selects country (only applies if option 1 used)", type=str, nargs="?")
    args = parser.parse_args()
    country = args.country
    dataType = args.dataType
    raceID = getRaceID(country)
    try:
        main(dataType, country, raceID)
    except KeyboardInterrupt:
        print("Exiting")
