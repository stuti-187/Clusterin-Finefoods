import pandas as pd
import operator

colname = ['product/productId', 'review/userId', 'review/profileName', 'review/helpfulness', 'review/score',
           'review/time', 'review/summary', 'review/text']
ch = ['.', '(', ')', '!', '/', '<', '>', ';', '"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', ' ', '?', '*',
      '~', '$', ':', '=', '@', '%', '^', '&', ']', '}', '{', '[', '|', '\\', '`', '#', '+']
data = pd.read_csv('output.csv', encoding="ISO-8859-1",
                   skipinitialspace=True, usecols=colname)

data1 = pd.read_csv('uniqueListFinal.csv', encoding="ISO-8859-1",
                    names=['colA'], header=None)
uniqueValuesDF1 = data1['colA']
uniqueValuesFinal = uniqueValuesDF1.tolist()
lst = list()
words = list()
topWords = dict()
uniqueValuesDF = data['review/text']
uniqueValuesList = uniqueValuesDF.tolist()
num = 0
for item in uniqueValuesList:
    if type(item) == str:
        for w in item.split():
            words.append(w)

for i in words:

    for character in ch:
        i = i.replace(character, "")

    i = i.lower()
    lst.append(i)

wordCount = dict()

for word in lst:
    if word not in wordCount.keys():
        wordCount[word] = 1
    else:
        count = wordCount[word]
        count = count + 1
        wordCount[word] = count

sorted_d = sorted(wordCount.items(), key=operator.itemgetter(1), reverse=True)

count = 0
for allWords in sorted_d:
    if count > 499:
        break
    if allWords[0] in uniqueValuesFinal:
        count = count + 1
        topWords[allWords[0]] = allWords[1]

OUTPUT_FILE_NAME = "top500.csv"
outfile = open(OUTPUT_FILE_NAME, "w")
header = [
    "Word",
    "Total Word Count"
]
outfile.write(",".join(header) + "\n")

for x in topWords:
    outfile.write(x + ", " + str(topWords[x]) + '\n')

outfile.close()
