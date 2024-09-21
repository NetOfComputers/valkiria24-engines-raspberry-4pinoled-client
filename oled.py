
import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board
import socket
import psutil  # Make sure to install psutil library

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

# Function to draw a big smiley face
def draw_smiley(x, y):
    oled.circle(x, y, 15, 1)  # Face
    oled.fill_rect(x - 5, y - 5, 5, 5, 1)  # Left eye
    oled.fill_rect(x + 5, y - 5, 5, 5, 1)  # Right eye
    oled.arc(x, y + 5, 10, 180, 360, 1)  # Smile

# Loop to keep updating the display
while True:
    # Clear the display
    oled.fill(0)

    # Get the current IP address
    ip_address = get_ip_address()

    if ip_address == "No IP":
        # Show the smiley face while no IP address
        draw_smiley(64, 32)  # Centered position for smiley
    else:
        # Get CPU and memory usage
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        # Prepare the display text
        oled.text('IP Address:', 0, 0, 1)
        oled.text(ip_address, 0, 10, 1)  # Display the IP on the next line
        oled.text(f'CPU Usage: {cpu_usage}%', 0, 20, 1)
        oled.text(f'Mem Usage: {mem_usage}%', 0, 30, 1)

    # Update the OLED display
    oled.show()
    
    time.sleep(2)  # Update every 2 seconds






# import time
# import busio
# from adafruit_ssd1306 import SSD1306_I2C
# import board
# import socket
# import psutil  # Make sure to install psutil library

# def get_ip_address():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("8.8.8.8", 80))
#         ip = s.getsockname()[0]
#         s.close()
#         return ip
#     except Exception:
#         return "No IP"

# # Create the I2C interface
# i2c = busio.I2C(3, 2)  # (SCL, SDA)

# # Create the OLED display
# oled = SSD1306_I2C(128, 64, i2c)
# oled.contrast(5)

# # Record the start time
# start_time = time.time()

# # Loop to keep updating the display
# while True:
    
    
#     # Clear the display
#     oled.fill(0)
    
#     # Get CPU and memory usage
#     cpu_usage = psutil.cpu_percent()
#     mem_usage = psutil.virtual_memory().percent
    
#     # Get the current IP address
#     ip_address = get_ip_address()
    
#     # Calculate elapsed time
#     elapsed_time = time.time() - start_time
    
#     # Prepare the display text
#     oled.text('IP Address:', 0, 0, 1)
#     oled.text(ip_address, 0, 10, 1)  # Display the IP on the next line
#     oled.text(f'CPU Usage: {cpu_usage}%', 0, 20, 1)
#     oled.text(f'Mem Usage: {mem_usage}%', 0, 30, 1)
#     oled.text(f'Time Elapsed: {int(elapsed_time)}s', 0, 40, 1)
    
#     # Update the OLED display
#     oled.show()
    
#     time.sleep(2)  # Update every 2 seconds
