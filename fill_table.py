"""This file was created with the help of chatGPT"""

import glob
import subprocess

instances = []

for file_path in glob.glob("from_thore/data/*.txt"):
    file_name = file_path.split("/")[-1]  # Get the filename only (without the path)
    instances.append(file_name)

instances.sort()

# Dictionary to store filename -> output mapping
print("Processing nodes...")
results_nodes = {}

for file_path in glob.glob("from_thore/data/*.txt"):
    file_name = file_path.split("/")[-1]  # Get the filename only (without the path)

    with open(file_path, "r") as f:
        try:
            # Run the subprocess and capture the output
            result = subprocess.run(
                [
                    "python3",
                    "get_n.py",
                ],  # Run the script (can be replaced with your script)
                stdin=f,  # Provide input via stdin
                capture_output=True,  # Capture stdout and stderr
                text=True,  # Make sure the output is captured as text
            )

            # Store the filename and its corresponding output in the dictionary
            print(".", end="")
            results_nodes[
                file_name
            ] = result.stdout.strip()  # .strip() to remove any extra newlines

        except subprocess.TimeoutExpired:
            print(f"Timed out on {file_name}")
            results_nodes[file_name] = None  # Store None for timeout cases

print()
print("Processing none...")
results_none = {}

for file_path in glob.glob("from_thore/data/*.txt"):
    file_name = file_path.split("/")[-1]  # Get the filename only (without the path)

    with open(file_path, "r") as f:
        try:
            # Run the subprocess and capture the output
            result = subprocess.run(
                [
                    "python3",
                    "none.py",
                ],  # Run the script (can be replaced with your script)
                stdin=f,  # Provide input via stdin
                capture_output=True,  # Capture stdout and stderr
                text=True,  # Make sure the output is captured as text
            )

            # Store the filename and its corresponding output in the dictionary
            print(".", end="")
            results_none[
                file_name
            ] = result.stdout.strip()  # .strip() to remove any extra newlines

        except subprocess.TimeoutExpired:
            print(f"Timed out on {file_name}")
            results_none[file_name] = None  # Store None for timeout cases

print()
print("Processing few...")
results_few = {}

for file_path in glob.glob("from_thore/data/*.txt"):
    file_name = file_path.split("/")[-1]  # Get the filename only (without the path)

    with open(file_path, "r") as f:
        try:
            # Run the subprocess and capture the output
            result = subprocess.run(
                [
                    "python3",
                    "few.py",
                ],  # Run the script (can be replaced with your script)
                stdin=f,  # Provide input via stdin
                capture_output=True,  # Capture stdout and stderr
                text=True,  # Make sure the output is captured as text
            )

            # Store the filename and its corresponding output in the dictionary
            print(".", end="")
            results_few[
                file_name
            ] = result.stdout.strip()  # .strip() to remove any extra newlines

        except subprocess.TimeoutExpired:
            print(f"Timed out on {file_name}")
            results_few[file_name] = None  # Store None for timeout cases

print()
print("Processing alternating...")
results_alternate = {}

for file_path in glob.glob("from_thore/data/*.txt"):
    file_name = file_path.split("/")[-1]  # Get the filename only (without the path)

    with open(file_path, "r") as f:
        try:
            # Run the subprocess and capture the output
            result = subprocess.run(
                [
                    "python3",
                    "alternate.py",
                ],  # Run the script (can be replaced with your script)
                stdin=f,  # Provide input via stdin
                capture_output=True,  # Capture stdout and stderr
                text=True,  # Make sure the output is captured as text
            )

            # Store the filename and its corresponding output in the dictionary
            print(".", end="")
            results_alternate[
                file_name
            ] = result.stdout.strip()  # .strip() to remove any extra newlines

        except subprocess.TimeoutExpired:
            print(f"Timed out on {file_name}")
            results_alternate[file_name] = None  # Store None for timeout cases

print()
print("Processing many...")
results_many = {}

for file_path in glob.glob("from_thore/data/*.txt"):
    file_name = file_path.split("/")[-1]  # Get the filename only (without the path)

    with open(file_path, "r") as f:
        try:
            # Run the subprocess and capture the output
            result = subprocess.run(
                [
                    "python3",
                    "many.py",
                ],  # Run the script (can be replaced with your script)
                stdin=f,  # Provide input via stdin
                capture_output=True,  # Capture stdout and stderr
                text=True,  # Make sure the output is captured as text
            )

            # Store the filename and its corresponding output in the dictionary
            print(".", end="")
            results_many[
                file_name
            ] = result.stdout.strip()  # .strip() to remove any extra newlines

        except subprocess.TimeoutExpired:
            print(f"Timed out on {file_name}")
            results_many[file_name] = None  # Store None for timeout cases


# Create or overwrite the 'results.txt' file and write the table header
print()
print("Writing results...")
with open("results.txt", "w") as f:
    # Write the header line to the file
    f.write("Instance name\t\tn\t\tA\t\tF\t\tM\t\tN\n")

    # Iterate over each file in results_none (or any dictionary, since they should have the same keys)
    for file_name in instances:
        # Remove the '.txt' from the file name
        instance_name = file_name.split(".")[0]  # Remove the .txt extension

        # Get results from each dictionary. If a result is None, use a placeholder (e.g., "Timeout" or "-1")
        nodes = results_nodes.get(
            file_name, "Timeout" if results_nodes.get(file_name) is None else "-1"
        )
        A = results_alternate.get(
            file_name, "Timeout" if results_alternate.get(file_name) is None else "-1"
        )
        F = results_few.get(
            file_name, "Timeout" if results_few.get(file_name) is None else "-1"
        )
        M = results_many.get(
            file_name, "Timeout" if results_many.get(file_name) is None else "-1"
        )
        N = results_none.get(
            file_name, "Timeout" if results_none.get(file_name) is None else "-1"
        )

        # Write each row in the desired format
        f.write(f"{instance_name}\t\t{nodes}\t\t{A}\t\t{F}\t\t{M}\t\t{N}\n")
