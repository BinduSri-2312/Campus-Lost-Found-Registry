# Campus Lost & Found Registry

A simple command-line application to manage lost and found items on a campus or hostel. Built entirely with **Core Python** — no external libraries, frameworks, or databases.

## About the Project

Students and staff often lose or find items on campus (bottles, umbrellas, ID cards, etc.) with no simple way to track them. This project solves that with a lightweight CLI tool that logs, searches, updates, and manages lost/found item records — with data saved persistently in a JSON file.

## Features

1. **Add Record** — Log a new lost/found item with a unique auto-generated ID
2. **View All Records** — Display all records in a table format
3. **Search Record** — Search by Record ID, item name, or location
4. **Update Record** — Update an item's status (Lost → Found → Claimed)
5. **Delete Record** — Remove a record after confirmation
6. **Display Summary Report** — View total records and status-wise counts

## Tech Stack / Concepts Used

- Python 3 (Core Python only — no external libraries)
- File Handling (JSON)
- Functions & User-defined Modules
- Loops & Conditional Statements
- Lists & Dictionaries
- try-except Error Handling

## Project Structure
lost_and_found/
│
├── main.py # Entry point — menu loop
├── file_handler.py # Handles reading/writing the JSON data file
├── record_operations.py # Core logic for all 6 features
├── utils.py # Helper functions (ID generation, input validation)
└── records.json # Auto-created on first "Add Record" (not included in repo)
## How to Run

1. Clone or download this repository
2. Make sure Python 3 is installed
3. Open a terminal in the project folder
4. Run: python main.py
5. Follow the on-screen menu to add, view, search, update, or delete records

Note: `records.json` is created automatically the first time you add a record — no setup needed.

## Sample Usage
========================================
CAMPUS LOST & FOUND REGISTRY
Add Record
View All Records
Search Record
Update Record
Delete Record
Display Summary Report
Exit
========================================
Enter your choice (1-7): 1

--- Add New Record ---
Enter item name: Blue Water Bottle
Enter description: Steel bottle with a dent on the side
Enter location: Library, 2nd floor
Enter date (YYYY-MM-DD): 2026-07-20
Enter status (Lost/Found/Claimed): Lost
Enter contact number (10 digits): 9876543210
Record added successfully! Your Record ID is 1.
## Future Improvements

- Add a login system to separate access for students vs campus staff/admin
- Allow updating fields beyond status (e.g., description, location)
- Add date-based filtering (e.g., view items reported in the last 7 days)
- Export summary reports to a text/PDF file
- Add a simple GUI using Tkinter (Core Python) as a next step beyond CLI

## Author

Built by Bindusri as a beginner project to practice Core Python fundamentals — functions, modules, file handling, and clean code structure.
