import rawpy
import imageio
import os

def convert_cr2_to_png(source_dir, output_dir):
    # Check if output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.cr2'):
            # Construct full file path
            file_path = os.path.join(source_dir, filename)
            # Process the CR2 file
            with rawpy.imread(file_path) as raw:
                # Postprocess to get an RGB image, adjust the quality settings as needed
                rgb = raw.postprocess()
            # Construct output file path
            output_file_path = os.path.join(output_dir, filename[:-4] + '.png')
            # Save as PNG
            imageio.imwrite(output_file_path, rgb)
            print(f"Converted {filename} to PNG and saved to {output_file_path}")

# Example usage
source_directory = '/Users/maxx/Desktop/100CANON'
output_directory = '/Users/maxx/Desktop/savded'
convert_cr2_to_png(source_directory, output_directory)
