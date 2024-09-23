import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board
import engine_animation

# Create the I2C interface
i2c = busio.I2C(3, 2)  # (SCL, SDA)

# Create the OLED display
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(5)  # Set contrast

def draw_frame(frame_data):
    oled.fill(0)  # Clear the display
    
    width = 64  # Original frame width
    height = 32  # Original frame height
    
    for byte_idx in range(512):  # Loop through all 512 bytes
        byte = frame_data[byte_idx]  # Get the current byte
        x = (byte_idx % width) * 2  # Determine the x coordinate (scaled by 2)
        y = (byte_idx // width) * 8 * 2  # Determine the y coordinate (scaled by 2)
        
        # Each byte corresponds to 8 vertical pixels (bits in the byte)
        for bit in range(8):
            pixel_on = (byte >> (7 - bit)) & 1  # Extract the bit for each pixel
            if pixel_on:
                # Scale the pixel to 2x2 block for the 128x64 screen
                oled.pixel(x, y + bit * 2, 1)  # Top-left of the 2x2 block
                oled.pixel(x + 1, y + bit * 2, 1)  # Top-right of the 2x2 block
                oled.pixel(x, y + bit * 2 + 1, 1)  # Bottom-left of the 2x2 block
                oled.pixel(x + 1, y + bit * 2 + 1, 1)  # Bottom-right of the 2x2 block
    
    oled.show()  # Update the display with the new frame

def play_animation(frames, delay=0.1):
    for frame in frames:
        draw_frame(frame)  # Draw each frame
        time.sleep(delay)  # Wait between frames

# Play the animation
play_animation(engine_animation.frames)
