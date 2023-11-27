import os

def display_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"\nContents of {file_path}:")
            print(file.read())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def search_for_file(script_directory, file_name):
    for root, dirs, files in os.walk(script_directory):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            abs_path = os.path.abspath(file_path)
            print(f"\nFile '{file_name}' found at: {abs_path}")
            return file_path
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
