import sys
from pathlib import Path
from src.PrintUtil import PrintFilesTable
import json, os
import ctypes

#--------------------------------------------------------
prefix = 'Invoice'
folders_selector = "copy*.*"
working_folder = Path.cwd() / 'examples' / 'samples'
if os.name == 'nt':
    history_filename = Path.cwd() / "history.json"
else:
    history_filename = Path.cwd() / ".history.json"

if not working_folder.exists():
    print("Folder doesn't exist")
    sys.exit()

#--------------------------------------------------------
counter = 0
names_list = []
history_exists = False

files_list = working_folder.glob(folders_selector)
for file in files_list:
    new_name = file.parent / f"{prefix}_{str(counter).zfill(3)}{file.suffix}"
    names_list.append({"old": str(file.absolute()) ,"new": str(new_name.absolute())})
    counter += 1

print("List of files to rename:")
PrintFilesTable(names_list)

#--------------------------------------------------------
while True:
    if history_filename.exists():
        user_input = input("\n\nEnter yes/y to confirm, r to rollback(q for quit): ")
        history_exists = True
    else:
        user_input = input("\n\nEnter yes/y to confirm(q for quit): ")
        if counter == 0:
            sys.exit()

    if user_input.lower() == 'y' or user_input.lower() == 'yes':
        # Rename files
        for item in names_list:
            before = Path(item["old"])
            after = Path(item["new"])
            before.rename(after)
        
        # Save data
        with open(history_filename, "w", encoding="utf-8") as f:
            json.dump(names_list, f)
        print("Done")
        break
    elif user_input.lower() == 'r' and history_filename.exists():
        # read files previous names
        with open(history_filename, "r", encoding='utf-8') as f:
            data = json.load(f)
            
        print("List of files to rename:")
        PrintFilesTable(data, reverse=True)
            
        input('Enter any letter to continue rollback:')
        
        for item in data:
            before = Path(item["new"])
            after = Path(item["old"])
            before.rename(after)
        
        os.remove(history_filename)
        print("Done")
        break
    elif user_input.lower() == 'q' or user_input.lower() == 'quit':
        print("\n\nFiles unchanged.")
        break


# Hide my changes folder
if os.name == 'nt' and not history_exists:
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ret = ctypes.windll.kernel32.SetFileAttributesW(str(history_filename), FILE_ATTRIBUTE_HIDDEN)
    if not ret:
        print("Failed to hide the file.")