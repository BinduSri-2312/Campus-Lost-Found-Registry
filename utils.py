# utils.py
# This module contains small helper functions used across the project.

def generate_id(records):
    """
    Generates a unique ID for a new record.
    Logic: If there are no records yet, start with ID 1.
    Otherwise, take the highest existing ID and add 1.
    """
    if len(records) == 0:        # Check if the list of records is empty
        return 1                 # First record gets ID 1
    else:
        # Get all existing IDs from the records list, then pick the maximum
        existing_ids = []
        for record in records:
            existing_ids.append(record["id"])
        return max(existing_ids) + 1   # New ID = highest ID so far + 1


def get_non_empty_input(prompt):
    """
    Keeps asking the user for input until they type something
    (prevents blank/empty entries like item name being "").
    """
    while True:                          # Loop forever until valid input is given
        value = input(prompt).strip()    # Take input and remove extra spaces
        if value == "":                  # If user just pressed Enter (empty)
            print("This field cannot be empty. Please try again.")
        else:
            return value                 # Valid input, return it and exit loop


def get_valid_status():
    """
    Asks the user to choose a status from a fixed list: Lost, Found, Claimed.
    Keeps asking until a valid choice is entered.
    """
    valid_statuses = ["Lost", "Found", "Claimed"]  # Allowed values only
    while True:
        status = input("Enter status (Lost/Found/Claimed): ").strip().title()
        if status in valid_statuses:     # Check if user's input matches allowed list
            return status
        else:
            print("Invalid status. Please enter Lost, Found, or Claimed.")


def get_valid_phone():
    """
    Validates that the contact number is exactly 10 digits.
    """
    while True:
        phone = input("Enter contact number (10 digits): ").strip()
        if phone.isdigit() and len(phone) == 10:   # Must be digits only, length 10
            return phone
        else:
            print("Invalid phone number. Enter exactly 10 digits.")