fileName = "/sys/bus/w1/devices/28-041702e74eff/w1_slave"

def documentConverterLines(file, shouldStrip):
    """


    Returns lines consisting of each line in the text file it's given.

    documentConverterLines(file, shouldStrip)

    file: The path of the text file, including the file itself
    shouldStrip: A bolean, if True, will remove the new line character including the whitespace left behind.
    """
    line_list = []

    with open(file) as file:
        line_list = file.readlines()
    if(shouldStrip):
        line_list = [item.rstrip() for item in line_list]

    return line_list

def documentConverterLine(file, line):
    """
    Returns a line, specified from the second argument given.

    documentConverterLine(File, line)

    file: The path of the text file, including the file itself
    line: An integer, of which line from the text file it should return.
    """
    with open(file) as file:
        lineString = file.readline(line)
    
    return lineString

def wordFinder(file, word, line=None):
    """
    Searches for a word specified

    wordFinder(file(required), word(require), line=None(optional))

    file: The path of the text file, including the file itself.
    word: The word which needs to be found.
    line: An optional argument, specifing which line the word is located.
    """
    with open(file) as file:
        words = file.read().split(" ")
    if(line == None):
        for i in range(len(words)):
            if(words[i] == word):
                return words[i]

def wordSplitter(file, letter, removeWhiteSpace=True):
    """
    Splittes up a text file into a list, while splitting each letter, specified from the list, into another list, which gets returned

    wordSplitter(file(required, letter=" "(required), removeWhiteSpace=True(optional)))

    file: The path of the text file, including the file itself.
    letter: The letter which determines where the list should be split. This letter is also removed during the process
    removeWhiteSpace: Defaults to true. Determines if all the whitespaces should also be removed.
    """
    with open(file) as file:
        words = file.read()
        if(removeWhiteSpace):
            words = words.split(" ")
        
        for i in range(len(words)):
            wordsTemp = words[i].split(letter)

    return wordsTemp
