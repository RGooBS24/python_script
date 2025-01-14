import os
import subprocess

# Path to the file containing the counter
file_path = "counter.py"

# Function to update the counter in the file
def update_counter():
    try:
        # Read the file content
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Update the counter value
        for i, line in enumerate(lines):
            if line.startswith("counter = "):
                # Extract the current counter value
                current_value = int(line.split("=")[1].strip())
                # Increment the counter
                new_value = current_value + 1
                lines[i] = f"counter = {new_value}\n"
                print(f"Updated counter to: {new_value}")
                break

        # Write the updated content back to the file
        with open(file_path, "w") as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"Error: {file_path} not found. Creating a new file with counter = 1.")
        with open(file_path, "w") as file:
            file.write("counter = 1\n")

# Function to run Git commands
def run_git_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command '{command}': {result.stderr}")
    else:
        print(f"Command '{command}' ran successfully.")

# Main script execution
if __name__ == "__main__":
    # Update the counter
    update_counter()

    # Stage the changes
    run_git_command("git add counter.py")

    # Commit the changes
    commit_message = "Update counter"
    run_git_command(f"git commit -m \"{commit_message}\"")

    # Push the changes
    run_git_command("git push")
