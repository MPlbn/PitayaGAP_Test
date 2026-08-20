import matplotlib.pyplot as plt
import Utils
import csv

def g1_s(uTestNumber = 1):
    path = f'data/S_TEST_{uTestNumber}.csv'
    with open(path, newline="") as file: #S_TEST_1-3
            reader = csv.reader(file, delimiter=';')
            next(reader)  # pomija nagłówek
    
            data = [[float(value) for value in row] for row in reader]

    y = [row[0] for row in data]

    plt.plot(y)
    plt.xlabel("t")
    plt.ylabel("V [mV]")
    plt.xticks([])
    plt.grid()
    plt.show()

def g1_f():
    with open("data/F_TEST_1.csv", newline="") as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # pomija nagłówek
    
            data = [[float(value) for value in row] for row in reader]

            data = [[value * 1000 for value in row] for row in data]

    y = [row[0] for row in data]

    plt.plot(y)
    plt.xlabel("t")
    plt.ylabel("V [mV]")
    plt.xticks([])
    plt.grid()
    plt.show()
    

def g2_s():
    with open("data/S_TEST_4.csv", newline="") as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # pomija nagłówek

        data = [[float(value) for value in row] for row in reader]

    y = [row[0] for row in data]

    plt.plot(y)
    plt.xlabel("t")
    plt.ylabel("IN1 [mV]")
    plt.grid()
    plt.show()

    print(f'data length {len(data)}')

    data = Utils.medianFilter(data, 0)

    print(f'data length {len(data)}')

    y = [row[0] for row in data]

    plt.plot(y)
    plt.xlabel("t")
    plt.ylabel("IN2")
    plt.grid()
    plt.show()

    newData = Utils.processDataResistance(data)

    x = [row[0] for row in newData]
    y = [row[1] for row in newData]

    plt.plot(x, y)
    plt.xlabel("Voltage [mV]")
    plt.ylabel("Current [mA]")
    plt.grid()
    plt.show()

def g2_f():
    with open("data/F_TEST_2.csv", newline="") as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # pomija nagłówek

        data = [[float(value) for value in row] for row in reader]

        data = [[value * 1000 for value in row] for row in data]

    y = [row[0] for row in data]

    plt.plot(y)
    plt.xlabel("t")
    plt.ylabel("IN1 [mV]")
    plt.grid()
    plt.show()

    print(f'data length {len(data)}')

    data = Utils.medianFilter(data, 0)

    print(f'data length {len(data)}')

    y = [row[0] for row in data]

    plt.plot(y)
    plt.xlabel("t")
    plt.ylabel("IN1")
    plt.grid()
    plt.show()

    newData = Utils.processDataResistance(data)

    x = [row[0] for row in newData]
    y = [row[1] for row in newData]

    plt.plot(x, y)
    plt.xlabel("Voltage [mV]")
    plt.ylabel("Current [mA]")
    plt.grid()
    plt.show()

def g3_s():
    with open("data/S_TEST_5.csv", newline="") as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # pomija nagłówek

        data = [[float(value) for value in row] for row in reader]

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.plot(x, y)
    plt.xlabel("IN1")
    plt.ylabel("IN2")
    plt.grid()
    plt.show()

    print(f'data length {len(data)}')

    data = Utils.medianFilter(data, 0)

    print(f'data length {len(data)}')

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.plot(x, y)
    plt.xlabel("IN1")
    plt.ylabel("IN2")
    plt.grid()
    plt.show()

    data = Utils.medianFilter(data, 1)

    print(f'data length {len(data)}')

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.plot(x, y)
    plt.xlabel("IN1")
    plt.ylabel("IN2")
    plt.grid()
    plt.show()

    newData = Utils.processDataDiode(data)

    x = [row[0] for row in newData]
    y = [row[1] for row in newData]

    plt.plot(x, y)
    plt.xlabel("Voltage [mV]")
    plt.ylabel("Current [uA]")
    plt.grid()
    plt.show()

def g3_f():
    with open("data/F_TEST_3.csv", newline="") as file:
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

    data = Utils.medianFilter(data, 0)

    print(f'data length {len(data)}')

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.plot(x, y)
    plt.xlabel("IN1")
    plt.ylabel("IN2")
    plt.grid()
    plt.show()

    data = Utils.medianFilter(data, 1)

    print(f'data length {len(data)}')

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.plot(x, y)
    plt.xlabel("IN1")
    plt.ylabel("IN2")
    plt.grid()
    plt.show()

    newData = Utils.processDataDiode(data)

    x = [row[0] for row in newData]
    y = [row[1] for row in newData]

    plt.plot(x, y)
    plt.xlabel("Voltage [mV]")
    plt.ylabel("Current [uA]")
    plt.grid()
    plt.show()

