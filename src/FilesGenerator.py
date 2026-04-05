from pathlib import Path
import random

N = 100
destination = Path.cwd() / 'examples' / 'samples'

if not destination.exists():
    destination.mkdir()

names_list = ['project', 'main', 'final', 'copy']
seperators = ['_', '-', ' ', '']

for i in range(N):
    name_size = random.randint(1, len(names_list))
    filename = random.choice(seperators).join(random.sample(names_list, name_size))
    file_path = destination / (filename + '.txt')

    j = 0
    while file_path.exists():
        j += 1
        file_path = destination / (filename + f'({j}).txt')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        file_path.write_text(filename)
