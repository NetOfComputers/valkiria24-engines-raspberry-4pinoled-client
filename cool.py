# import time
# import busio
# from adafruit_ssd1306 import SSD1306_I2C
# import board

# # Create the I2C interface
# i2c = busio.I2C(3, 2)  # (SCL, SDA)

# # Create the OLED display
# oled = SSD1306_I2C(128, 64, i2c)
# oled.contrast(5)

# def draw_smiley(x, y):
#     # Draw a big smiley face
#     oled.circle(x, y, 15, 1)  # Face
#     oled.fill_rect(x - 5, y - 5, 5, 5, 1)  # Left eye
#     oled.fill_rect(x + 5, y - 5, 5, 5, 1)  # Right eye
#     oled.arc(x, y + 5, 10, 180, 360, 1)  # Smile

# def display_smiley():
#     x, y = 64, 32  # Centered position on the screen

#     oled.fill(0)  # Clear the display
#     draw_smiley(x, y)  # Draw the big smiley face
#     oled.show()  # Update the display

# # Display the smiley face
# display_smiley()


# import time
# import busio
# from adafruit_ssd1306 import SSD1306_I2C
# import board

# # Create the I2C interface
# i2c = busio.I2C(3, 2)  # (SCL, SDA)

# # Create the OLED display
# oled = SSD1306_I2C(128, 64, i2c)
# oled.contrast(5)

# def draw_bird(x, y):
#     # Body (oval-shaped by using multiple overlapping rectangles)
#     oled.fill_rect(x, y, 12, 5, 1)  # Main body
#     oled.fill_rect(x + 1, y - 1, 10, 5, 1)  # Upper part of the body
#     oled.fill_rect(x + 2, y - 2, 8, 5, 1)  # Uppermost part of the body
    
#     # Eye (slightly larger for more detail)
#     oled.fill_rect(x + 3, y - 3, 3, 3, 1)  # Eye
    
#     # Beak (small triangle using lines)
#     oled.line(x + 1, y + 1, x - 2, y, 1)  # Beak top line
#     oled.line(x - 2, y, x + 1, y + 3, 1)  # Beak bottom line
    
#     # Wing (curved lines to show feathers)
#     oled.line(x + 6, y + 1, x + 11, y - 3, 1)  # Top of the wing
#     oled.line(x + 11, y - 3, x + 8, y + 2, 1)  # Bottom of the wing
    
#     # Tail (more angled, defined lines)
#     oled.line(x + 12, y - 2, x + 14, y - 5, 1)  # Top tail feather
#     oled.line(x + 12, y, x + 15, y + 2, 1)  # Bottom tail feather
#     oled.line(x + 14, y - 5, x + 15, y + 2, 1)  # Tail connecting line

# def bounce_bird():
#     x, y = 10, 20
#     dx, dy = 2, 1  # Movement direction

#     while True:
#         oled.fill(0)  # Clear the display
        
#         draw_bird(x, y)  # Draw the bird

#         # Update the OLED display
#         oled.show()
        
#         # Move the bird
#         x += dx
#         y += dy

#         # Bounce off walls
#         if x >= 118 or x <= 0:
#             dx *= -1
#         if y >= 54 or y <= 0:
#             dy *= -1
        
#         time.sleep(0.05)  # Animation speed

# # Start the animation
# bounce_bird()



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
            oled.contrast(30)
            dx *= -1
        if y <= size or y >= (64 - size):
            oled.contrast(30)
            dy *= -1
        oled.contrast(5)
        time.sleep(0.05)  # Animation speed

# Start the animation with a size variable and a speed multiplier
bounce_animation(size, speed_multiplier=5)  # Increasing speed by multiplying direction
