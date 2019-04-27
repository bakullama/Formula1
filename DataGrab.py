

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


def main():
    dat = getdata("https://www.formula1.com/en/results.html/2019/races/1002/china/race-result.html")
    display(dat, ["Position", "Number", "First Name", "Last Name", "Car", "Laps", "Time", "Points"], 30)



if __name__ == "__main__":
    main()
