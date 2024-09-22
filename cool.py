
import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board

# Create the I2C interface
i2c = busio.I2C(3, 2)  # (SCL, SDA)

# Create the OLED display
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(5)

# New variable to control the size of the smiley
size = 20  # Change this variable to control the size of the smiley

def bounce_animation(size, speed_multiplier=1):
    x, y = size, size
    dx, dy = 2 * speed_multiplier, 1 * speed_multiplier  # Speed multiplied by a factor

    while True:
        oled.fill(0)  # Clear the display
        
        oled.circle(x, y, 10, 1)  # Body

        # Draw the wings (lines)
        oled.line(x - 10, y, x - 20, y - 5, 1)  # Left wing
        oled.line(x - 10, y, x - 20, y + 5, 1)  # Left wing
        oled.line(x + 10, y, x + 20, y - 5, 1)  # Right wing
        oled.line(x + 10, y, x + 20, y + 5, 1)  # Right wing

        # Draw the beak (triangle using lines)
        oled.line(x + 10, y, x + 15, y, 1)  # Right side of beak
        oled.line(x + 10, y, x + 10, y + 5, 1)  # Bottom of beak

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

# Start the animation with a size variable and a speed multiplier
bounce_animation(size, speed_multiplier=5)  # Increasing speed by multiplying direction
