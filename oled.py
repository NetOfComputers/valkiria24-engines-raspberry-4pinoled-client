import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board
import socket
import psutil  # Make sure to install psutil library
import os  # For rebooting

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

# Variables for tracking disconnection time
disconnection_start = None  # To track when disconnection started
disconnection_duration = 0  # To accumulate disconnection time

size = 20
speed_multiplier = 4
x, y = size, size
dx, dy = 2 * speed_multiplier, 1 * speed_multiplier  # Speed multiplied by a factor

# Loop to keep updating the display
while True:
    # Clear the display
    oled.fill(0)

    # Get CPU and memory usage
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    cpu_thermal = str(psutil.sensors_temperatures()['cpu_thermal'][0]).split('current=')[1].split(',')[0]

    # Get the current IP address
    ip_address = get_ip_address()

    if 'No IP' in ip_address:
        # Track disconnection time
        if disconnection_start is None:
            disconnection_start = time.time()  # Start the timer

        # Calculate the disconnection duration
        disconnection_duration = time.time() - disconnection_start

        # If disconnected for more than 30 seconds, reboot
        if disconnection_duration > 30:
            oled.fill(0)  # Clear the display
            oled.text('Rebooting...', 0, 30, 1)
            oled.show()
            time.sleep(1)  # Give some time to display the message
            os.system('sudo reboot')  # Reboot the system

        # Draw a bouncing smiley face using basic shapes
        oled.circle(x, y, size, 1)  # Head (size depends on variable)
        oled.rect(x - size // 3, y - size // 3, size // 5, size // 5, 1)  # Left eye
        oled.rect(x + size // 5, y - size // 3, size // 5, size // 5, 1)  # Right eye
        oled.line(x - size // 2, y + size // 5, x + size // 2, y + size // 5, 1)  # Mouth

        # Update the OLED display
        oled.show()

        # Move the smiley
        x += dx
        y += dy

        # Bounce off walls, taking the size into account
        if x <= size or x >= (128 - size):
            dx *= -1
        if y <= size or y >= (64 - size):
            dy *= -1

        time.sleep(0.05)  # Animation speed

    else:
        # Reset disconnection tracking since we have an IP
        disconnection_start = None
        disconnection_duration = 0

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Prepare the display text
        oled.text('IP Address:', 0, 0, 1)
        oled.text(ip_address, 0, 10, 1)  # Display the IP on the next line
        oled.text(f'CPU Usage: {cpu_usage}%', 0, 20, 1)
        oled.text(f'Mem Usage: {mem_usage}%', 0, 30, 1)
        oled.text(f'Cpu Temp: {cpu_thermal}C', 0, 40, 1)
        oled.text(f'Time Elapsed: {int(elapsed_time)}s', 0, 50, 1)

        # Update the OLED display
        oled.show()

        time.sleep(2)  # Update every 2 seconds
