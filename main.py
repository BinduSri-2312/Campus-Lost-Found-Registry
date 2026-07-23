# main.py
# This is the entry point of the program.
# It displays a menu and lets the user choose what to do.

import record_operations   # Our own module with all 6 feature functions


def show_menu():
    """
    Displays the main menu options to the user.
    """
    print("=" * 40)
    print("   CAMPUS LOST & FOUND REGISTRY")
    print("=" * 40)
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Display Summary Report")
    print("7. Exit")
    print("=" * 40)


def main():
    """
    The main program loop. Keeps showing the menu until the user exits.
    """
    while True:                       # Infinite loop - runs until user chooses to exit
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            record_operations.add_record()
        elif choice == "2":
            record_operations.view_all_records()
        elif choice == "3":
            record_operations.search_record()
        elif choice == "4":
            record_operations.update_record()
        elif choice == "5":
            record_operations.delete_record()
        elif choice == "6":
            record_operations.display_summary()
        elif choice == "7":
            print("Thank you for using the Lost & Found Registry. Goodbye!")
            break                     # Exits the while loop, ending the program
        else:
            print("Invalid choice. Please enter a number between 1 and 7.\n")


# This ensures main() only runs when this file is executed directly,
# not when it's imported by another file (good Python practice).
if __name__ == "__main__":
    main()