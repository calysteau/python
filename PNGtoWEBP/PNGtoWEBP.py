import argparse
from PIL import Image
import os
from tqdm import tqdm

# Create an argument parser
parser = argparse.ArgumentParser(description='Convert PNG images to WebP images while preserving transparency.')
parser.add_argument('--input_png_dir', required=True, help='Directory containing PNG images to be converted.')
parser.add_argument('--output_webp_dir', required=True, help='Output directory for the converted WebP images.')
args = parser.parse_args()

# Directories
input_png_dir = args.input_png_dir
output_webp_dir = args.output_webp_dir

if not os.path.exists(output_webp_dir):
    os.makedirs(output_webp_dir)


# Function to convert a PNG image to WebP while preserving transparency
def convert_png_to_webp(png_path, output_dir):
    image = Image.open(png_path)
    relative_path = os.path.relpath(png_path, input_png_dir)
    path_without_extension, _ = os.path.splitext(relative_path)
    webp_file_path = os.path.join(output_dir, path_without_extension + ".webp")
    os.makedirs(os.path.dirname(webp_file_path), exist_ok=True)
    image.save(webp_file_path, "webp", quality=95, lossless=True)


total_png_files = sum(1 for _, _, files in os.walk(input_png_dir) for file in files if file.endswith(".png"))
progress_bar = tqdm(total=total_png_files, unit="image")

for folder, _, files in os.walk(input_png_dir):
    for file in files:
        if file.endswith(".png"):
            png_file_path = os.path.join(folder, file)
            convert_png_to_webp(png_file_path, output_webp_dir)
            progress_bar.update(1)

progress_bar.close()
print("Conversion completed.")
