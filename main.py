import argparse
import time
import requests
import lxml.html as lh
from datetime import datetime
from prettytable import PrettyTable
from os import system


countries = ["australia", "bahrain", "china", "azerbaijan", "spain", "monaco",
             "canada", "france", "austria", "great_britain", "germany", "hungary",
             "belgium", "italy", "singapore", "russia", "japan", "mexico",
             "united_states", "brazil", "abu_dhabi"]


def main(dataType, country, raceID):
    if dataType == 0:
        url = "https://www.formula1.com/en/results.html/2020/drivers.html"
        headers = ["Position", "First Name", "Last Name", "Nationality", "Car", "Points"]
        waitTime = 30
    elif dataType == 1:
        if country == None:
            print("no country specified")
            exit()
        url = "https://www.formula1.com/en/results.html/2020/races/{id}/{country}/race-result.html".format(id = raceID, country=country)
        headers = ["Position", "Number", "First Name", "Last Name", "Car", "Laps", "Time", "Points"]
        waitTime = 10
    else:
        print("Invalid flags")

    try:
        data = getdata(url)
    except IndexError:
        print("An error occured, are you sure this race has happened yet?")
        exit()
    display(data, headers, waitTime)


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


def getdata(url):

        page = requests.get(url)
        doc = lh.fromstring(page.content)
        tbody = doc.xpath("//tbody")
        dataraw = []
        print(tbody)

        for t in tbody[0]:
            name = t.text_content()
            dataraw.append(name)
        data = []

        for j in range(20):
            data.append([])
            popped = 0
            row = dataraw[j].split("\n")
            for i in range(len(row)):
                row[i - popped] = row[i - popped].strip()
                if row[i - popped] == "":
                    row.pop(i - popped)
                    popped += 1
            if "race-result" in url:
                row.pop(4)
            else:
                row.pop(3)
            data[j] = row

        return data


def display(data, headings, waitTime):
    while True:
        system("clear")
        t = PrettyTable(headings)
        for i in data:
            t.add_row(i)
        print(t)
        print("local time:")
        print(datetime.now().strftime('%H:%M'))
        time.sleep(waitTime)


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
