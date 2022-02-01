import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
df=pd.read_csv("train.csv")
id=df['id']
text=df['text']
def lab3():
    s=dict()
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    count=0
    for a in id:
        string=text[count].lower()
        words=string.split()
        lis=[]
        for word in words:
            if word not in stop_words:
                lis.append(ps.stem(word))
        s[a]=lis
        count+=1
    stance=[]
    sentence=input("enter a sentence:")
    yoda=sentence.split()
    for word in yoda:
        if word not in stop_words:
            x=ps.stem(word)
            stance.append(x.lower())
    s1=dict()
    for a in stance:
        dic=dict()
        for i in s:
            bro = s[i]
            if a in bro:
                lis = []

                for j in range(0,len(bro)):
                    if(a==bro[j]):
                        lis.append(j)
                dic[i]=lis
        res = not dic
        if(str(res)!=True):
            s1[a]=dic
    for a in s1:
        print(a,s1[a])
lab3()