# file_handler.py
# This module handles reading from and writing to the JSON data file.

import json  # Built-in module to work with JSON data (comes with core Python)

FILE_NAME = "records.json"   # The name of our data file (constant, hence CAPS)


def load_records():
    """
    Loads all records from the JSON file.
    If the file doesn't exist yet (first time running the app),
    it returns an empty list instead of crashing.
    """
    try:
        with open(FILE_NAME, "r") as file:   # Open the file in "read" mode
            data = json.load(file)           # Convert JSON text into a Python list
            return data
    except FileNotFoundError:
        # This runs if records.json doesn't exist yet — perfectly normal on first run
        return []
    except json.JSONDecodeError:
        # This runs if the file exists but is empty or has broken/corrupted JSON
        print("Warning: Data file was empty or corrupted. Starting fresh.")
        return []


def save_records(records):
    """
    Saves the given list of records into the JSON file.
    Overwrites the old file content with the updated data.
    """
    try:
        with open(FILE_NAME, "w") as file:        # Open file in "write" mode
            json.dump(records, file, indent=4)    # Convert Python list -> JSON, write to file
    except Exception as e:
        # Catches any unexpected error during saving (e.g., disk full, permission issue)
        print(f"Error saving data: {e}")