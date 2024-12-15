import time
import board
import adafruit_dht

# Create a DHT11 sensor object using GPIO4
dht_sensor = adafruit_dht.DHT11(board.D4)  # board.D4 corresponds to GPIO4

# Open a log file in append mode
log_file_path = '/home/bjam/Documents/PerejilesLemonade/valkiria24-engines-raspberry-4pinoled-client/dht_log.txt'

while True:
    try:
        # Read the temperature and humidity
        temperature_c = dht_sensor.temperature
        humidity = dht_sensor.humidity
        
        # Get the current time for the log entry
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        if temperature_c is not None and humidity is not None:
            log_entry = f'{current_time} - Temperature: {temperature_c}°C, Humidity: {humidity}%\n'
            print(log_entry.strip())  # Print to console
            # Write the log entry to the log file
            with open(log_file_path, 'a') as log_file:
                log_file.write(log_entry)
        else:
            print('Failed to retrieve data from sensor')

    except RuntimeError as e:
        # Handle any read errors
        print(f'RuntimeError: {e}')
    
    time.sleep(5)  # Wait before the next reading
