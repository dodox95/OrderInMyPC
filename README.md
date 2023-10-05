# File Organizer

A simple and user-friendly tool that helps organize files in a selected directory based on their file extensions. The application uses Python's `tkinter` for its GUI, providing a smooth user experience.

## Features:

- **File Organization**: Automatically sort files into folders based on their extensions.
- **Special Case Handling**: Handles special file extensions like `.tar.gz`.
- **Prevents Overwriting**: Ensures files with the same name do not get overwritten.
- **Removes Empty Folders**: After organization, the tool removes any empty subfolders.
- **GUI-Based**: Easily select folders and view progress through the GUI.

## How to Use:

1. Run the script.
2. Click on the "Order Files" button.
3. Select the folder you wish to organize.
4. The tool will organize the files and notify you once the process is complete.

## Functions:

- `get_file_extension(filename)`: Gets the file extension. It has special handling for compound extensions like `.tar.gz`.
  
- `organize_folder(path)`: Organizes the files based on their extensions in the provided path.

- `remove_empty_folders(path)`: Checks and removes empty folders from the provided path.

- `order_files()`: The main function that initializes the organizing process through GUI prompts.

## GUI:

The application features a minimalistic GUI that prompts users to select the folder they wish to organize and displays success/error messages based on the result of the organization.

## Requirements:

- Python 3
- tkinter (Usually comes bundled with Python)

## Installation & Setup:

1. Ensure you have Python 3 installed.
2. Clone or download the repository.
3. Run the script to launch the application.

## Notes:

- Always backup your files before using any file organizing tools to prevent accidental data loss.
- This is a basic version, and improvements can be made based on user feedback or specific needs.

## Contribution:

Feel free to fork the repository and make improvements or add new features. Pull requests are welcome!

