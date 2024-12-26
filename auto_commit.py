import os
import time
from datetime import datetime
import subprocess

# Path to your repository
repo_path = os.getcwd()

# Change the file that will be modified
file_path = os.path.join(repo_path, "example.txt")

# Function to modify the file
def modify_file():
    with open(file_path, "a") as f:
        # Append the current time to the file
        f.write(f"Changes made at {datetime.now()}\n")

# Function to run Git commands
def git_commit_push():
    subprocess.run(["git", "add", file_path], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", "Automated commit at " + str(datetime.now())], cwd=repo_path)
    subprocess.run(["git", "push"], cwd=repo_path)

# Main loop to make changes and commit every 15 minutes
while True:
    modify_file()  # Modify the file
    git_commit_push()  # Commit and push the changes
    time.sleep(15 * 60)  # Wait for 15 minutes before running again
