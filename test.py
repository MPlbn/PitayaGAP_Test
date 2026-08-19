import matplotlib.pyplot as plt
import Utils
import csv

with open("data/dioda1fast.csv", newline="") as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # pomija nagłówek

    data = [[float(value) for value in row] for row in reader]

## for fast:
    data = [[value * 1000 for value in row] for row in data]
##end for fast

x = [row[0] for row in data]
y = [row[1] for row in data]

plt.plot(x, y)
plt.xlabel("IN1")
plt.ylabel("IN2")
plt.grid()
plt.show()

print(f'data length {len(data)}')

Utils.filterIN1(data)

print(f'data length {len(data)}')

x = [row[0] for row in data]
y = [row[1] for row in data]

plt.plot(x, y)
plt.xlabel("IN1")
plt.ylabel("IN2")
plt.grid()
plt.show()

Utils.filterIN2(data)

print(f'data length {len(data)}')

x = [row[0] for row in data]
y = [row[1] for row in data]

plt.plot(x, y)
plt.xlabel("IN1")
plt.ylabel("IN2")
plt.grid()
plt.show()

newData = Utils.processData(data)

x = [row[0] for row in newData]
y = [row[1] for row in newData]

plt.plot(x, y)
plt.xlabel("Voltage [mV]")
plt.ylabel("Current [uA]")
plt.grid()
plt.show()
