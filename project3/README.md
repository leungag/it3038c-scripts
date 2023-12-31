# File and Directory Search
## Overview
This Python script helps you search for files and directories within a specified directory and its subdirectories. 
It provides the ability to view the content of files and list the contents of directories.
<br/>
<br/>
* Download dirandfile.py script.
* Make sure Python is installed on your system.

<br/>
PowerShell can work with this program once the script is downloaded and Python is installed.

To run the script in PowerShell run the command:

```javascript
python dirandfile.py
```
### Follow the Prompts:

* Enter the type of search: 'file' or 'directory'.
* Enter the name of the file or directory you're looking for.
* If searching for a file, the script will display its content if found.
* If searching for a directory, the script will display its path and list its contents.

## Example
### Search for a File
``` python
Enter 'file' or 'directory' to search (or 'exit' to quit): file
Enter the file name: example.txt
```
![image](https://github.com/leungag/it3038c-scripts/assets/142808905/aecce36b-8026-4646-bcd2-b087703994ca)



### Search for a Directory
``` python
Enter 'file' or 'directory' to search (or 'exit' to quit): directory
Enter the file name: node
```
![image](https://github.com/leungag/it3038c-scripts/assets/142808905/21cae463-9288-4db6-a32d-a5745b130880)


## Notes
* Make sure to provide the correct file name or directory name.
* The script searches in the current directory and its subdirectories.
* After 15 seconds of searching for a file or directory, if not found within the timeframe, a timeout error will appear.
* Enter 'exit' at any time to exit the program.


## Why it is Useful
This Python program serves as an efficient directory and file search tool.
It simplifies the process and offers a quick and easy search for files and directories within a specific starting directory. The program provides detailed information about the action and contents in the directory or file. Additionally, the program has a user-friendly interface, making it accessible to experienced professionals and those new to the command line. 

### Source
The code section incorporates initial snippets generated by ChatGPT, followed by further customization to meet specific requirements.

OpenAI. (2023). ChatGPT (Nov 21 version) [Large language model]. https://chat.openai.com

