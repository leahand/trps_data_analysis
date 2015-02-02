__author__ = 'leah'

from Detector import Detector
from DetectorSet import DetectorSet
import os
import csv
from datetime import datetime


def import_pasadena_data(data_directory):
    sensor_list = [Detector('volume')]
    detector_list = [DetectorSet(sensor_list)]
    return detector_list


def import_arcadia_archived_data(data_directory='/Users/leah/Desktop/Sensor Data/Arcadia/Historical 5-min Sensor Data (from TransSuite)/TCS Detector Archive/Arcadia Detector Archive - 2014-02-09'):
    detector_dictionary = {}
    for filename in os.listdir(data_directory):
        if '.csv' not in filename:
            continue
        with open(os.path.join(data_directory, filename), 'rb') as csvfile:
            linedict = csv.DictReader(csvfile)
            volume = []
            occupancy = []
            timestamps = []
            id = 0
            for row in linedict:
                id = int(row['Detector ID'])
                timestamps.append(datetime.strptime(row[' "Archive Date"'], '%a %b %d %H:%M:%S %Z %Y'))
                if 'ON_LINE' in row[' Status']:
                    volume.append(float(row[' Volume']))
                    occupancy.append(float(row[' Occupancy']))
                else: # sensor is offline
                    volume.append(None)
                    occupancy.append(None)
                control_id = int(str(id)[0:-2])
            detector_dictionary.setdefault(control_id, []).append(Detector(time_array=timestamps, volume=volume,
                                                                           occupancy=occupancy, sensor_id=id,
                                                                           control_id=control_id))
    detector_list = []
    for control_id, sensor_list in detector_dictionary.iteritems():
        detector_list.append(DetectorSet(sensor_list, detector_id=control_id, control_id=control_id))
    return detector_dictionary, detector_list


