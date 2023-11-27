import os

def search_file():
    while True:
        directory_name = input("Enter the name of the directory (or type 'exit' to quit): ")

        if directory_name.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        file_name = input("Enter the name or part of the name of the file: ")

        for root, dirs, files in os.walk(os.getcwd()):
            for dir_name in dirs:
                if directory_name in dir_name:
                    directory_path = os.path.join(root, dir_name)

                    for file in files:
                        if file_name in file:
                            file_path = os.path.join(directory_path, file)
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
                    break  # Exit the middle loop if file is found
            else:
                continue  # Only executed if the middle loop did NOT break
            break  # Exit the outer loop if directory is found
        else:
            print(f"Directory '{directory_name}' not found.")

if __name__ == "__main__":
    search_file()
