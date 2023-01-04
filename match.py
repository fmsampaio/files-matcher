import sys
import os
import click

from difflib import SequenceMatcher

TARGET_FILES_EXT = '.mem'

@click.command()
@click.option('-s', '--single_path', default='null', help='Similarity evaluation within a single path.')
@click.option('-m', '--multi_path', type=(str,str), default=('null','null'), help='Similarity evaluation considering a combination of two paths.')

def checkSimilarity(single_path, multi_path):
    filesList1 = []
    filesList2 = []
    
    handleFilesList(single_path, multi_path, filesList1, filesList2)
    
    reportList = compareFilesLists(filesList1, filesList2)
    exportReportAsTsv(reportList)


def handleFilesList(single_path, multi_path, filesList1, filesList2):
    print(single_path, multi_path)
    if single_path != 'null':
        fillFilesList(filesList1, single_path)
        fillFilesList(filesList2, single_path)
    elif multi_path[0] != 'null':
        fillFilesList(filesList1,multi_path[0])
        fillFilesList(filesList2,multi_path[1])
    else:
        print(f'[Error] A single or multi path option must be informed!')
        exit()
    

def fillFilesList(filesList, argPath):
    if os.path.isfile(argPath):
        filesList.append(os.path.abspath(argPath)) #FIX: insert the complete path
    elif os.path.isdir(argPath):
        for path, subdirs, files in os.walk(argPath):
            for name in files:
                filesList.append(os.path.abspath(f'{path}/{name}'))
    else:
        print(f'[Error] Given path ({argPath}) is not a file neither a folder')
        exit()
    
def compareFilesLists(filesList1, filesList2):
    reportList = []
    totalComps = len(filesList1) * len(filesList2)

    idComp = 0
    for file1 in filesList1:
        for file2 in filesList2:       
            if file1 != file2 and file1.endswith(TARGET_FILES_EXT) and file2.endswith(TARGET_FILES_EXT):
                status = float(idComp)/totalComps * 100
                print(f'[Status] {status:.1f}%')
                reportList.append(matchFiles(file1, file2))
            idComp += 1
    
    return reportList

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

def exportReportAsTsv(reportList):
    fpReport = open("report.tsv", "w")
    fpReport.write('similarity\tfile_1\tfile_2\n')
    for report in reportList:
        fpReport.write(generateTsvLine(report))
    fpReport.close()

def generateTsvLine(r):
    return f'{r["similarity"]}\t{r["file1"]}\t{r["file2"]}\n'



if __name__ == '__main__':
    checkSimilarity()
