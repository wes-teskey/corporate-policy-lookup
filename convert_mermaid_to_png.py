# convert_mermaid_to_png.py

import os
import subprocess
import sys
from utils_find_data_dir import find_data_directory

def find_mmdc():
    """Find the mmdc executable"""
    if sys.platform.startswith('win'):
        # On Windows, check the default npm global installation path
        user_profile = os.environ.get('USERPROFILE')
        if user_profile:
            mmdc_path = os.path.join(user_profile, 'AppData', 'Roaming', 'npm', 'mmdc.cmd')
            if os.path.exists(mmdc_path):
                return mmdc_path
    
    # On other systems or if not found in the default location, try the PATH
    try:
        subprocess.run(['mmdc', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return 'mmdc'
    except:
        return None

def convert_mermaid_to_png():
    data_dir = find_data_directory()
    mermaid_files = [f for f in os.listdir(data_dir) if f.endswith('_mermaid.txt')]

    mmdc_path = find_mmdc()
    if not mmdc_path:
        print("Error: Mermaid CLI (mmdc) not found. Please install it using 'npm install -g @mermaid-js/mermaid-cli'")
        print("If you've already installed it, you may need to add its location to your system's PATH.")
        return

    for mermaid_file in mermaid_files:
        mermaid_path = os.path.join(data_dir, mermaid_file)
        png_path = os.path.join(data_dir, mermaid_file.replace('_mermaid.txt', '_diagram.png'))

        try:
            subprocess.run([mmdc_path, '-i', mermaid_path, '-o', png_path], check=True)
            print(f"Converted {mermaid_file} to PNG")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {mermaid_file}: {e}")

if __name__ == "__main__":
    convert_mermaid_to_png()
