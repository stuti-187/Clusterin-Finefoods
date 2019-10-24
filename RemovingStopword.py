import pandas as pd
import csv
data = pd.read_csv('uniqueList1.csv', encoding = "ISO-8859-1",names=['colA'], header=None)
uniqueValueswithStopwordsDF=data['colA']
words=uniqueValueswithStopwordsDF.tolist()
stopWordsList=list()
uniqueWords=list()
stopWords=open('longstopWords.txt')
for line in stopWords:
    line = line.strip()
    stopWordsList.append(line)

for word in words:
    if word not in stopWordsList and type(word) == str:
        uniqueWords.append(word)

#for uniqueWord in uniqueWords:
#    print(uniqueWord)

OUTPUT_FILE_NAME="uniqueListFinal.csv"
outfile = open(OUTPUT_FILE_NAME,"w",encoding = "utf-8")

outfile.write("\n".join(uniqueWords))

outfile.close()
