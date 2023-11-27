import os

def list_files_and_directories(directory):
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

def main():
    script_directory = os.path.dirname(os.path.realpath(__file__))

    while True:
        directory = input("\nEnter the directory name (or 'exit' to quit): ")
        
        if directory.lower() == 'exit':
            break

        directory_path = os.path.join(script_directory, directory)

        if not os.path.exists(directory_path):
            print(f"Directory '{directory}' not found. Please enter a valid directory.")
            continue

        abs_path = os.path.abspath(directory_path)
        print(f"\nExact path of '{directory}': {abs_path}")
        
        list_files_and_directories(directory_path)

        file_name = input("\nEnter the file name you want to view (or 'skip' to skip): ")

        if file_name.lower() == 'skip':
            continue

        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):
            display_file_content(file_path)
        else:
            print(f"File '{file_name}' not found in the directory.")

if __name__ == "__main__":
    main()
