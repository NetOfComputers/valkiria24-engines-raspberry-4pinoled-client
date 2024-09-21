import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board

# Create the I2C interface
i2c = busio.I2C(3, 2)  # (SCL, SDA)

# Create the OLED display
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(5)

def bounce_smiley():
    x, y = 0, 0
    dx, dy = 2, 1  # Movement direction

    while True:
        oled.fill(0)  # Clear the display
        
        # Draw a simple smiley face
        oled.circle(x + 10, y + 10, 10, 1)  # Head
        oled.fill_circle(x + 7, y + 7, 2, 1)  # Left eye
        oled.fill_circle(x + 13, y + 7, 2, 1)  # Right eye
        oled.fill_rect(x + 7, y + 12, 6, 1, 1)  # Mouth

        # Update the OLED display
        oled.show()
        
        # Move the smiley
        x += dx
        y += dy

        # Bounce off walls
        if x <= 0 or x >= 118:
            dx *= -1
        if y <= 0 or y >= 54:
            dy *= -1
        
        time.sleep(0.05)  # Animation speed

# Start the animation
bounce_smiley()
