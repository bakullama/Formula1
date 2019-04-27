import time
import requests
import lxml.html as lh
from datetime import datetime
from prettytable import PrettyTable
from os import system

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
