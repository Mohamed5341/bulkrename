from pathlib import Path

def PrintTabular(titles, table, seperator='->'):
    lenths = [0]*len(titles)
    for row in table:
        for i in range(len(row)):
            if len(row[i]) > lenths[i]:
                lenths[i] = len(row[i])
    
    result = ''
    for i in range(len(titles)-1):
        result += titles[i].ljust(lenths[i]) + ' ' + seperator + ' '
    result += titles[-1].ljust(lenths[-1]) + '\n' # Last item in the titles
    
    # Header seperator
    for i in range(len(titles)-1):
        result += ''.ljust(lenths[i],'-') + '-' + '+'*len(seperator) + '-'
    result += ''.ljust(lenths[-1],'-') + '\n'
    
    for row in table:
        for i in range(len(row)-1):
            result += row[i].ljust(lenths[i]) + ' ' + seperator + ' '
        result += row[-1].ljust(lenths[-1]) + '\n' # Last item in the row
    
    print(result)

def PrintFilesTable(data, reverse = False):
    titles = ['Before', 'After']
    names = []
    sep = '->'
    for item in data:
        before = Path(item["old"])
        after = Path(item["new"])
        names.append((before.name, after.name))
    
    if reverse:
        sep = '<-'
    PrintTabular(titles, names, seperator=sep)