import numpy as np
sensor_readings=np.array([25.5, 26.0, np.nan, 27.8, np.inf, 26.4])
print("________Original_Dataset________\n",sensor_readings)
print("_____Detecting missing values_____\n",np.isnan(sensor_readings))
print("_____Detecting infinite values_____\n",np.isinf(sensor_readings))
sensor_readings[np.isnan(sensor_readings)]=0
sensor_readings[np.isinf(sensor_readings)]=0
print("______Handiling_missing_values_______\n",sensor_readings)
print("______Handliing_infinte_values_______\n",sensor_readings)

