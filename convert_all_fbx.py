import os
import json
import subprocess
from tqdm import tqdm

def convert_files(config):
    # Extracting configuration
    source_directory = config["source_directory"]
    destination_directory = config["destination_directory"]
    fbx_converter_path = config["fbx_converter_path"]
    source_format = config["source_format"]
    destination_format = config["destination_format"]
    fbx_mode = config.get("fbx_mode", "binary")  # Default to binary if not specified

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Collect all the FBX files in the source directory and its sub-directories
    all_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(source_directory) for f in filenames if f.endswith('.fbx')]

    # Convert each FBX file
    for source_path in tqdm(all_files, desc="Converting files", unit="file"):
        relative_path = os.path.relpath(source_path, source_directory)
        dest_path = os.path.join(destination_directory, relative_path)

        # Create any necessary sub-directories in the destination
        dest_dir = os.path.dirname(dest_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Convert the file using FBXCONVERTER
        conversion_command = [fbx_converter_path, source_path, dest_path, f"/sff{source_format}", f"/dff{destination_format}", "/l"]
        if source_format.lower() == "fbx" and destination_format.lower() == "fbx":
            conversion_command.append(f"/fbx{fbx_mode}")

        subprocess.run(conversion_command)

if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)
    convert_files(config)
