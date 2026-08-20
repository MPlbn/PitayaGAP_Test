## module responsible for providing filtering functions to the data captured in CSV files
from statistics import median

def singleFilter(uDataSet, uThreshold=10, channel = 0):
    i = 1
    counter = 0
    while(i < len(uDataSet) - 1):
        differenceValue = uDataSet[i][channel] - uDataSet[i-1][channel]
        if(abs(differenceValue) > uThreshold):
            print(f'{uDataSet[i][0]} - {uDataSet[i-1][0]}')
            uDataSet.pop(i)
            counter += 1
        else:
            i += 1

    print(f'Counter value: {counter}')



def dualFilter(uDataSet, uThreshold=20, channel = 1):
    i = 1
    counter = 0
    while(i < len(uDataSet) - 2):
        differenceValuePrevious = uDataSet[i][channel] - uDataSet[i-1][channel]
        differenceValueNext = uDataSet[i][channel] - uDataSet[i+1][channel]
        if(abs(differenceValuePrevious) > uThreshold and abs(differenceValueNext) > uThreshold):
            uDataSet.pop(i)
            counter += 1
        else:
            i += 1

    print(f'Counter value: {counter}')


def medianFilter(uDataSet, channel = 0):
    filtered = [row[:] for row in uDataSet]

    for i in range(2, len(uDataSet)-2):
        window = [uDataSet[j][channel] for j in range(i-2, i+3)]
        filtered[i][channel] = median(window)
    return filtered


def processDataDiode(uDataSet, uResistance = 1000):
    newDataSet = []

    for row in uDataSet:
        VOut = row[0] #mV
        VDiode = row[1] #mV
        current = (VOut - VDiode) / uResistance * 1000 #uA

        newDataSet.append([VDiode, current])

    return newDataSet

def processDataResistance(uDataSet, uResistance = 1000):
    newDataSet = []
    for row in uDataSet:
        VOut = row[0] #mV
        current = VOut / uResistance #mA
    
        newDataSet.append([VOut, current])
    
    return newDataSet