import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import rawpy
import tempfile

source_directory = '/Users/maxx/Desktop/100CANON'
output_directory = '/Users/maxx/Desktop/savded'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Function to convert and compress a single CR2 file
def process_file(filename):
    if filename.lower().endswith('.cr2'):
        cr2_path = os.path.join(source_directory, filename)
        compressed_png_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}_compressed.png')

        try:
            # Convert CR2 to PNG and resize
            with rawpy.imread(cr2_path) as raw:
                rgb_image = raw.postprocess()
                image = Image.fromarray(rgb_image)

                # Resize image if width is greater than 1920 pixels
                max_width = 1920
                if image.width > max_width:
                    ratio = max_width / image.width
                    new_height = int(image.height * ratio)
                    image = image.resize((max_width, new_height), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
                    print(f'Resized {filename} to {max_width}px width.')

                with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_png:
                    image.save(temp_png.name, 'PNG')
                    temp_png_path = temp_png.name

            # Compress PNG using pngquant
            result = subprocess.run(
                ['pngquant', '--quality=65-80', '--output', compressed_png_path, '--force', temp_png_path],
                check=False, capture_output=True
            )

            if result.returncode != 0:
                raise Exception(f'pngquant failed for {filename} with message: {result.stderr.decode().strip()}')

            print(f'Compressed {filename} to {compressed_png_path}.')

            # Remove temporary PNG file
            os.remove(temp_png_path)
            print(f'Removed temporary file {temp_png_path}.')

        except Exception as e:
            print(f'Error processing {filename}: {e}')

# Main function to handle all files in the directory
def convert_and_compress_cr2(source_dir, output_dir):
    filenames = [f for f in os.listdir(source_dir) if f.lower().endswith('.cr2')]

    # Limit the number of concurrent threads to 5
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(process_file, filenames)

# Convert and compress all CR2 files in the source directory
convert_and_compress_cr2(source_directory, output_directory)
