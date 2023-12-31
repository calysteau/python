import argparse
import os
from tqdm import tqdm
import rasterio
from rasterio.shutil import copy
import copy as python_copy  # Import the copy method from the built-in copy module

# Create an argument parser
parser = argparse.ArgumentParser(description='Convert GeoTIFF files to Cloud Optimized GeoTIFF (COG).')
parser.add_argument('--input_geotiff_dir', required=True, help='Directory containing GeoTIFF files to convert.')
parser.add_argument('--output_cog_dir', required=True, help='Output directory for the converted COG files.')
args = parser.parse_args()

# Directories for GeoTIFF and COG files
input_geotiff_dir = args.input_geotiff_dir
output_cog_dir = args.output_cog_dir

# Create output directory for COGs
if not os.path.exists(output_cog_dir):
    os.makedirs(output_cog_dir)


# Function to convert a GeoTIFF file to COG
def convert_geotiff_to_cog(geotiff_path, cog_dir):
    with rasterio.open(geotiff_path) as src:
        profile = python_copy.copy(src.profile)  # Use the copy method to copy the profile
        profile.update(driver='GTiff', tiled=True, blockxsize=512, blockysize=512, compress='LZW')

        relative_path = os.path.relpath(geotiff_path, input_geotiff_dir)
        path_without_extension, _ = os.path.splitext(relative_path)
        cog_file_path = os.path.join(cog_dir, path_without_extension + ".tif")

        os.makedirs(os.path.dirname(cog_file_path), exist_ok=True)

        copy(src, cog_file_path, copy_src_overviews=True, **profile)


# Count total number of GeoTIFF files
total_geotiff_files = sum(1 for _, _, files in os.walk(input_geotiff_dir) for file in files if file.endswith(".tif"))

# Progress bar
progress_bar = tqdm(total=total_geotiff_files, unit="file")

# Loop through and convert GeoTIFF files to COG
for folder, _, files in os.walk(input_geotiff_dir):
    for file in files:
        if file.endswith(".tif"):
            geotiff_file_path = os.path.join(folder, file)
            convert_geotiff_to_cog(geotiff_file_path, output_cog_dir)
            progress_bar.update(1)

# Close the progress bar
progress_bar.close()

print("COG conversion completed.")
