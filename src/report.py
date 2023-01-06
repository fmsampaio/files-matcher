class Report:
    def __init__(self, file1, file2, similarity):
        self.file1 = file1
        self.file2 = file2
        self.similarity = float(similarity)    

    def __hash__(self):
        return hash(self.file1 + self.file2 if self.file1 > self.file2 else self.file2 + self.file1)

    def __eq__(self, obj):
        return self.__hash__() == obj.__hash__()

    def __str__(self):
        return f'{(self.similarity*100):.2f}\t{self.file1}\t{self.file2}\n'
    
    def __lt__(self, obj):
        return self.similarity < obj.similarity