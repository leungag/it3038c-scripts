import os
import time

def display_directory_contents(directory):
    try:
        with os.scandir(directory) as entries:  # Use os.scandir to get directory contents
            print(f"\nContents of {directory}:")
            for entry in entries:
                print(entry.name) # Print the names of entries in the directory
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")  # Handle the case where the directory is not found

def display_file_content(file_path):
    try:
        with open(file_path, 'r') as file: # Open and read the contents of the file
            print(f"\nContents of {file_path}:")
            print(file.read())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied for file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")

def search_for_file(start_directory, name, is_directory, timeout_seconds=15):
    start_time = time.time()

    current_directory = start_directory

    while current_directory: # Use os.walk to iterate over all directories and files in the current directory
        for root, dirs, files in os.walk(current_directory):
            if is_directory:
                for directory in dirs:
                    if directory.startswith(name):  # Search for directories that match the given name
                        directory_path = os.path.join(root, directory)
                        abs_path = os.path.abspath(directory_path)
                        print(f"\nDirectory '{directory}' found at: {abs_path}")
                        display_directory_contents(directory_path) # Display the contents of the found directory
                        return directory_path
            else:
                for filename in files: # Search for files that match the given name
                    if filename.startswith(name):
                        file_path = os.path.join(root, filename)
                        abs_path = os.path.abspath(file_path)
                        print(f"\nFile '{filename}' found at: {abs_path}")
                        return file_path

        current_directory = os.path.dirname(current_directory)

        # Check if the timeout has been reached if file or directory not found
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout_seconds:
            print(f"Timeout reached ({timeout_seconds} seconds). Directory or file '{name}' not found.")
            return None

    return None

def main():
    script_directory = os.path.dirname(os.path.realpath(__file__)) # Get the directory where the script is located

    while True:
        search_type = input("\nEnter 'file' or 'directory' to search (or 'exit' to quit): ").lower() # Prompt the user to enter the type of search (file or directory)

        if search_type == 'exit':
            break
        elif search_type not in ['file', 'directory']:
            print("Invalid input. Please enter 'file', 'directory', or 'exit'.")
            continue

        name = input(f"\nEnter the {'file' if search_type == 'file' else 'directory'} name: ")

        if search_type == 'file': # Search for the file and display its contents
            file_path = search_for_file(script_directory, name, is_directory=False)
            if file_path:
                display_file_content(file_path)
            else:
                print(f"File '{name}' not found.")
        elif search_type == 'directory': # Search for the directory and display its contents
            directory_path = search_for_file(script_directory, name, is_directory=True)
            if not directory_path:
                print(f"Directory '{name}' not found.")

if __name__ == "__main__":
    main()
