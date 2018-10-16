# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:31:43 2018

@author: Harika
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing datasets

#data deduplication
dataset= pd.read_csv('googleplaystore.csv')
X = dataset.iloc[:,:].values
primKey = dataset.iloc[:,0]

data1 = []
dedupData = []
for i in X:
    if i[0] not in data1:
        data1.append(i[0])
        dedupData.append(i.tolist())
    

dedupData = np.array(dedupData)


df = pd.DataFrame(dedupData, columns = ['App', 'Category','Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Last updated','current version','Android version'])

#removing identical columns

dedupData = df.drop('Genres', axis =1)
dedupData = dedupData.drop('Type', axis =1)

#removing missing values

rats = 0.0
j =len(dedupData.index)

for i in range(j-1):
    rats = float(dedupData.iloc[i,2])
    if (rats<1.0 or rats >5.0):
        dedupData = dedupData.drop(dedupData[i].index)
     
dedupData.reset_index()
k =len(dedupData.index)  
rating = np.empty([k]) 
for i in range(k):
    rating[i] = float(dedupData.iloc[i,2])
#tf = dedupData.isnull()

dedupData.iloc[:,2] = rating
dedupData.replace("nan", np.nan, inplace = True)   
dedupData.info()

import statistics
currver_mod=statistics.mode(dedupData['current version'])
andver_mod = statistics.mode(dedupData['Android version'])

new = dedupData.values
dedupData.info()

def ReplaceNullWithMostFreq(series, most_fre):
    c=0
    for i in series:
        print(i)
        if(i == 'nan'):
            series[c] = most_fre
            #print(series[c])
            #check =90
        c+=1

ReplaceNullWithMostFreq(dedupData['current version'], currver_mod)




from sklearn.preprocessing import Imputer

def replaceMissing(data, strat):
    numpyArr = data.as_matrix()
    imputer = Imputer(missing_values = 'NaN', strategy = strat, axis = 0)
    imputer = imputer.fit(numpyArr[:,2:3])
    numpyArr[:,2:3] = imputer.transform(numpyArr[:,2:3])
    #imputer = imputer.fit(numpyArr[:,9:11])
    #numpyArr[:,9:11] = imputer.transform(numpyArr[:,9:11])
    data = pd.DataFrame(numpyArr, columns = ['App', 'Category','Rating','Reviews','Size','Installs','Price','Content Rating','Last updated','current version','Android version'])
    return data


"""
def replaceMissing(data, strat,ind):
    numpyArr = data.as_matrix()
    imputer = Imputer(missing_values = 'NaN', strategy = strat, axis = 0)
    imputer = imputer.fit(numpyArr[:,ind:ind+1])
    numpyArr[:,ind:ind+1] = imputer.transform(numpyArr[:,ind:ind+1])
    #imputer = imputer.fit(numpyArr[:,9:11])
    #numpyArr[:,9:11] = imputer.transform(numpyArr[:,9:11])
    data = pd.DataFrame(numpyArr, columns = ['App', 'Category','Rating','Reviews','Size','Installs','Price','Content Rating','Last updated','current version','Android version'])
    return data


"""



MeanReplaced = replaceMissing(dedupData,'mean')
MedianReplaced = replaceMissing(dedupData,'median')
ModeReplaced = replaceMissing(dedupData,'most_frequent')

dupli = MeanReplaced.copy()


np.moModeReplaced['current version']
#dedupData.mode()
"""
ModeReplaced.info()

#Categorical
#%timeit [x.strip('$') for x in dedupData.Price]


price = np.empty([k]) 
for i in range(k):
    price[i] = int(dedupData.iloc[i,6])

label_encoded= MeanReplaced.as_matrix()
"""
def CategoricalReplacement(series):
    l = 0
    h = 0
    dict = {}
    for i in series:
        if i not in dict and i!=np.nan:
            dict[i] = l;
            l+=1
        series[h] = dict[series[h]]
        h+=1
    return dict
   
#MeanReplaced.info()

#CurrentDate = dt.datetime.now()

from datetime import datetime
new = dupli['Last updated']
months = dict(Jan=1, Feb=2, Mar=3, Apr=4, May=5, Jun=6, Jul=7, Aug=8, Sep=9, Oct=10, Nov=11, Dec=12)
new_dt=[]
last_upd = []
c=0
for date in new:
    d = date.split("-")
    d[2] = "20"+d[2]
    new_dt.append(datetime(int(d[2]),months[d[1]],int(d[0])))
    delta = datetime.now() - new_dt[c]
    new[c] = delta.days
    c+=1
    
dupli['Last updated'] = new
    
#type(delta) 
"""  
   
    c+=1
    
    date_form = time.strptime(date, "%d-%m-%Y")
    time.strftime("%d/%m/%Y", date_form)
    
    month =""
    for f in date:
        if(f.isalpha()):
            month = month+f
    month_list.append(month)
    date.replace(month,"jki")
    dateArr.append(date)
    new[c,8] = date
    c+=1"""

type(dupli['Rating'][2])

Categor_dict = CategoricalReplacement(dupli['Category'])
#Rating_dict = CategoricalReplacement(dupli['Rating'])
#Installs_dict = CategoricalReplacement(dupli['Installs'])
#Price = CategoricalReplacement(dupli['Price'])
ContentRating_dict = CategoricalReplacement(dupli['Content Rating'])
curr_version_dict = CategoricalReplacement(dupli['current version'])
and_version_dict = CategoricalReplacement(dupli['Android version'])
#size_dict = CategoricalReplacement(dupli['Size'])
npArr = dupli.values
new = npArr[:,3]
c=0
s=""
for s in new:
    dupli['Reviews'] = int(s)
    c+=1
    
    
type()
    
    new[c] = delta.days
    c+=1
type(dupli['Reviews'][3])
Reviews_dict = CategoricalReplacement(dupli['Reviews'])
# to convert reviews, size, installs, price, current version, android version, content rating to numbers
# ratings, last updated, category already converted
sd = "12M"
sd[:-1]

sd.split('M')
MeanReplaced['App'].nunique()
"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
label_encoded[:,7] = labelencoder.fit_transform(label_encoded[:,7])
label_encoded[:,5] = labelencoder.fit_transform(label_encoded[:,5]) 
label_encoded= pd.DataFrame(label_encoded)
"""
type(dedupData['current version'][930])
dedupData['current version'][i]
"""MeanReplacedData = dedupData
replaceWithMean(MeanReplacedData)
"""
dedupData
"""MedianReplacedData = dedupData
replaceWithMean(MedianReplacedData)

dedupData.mode()

ModeReplacedData = dedupData
replaceWithMode(ModeReplacedData)
"""
MeanReplaced.info()

dedupData.Rating.mean()
pr = MeanReplaced['Price']