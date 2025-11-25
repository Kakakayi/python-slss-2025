# Data Analysis
# Author: Karina Luo
#

# Analyse the data provided in class


def main():
    total = 0
    june_max = 0
    path = "data/NYC_Central_Park_weather_1869-2022 (1).csv"
    file = open(path)
    percipitation1 = 0
    min_total = 0
    june_total = 0
    header_row = file.readline()
    for line in file:
        print(line)
        info = line.split(",")
        percipitation = info[1].strip()
        max_percipitation = info[5].strip()
        month = info[0].split("-")
        june = month[1]
        if june == "06" and max_percipitation != " ":
            june_max += float(max_percipitation)
            june_total += 1
        min_percipitation = info[4].strip()

        if min_percipitation == "":
            min_total += 0
        else:
            min_total += float(min_percipitation)
        percipitation1 += float(percipitation)
        total += 1

    print(f"{june_max / june_total} def F")
    print(f"{min_total / total} deg F")
    print(f"{percipitation1 / (total)} in")
    print(total)
    file.close()


if __name__ == "__main__":
    main()
