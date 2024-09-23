import rocket_animation
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

with open('expanded_rocket_animation.py','w') as era:
    era.write(f'[\n{'\n'.join(str(item) for item in expanded_python_frames)}\n]')

