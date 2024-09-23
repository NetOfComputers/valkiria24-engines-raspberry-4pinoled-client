from PIL import Image
import engine_animation

def save_frame_as_image(frame_data, file_name="frame_image.bmp"):
    """
    Save a 64x32 frame (represented as a 512-byte array) as a 128x64 image file.
    :param frame_data: List of 512 bytes, each representing 8 vertical pixels
    :param file_name: The name of the file to save (e.g., frame_image.bmp)
    """
    width, height = 64, 32  # The original frame size (64x32)
    scale_factor = 2  # To scale the frame to 128x64

    # Create a blank image (grayscale mode "1" for 1-bit pixels)
    img = Image.new("1", (width * scale_factor, height * scale_factor))

    # Iterate over the byte array and set pixels
    for byte_idx in range(512):
        byte = frame_data[byte_idx]
        x = byte_idx % width
        y = byte_idx // width

        # Each byte represents 8 vertical pixels (bits)
        for bit in range(8):
            pixel_on = (byte >> (7 - bit)) & 1  # Extract the bit for each pixel
            if pixel_on:
                # Calculate the scaled pixel positions
                for dx in range(scale_factor):
                    for dy in range(scale_factor):
                        img.putpixel((x * scale_factor + dx, y * scale_factor * 2 + bit * scale_factor + dy), 1)

    # Save the image to the specified file
    img.save(file_name)
    print(f"Frame saved as {file_name}")

# Save the first frame as a bitmap image
save_frame_as_image(engine_animation.frames[0], "frame_image.bmp")
