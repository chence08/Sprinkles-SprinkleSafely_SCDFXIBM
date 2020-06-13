import csv, random

weather_file = open('weather.csv')
lines = [line.strip().split(',') for line in weather_file]

data = lines[1:]

twohours = [i for i in range(0, 121, 5)]
rest_time = [25, 55, 85, 115]

# 20 Participants with different fitness levels
initial_heartRate = [random.randint(55, 65) for i in range(20)]
header = ['SN/Trainee'] + [str(i) for i in range(1,21)]
row_list = [initial_heartRate]

def feelslike(temperature, humidity, ws):
    temperature = float(temperature)
    humidity = float(humidity)
    ws = float(ws)
    return temperature * humidity / (ws + 1)

for i in range(1, len(data)):
    previous_heartRate = row_list[i-1]
    previous_weather = data[i-1]
    SN, minutes, temperature, humidity, wd, ws = previous_weather
    previous_feel = feelslike(temperature, humidity, ws)
    current_weather = data[i]
    SN1, minutes1, temperature1, humidity1, wd1, ws1 = current_weather
    current_feel = feelslike(temperature1, humidity1, ws1)
    if int(minutes1) in rest_time:
        newHeartRate = list(map(lambda x: x - random.randint(10, 15), previous_heartRate))
    else:
        if current_feel > previous_feel:
            newHeartRate = list(map(lambda x: x + random.randint(3, 10), previous_heartRate))
        else:
            newHeartRate = list(map(lambda x: x + random.randint(-1, 5), previous_heartRate))

    row_list.append(newHeartRate)

for i in range(len(row_list)):
    row_list[i].insert(0, i+1)



with open('heartrates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(row_list)



