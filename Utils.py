## module responsible for providing filtering functions to the data captured in CSV files

def filterIN1(uDataSet, uThreshold=20):
    i = 1
    counter = 0
    while(i < len(uDataSet) - 1):
        differenceValue = uDataSet[i][0] - uDataSet[i-1][0]
        if(abs(differenceValue) > uThreshold):
            uDataSet.pop(i)
            counter += 1
        else:
            i += 1

    print(f'Counter value: {counter}')



def filterIN2(uDataSet, uThreshold=10):
    i = 1
    counter = 0
    while(i < len(uDataSet) - 2):
        differenceValuePrevious = uDataSet[i][1] - uDataSet[i-1][1]
        differenceValueNext = uDataSet[i][1] - uDataSet[i+1][1]
        if(abs(differenceValuePrevious) > uThreshold and abs(differenceValueNext) > uThreshold):
            uDataSet.pop(i)
            counter += 1
        else:
            i += 1

    print(f'Counter value: {counter}')

def processData(uDataSet, uResistance = 1000):
    newDataSet = []

    for row in uDataSet:
        VOut = row[0]
        VDiode = row[1]
        current = (VOut - VDiode) / uResistance

        newDataSet.append([VDiode, current])

    return newDataSet