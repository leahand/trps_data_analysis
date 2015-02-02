__author__ = 'leah'
from data_import_tools import import_arcadia_archived_data
from matplotlib import pyplot as plt

detector_dict, detector_list = import_arcadia_archived_data()
huntington_baldwin = detector_dict[3092]
for det in huntington_baldwin:
    plt.figure()
    df = det.data
    # df.volume.plot()
    plt.plot(df.occupancy, df.volume, 'bo')
    plt.xlabel('occupancy')
    plt.ylabel('volume')
plt.show()