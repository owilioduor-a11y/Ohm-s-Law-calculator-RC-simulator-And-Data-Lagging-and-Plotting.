### Lab 3: Data Logging and Plotting
### Goal: Write a Python program to log data to a file and plot it.
### Modify code to log both temperature and humidity.
### Use different file formats (CSV, TXT).
### Add error handling for file operations.

import random, time
import matplotlib. pyplot as plt

temps = []
for t in range (10):
    temp = 25 + random. uniform(-1, 1)
    temps . append (temp)
    with open ("temps. csv", "a") as f:
       f.write(f"{t},{temp}\n")
    time.sleep (0.5)

plt. plot (temps)
plt.xlabel("Time (s)")
plt.ylabel ("Temperature (C)")
plt .title ("Temperature Log")
plt . show ()

# Modified code to log both temperature and humidity in CSV and TXT formats with error handling
import random
import time
import matplotlib.pyplot as plt
import csv

temps = []
humidities = []
for t in range(10):
    temp = 25 + random.uniform(-1, 1)
    humidity = 50 + random.uniform(-5, 5)
    temps.append(temp)
    humidities.append(humidity)
    
    # Log to CSV file

    try:
        with open("data_log.csv", "a", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([t, temp, humidity])
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

    
    # Log to TXT file

    try:
        with open("data_log.txt", "a") as txtfile:
            txtfile.write(f"Time: {t}, Temperature: {temp}, Humidity: {humidity}\n")
    except IOError as e:
        print(f"Error writing to TXT file: {e}")
    
    time.sleep(0.5)
    
# Plotting temperature and humidity

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(temps, label='Temperature (C)', color='r')
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.title("Temperature Log")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(humidities, label='Humidity (%)', color='b')
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.title("Humidity Log")
plt.legend()
plt.tight_layout()
plt.show()
