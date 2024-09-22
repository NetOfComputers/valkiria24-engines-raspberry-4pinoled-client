
import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board

# Create the I2C interface
i2c = busio.I2C(3, 2)  # (SCL, SDA)

CONTRAST = 5
MAX_CONTRAST = 60

# Create the OLED display
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(CONTRAST)

# New variable to control the size of the smiley
size = 20  # Change this variable to control the size of the smiley
maxBounceTimes = 20
bounced = False
bounceContrastTimes = maxBounceTimes
def bounce_animation(size, speed_multiplier=1):
    global bounced, bounceContrastTimes
    x, y = size, size
    dx, dy = 2 * speed_multiplier, 1 * speed_multiplier  # Speed multiplied by a factor

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
            bounced = True
            oled.contrast(MAX_CONTRAST)
            dx *= -1
        if y <= size or y >= (64 - size):
            bounced = True
            oled.contrast(MAX_CONTRAST)
            dy *= -1
        if bounced:
            if bounceContrastTimes>0:
                bounceContrastTimes -= 1
            else:
                bounceContrastTimes=maxBounceTimes
                bounced=False
                oled.contrast(CONTRAST)
        time.sleep(0.01)  # Animation speed

# Start the animation with a size variable and a speed multiplier
bounce_animation(size, speed_multiplier=7)  # Increasing speed by multiplying direction
