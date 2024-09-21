import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board
import socket
import psutil

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "No IP"

# Create the I2C interface
i2c = busio.I2C(3, 2)  # (SCL, SDA)

# Create the OLED display
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(5)

# Record the start time
start_time = time.time()

def display_animation(ip_address, cpu_usage, mem_usage, elapsed_time):
    oled.fill(0)  # Clear the display

    # Display static text
    oled.text('IP Address:', 0, 0, 1)
    
    # Scroll IP address
    ip_len = len(ip_address)
    for i in range(-128, ip_len + 1):
        oled.fill(0)  # Clear before drawing
        oled.text(ip_address[i:i + 128], i, 10, 1)  # Scroll effect
        oled.text(f'CPU Usage: {cpu_usage}%', 0, 20, 1)
        oled.text(f'Mem Usage: {mem_usage}%', 0, 30, 1)
        oled.text(f'Time Elapsed: {int(elapsed_time)}s', 0, 40, 1)
        oled.show()
        time.sleep(0.05)  # Adjust speed of scrolling

while True:
    # Get CPU and memory usage
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    
    # Get the current IP address
    ip_address = get_ip_address()
    
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    
    # Display animation with updated values
    display_animation(ip_address, cpu_usage, mem_usage, elapsed_time)
    
    time.sleep(2)  # Wait before next update
