import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r'/Users/jack/Documents/Cranfield/SDC/Maria/maria_tests_input_stepped2_proc.csv')
#df1 = pd.read_csv (r'/Users/jack/Documents/Cranfield/SDC/test_2/data_test_2_proccessed.csv')
##df2 = pd.read_csv (r'/Users/jack/Documents/Cranfield/SDC/linear tests/linear_accel_2s_proc.csv')
#df3 = pd.read_csv (r'/Users/jack/Documents/Cranfield/SDC/4.5_0.8/KP_test_80_proc.csv')

#print(df)
target = [-0.025 for x in range(len(df['y_speed']))]
lower_bound = [-0.0279 for x in range(len(df['y_speed']))]
upper_bound = [-0.02 for x in range(len(df['y_speed']))]

row = 0
readings = [ 0 for x in range(len(df['x_pos']))]
for x in df['x_pos']:
    if df['y_speed'][row] >= lower_bound[0] and df['y_speed'][row] <= -lower_bound[0]:
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



target = [-0.025 for x in range(len(df['y_speed']))]
lower_bound = [-0.0279 for x in range(len(df['y_speed']))]
upper_bound = [-0.02 for x in range(len(df['y_speed']))]

plt.figure('Speed')
plt.plot([x for x in range(len(df['y_speed']))], df['y_speed'], label = 'linear 1s')
#plt.plot([x for x in range(len(df1['y_speed']))], df1['y_speed'],label = 'original linear 1s')
#plt.plot([x for x in range(len(df2['y_speed']))], df2['y_speed'],label = 'linear 2s')
#plt.plot([x for x in range(len(df3['y_speed']))], df3['y_speed'])

plt.plot([x for x in range(len(df['y_speed']))], target)
plt.plot([x for x in range(len(df['y_speed']))], lower_bound)
plt.plot([x for x in range(len(df['y_speed']))], upper_bound)
#plt.axis([0,803, -1.6,1.6])
plt.ylabel('Angular speed in rad /s')
plt.xlabel('Time/s')
plt.legend()


plt.figure('bins')
plt.bar([x+2.5 for x in angle_bins], angle_bin_count, 5)
plt.xlabel('degrees (5 degree bars)')
plt.ylabel('count')
plt.axis([0,360, 0, 100])

plt.figure('DC')
plt.plot([x/4 for x in range(len(df['y_speed']))], df['Duty cycle'], label = 'linear 1s')
#plt.plot([x for x in range(len(df1['y_speed']))], df1['Duty cycle'],label = 'original linear 1s')
#plt.plot([x for x in range(len(df2['y_speed']))], df2['Duty cycle'],label = 'linear 2s')
plt.plot([x/4 for x in range(len(df['y_speed']))], [12 for x in range(len(df['y_speed']))], color='black')
plt.plot([x/4 for x in range(len(df['y_speed']))], [4.5 for x in range(len(df['y_speed']))], color='black')
plt.legend()
"""
plt.figure('scatter')
plt.scatter(readings, [0 for x in range(len(df['x_pos']))])
"""
"""
plt.figure('position')
plt.plot([x for x in range(len(df['y_speed']))], df['x_pos'])
plt.plot([x for x in range(len(df1['y_speed']))], df1['x_pos'])
plt.plot([x for x in range(len(df2['y_speed']))], df2['x_pos'])
plt.plot([x for x in range(len(df3['y_speed']))], df3['x_pos'])
"""
plt.show()
