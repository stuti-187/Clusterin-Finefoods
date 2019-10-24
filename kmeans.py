import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

colnames = ['Word', 'Total Word Count']
data = pd.read_csv('top500.csv', encoding="ISO-8859-1", skipinitialspace=True,
                   usecols=colnames)
uniqueValuesDF = data['Word']
uniqueValues = uniqueValuesDF.tolist()

colname = uniqueValues
data = pd.read_csv('vectors.csv', encoding="ISO-8859-1", skipinitialspace=True,
                   usecols=colname)

df = pd.DataFrame(data, columns=colname)
# print(df)
kmeans = KMeans(n_clusters=10).fit(df)
centroids = kmeans.cluster_centers_
# print(centroids)

OUTPUT_FILE_NAME = "centroids.csv"
outfile = open(OUTPUT_FILE_NAME, "w")
header = ""
for item in uniqueValues:
    header = header + str(item) + ", "

outfile.write(header + "\n")

result = ""
for values in centroids:
    for singleValue in values:
        result = result + str(singleValue) + ", "
    result = result + "\n"
    outfile.write(result)
    result = ""

outfile.close()

# plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
# plt.show()
