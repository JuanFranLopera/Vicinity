import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r'/Users/jack/Documents/Cranfield/SDC/data_test_1.csv')
#print(df)

row = 0
readings = [ 0 for x in range(len(df['x_pos']))]
for x in df['x_pos']:
    if df['y_speed_degrees'][row] <= 1.661578 and df['y_speed_degrees'][row] >= -1.661578:
        readings[row] = x
    else:
        readings[row] = -1
    row +=1




bin_size = 5
angle_bins = [x for x in range(0,365, bin_size)]
angle_bin_count = [0 for x in range(len(angle_bins))]
for i in range(len(angle_bins)-1):
    for x in readings:
        if x >= angle_bins[i] and x < angle_bins[i+1]:
            angle_bin_count[i] += 1





plt.figure('Speed')
plt.plot([x for x in range(len(df['y_speed_degrees']))], df['y_speed_degrees'])
plt.plot([x for x in range(len(df['y_speed_degrees']))], df['target_degrees'])
plt.plot([x for x in range(len(df['y_speed_degrees']))], [-x for x in df['target_degrees']])
#plt.axis([0,803, -1.6,1.6])
plt.ylabel('Angular speed in degrees')
plt.xlabel('Time/s')

plt.figure('bins')
plt.bar(angle_bins, angle_bin_count, 5)
plt.xlabel('degrees (5 degree bars)')
plt.ylabel('count')

plt.figure('DC')
plt.bar([x for x in range(len(df['y_speed_degrees']))], df['Duty cycle'])


plt.figure('scatter')
plt.scatter(readings, [0 for x in range(len(df['x_pos']))])
plt.show()