import sys
import os

from difflib import SequenceMatcher

filesList1 = []
filesList2 = []

def fillFilesList(argPath):
    returnable = []
    if os.path.isfile(argPath):
        returnable.append(os.path.abspath(argPath)) #FIX: insert the complete path
    elif os.path.isdir(argPath):
        for path, subdirs, files in os.walk(argPath):
            for name in files:
                returnable.append(os.path.abspath(f'{path}/{name}'))
    else:
        print(f'[Error] Given path ({argPath}) is not a file neither a folder')
        exit()
    
    return returnable

def matchFiles(file1, file2):
    text1 = open(file1).read()
    text2 = open(file2).read()    
    m = SequenceMatcher(None, text1, text2)
    similarity = m.ratio()

    return {
        'file1' : file1,
        'file2' : file2,
        'similarity' : similarity * 100
        }
   

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(f'[Error] Wrong number of arguments (expected 2, given {len(sys.argv)-1})')
        exit()

    filesList1 = fillFilesList(sys.argv[1])
    filesList2 = fillFilesList(sys.argv[2])

    print(f'[DBG] Files list 1: {filesList1}')
    print(f'[DBG] Files list 2: {filesList2}')

    reportList = []

    for file1 in filesList1:
        for file2 in filesList2:
            
            if file1 != file2 and file1.endswith('.circ') and file2.endswith('.circ'):
                print(file1)
                print(file2 + '\n\n')
                reportList.append(matchFiles(file1, file2))
    
    print('[DBG] Report:')
    for report in reportList:
        print(report)