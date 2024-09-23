import time
import busio
from adafruit_ssd1306 import SSD1306_I2C
import board
# import bird_animation
import rocket_animation



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
def duplicate_frame(frame_data, width=128, height=32):
    expanded_frame = []
    
    # Iterar sobre cada fila de bytes (cada fila contiene width/8 bytes)
    for row in range(height):
        start = row * (width // 8)
        end = start + (width // 8)
        
        # Obtener una fila completa del frame original
        row_data = frame_data[start:end]
        
        # Duplicar la fila y añadirla dos veces al frame expandido
        expanded_frame.extend(row_data)  # Primera vez
        expanded_frame.extend(row_data)  # Segunda vez (duplicación)
    
    return expanded_frame
def expand_frames(frames):
    expanded_frames = []
    for frame in frames:
        expanded_frames.append(duplicate_frame(frame))
    return expanded_frames

expanded_python_frames = expand_frames(rocket_animation.frames)
# import frame1
# import frame2
def play_animation(frames, delay=0.1):
    for frame in frames:
        draw_frame(frame)
        time.sleep(delay)  # Controla la velocidad de la animación
    
    # draw_frame(frame1.frame)
    # time.sleep(3)
    # draw_frame(frame2.frame)
    # time.sleep(3)
import expanded_rocket_animation
# Iniciar la animación
play_animation(expanded_rocket_animation)
