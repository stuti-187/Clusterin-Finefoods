import os
print("Converting data into CSV format")
os.system('python2.6 DataConversion.py')
print("Converted data has been stored output.csv")
print("Now finding the set L")
os.system('python UniqueWords.py')
print("Set L has been stored in uniqueList1.csv")
print("Now creating set W")
os.system('python RemovingStopword.py')
print("Set W has been created and stored in uniqueListFinal.csv")
print("Finding the top 500 words")
os.system('python Count.py')
print("Top 500 words have been stored in  top500.csv")
print("Vectorizing the data for clustering")
os.system('python vectorize.py')
print("Vectors have been stored in vectors.csv")
print("Finding the centroids of the 10 clusters craeted")
os.system('python kmeans.py')
print("Centroids of the 10 clusters have been stored in centroids.csv")
print("Now we will fetch the top 5 words and their feature values in each cluster")
os.system('python top5.py')
