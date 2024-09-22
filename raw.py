import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board
import bird_animation




# Create the I2C interface
i2c = busio.I2C(3, 2)  # (SCL, SDA)

CONTRAST = 5
MAX_CONTRAST = 60

# Create the OLED display
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(CONTRAST)

# Para pantallas 128
def draw_frame(frame_data):
    oled.fill(0)  # Limpia la pantalla
    
    for byte_index, byte_value in enumerate(frame_data):
        for bit in range(8):
            # Calcula las coordenadas x e y
            x = (byte_index % 16) * 8 + bit  # 16 bytes por fila (128 píxeles / 8 bits por byte)
            y = byte_index // 16  # Cada fila tiene 16 bytes (128 píxeles / 8 bits)
            
            # Limitar el dibujo a la mitad superior de la pantalla (asumiendo una pantalla de 128x64)
            if y < 32:
                if byte_value & (1 << (7 - bit)):
                    oled.pixel(x, y, 1)  # Píxel encendido
                else:
                    oled.pixel(x, y, 0)  # Píxel apagado
    
    oled.show()  # Actualiza la pantalla

# def draw_frame(frame_data):
    # oled.fill(0)  # Limpia la pantalla
    
    # for byte_index, byte_value in enumerate(frame_data):
    #     for bit in range(8):
    #         # Calcula las coordenadas x e y
    #         x = (byte_index % 16) * 8 + bit  # 16 bytes por fila (128 píxeles / 8 bits por byte)
    #         y = byte_index // 16  # Cada fila tiene 16 bytes (128 píxeles / 8 bits)
            
    #         # Dibuja el píxel en función de si el bit está encendido o apagado
    #         if byte_value & (1 << (7 - bit)):
    #             oled.pixel(x, y, 1)  # Píxel encendido
    #         else:
    #             oled.pixel(x, y, 0)  # Píxel apagado
    
    # oled.show()  # Actualiza la pantalla


def play_animation(frames, delay=0.1):
    for frame in frames:
        draw_frame(frame)
        time.sleep(delay)  # Controla la velocidad de la animación

# Iniciar la animación
play_animation(bird_animation.frames)
