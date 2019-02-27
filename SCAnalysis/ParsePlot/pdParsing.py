import csv
import pandas as pd

""" 
mtA, mtB: Motor A and B message
  V: Motor bus voltage
  I: Motor bus current
  S: Vehicle speed
  O: Odometer

mtA_t, mtB_t: Motor A and B temperature
  HT: Heat sink temperature
  MT: Motor temperature

bat_v: Battery message
  max: Max voltage across all modules
  min: Min voltage across all modules
  avg: Average voltage across all modules

bat_t: Battery temperature
  max: Max temperature across all modules
  min: Min temperature across all modules
  avg: Average temperature across all modules

gps: GPS data
  lat: Latitude
  lon: Longitude
  speed: Speed as reported by GPS
"""


def parse():
    # dictionary of csvs with dictionaries inside
    # 'mtA', 'mtB', 'mtA_t', 'mtB_t', 'bat', 'bat_t', 'gps'
    csvs = {}

    file_names = {'mtA', 'mtB', 'mtA_t', 'mtB_t', 'bat_v', 'bat_t', 'gps'}

    for file in file_names:
        df = pd.read_csv('./real_data/' + file + '.csv')
        csvs[file] = df.to_dict(orient='list')

    return csvs
