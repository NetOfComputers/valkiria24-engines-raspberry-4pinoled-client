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
    original_contrast = 5  # Original contrast
    bounce_contrast = 200  # Higher contrast on bounce
    bounce_duration = 0.1  # Duration for the bounce contrast effect

    while True:
        oled.fill(0)  # Clear the display

        # Draw a bouncing smiley face using basic shapes
        oled.circle(x, y, size, 1)  # Head (size depends on variable)
        oled.rect(x - size//3, y - size//3, size//5, size//5, 1)  # Left eye
        oled.rect(x + size//5, y - size//3, size//5, size//5, 1)  # Right eye
        oled.line(x - size//2, y + size//5, x + size//2, y + size//5, 1)  # Mouth

        # Update the OLED display
        oled.show()
        
        # Move the smiley
        x += dx
        y += dy

        # Bounce off walls, taking the size into account
        if x <= size or x >= (128 - size):
            dx *= -1
            oled.contrast(bounce_contrast)  # Set higher contrast on bounce
            time.sleep(bounce_duration)  # Pause briefly
            oled.contrast(original_contrast)  # Return to original contrast
            
        if y <= size or y >= (64 - size):
            dy *= -1
            oled.contrast(bounce_contrast)  # Set higher contrast on bounce
            time.sleep(bounce_duration)  # Pause briefly
            oled.contrast(original_contrast)  # Return to original contrast

        time.sleep(0.01)  # Adjust the animation speed

# Start the animation with a size variable and a speed multiplier
bounce_animation(size, speed_multiplier=2)  # Increasing speed by multiplying direction
