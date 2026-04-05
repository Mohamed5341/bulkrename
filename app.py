from pathlib import Path
import sys

prefix = 'Invoice'
working_folder = Path.cwd() / 'examples' / 'samples'

if not working_folder.exists():
    print("Folder doesn't exist")
    sys.exit()

counter = 0

for file in working_folder.iterdir():
    Path.rename(file, file.parent / f"{prefix}_{str(counter).zfill(3)}{file.suffix}")
    counter += 1

