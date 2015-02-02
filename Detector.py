__author__ = 'leah'
import pandas as pd


class Detector:
    def __init__(self, time_array=[], volume=[], occupancy=[], sensor_id=0, control_id=0, description=''):
        self.sensor_id = sensor_id
        self.control_id = control_id
        self.description = description
        self.sensor_type = self.get_sensor_type(volume, occupancy)
        self.data = self.initialize_data(time_array, volume, occupancy)

    @staticmethod
    def get_sensor_type(volume, occupancy):
        no_vol = len(volume) == 0 or volume == [None] * len(volume)
        no_occ = len(occupancy) == 0 or occupancy == [None] * len(occupancy)
        if no_vol and no_occ:
            return 'unknown'
            # volume = []
            # occupancy = []
        elif no_vol and not no_occ:
            return 'occupancy'
            # volume = []
        elif no_occ and not no_vol:
            return 'volume'
            # occupancy = []
        else:
            return 'combined'


    def initialize_data(self, time, vol, occ):
        data_dict={}
        if self.sensor_type == 'combined':
            data_dict = {'volume': vol, 'occupancy': occ}
        elif self.sensor_type == 'volume':
            data_dict = {'volume': vol}
        elif self.sensor_type == 'occupancy':
            data_dict = {'occupancy': occ}
        return pd.DataFrame(data_dict, index=time)

    def update_data(self, new_time, new_data):
        self.data.loc[new_time] = new_data

    def get_latest_data(self):
        latest_time = max(self.data.index)
        return self.data[latest_time], latest_time



