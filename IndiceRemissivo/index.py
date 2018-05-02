import re
# biblioteca de expressão regular do python;

def printTable(wordTable):
    print("Palavra:  Frequência ")
    for key in wordTable.keys():
        print("%s:  %d" % (key, wordTable[key]))
    #for

def countWords(file, wordTable):
    for line in file:
        words = re.split('[\W]', line)
        for word in words:
            if word != '':
                if (word in wordTable.keys()):
                    wordTable[word] += 1
                else:
                    wordTable[word] = 1
        #for
    # for

def main():
    wordTable = {}
    try:
        file = open("palavras.txt", "r", encoding="utf-8")
        countWords(file, wordTable)
        printTable(wordTable)
    except IOError:
        print("File Not Found!")

    file.close()

if __name__ == "__main__":
    main()
