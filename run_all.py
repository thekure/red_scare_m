import glob
import subprocess

# Changing the argument 'main.py' in line 10 will change what is run for all files.

for file_path in glob.glob('from_thore/data/*.txt'):
    print(f"Processing file: {file_path}")
    with open(file_path, 'r') as f:
        try:
            subprocess.run(['python3', 'main.py'], stdin=f)  # Direct file to stdin
        except subprocess.TimeoutExpired:
            print(f"Timed out on {file_path}")