#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello\nworld!")


# In[2]:


float(2)


# In[3]:


str(3.1)


# In[4]:


type(int(1.0))


# In[5]:


A=(0,1,2,3)

A[-1]
A[3]


# In[9]:


B=['a','b','c']
B[1:]


# In[10]:


D={'a':0,'b':1,'c':2}
D.values()


# In[2]:


PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
New =[0]

while (PlayListRatings[i] > 6):
    New = PlayListRatings[i]
    print(New)
    i = i+1


# In[5]:


def f(c):
    
    return sum(c)


a = [1,2]

f(a)


# In[7]:


class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1
        

my_car = Car(make='BMW', model='M3', color='red')


# In[8]:


my_car.car_info()


# In[10]:


my_car = Car('BMW', 'M3', 'red')
my_car.car_info()


# In[14]:


my_car = Car(model='M3', make='BMW', color='red')
my_car.car_info()   #here the value of make is still the same


# In[15]:


my_car = Car('M3', 'BMW', color='red')
my_car.car_info() #here the value of make is not the same so you can't change the order, if you want to do it yo need to use the other options above


# In[15]:


#Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"
#freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
#freqOf - returns the frequency of the word passed in argument.


class analysedText(object):

    def __init__ (self, text): #constructor 
        paragraph = text.lower()
        text = paragraph.replace('.','').replace(',','').replace('!','').replace('?','')
        self.fmtText = text
        pass

    def freqAll(self):
        listtext = self.fmtText.split(' ') #you have to split the text to convert it into a list
        unique = set(listtext) #change the list into a set
        
        dic = {}
        for i in unique:
            dic[i] = listtext.count(i)
        return dic
        pass

    def freqOf(self,word):
        checkdic = self.freqAll()
        
        if word in checkdic:
            return checkdic[word]
        else:
            return 0
        pass

    


# In[16]:


import sys

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )
    


# In[211]:



N=5

with open('ex4.csv','r') as file:
    file1 = file.readlines()[1:] #take out the header 
    m = []
    for i in file1:
        file2 =i.strip('\n') #take out the \n
        file3 = file2.split(',') #take out the ,
        file4 = file3[1] #makes a string called file4
        #file4 = file3[1::2] makes a list of one string each time 
        m.append(float(file4)) #put all the values in file4 into ONE list called m and change them into floats 

        
m
    


# In[212]:


s = []
j=0
cond = N
while cond <= len(m):
    s.append(sum(m[j:cond])/N)
    j=j+1
    cond = cond+1

s


# In[203]:


cond = N
while cond < len(m):
    s.append(sum(m[j:cond])/N)
    j=j+1
    cond = cond+1

s


# In[82]:


from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)


# In[75]:


# This method is no the best because is long and it takes a lot to change a list of lists into a string. I made it but is not the best way to do it
with open('members.txt','r') as currentmen:
    header = currentmen.seek(0)
    file5 = currentmen.readline()
    file6 = currentmen.readlines()[1:] #take out the header 
    file9 = []
    for k in file6:
        file7 = k.replace('\n','')
        file8 = file7.split()
        file9.append(file8)
    
    file10 = []
    file11 = []
    for b in file9:
        if b[2] == 'no':
            file10.append(b)
        else: 
            file11.append(b)  

with open('members1.txt','w') as currentmem1:
    currentmem1.write(file5)
    for x in file11:
        for p in x:
            mem = currentmem1.write('\t' + p)
        mem = currentmem1.write('\n')
        
with open('nomem.txt', 'w') as nomem1: 
    nomem1.write(file5)
    for w in file10:
        for a in w:
            exmem = nomem1.write('\t' + a)
        exmem = nomem1.write('\n')


# In[29]:


#Better way to do it, you can search a word in the text or file given. 
    with open(currentMem,'r+') as current:
        header = current.readline() #save the head of the file in the variable header 
        file = current.readlines()#[1:] take out the header
        with open(exMem, 'a+') as nomem:
            current.seek(0)
            current.write(header)
            i = 1
            for i in file: 
                if 'no' in i: 
                    nomem.write(i)
                else: 
                    current.write(i)
            current.truncate()
#r+ opens a file for reading and writing at the begining of the file
#a+ opens a file for reading and appending (at the end of the file)
#w+ openas a file for reading and writing


# In[85]:


import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
df


# In[87]:


#second-row and first column
df.iloc[1,0]


# In[89]:


df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
df['a']==1


# In[ ]:


#https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/535aa2cf-35a1-49ef-979b-3bfb3045ec13/view?access_token=78e5314dede5da1e786dd21e7e3a2057c54829ec91bbb9032fe1ed973cd9d30e
#publicar este trabajo en github


# In[7]:


get_ipython().system('pip install xlrd')
import pandas as pd
import numpy as np
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)


# In[8]:


df.head()


# In[12]:



new_index=['a','b','c','d','e','f','g','h']

df_new = df
df_new.index = new_index

df_new.loc['a','Artist']

df_new.loc['a':'d', 'Artist']


# In[14]:


A=np.array([[1,2],[3,4],[5,6],[7,8]])
A


# In[ ]:




