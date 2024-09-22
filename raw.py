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
def draw_frame_correctly(frame_data):
    oled.fill(0)  # Limpia la pantalla
    
    # Procesar el frame de manera correcta (128x32 en una pantalla de 128x64)
    for byte_index, byte_value in enumerate(frame_data):
        # Calcular las coordenadas de la pantalla
        x = byte_index % 128  # 128 bytes por fila (una fila de 128 píxeles)
        y = (byte_index // 128) * 8  # Cada byte representa 8 píxeles verticales
        
        # Procesar cada bit del byte
        for bit in range(8):
            # Dibuja el píxel correspondiente en la pantalla
            if byte_value & (1 << (7 - bit)):
                oled.pixel(x, y + bit, 1)  # Dibuja el píxel en la posición correcta
            else:
                oled.pixel(x, y + bit, 0)  # Apaga el píxel si no está encendido
    
    oled.show()  # Actualiza la pantalla

# Para pantallas 128
def draw_frame_expanded(frame_data):
    oled.fill(0)  # Limpia la pantalla
    
    for byte_index, byte_value in enumerate(frame_data):
        for bit in range(8):
            # Calcula las coordenadas x e y
            x = (byte_index % 16) * 8 + bit
            y = byte_index // 16
            
            # Duplicar cada píxel verticalmente para expandir a una pantalla de 64 píxeles de alto
            if byte_value & (1 << (7 - bit)):
                oled.pixel(x, y, 1)  # Píxel en la posición original
                oled.pixel(x, y + 32, 1)  # Píxel duplicado debajo para llenar la pantalla
            else:
                oled.pixel(x, y, 0)
                oled.pixel(x, y + 32, 0)
    
    oled.show()  # Actualiza la pantalla


def draw_frame(frame_data):
    oled.fill(0)  # Limpia la pantalla
    
    for byte_index, byte_value in enumerate(frame_data):
        for bit in range(8):
            # Calcula las coordenadas x e y
            x = (byte_index % 16) * 8 + bit  # 16 bytes por fila (128 píxeles / 8 bits por byte)
            y = byte_index // 16  # Cada fila tiene 16 bytes (128 píxeles / 8 bits)
            
            # Dibuja el píxel en función de si el bit está encendido o apagado
            if byte_value & (1 << (7 - bit)):
                oled.pixel(x, y, 1)  # Píxel encendido
            else:
                oled.pixel(x, y, 0)  # Píxel apagado
    
    oled.show()  # Actualiza la pantalla


def play_animation(frames, delay=0.1):
    for frame in frames:
        draw_frame_correctly(frame)
        time.sleep(delay)  # Controla la velocidad de la animación

# Iniciar la animación
play_animation(bird_animation.frames)
