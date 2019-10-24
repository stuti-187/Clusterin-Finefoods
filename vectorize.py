import pandas as pd
import csv
from sklearn.feature_extraction.text import CountVectorizer

columns = ['product/productId', 'review/userId', 'review/profileName', 'review/helpfulness', 'review/score',
           'review/time', 'review/summary', 'review/text']

textData = pd.read_csv('output.csv', encoding="ISO-8859-1", skipinitialspace=True,
                       usecols=columns)
colnames = ['Word', 'Total Word Count']
data = pd.read_csv('top500.csv', encoding="ISO-8859-1", skipinitialspace=True,
                   usecols=colnames)
reviewTextDF = textData['review/text']
reviewText = reviewTextDF.tolist()

uniqueValuesDF = data['Word']
uniqueValues = uniqueValuesDF.tolist()
uniqueList = dict()
i = 0
for word in uniqueValues:
    uniqueList[word] = i
    i = i + 1
# print(reviewText[0])

# text = ["Good good good taste great.***flavor ,my"]
vectorizer = CountVectorizer(binary=True)
vectorizer.vocabulary_ = uniqueList
vectorList = list()
for review in reviewText:
    review = [str(review)]
    vector = vectorizer.transform(review)
    vectorList.append(vector.toarray())

OUTPUT_FILE_NAME = "vectors.csv"
outfile = open(OUTPUT_FILE_NAME, "w")
header = ""
for item in uniqueList:
    header = header + str(item) + ", "

outfile.write(header + "\n")

result = ""
for values in vectorList:
    for value in values:
        for singleValue in value:
            result = result + str(singleValue) + ", "

    result = result + "\n"
    outfile.write(result)
    result = ""

outfile.close()

# print(vectorList[0])
#
# vector = vectorizer.transform(text)
# print(vectorizer.vocabulary_)
# print(type(vector))

# for something in uniqueList:
#     print("key:" + str(something) + ", word:" + str(uniqueList[something]))
