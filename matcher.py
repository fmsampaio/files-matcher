import os

from difflib import SequenceMatcher
from report import Report

class Matcher:
    def __init__(self):
        self.filesList1 = []
        self.filesList2 = []
        self.reportSet = set()

        self.OUTPUT_REPORT_FOLDER = 'outputs/'

    def handleSinglePathFilesList(self, path):
        self.fillFilesList(self.filesList1, path)
        self.fillFilesList(self.filesList2, path)

    def handleMultiPathFilesList(self, paths):
        self.fillFilesList(self.filesList1, paths[0])
        self.fillFilesList(self.filesList2, paths[1])
    
    def fillFilesList(self, filesList, argPath):
        if os.path.isfile(argPath):
            filesList.append(os.path.abspath(argPath))
        elif os.path.isdir(argPath):
            for path, subdirs, files in os.walk(argPath):
                for name in files:
                    filesList.append(os.path.abspath(f'{path}/{name}'))
        else:
            print(f'[Error] Given path ({argPath}) is not a file neither a folder')
            exit()

    def compareFilesLists(self, extensions):
        totalComps = len(self.filesList1) * len(self.filesList2)

        idComp = 0
        for file1 in self.filesList1:
            for file2 in self.filesList2:
                isFile1ToBeCompared = self.checkExtension(file1, extensions)
                isFile2ToBeCompared = self.checkExtension(file2, extensions)
                if file1 != file2 and isFile1ToBeCompared and isFile2ToBeCompared:
                    status = float(idComp)/totalComps * 100
                    print(f'[Status] {status:.1f}%')
                    self.reportSet.add(self.matchFiles(file1, file2))
                idComp += 1
        
    
    def matchFiles(self, file1, file2):
        text1 = open(file1, encoding = "ISO-8859-1").read()
        text2 = open(file2, encoding = "ISO-8859-1").read()    
        m = SequenceMatcher(None, text1, text2)
        similarity = float(m.ratio())

        return Report(file1, file2, similarity)

    def checkExtension(self, fileName, extensions):
        returnable = False

        if extensions[0] == 'all':
            returnable = True
        else:
            for ext in extensions:
                if fileName.endswith(ext):
                    returnable = True
        return returnable  

    def exportReportAsTsv(self, fileName='report.tsv'):
        fpReport = open(f'{self.OUTPUT_REPORT_FOLDER}/{fileName}', 'w')
        fpReport.write('similarity\tfile_1\tfile_2\n')

        reportList = sorted(list(self.reportSet))

        for report in reportList:
            fpReport.write(str(report))
        fpReport.close()