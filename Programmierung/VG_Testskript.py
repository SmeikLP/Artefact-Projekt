#Created with support by ChatGPT and friends
#Currently unusable becouse of not imported packages and bugs

import time
import Adafruit_ADS1x15
import Adafruit_SSD1306
from GravityTDS import GravityTDS
import RPi.GPIO as GPIO
import csv

# GPIO pins for water pump relay, LED lamps, and valve control
WATER_PUMP_PIN = 18  # Change to the actual GPIO pin you are using for the water pump relay
LED_LAMPS_PIN = 17   # Change to the actual GPIO pin you are using for the LED lamps relay
VALVE_PIN = 22       # Change to the actual GPIO pin you are using for the valve control

# CSV file name for logging
LOG_FILE_NAME = 'sensor_log.csv'

# Initialize pH sensor (ADS1115)
adc_ph = Adafruit_ADS1x15.ADS1115()
GAIN_PH = 1  # Adjust the gain based on your pH sensor's specifications

# Initialize EC/TDS sensor
tds_sensor = GravityTDS()

# Initialize OLED display
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3D)

# Initialize GPIO for water pump, LED lamps, and valve control
GPIO.setmode(GPIO.BCM)
GPIO.setup(WATER_PUMP_PIN, GPIO.OUT)
GPIO.setup(LED_LAMPS_PIN, GPIO.OUT)
GPIO.setup(VALVE_PIN, GPIO.OUT)

# Initialize display
disp.begin()
disp.clear()
disp.display()

# Function to read pH value from the sensor
def read_ph_value():
    # Read raw ADC value
    raw_value = adc_ph.read_adc(0, gain=GAIN_PH)

    # Convert raw value to pH (adjust conversion factor based on your sensor)
    ph_value = raw_value * 0.00488758553  # Adjust based on your calibration

    return ph_value

# Function to read EC/TDS value from the sensor
def read_ec_tds_values():
    # Read EC/TDS values from the sensor
    ec_value = tds_sensor.read_ec()
    tds_value = tds_sensor.read_tds()

    return ec_value, tds_value

# Function to read temperature value from the sensor (adjust based on your sensor)
def read_temperature():
    # Replace this with your temperature sensor code
    # For example, if using a DS18B20 temperature sensor, you can use the w1thermsensor library

    # Sample code (uncomment and replace as needed):
    # from w1thermsensor import W1ThermSensor
    # sensor = W1ThermSensor()
    # temperature_celsius = sensor.get_temperature()

    # Placeholder value, replace it with actual temperature reading
    temperature_celsius = 25.0

    return temperature_celsius

# Function to control the water pump based on sensor values
def control_water_pump(ph_threshold, ec_threshold):
    ph_value = read_ph_value()
    ec_value, _ = read_ec_tds_values()

    # Check if pH or EC values exceed the threshold
    if ph_value > ph_threshold or ec_value > ec_threshold:
        # Turn on the water pump
        GPIO.output(WATER_PUMP_PIN, GPIO.HIGH)
        print(f'Water pump activated. pH: {ph_value}, EC: {ec_value}')
        return 'Pump Activated'
    else:
        # Turn off the water pump
        GPIO.output(WATER_PUMP_PIN, GPIO.LOW)
        print(f'Water pump deactivated. pH: {ph_value}, EC: {ec_value}')
        return 'Pump Deactivated'

# Function to control the LED lamps
def control_led_lamps(schedule_hours, on_duration_hours):
    current_time = time.localtime()
    current_hour = current_time.tm_hour

    # Check if the current time is within the schedule
    if current_hour in schedule_hours:
        # Turn on the LED lamps
        GPIO.output(LED_LAMPS_PIN, GPIO.HIGH)
        print(f'LED lamps turned on for {on_duration_hours} hours.')
        
        # Wait for the specified on duration
        time.sleep(on_duration_hours * 3600)

        # Turn off the LED lamps after the on duration
        GPIO.output(LED_LAMPS_PIN, GPIO.LOW)
        print('LED lamps turned off.')
        return 'Lamps Activated'
    else:
        # Turn off the LED lamps if not in the schedule
        GPIO.output(LED_LAMPS_PIN, GPIO.LOW)
        return 'Lamps Deactivated'

# Function to control the valve based on sensor values
def control_valve(ph_threshold, ec_threshold, valve_open_duration):
    ph_value = read_ph_value()
    ec_value, _ = read_ec_tds_values()

    # Check if pH or EC values exceed the threshold
    if ph_value > ph_threshold or ec_value > ec_threshold:
        # Open the valve
        GPIO.output(VALVE_PIN, GPIO.HIGH)
        print(f'Valve opened. pH: {ph_value}, EC: {ec_value}')

        # Wait for the specified valve open duration
        time.sleep(valve_open_duration * 3600)

        # Close the valve after the open duration
        GPIO.output(VALVE_PIN, GPIO.LOW)
        print('Valve closed.')
        return 'Valve Opened'
    else:
        # Close the valve if pH and EC values are below the threshold
        GPIO.output(VALVE_PIN, GPIO.LOW)
        return 'Valve Closed'

# Function to log data to CSV file
def log_data(state, ph_value, temperature, ec_value, tds_value):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE_NAME, mode='a', newline='') as csvfile:
        fieldnames = ['Timestamp', 'State', 'pH', 'Temperature', 'EC', 'TDS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data to CSV
        writer.writerow({'Timestamp': current_time, 'State': state,
                         'pH': ph_value, 'Temperature': temperature,
                         'EC': ec_value, 'TDS': tds_value})

# Main loop
while True :
    # Read sensor values
    ph_value = read_ph_value()
    temperature = read_temperature()
    ec_value, tds_value = read_ec_tds_values()

     # Display values on OLED
    disp.clear()
    disp.draw.text((0, 0), f'pH: {ph_value:0.2f}', font=None, fill=1)
    disp.draw.text((0, 16), f'Temperature: {temperature:.2f}°C', font=None, fill=1)
    disp.draw.text((0, 32), f'EC: {ec_value:.2f} μS/cm', font=None, fill=1)
    disp.draw.text(0, 48), f'TDS)
