import os

def display_directory_contents(directory):
    try:
        with os.scandir(directory) as entries:
            print(f"\nContents of {directory}:")
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

def display_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"\nContents of {file_path}:")
            print(file.read())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied for file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")

def search_for_file(start_directory, name, is_directory):
    current_directory = start_directory

    while current_directory:
        for root, dirs, files in os.walk(current_directory):
            if is_directory:
                for directory in dirs:
                    if directory.startswith(name):
                        directory_path = os.path.join(root, directory)
                        abs_path = os.path.abspath(directory_path)
                        print(f"\nDirectory '{directory}' found at: {abs_path}")
                        display_directory_contents(directory_path)
                        return directory_path
            else:
                for filename in files:
                    if filename.startswith(name):
                        file_path = os.path.join(root, filename)
                        abs_path = os.path.abspath(file_path)
                        print(f"\nFile '{filename}' found at: {abs_path}")
                        return file_path

        # Move up to the parent directory
        current_directory = os.path.dirname(current_directory)

    return None

def main():
    script_directory = os.path.dirname(os.path.realpath(__file__))

    while True:
        search_type = input("\nEnter 'file' or 'directory' to search (or 'exit' to quit): ").lower()

        if search_type == 'exit':
            break
        elif search_type not in ['file', 'directory']:
            print("Invalid input. Please enter 'file', 'directory', or 'exit'.")
            continue

        name = input(f"\nEnter the {'file' if search_type == 'file' else 'directory'} name: ")

        if search_type == 'file':
            file_path = search_for_file(script_directory, name, is_directory=False)
            if file_path:
                display_file_content(file_path)
            else:
                print(f"File '{name}' not found.")
        elif search_type == 'directory':
            directory_path = search_for_file(script_directory, name, is_directory=True)
            if not directory_path:
                print(f"Directory '{name}' not found.")

if __name__ == "__main__":
    main()
