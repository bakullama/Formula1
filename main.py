import DataGrab
import time
import requests
import argparse
import lxml.html as lh
from datetime import datetime
from prettytable import PrettyTable
from os import system

def main(args):
    if args == 0:
        url = "https://www.formula1.com/en/results.html/2019/drivers.html"
        headers = ["Position", "First Name", "Last Name", "Nationality", "Car", "Points"]
        waitTime = 30
    elif args == 1:
        url = "https://www.formula1.com/en/results.html/2019/races/1002/china/race-result.html"
        headers = ["Position", "Number", "First Name", "Last Name", "Car", "Laps", "Time", "Points"]
        waitTime = 10
    else:
        print("Invalid flags")

    data = DataGrab.getdata(url)
    DataGrab.display(data, headers, waitTime)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataType", help="selects data to view [default: 0]\nDriver Standings: 0\nRace Data: 1", type=int)
    args = parser.parse_args()
    dataType = args.dataType
    main(dataType)
