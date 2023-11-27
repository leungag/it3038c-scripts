import os

def search_file():
    file_name = input("Enter the name or part of the name of the file: ")

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file_name in file:
                file_path = os.path.join(root, file)
                print(f"File found at: {file_path}")

                view_content = input("Do you want to view the content of the file? (yes/no): ")
                if view_content.lower() == "yes":
                    try:
                        with open(file_path, 'r') as file_content:
                            content = file_content.read()
                            print(f"\nFile Content:\n{content}")
                    except Exception as e:
                        print(f"Error reading file: {e}")
                return

    print(f"File '{file_name}' not found.")

if __name__ == "__main__":
    search_file()
