import os

def search_file():
    while True:
        directory_path = input("Enter the directory path (or type 'exit' to quit): ")

        if directory_path.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        file_name = input("Enter the name or part of the name of the file: ")

        for root, dirs, files in os.walk(directory_path):
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
                    break  # Exit the inner loop if file is found
            else:
                continue  # Only executed if the inner loop did NOT break
            break  # Exit the outer loop if file is found
        else:
            print(f"File '{file_name}' not found in the specified directory.")

if __name__ == "__main__":
    search_file()
