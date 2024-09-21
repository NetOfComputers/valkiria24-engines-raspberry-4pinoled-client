import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board

# Create the I2C interface
i2c = busio.I2C(3, 2)  # (SCL, SDA)

# Create the OLED display
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(5)

def draw_bird(x, y):
    # Draw a simple bird using triangles and lines
    oled.fill_triangle(x, y, x + 5, y - 5, x + 10, y, 1)  # Body
    oled.line(x + 5, y - 5, x + 5, y - 10, 1)  # Wing
    oled.fill_triangle(x + 5, y, x + 8, y + 3, x + 10, y, 1)  # Tail

def bounce_bird():
    x, y = 10, 20
    dx, dy = 2, 1  # Movement direction

    while True:
        oled.fill(0)  # Clear the display
        
        draw_bird(x, y)  # Draw the bird

        # Update the OLED display
        oled.show()
        
        # Move the bird
        x += dx
        y += dy

        # Bounce off walls
        if x >= 118 or x <= 0:
            dx *= -1
        if y >= 54 or y <= 0:
            dy *= -1
        
        time.sleep(0.05)  # Animation speed

# Start the animation
bounce_bird()



# import time
# import busio
# from adafruit_ssd1306 import SSD1306_I2C
# import board

# # Create the I2C interface
# i2c = busio.I2C(3, 2)  # (SCL, SDA)

# # Create the OLED display
# oled = SSD1306_I2C(128, 64, i2c)
# oled.contrast(5)

# def bounce_animation():
#     x, y = 10, 10
#     dx, dy = 2, 1  # Movement direction

#     while True:
#         oled.fill(0)  # Clear the display
        
#         # Draw a bouncing smiley face using basic shapes
#         oled.circle(x, y, 10, 1)  # Head
#         oled.rect(x - 3, y - 3, 2, 2, 1)  # Left eye
#         oled.rect(x + 1, y - 3, 2, 2, 1)  # Right eye
#         oled.line(x - 5, y + 2, x + 5, y + 2, 1)  # Mouth

#         # Update the OLED display
#         oled.show()
        
#         # Move the smiley
#         x += dx
#         y += dy

#         # Bounce off walls
#         if x <= 10 or x >= 118:
#             dx *= -1
#         if y <= 10 or y >= 54:
#             dy *= -1
        
#         time.sleep(0.05)  # Animation speed

# # Start the animation
# bounce_animation()
