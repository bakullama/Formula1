from datetime import datetime
from prettytable import PrettyTable
from os import system
import time
import requests
import lxml.html as lh

# Driver Format: [Position, First Name, Last Name, code, Nationality, Car, Points]
# ['1', 'Lewis', 'Hamilton', 'GBR', 'Mercedes', '68']

def getDrivers(url):

        page = requests.get(url)
        doc = lh.fromstring(page.content)
        tbody = doc.xpath("//tbody")
        driverraw = []
        print(tbody)

        for t in tbody[0]:
            name = t.text_content()
            driverraw.append(name)
        drivers = []

        for j in range(20):
            drivers.append([])
            popped = 0
            driver = driverraw[j].split("\n")
            for i in range(len(driver)):
                driver[i - popped] = driver[i - popped].strip()
                if driver[i - popped] == "":
                    driver.pop(i - popped)
                    popped += 1
            driver.pop(3)
            drivers[j] = driver

        return drivers

def display(drivers):
    while True:
        system("clear")
        print("""'########::'#######::'########::'##::::'##:'##::::'##:'##::::::::::'###::::::::::'##:::
 ##.....::'##.... ##: ##.... ##: ###::'###: ##:::: ##: ##:::::::::'## ##:::::::'####:::
 ##::::::: ##:::: ##: ##:::: ##: ####'####: ##:::: ##: ##::::::::'##:. ##::::::.. ##:::
 ######::: ##:::: ##: ########:: ## ### ##: ##:::: ##: ##:::::::'##:::. ##::::::: ##:::
 ##...:::: ##:::: ##: ##.. ##::: ##. #: ##: ##:::: ##: ##::::::: #########::::::: ##:::
 ##::::::: ##:::: ##: ##::. ##:: ##:.:: ##: ##:::: ##: ##::::::: ##.... ##::::::: ##:::
 ##:::::::. #######:: ##:::. ##: ##:::: ##:. #######:: ########: ##:::: ##:::::'######:
..:::::::::.......:::..:::::..::..:::::..:::.......:::........::..:::::..::::::......::""")
        t = PrettyTable(["Position", "First Name", "Last Name", "Nationality", "Car", "Points"])
        for i in drivers:
            t.add_row(i)
        print(t)
        print("local time:")
        print(datetime.now().strftime('%H:%M:%S'))
        time.sleep(1)

def main():
    drivers = getDrivers("https://www.formula1.com/en/results.html/2019/drivers.html")
    display(drivers)



if __name__ == "__main__":
    main()
