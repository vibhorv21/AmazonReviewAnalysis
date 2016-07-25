import sklearn
import os
from pprint import pprint
from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

path="./data"
directory=[]
label=[]
overall=0

for root, dirs, files in os.walk(path, topdown=False):
    i=0
    for name in dirs :
    	directory.append(name)

dataset=sklearn.datasets.load_files(path,categories=directory,shuffle=False)
vect = CountVectorizer(decode_error='ignore',stop_words='english')
X= vect.fit_transform(dataset.data)

Y=[]
l=0
for f in dataset.filenames:
    if "pos" in f:
        Y.append(1)
    else:
        Y.append(-1)
    l=l+1


classifier= MultinomialNB().fit(X,Y)
temp=[]
ini = raw_input("Enter Your Review : ")
temp.append(ini)
temp.append("Bad")
X1= vect.transform(temp)
I_p = classifier.predict_proba(X1)
I = classifier.predict(X1)
if I[0]==1 :
    print "Review is Positive with confidence " + str(I_p[0][1]*100) + " % "
elif I[0]==-1 :
    print "Review is Negative with confidence " + str(I_p[0][0]*100) + " % "
