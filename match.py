import sys

from difflib import SequenceMatcher


if __name__ == '__main__':
    text1 = open(sys.argv[1]).read()
    text2 = open(sys.argv[2]).read()
    
    m = SequenceMatcher(None, text1, text2)
    print(m.ratio())