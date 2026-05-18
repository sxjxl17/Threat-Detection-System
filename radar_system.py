import numpy as np

print("\n-----SAFFRON STRATEGIC SYSTEMS-----\n\n    Threat Detection System\n")
np.random.seed(42)
radar_data = np.random.randint(0,100,(10,10))
print("RADAR GRID: ")
print(radar_data)

# Average threat level
print("\nAverage Threat: ",radar_data.mean())

# Maximum threat level
print("\nMaximum Threat: ",radar_data.max())

#Minimum threat level
print(f"\nLowest Threat: {radar_data.min()}")

# Suspicious signals
print(f"\nSuspicious signals: {radar_data[radar_data > 85]}")

# Threat locations
print(f"\nSuspicious threat locations: {np.argwhere(radar_data>85)}")

# Critical alerts
print(f"\nCritial alerts: {radar_data[radar_data > 95]}")
print(f"\nCritical alert locations: {np.argwhere(radar_data > 95)}")

# Region wise analysis
region_avg = radar_data.mean(axis=1)
print(f"\nAverage danger per region: {region_avg}")

print(f"\nMost dangerous region: {np.argmax(region_avg)}")

# Night vision radar detection
night_scan = radar_data+100
print(f"\nNight vision detection: \n{night_scan}")