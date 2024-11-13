import glob
import subprocess

for file_path in glob.glob('from_thore/data/*.txt'):
    print(f"Processing file: {file_path}")
    with open(file_path, 'r') as f:
        try:
            subprocess.run(['python3', 'main.py'], stdin=f)  # Direct file to stdin
        except subprocess.TimeoutExpired:
            print(f"Timed out on {file_path}")