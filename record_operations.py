# record_operations.py
# This module contains the core logic for all 6 features of the app.

import file_handler   # Our own module to load/save records from JSON
import utils           # Our own module for ID generation and input validation


def add_record():
    """
    Feature 1: Add a new lost/found item record.
    """
    records = file_handler.load_records()   # Step 1: Load existing records from file

    print("\n--- Add New Record ---")
    item_name = utils.get_non_empty_input("Enter item name: ")
    description = utils.get_non_empty_input("Enter description: ")
    location = utils.get_non_empty_input("Enter location: ")
    date = utils.get_non_empty_input("Enter date (YYYY-MM-DD): ")
    status = utils.get_valid_status()
    contact = utils.get_valid_phone()

    new_id = utils.generate_id(records)   # Step 2: Generate a unique ID

    # Step 3: Build the record as a dictionary
    new_record = {
        "id": new_id,
        "item_name": item_name,
        "description": description,
        "location": location,
        "date": date,
        "status": status,
        "contact": contact
    }

    records.append(new_record)          # Step 4: Add new record to the list
    file_handler.save_records(records)  # Step 5: Save the updated list back to file

    print(f"Record added successfully! Your Record ID is {new_id}.\n")


def view_all_records():
    """
    Feature 2: Display all records in a readable table format.
    """
    records = file_handler.load_records()

    print("\n--- All Records ---")
    if len(records) == 0:                 # Check if there's nothing to show
        print("No records found.\n")
        return                            # Exit the function early

    # Print a simple table header
    print(f"{'ID':<5}{'Item':<20}{'Location':<20}{'Status':<10}{'Date':<12}")
    print("-" * 67)

    for record in records:                # Loop through each record and print its row
        print(f"{record['id']:<5}{record['item_name']:<20}{record['location']:<20}"
              f"{record['status']:<10}{record['date']:<12}")
    print()


def search_record():
    """
    Feature 3: Search for a record by ID or item name/location keyword.
    """
    records = file_handler.load_records()

    if len(records) == 0:
        print("\nNo records found to search.\n")
        return

    print("\n--- Search Record ---")
    keyword = input("Enter Record ID or keyword (item name/location): ").strip().lower()

    found_records = []   # We'll collect all matches here

    for record in records:
        # Match by ID (convert record id to string to compare with typed text)
        if str(record["id"]) == keyword:
            found_records.append(record)
        # Match by keyword found anywhere in item name or location (case-insensitive)
        elif keyword in record["item_name"].lower() or keyword in record["location"].lower():
            found_records.append(record)

    if len(found_records) == 0:
        print("No matching records found.\n")
    else:
        print(f"\nFound {len(found_records)} matching record(s):")
        for record in found_records:
            print(record)   # Simple print of the dictionary for now
        print()


def update_record():
    """
    Feature 4: Update the status of an existing record (e.g., Lost -> Claimed).
    """
    records = file_handler.load_records()

    if len(records) == 0:
        print("\nNo records found to update.\n")
        return

    print("\n--- Update Record ---")
    try:
        record_id = int(input("Enter the Record ID to update: "))  # Convert text to number
    except ValueError:
        print("Invalid ID. Please enter a number.\n")
        return

    # Search for the record with matching ID
    record_found = None
    for record in records:
        if record["id"] == record_id:
            record_found = record
            break             # Stop looping once we find it

    if record_found is None:
        print("Record not found.\n")
        return

    print(f"Current status: {record_found['status']}")
    new_status = utils.get_valid_status()   # Ask for new status with validation
    record_found["status"] = new_status     # Update the dictionary directly

    file_handler.save_records(records)      # Save the whole updated list back
    print("Record updated successfully!\n")


def delete_record():
    """
    Feature 5: Delete a record by its ID.
    """
    records = file_handler.load_records()

    if len(records) == 0:
        print("\nNo records found to delete.\n")
        return

    print("\n--- Delete Record ---")
    try:
        record_id = int(input("Enter the Record ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.\n")
        return

    record_found = None
    for record in records:
        if record["id"] == record_id:
            record_found = record
            break

    if record_found is None:
        print("Record not found.\n")
        return

    confirm = input(f"Are you sure you want to delete '{record_found['item_name']}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        records.remove(record_found)          # Remove this dictionary from the list
        file_handler.save_records(records)    # Save updated list
        print("Record deleted successfully!\n")
    else:
        print("Deletion cancelled.\n")


def display_summary():
    """
    Feature 6: Display a summary report of all records.
    """
    records = file_handler.load_records()

    print("\n--- Summary Report ---")
    if len(records) == 0:
        print("No records found.\n")
        return

    total = len(records)

    # Use a dictionary to count how many records exist per status
    status_count = {"Lost": 0, "Found": 0, "Claimed": 0}

    for record in records:
        status = record["status"]
        status_count[status] = status_count[status] + 1   # Increase the count for this status

    print(f"Total records: {total}")
    print(f"Lost items: {status_count['Lost']}")
    print(f"Found items: {status_count['Found']}")
    print(f"Claimed items: {status_count['Claimed']}")
    print()