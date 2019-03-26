"""

Module: plot.py
Author: Kathryn Schantz
Purpose: Series of functions that takes data parsed from csv and plots the graphs and returns the resulting figure.

"""

from SCAnalysis.ParsePlot import pdParsing as parse
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


# mtA : 'pc_time', 'V', 'I', 'S', 'O'
# mtB : 'pc_time', 'V', 'I', 'S', 'O'
# mtA_t : 'pc_time', 'MT'
# mtB_t : 'pc_time', 'MT'
# bat_v : 'pc_time', 'max', 'min', 'avg'
# bat_t : 'pc_time', 'max', 'min', 'avg'

def unix_to_dt(unix_times):
    dateT = []
    for ts in unix_times:
        dateT.append(datetime.utcfromtimestamp(ts))
    return dateT


def speed_time(path):
    fig = plt.figure()

    data = parse.parse(path)
    motorA = data['mtA']
    motorB = data['mtB']

    timeA = np.array(unix_to_dt(motorA['pc_time']))
    timeB = np.array(unix_to_dt(motorB['pc_time']))
    speedA = np.array(motorA['S'])
    speedB = np.array(motorB['S'])

    ax = fig.add_subplot(1, 1, 1)
    ax.plot(timeA, speedA, 'r', timeB, speedB, 'b')
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed')
    ax.set_title('Speed vs Time')

    return fig


# def SOC_time():
#    fig = plt.figure()

#    data = parse.parse()
#    battery = data['bat_v']

#    time = np.array(unix_to_dt(battery['pc_time']))
#    SOC = np.array(battery['SOC'])

#    ax = fig.add_subplot()
#    ax.plot(time, SOC, 'k')
#    ax.set_xlabel('Time')
#    ax.set_ylabel('SOC')
#    ax.set_title('SOC vs Time')

#    return fig

def voltage_time(path):
    fig = plt.figure()

    data = parse.parse(path)
    battery = data['bat_v']

    time = np.array(unix_to_dt(battery['pc_time']))
    voltage_high = np.array(battery['max'])
    voltage_low = np.array(battery['min'])
    voltage_avg = np.array(battery['avg'])

    ax = fig.add_subplot(1, 1, 1)
    ax.plot(time, voltage_high, 'r', time, voltage_low, 'b', time, voltage_avg, 'k')
    ax.set_xlabel('Time')
    ax.set_ylabel('Voltage')
    ax.set_title('Voltage vs Time')

    return fig


def motor_current_time(path):
    fig = plt.figure()

    data = parse.parse(path)
    motorA = data['mtA']
    motorB = data['mtB']

    timeA = np.array(unix_to_dt(motorA['pc_time']))
    timeB = np.array(unix_to_dt(motorB['pc_time']))
    currentA = np.array(motorA['I'])
    currentB = np.array(motorB['I'])

    ax = fig.add_subplot(1, 1, 1)
    ax.plot(timeA, currentA, 'r', timeB, currentB, 'b')
    ax.set_xlabel('Time')
    ax.set_ylabel('Motor Current')
    ax.set_title('Motor Current vs Time')

    return fig


def battery_current_time():
    fig = plt.figure()

    data = parse.parse()
    curr = data['curr']

    time = np.array(unix_to_dt(curr['pc_time']))
    current = np.array(curr['val'])

    ax = fig.add_subplot()
    ax.plot(time, current, 'k')
    ax.set_xlabel('Time')
    ax.set_ylabel('Battery Current')
    ax.set_title('Battery Current vs Time')

    return fig


def motor_temp_time(path):
    fig = plt.figure()

    data = parse.parse(path)
    motorA = data['mtA_t']
    motorB = data['mtB_t']

    timeA = np.array(unix_to_dt(motorA['pc_time']))
    timeB = np.array(unix_to_dt(motorB['pc_time']))
    tempA = np.array(motorA['MT'])
    tempB = np.array(motorB['MT'])

    ax = fig.add_subplot(1, 1, 1)
    ax.plot(timeA, tempA, 'r', timeB, tempB, 'b')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Motor Temperature vs Time')

    return fig


def battery_temp_time(path):
    fig = plt.figure()

    data = parse.parse(path)
    bat = data['bat_t']

    time = np.array(unix_to_dt(bat['pc_time']))
    temp_high = np.array(bat['max'])
    temp_low = np.array(bat['min'])
    temp_avg = np.array(bat['avg'])

    ax = fig.add_subplot(1, 1, 1)
    ax.plot(time, temp_high, 'r', time, temp_low, 'b', time, temp_avg, 'k')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Battery vs Time')

    return fig
