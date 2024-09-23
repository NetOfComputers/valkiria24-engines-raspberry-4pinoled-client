import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board
# import bird_animation
# import rocket_animation
import engine_animation


# Create the I2C interface
i2c = busio.I2C(3, 2)  # (SCL, SDA)

CONTRAST = 5
MAX_CONTRAST = 60

# Create the OLED display
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(CONTRAST)

# oled.fill(1)
def draw_frame(frame_data):
    oled.fill(0)
    """
    Draw a frame (64x32) on a 128x64 OLED screen by scaling it up 2x.
    :param oled: The OLED display object (with a .pixel() method)
    :param frame_data: List of 512 integers, each representing 8 vertical pixels
    """
    width = 64
    height = 32
    
    for byte_idx in range(512):
        byte = frame_data[byte_idx]
        x = (byte_idx % width) * 2  # Determine the x coordinate (scaled)
        y = (byte_idx // width) * 8 * 2  # Determine the y coordinate (scaled, 8 vertical pixels per byte)

        # Each byte corresponds to 8 vertical pixels (bits)
        for bit in range(8):
            pixel_on = (byte >> (7 - bit)) & 1  # Extract the bit for each pixel
            if pixel_on:
                # Draw a 2x2 block for each pixel
                oled.pixel(x, y + bit * 2, 1)
                oled.pixel(x + 1, y + bit * 2, 1)
                oled.pixel(x, y + bit * 2 + 1, 1)
                oled.pixel(x + 1, y + bit * 2 + 1, 1)
        
    oled.show()  # Actualiza la pantalla            
def play_animation(frames, delay=0.1):
    for frame in frames:
        draw_frame(frame)
        time.sleep(delay)

play_animation(engine_animation.frames)