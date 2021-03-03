from string import *
book = "E:\Academics\Python\Python Programs\\test book.txt"
with open(book,'r') as fd:
    words = fd.read().split()
    def clean (word):
        cleansed=' '
        for char in word:
            if ((char in punctuation)or (char in whitespace)):
                pass
            else:
                cleansed.t=char.lower()
            return cleansed
    print("{} has {} words".format(bool,len([clean(words) for used in words])))