import os

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

def search_for_file(start_directory, file_name):
    current_directory = start_directory

    while current_directory:
        for root, dirs, files in os.walk(current_directory):
            for filename in files:
                if filename.startswith(file_name):
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
        file_name = input("\nEnter the file name (or 'exit' to quit): ")

        if file_name.lower() == 'exit':
            break

        file_path = search_for_file(script_directory, file_name)

        if file_path:
            display_file_content(file_path)
        else:
            print(f"File '{file_name}' not found.")

if __name__ == "__main__":
    main()
