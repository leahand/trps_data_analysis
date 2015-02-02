__author__ = 'leah'
from data_import_tools import import_arcadia_archived_data


detector_list = import_arcadia_archived_data()
for d in detector_list:
    print '------------', d.control_id, '------------'
    for s in d.sensors:
        print s.sensor_id, ' '+s.sensor_type

