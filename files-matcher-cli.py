import sys
import os
import click

from difflib import SequenceMatcher
from report import Report

OUTPUT_REPORT_FOLDER = 'outputs/'

@click.command()
@click.option('-s', '--single_path', default='null', help='Similarity evaluation within a single path.')
@click.option('-m', '--multi_path', type=(str,str), default=('null','null'), help='Similarity evaluation considering a combination of two paths.')
@click.option('-e', '--ext', multiple=True, default=['all'], help='Filter the similarity verification to specified file extensions (Default: all).')

def checkSimilarity(single_path, multi_path, ext):
    filesList1 = []
    filesList2 = []
    
    handleFilesList(single_path, multi_path, filesList1, filesList2)
    
    reportSet = compareFilesLists(filesList1, filesList2, ext)
    exportReportAsTsv(reportSet)


def handleFilesList(single_path, multi_path, filesList1, filesList2):
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
    
def compareFilesLists(filesList1, filesList2, extensions):
    reportSet = set()
    totalComps = len(filesList1) * len(filesList2)

    idComp = 0
    for file1 in filesList1:
        for file2 in filesList2:
            isFile1ToBeCompared = checkExtension(file1, extensions)
            isFile2ToBeCompared = checkExtension(file2, extensions)
            if file1 != file2 and isFile1ToBeCompared and isFile2ToBeCompared:
                status = float(idComp)/totalComps * 100
                print(f'[Status] {status:.1f}%')
                reportSet.add(matchFiles(file1, file2))
            idComp += 1
    
    return reportSet

def matchFiles(file1, file2):
    text1 = open(file1, encoding = "ISO-8859-1").read()
    text2 = open(file2, encoding = "ISO-8859-1").read()    
    m = SequenceMatcher(None, text1, text2)
    similarity = float(m.ratio())

    return Report(file1, file2, similarity)

def checkExtension(fileName, extensions):
    returnable = False

    if extensions[0] == 'all':
        returnable = True
    else:
        for ext in extensions:
            if fileName.endswith(ext):
                returnable = True
    return returnable

def exportReportAsTsv(reportSet):
    fpReport = open(f'{OUTPUT_REPORT_FOLDER}/report.tsv', 'w')
    fpReport.write('similarity\tfile_1\tfile_2\n')

    reportList = sorted(list(reportSet))

    for report in reportList:
        fpReport.write(str(report))
    fpReport.close()


if __name__ == '__main__':
    checkSimilarity()
