import random, csv, datetime

row_list = []
SN = 0
# for i in range(1,31):
#     Date = str(datetime.date(2019, 7, i))
for j in range(0, 121, 5):
    SN += 1
    Temperature = random.randint(270, 370)/10
    Humidity = random.randint(50, 100)
    WindDirection = random.randint(0, 359)
    WindSpeed = random.randint(0, 150)/10
    row = [SN, j, Temperature, Humidity, WindDirection, WindSpeed]
    row = list(map(lambda x: str(x), row))
    row_list.append(row)






with open('weather.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['SN', 'Minutes into training', 'Temperature', 'Relative Humidity', 'Wind Direction', 'Wind Speed'])
    writer.writerows(row_list)