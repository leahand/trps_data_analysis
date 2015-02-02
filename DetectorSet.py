__author__ = 'leah'
import pandas as pd


class DetectorSet:
    def __init__(self, sensors, detector_id=None, control_id=None, coordinates=(0.0, 0.0)):
        self.sensors = sensors
        self.detector_id = detector_id
        self.control_id = control_id
        self.coordinates = coordinates

    # def get_intersection_id_from_sensors(self):
    #     all_ids = {d.intersection_id for d in self.sensors}
    #     if len(all_ids) > 1:
    #         return None
    #     else:
    #         return int(list(all_ids)[0])

