import pandas as pd
import operator
from collections import Counter

colnames = ['Word', 'Total Word Count']
data1 = pd.read_csv('top500.csv', encoding="ISO-8859-1", skipinitialspace=True,
                    usecols=colnames)
uniqueValuesDF = data1['Word']
uniqueValues = uniqueValuesDF.tolist()

colname = uniqueValues
data = pd.read_csv('centroids.csv', encoding="ISO-8859-1", skipinitialspace=True,
                   usecols=colname)

data = data.transpose()
#
#
cluster1 = dict()
cluster2=dict()
cluster3=dict()
cluster4=dict()
cluster5=dict()
cluster6=dict()
cluster7=dict()
cluster8=dict()
cluster9=dict()
cluster10=dict()


#cluster1
i = 0
for val in uniqueValues:
    cluster1[val] = data[0][i]
    i = i + 1

k = Counter(cluster1)
high = k.most_common(5)


print("Top 5 words and their feature values in Cluster 1:")
for j in high:
    print(j[0], " :", j[1], " ")

print("\n")
#cluster2
i=0
for val in uniqueValues:
    cluster2[val]=data[1][i]
    i=i+1

k = Counter(cluster2)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 2:\n")
for j in high:
    print(j[0], " :", j[1], " ")

print("\n")
#cluster3
i=0
for val in uniqueValues:
    cluster3[val]=data[2][i]
    i=i+1

k = Counter(cluster3)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 3:\n")
for j in high:
    print(j[0], " :", j[1], " ")

print("\n")
#cluster4
i=0
for val in uniqueValues:
    cluster4[val]=data[3][i]
    i=i+1

k = Counter(cluster4)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 4:\n")
for j in high:
    print(j[0], " :", j[1], " ")
print("\n")

#cluster5
i=0
for val in uniqueValues:
    cluster5[val]=data[4][i]
    i=i+1

k = Counter(cluster5)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 5:\n")
for j in high:
    print(j[0], " :", j[1], " ")

print("\n")
#cluster6
i=0
for val in uniqueValues:
    cluster6[val]=data[5][i]
    i=i+1
k = Counter(cluster6)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 6:\n")
for j in high:
    print(j[0], " :", j[1], " ")

print("\n")
#cluster7
i=0
for val in uniqueValues:
    cluster7[val]=data[6][i]
    i=i+1

k = Counter(cluster7)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 7:\n")
for j in high:
    print(j[0], " :", j[1], " ")

print("\n")
#cluster8
i=0
for val in uniqueValues:
    cluster8[val]=data[7][i]
    i=i+1
k = Counter(cluster8)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 8:\n")
for j in high:
    print(j[0], " :", j[1], " ")

print("\n")
#cluster9
i=0
for val in uniqueValues:
    cluster9[val]=data[8][i]
    i=i+1
k = Counter(cluster9)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 9:\n")
for j in high:
    print(j[0], " :", j[1], " ")

print("\n")
#cluster10
i=0
for val in uniqueValues:
    cluster10[val]=data[9][i]
    i=i+1
k = Counter(cluster10)
high = k.most_common(5)
print("Top 5 words and their feature values in Cluster 10:\n")
for j in high:
    print(j[0], " :", j[1], " ")
