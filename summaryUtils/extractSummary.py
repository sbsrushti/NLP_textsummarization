from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import numpy,math
import os

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 1
extractionRatio = 0.4

rootDir = "../Dataset/bbc-2/politics"

def traverserFolder(folderPath):
    fileNames = os.listdir(folderPath)
    for fileName in fileNames:
        if not ".DS_Store" in fileName and ".txt" in fileName:
            generateSummary(folderPath, fileName)

def generateSummary(dirPath, fileName):
    fileAbsPath = os.path.join(dirPath, fileName)
    fileName = os.path.basename(fileAbsPath)
    fileHandler = open(fileAbsPath, "r", encoding="latin1")
    fileContent = fileHandler.read().strip()
    no_of_line = len(fileContent.split("."))
    requiredSentenceCount = math.ceil(no_of_line * extractionRatio)
    if __name__ == "__main__":
        # or for plain text files
        parser = PlaintextParser.from_file(fileAbsPath, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        sentences = summarizer(parser.document, requiredSentenceCount)
        print(sentences)
        content =""
        for sentence in sentences:
            content += str(sentence)
        writeSummaryToFile(content, fileName)

def writeSummaryToFile(sentences,fileName):
    folderName = fileName.split(".")[0]
    fileHandler = open("../results/"+folderName+"/sumy_"+fileName, "w");
    fileHandler.write(sentences)
    fileHandler.close()




traverserFolder(rootDir)







