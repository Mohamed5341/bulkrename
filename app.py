import sys
from pathlib import Path
from src.PrintUtil import PrintFilesTable

prefix = 'Invoice'
working_folder = Path.cwd() / 'examples' / 'samples'

if not working_folder.exists():
    print("Folder doesn't exist")
    sys.exit()

counter = 0
names_list = []

for file in working_folder.iterdir():
    names_list.append((file ,file.parent / f"{prefix}_{str(counter).zfill(3)}{file.suffix}"))
    counter += 1

print("List of files to rename:")
PrintFilesTable(names_list)

while True:
    user_input = input("\n\nEnter yes/y to confirm(q for quit): ")

    if user_input.lower() == 'y' or user_input.lower() == 'yes':
        # Rename files
        for before, after in names_list:
            before.rename(after)
        print("Done")
        break
    elif user_input.lower() == 'q' or user_input.lower() == 'quit':
        print("\n\nFiles unchanged.")
        break
        