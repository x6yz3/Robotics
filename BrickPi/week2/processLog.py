import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def processLog(logfile):
    data = pd.read_csv(logfile, sep="\t", header=None)

    print(data.shape[1])

    for col in range(1, data.shape[1]-1):
        initial = data[col][0]
        for row in range(data.shape[0]):
            data[col][row] -= initial
            data[col][row] = round(data[col][row], 6)
    dataframe = pd.concat([data[0], data[1], data[2], data[3], data[4], data[5]], axis=1)
    name = logfile[:-4]
    dataframe.to_csv('logs/'+ name +'.log', header=None, index=False, sep='\t')

def drawfigure(logfile):
    data = pd.read_csv(logfile, sep="\t", header=None)
    fig = plt.figure(1)

    figure1 = plt.subplot(211)
    plt.plot(data[0], data[1], label="Reference angle")
    plt.plot(data[0],data[2], label="Actual angle")
    figure1.set_title('Left motor', fontsize=14)
    plt.xlabel('Time', fontsize=10)
    plt.ylabel('Angle [Radians]', fontsize=10)

    figure2 = plt.subplot(212)
    plt.plot(data[0],data[3], label ="Reference angle")
    plt.plot(data[0],data[4], label="Actual angle")
    figure2.set_title('Right motor', fontsize=14)
    plt.xlabel('Time', fontsize=10)
    plt.ylabel('Angle [Radians]', fontsize=10)
    fig = plt.gcf()
    # plt.show()
    name = logfile[:-4]
    fig.savefig('figures/'+ name + '.png', dpi = 100)

if __name__ == '__main__':
    with open('logs/logs_name.txt', 'r') as f:
        for name in f:
            processLog('logs/'+ name+'.log')
            drawfigure('logs/'+ name+'.log')
    # processLog("logs/motor_position_1_360.0.log")
    # drawfigure('write.txt')
