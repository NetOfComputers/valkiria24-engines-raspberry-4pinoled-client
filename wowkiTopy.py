import re

# Función que convierte el array de Arduino a Python
def arduino_to_python_array(arduino_code):
    # Usar expresiones regulares para extraer los arrays de números
    array_pattern = r'\{([0-9,\s]*)\}'
    matches = re.findall(array_pattern, arduino_code)
    
    python_arrays = []

    # Iterar sobre cada match y convertirlo en una lista de enteros
    for match in matches:
        # Eliminar espacios y separar los números por comas
        byte_values = match.strip().split(',')
        # Convertir los valores a enteros
        byte_values = [int(value) for value in byte_values if value.strip().isdigit()]
        # Añadir el array convertido a la lista de Python
        python_arrays.append(byte_values)

    return python_arrays

filename = 'rocket'

# Leer el archivo de texto con el código Arduino
with open(f'{filename}.arduino.txt', 'r') as f:
    arduino_code = f.read()

# Convertir el código Arduino a un array de Python
python_frames = arduino_to_python_array(arduino_code)

# Imprimir el resultado en formato Python
with open(f'{filename}_animation.py','w') as bi:
    bi.write("frames = [")
    for frame in python_frames:
        bi.write(f"    {frame},")
    bi.write("]")
