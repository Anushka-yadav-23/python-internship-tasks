# ==========================================
# Task 1 - File Handling and Automation
# Internship Project
# ==========================================

import os
import shutil

try:
    print("Starting File Automation Project...\n")

    # Source file
    source_file = "sample.txt"

    # Output folder
    output_folder = "output"

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read file content
    with open(source_file, "r") as file:
        content = file.read()

    print("Original File Content:")
    print(content)

    # Write content to a new file
    copied_file = os.path.join(output_folder, "copied_sample.txt")

    with open(copied_file, "w") as file:
        file.write(content)

    print("\nFile copied successfully.")

    # Rename file
    renamed_file = os.path.join(output_folder, "renamed_sample.txt")
    os.rename(copied_file, renamed_file)

    print("File renamed successfully.")

    # Create archive folder
    archive_folder = os.path.join(output_folder, "archive")

    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    # Move file
    moved_file = os.path.join(
        archive_folder,
        "renamed_sample.txt"
    )

    shutil.move(renamed_file, moved_file)

    print("File moved successfully.")

    # Create temporary file
    temp_file = os.path.join(output_folder, "temp.txt")

    with open(temp_file, "w") as file:
        file.write("This is a temporary file.")

    print("Temporary file created.")

    # Delete temporary file
    os.remove(temp_file)

    print("Temporary file deleted successfully.")

    print("\nAutomation Completed Successfully!")

except FileNotFoundError:
    print("Error: Source file not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)