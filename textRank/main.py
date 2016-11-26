from nlp_project.textRank.documentPreprocessing import document_Processing
from nlp_project.textRank.pageRank import page_Rank
import os
source_file = "InputFile.txt"
sentence_Filtered_File = "preprocessed_text.txt"
targetFile = "TargetFile1.txt"
stopwords_file = "stopwords.txt"
max = 3

for root, subdirs, files in os.walk("C:/Users/Srushti/PycharmProjects/text_summ/nlp_project/Dataset/bbc-2/politics"):
    if not subdirs:
        for file in files:
            doc = document_Processing()
            doc.preprocessing(root + "/" + file, sentence_Filtered_File, stopwords_file)
            pageScore = page_Rank()
            folderName = file.split(".")[0]
            pageScore.calculatePageRank(sentence_Filtered_File, "../results/" + folderName + "/pagerank_" + file, max)





