import pandas as pd
import csv

colname = ['product/productId', 'review/userId', 'review/profileName', 'review/helpfulness', 'review/score',
           'review/time', 'review/summary', 'review/text']

ch = ['.', '(', ')', '!', '/', '<', '>', ';', '"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', ' ', '?', '*',
      '~', '$', ':', '=', '@', '%', '^', '&', ']', '}', '{', '[', '|', '\\', '`', '#', '+']
data = pd.read_csv('output.csv', encoding="ISO-8859-1", skipinitialspace=True,
                   usecols=colname)

lst = set()
words = set()

uniqueValuesDF = data['review/text']
uniqueValuesList = uniqueValuesDF.tolist()
# print(uniqueValuesList)
num = 0
for item in uniqueValuesList:
    if (type(item) == str):
        for w in item.split():
            words.add(w)

for i in words:

    for character in ch:
        i = i.replace(character, "")

    i = i.lower()
    lst.add(i)

# for a in lst:
#    print(a)

OUTPUT_FILE_NAME = "uniqueList1.csv"
outfile = open(OUTPUT_FILE_NAME, "w", encoding="utf-8")

outfile.write("\n".join(lst))

outfile.close()

#    data['review/text'][ind]
# reviews=data.values.tolist()
# print(reviews)


# print(type(uniqueValuesDF))

# lol=['quality.', 'The', 'product', 'looks', 'more', 'like', 'a', 'stew']
# for i in range(len(lol)):
#    lol[i]=lol[i].replace(".","")
# print(lol)
