# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:12:46 2018

@author: www
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns

train = pd.read_excel(r'E:\data\ProblemCData.xlsx',encoding='gbk')


ca = pd.DataFrame()
ca = train[train.StateCode=='CA']
ca.to_csv(r'E:\data\CA.csv')

az = pd.DataFrame()
az = train[train.StateCode=='AZ']
az.to_csv(r'E:\data\AZ.csv')

nm = pd.DataFrame()
nm = train[train.StateCode=='NM']
nm.to_csv(r'E:\data\NM.csv')

tx = pd.DataFrame()
tx = train[train.StateCode=='TX']
tx.to_csv(r'E:\data\TX.csv')




#对ca表的处理

grouped = ca.groupby('MSN')

ca_feature = pd.DataFrame(columns= ca.MSN.unique(),index=[i for i in range(1960,2010)])

m = ca_feature.columns

for i in m:
     h = grouped.get_group(i)
     if h.shape[0] == 50:
          ca_feature[i] = h['Data'].values


for i in m:
     h = grouped.get_group(i)
     if h.shape[0] == 40:
          ca_feature[i][10:] = h['Data'].values

for i in m:
    h = grouped.get_group(i)
    if (h.shape[0] != 40 and h.shape[0]!=50):
         print(i)
#GDPRX SFCCB SFEIB SFINB SFRCB SFTCB TETGR


ca_feature.to_csv(r'E:\data\ca_feature.csv')

          
 #对az表的处理
 
grouped = az.groupby('MSN')
 
az_feature = pd.DataFrame(columns= az.MSN.unique(),index=[i for i in range(1960,2010)])        
     
m = az_feature.columns

for i in m:
     h = grouped.get_group(i)
     if h.shape[0] == 50:
          az_feature[i] = h['Data'].values


for i in m:
     h = grouped.get_group(i)
     if h.shape[0] == 40:
          az_feature[i][10:] = h['Data'].values

for i in m:
    h = grouped.get_group(i)
    if (h.shape[0] != 40 and h.shape[0]!=50):
         print(i)
#GDPRX SFCCB SFEIB SFINB SFRCB SFTCB TETGR
az_feature.to_csv(r'E:\data\az_feature.csv')



#对nm表的处理
grouped = nm.groupby('MSN')
nm_feature = pd.DataFrame(columns= nm.MSN.unique(),index=[i for i in range(1960,2010)])        
m = nm_feature.columns

for i in m:
     h = grouped.get_group(i)
     if h.shape[0] == 50:
          nm_feature[i] = h['Data'].values

for i in m:
     h = grouped.get_group(i)
     if h.shape[0] == 40:
          nm_feature[i][10:] = h['Data'].values

for i in m:
    h = grouped.get_group(i)
    if (h.shape[0] != 40 and h.shape[0]!=50):
         print(i)
nm_feature.to_csv(r'E:\data\nm_feature.csv')         

#对tx表的处理
grouped = tx.groupby('MSN')
tx_feature = pd.DataFrame(columns= tx.MSN.unique(),index=[i for i in range(1960,2010)])        
m = tx_feature.columns
for i in m:
     h = grouped.get_group(i)
     if h.shape[0] == 50:
          tx_feature[i] = h['Data'].values

for i in m:
     h = grouped.get_group(i)
     if h.shape[0] == 40:
          tx_feature[i][10:] = h['Data'].values

for i in m:
    h = grouped.get_group(i)
    if (h.shape[0] != 40 and h.shape[0]!=50):
         print(i)
tx_feature.to_csv(r'E:\data\tx_feature.csv') 

#读入处理完的表
ca_feature2 = pd.read_csv(r'E:\data\ane\ca_feature.csv')

az_feature2 = pd.read_csv(r'E:\data\ane\az_feature.csv')

nm_feature2 = pd.read_csv(r'E:\data\ane\nm_feature.csv')

tx_feature2 = pd.read_csv(r'E:\data\ane\tx_feature.csv')



ca_feature = pd.DataFrame()
az_feature = pd.DataFrame()
nm_feature = pd.DataFrame()
tx_feature = pd.DataFrame()




def fun1(ca_feature, ca_feature2):
     ca_feature['year'] = ca_feature2['year']
     #总能源概况
     ca_feature['总能源生产'] = ca_feature2['TEPRB']
     ca_feature['总能源消耗'] = ca_feature2['TETCB']
     ca_feature['总能源平均价格'] = ca_feature2['TETCD']
     ca_feature['能源总支出'] = ca_feature2['TETCV']
     ca_feature['每美元消耗的能源总量'] = ca_feature2['TETGR']
     
     #人均能源概况
     ca_feature['人均能源消费总量'] = ca_feature2['TETPB']
     ca_feature['人均能源总支出'] = ca_feature2['TETPV']
     
     ca_feature['常住人口'] = ca_feature2['TPOPP']
     
     #不同部门概况
     ca_feature['运输部门'] = ca_feature2['TNACB']
     ca_feature['商业部门'] = ca_feature2['TNCCB']
     ca_feature['工业部门'] = ca_feature2['TNICB']
     ca_feature['住宅部门'] = ca_feature2['TNRCB']
     
     #再生能源概况
     ca_feature['可再生能源生产'] = ca_feature2['REPRB']
     ca_feature['可再生能源总消费'] = ca_feature2['RETCB']
     
     return ca_feature

ca_feature = fun1(ca_feature, ca_feature2)
az_feature = fun1(az_feature, az_feature2)
nm_feature = fun1(nm_feature, nm_feature2)
tx_feature = fun1(tx_feature, tx_feature2)


#取总能源概况
def fun2(train):
     return train['总能源生产'].mean(),train['总能源消耗'].mean(),train['总能源平均价格'].mean(),train['能源总支出'].mean()

a = fun2(ca_feature)
a = fun2(az_feature)
a = fun2(nm_feature)
a = fun2(tx_feature)

ca_feature = ca_feature.set_index(ca_feature['year'])

#取人均能源概况   双y折线图
fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(ca_feature['year'], ca_feature['人均能源消费总量'],'r')
ax1.set_ylabel('TETPB')
ax1.set_title('CA')

ax2 = ax1.twinx()
ax2.plot(ca_feature['year'], ca_feature['人均能源总支出'], 'b')
ax2.set_xlim([1960, 2010])
ax2.set_ylabel('TETPV')



ax1 = plt.subplot(222)
ax1.plot(az_feature['year'], az_feature['人均能源消费总量'],'r')
ax1.set_ylabel('TETPB')
ax1.set_title('AZ')

ax2 = ax1.twinx()
ax2.plot(az_feature['year'], az_feature['人均能源总支出'], 'b')
ax2.set_xlim([1960, 2010])
ax2.set_ylabel('TETPV')


ax1 = plt.subplot(223)
ax1.plot(nm_feature['year'], nm_feature['人均能源消费总量'],'r')
ax1.set_ylabel('TETPB')
ax1.set_title('NM')

ax2 = ax1.twinx()
ax2.plot(nm_feature['year'], nm_feature['人均能源总支出'], 'b')
ax2.set_xlim([1960, 2010])
ax2.set_ylabel('TETPV')

ax1 = plt.subplot(224)
ax1.plot(tx_feature['year'], tx_feature['人均能源消费总量'],'r')
ax1.set_ylabel('TETPB')
ax1.set_title('TX')

ax2 = ax1.twinx()
ax2.plot(tx_feature['year'], tx_feature['人均能源总支出'], 'b')
ax2.set_xlim([1960, 2010])
ax2.set_ylabel('TETPV')

plt.tight_layout()


#取不同部门概况    饼图

#先取到50年的各部门的总量
def fun3(train):
     return train['运输部门'].sum(), train['商业部门'].sum(), train['工业部门'].sum(), train['住宅部门'].sum()
a = fun3(ca_feature)
b = fun3(az_feature)
c = fun3(nm_feature)
d = fun3(tx_feature)

fig = plt.figure()

labels = ['TNACB', 'TNCCB', 'TNICB', 'TNRCB']

ax1 = fig.add_subplot(221)
ax1.pie(a, labels=labels, autopct='%1.2f%%')
ax1.set_title("CA") 

ax1 = fig.add_subplot(222)
ax1.pie(b, labels=labels, autopct='%1.2f%%')
ax1.set_title("AZ")

ax1 = fig.add_subplot(223)
ax1.pie(c, labels=labels, autopct='%1.2f%%')
ax1.set_title("NM")

ax1 = fig.add_subplot(224)
ax1.pie(d, labels=labels, autopct='%1.2f%%')
ax1.set_title("TX")

plt.tight_layout()


#取可再生能源概况   



def fun4(ca_feature, ca_feature2):
     ca_feature['煤炭消耗量'] = ca_feature2['CLTXP']
     ca_feature['石油消耗量'] = ca_feature2['PATCB']
     ca_feature['天然气消耗量'] = ca_feature2['NNTCB']
     ca_feature['核能消耗量'] = ca_feature2['NUETB']
     ca_feature['风能消耗量'] = ca_feature2['WYTCB']
     ca_feature['太阳能消耗量'] = ca_feature2['SOTCB']
     ca_feature['地热能消耗量'] = ca_feature2['GETCB']
     ca_feature['水能消耗量'] = ca_feature2['HYTCB']
     ca_feature['生物质能'] = ca_feature2['BMTCB']
     ca_feature['净进口电量'] = ca_feature2['ELNIB']
     return ca_feature

ca_feature = fun4(ca_feature, ca_feature2)
az_feature = fun4(az_feature, az_feature2)
nm_feature = fun4(nm_feature, nm_feature2)
tx_feature = fun4(tx_feature, tx_feature2)

#总能源堆积图       

plt.figure(figsize=(13,10))
plt.subplot(221)
colors = ['#000000','#666633','#003333', '#663333','#000066', '#006600','#CCCC99','#336666','#660099','#CD6600']
labels=['CLTXP','PATCB','NNTCB','NUETB','WYTCB','SOTCB','GETCB','HYTCB','BMTCB','ELNIB']
plt.stackplot(ca_feature['year'], ca_feature['煤炭消耗量'],ca_feature['石油消耗量'],ca_feature['天然气消耗量'],ca_feature['核能消耗量'], ca_feature['风能消耗量'],ca_feature['太阳能消耗量'], ca_feature['地热能消耗量'],ca_feature['水能消耗量'], ca_feature['生物质能'],ca_feature['净进口电量'],colors=colors,labels=labels)
plt.title('CA')
plt.legend(loc = 'upper left')

plt.subplot(222)
colors = ['#000000','#666633','#003333', '#663333','#000066', '#006600','#CCCC99','#336666','#660099','#CD6600']
labels=['CLTXP','PATCB','NNTCB','NUETB','WYTCB','SOTCB','GETCB','HYTCB','BMTCB','ELNIB']
plt.stackplot(az_feature['year'], az_feature['煤炭消耗量'],az_feature['石油消耗量'],az_feature['天然气消耗量'],az_feature['核能消耗量'], az_feature['风能消耗量'],az_feature['太阳能消耗量'], az_feature['地热能消耗量'],az_feature['水能消耗量'], az_feature['生物质能'],az_feature['净进口电量'],colors=colors,labels=labels)
plt.title('AZ')
plt.legend(loc = 'upper left')

plt.subplot(223)
colors = ['#000000','#666633','#003333', '#663333','#000066', '#006600','#CCCC99','#336666','#660099','#CD6600']
labels=['CLTXP','PATCB','NNTCB','NUETB','WYTCB','SOTCB','GETCB','HYTCB','BMTCB','ELNIB']
plt.stackplot(nm_feature['year'], nm_feature['煤炭消耗量'],nm_feature['石油消耗量'],nm_feature['天然气消耗量'],nm_feature['核能消耗量'], nm_feature['风能消耗量'],nm_feature['太阳能消耗量'], nm_feature['地热能消耗量'],nm_feature['水能消耗量'], nm_feature['生物质能'],nm_feature['净进口电量'],colors=colors,labels=labels)
plt.title('NM')
plt.legend(loc = 'upper left')

plt.subplot(224)
colors = ['#000000','#666633','#003333', '#663333','#000066', '#006600','#CCCC99','#336666','#660099','#CD6600']
labels=['CLTXP','PATCB','NNTCB','NUETB','WYTCB','SOTCB','GETCB','HYTCB','BMTCB','ELNIB']
plt.stackplot(tx_feature['year'], tx_feature['煤炭消耗量'],tx_feature['石油消耗量'],tx_feature['天然气消耗量'],tx_feature['核能消耗量'], tx_feature['风能消耗量'],tx_feature['太阳能消耗量'], tx_feature['地热能消耗量'],tx_feature['水能消耗量'], tx_feature['生物质能'],tx_feature['净进口电量'],colors=colors,labels=labels)
plt.title('TX')
plt.legend(loc = 'upper left')

plt.tight_layout()

#核能以及可再生能源堆积图

plt.figure(figsize=(13,10))
plt.subplot(221)
colors = ['#663333','#000066', '#006600','#CCCC99','#336666','#660099']
labels=['NUETB','WYTCB','SOTCB','GETCB','HYTCB','BMTCB']
plt.stackplot(ca_feature['year'], ca_feature['核能消耗量'], ca_feature['风能消耗量'],ca_feature['太阳能消耗量'], ca_feature['地热能消耗量'],ca_feature['水能消耗量'], ca_feature['生物质能'],colors=colors,labels=labels)
plt.title('CA')
plt.legend(loc = 'upper left')

plt.subplot(222)
colors = ['#663333','#000066', '#006600','#CCCC99','#336666','#660099']
labels=['NUETB','WYTCB','SOTCB','GETCB','HYTCB','BMTCB']
plt.stackplot(az_feature['year'], az_feature['核能消耗量'], az_feature['风能消耗量'],az_feature['太阳能消耗量'], az_feature['地热能消耗量'],az_feature['水能消耗量'], az_feature['生物质能'],colors=colors,labels=labels)
plt.title('AZ')
plt.legend(loc = 'upper left')

plt.subplot(223)
colors = ['#663333','#000066', '#006600','#CCCC99','#336666','#660099']
labels=['NUETB','WYTCB','SOTCB','GETCB','HYTCB','BMTCB']
plt.stackplot(nm_feature['year'], nm_feature['核能消耗量'], nm_feature['风能消耗量'],nm_feature['太阳能消耗量'], nm_feature['地热能消耗量'],nm_feature['水能消耗量'], nm_feature['生物质能'],colors=colors,labels=labels)
plt.title('NM')
plt.legend(loc = 'upper left')

plt.subplot(224)
colors = ['#663333','#000066', '#006600','#CCCC99','#336666','#660099']
labels=['NUETB','WYTCB','SOTCB','GETCB','HYTCB','BMTCB']
plt.stackplot(tx_feature['year'], tx_feature['核能消耗量'], tx_feature['风能消耗量'],tx_feature['太阳能消耗量'], tx_feature['地热能消耗量'],tx_feature['水能消耗量'], tx_feature['生物质能'],colors=colors,labels=labels)
plt.title('TX')
plt.legend(loc = 'upper left')

plt.tight_layout()



#四洲使用可再生能源概况
ca_feature['可再生生产'] = ca_feature2['REPRB']
ca_feature['可再生总消费'] = ca_feature2['RETCB']
ca_feature['GDP'] = ca_feature2['GDPRX']
ca_feature['可再生生产比例'] = ca_feature['可再生生产'] / ca_feature['总能源生产']
ca_feature['可再生消费比例'] = ca_feature['可再生总消费'] / ca_feature['总能源消耗']
ca_feature['能源供需'] = ca_feature['总能源生产'] / ca_feature['总能源消耗']

az_feature['可再生生产'] = az_feature2['REPRB']
az_feature['可再生总消费'] = az_feature2['RETCB']
az_feature['GDP'] = az_feature2['GDPRX']
az_feature['可再生生产比例'] = az_feature['可再生生产'] / az_feature['总能源生产']
az_feature['可再生消费比例'] = az_feature['可再生总消费'] / az_feature['总能源消耗']
az_feature['能源供需'] = az_feature['总能源生产'] / az_feature['总能源消耗']

nm_feature['可再生生产'] = nm_feature2['REPRB']
nm_feature['可再生总消费'] = nm_feature2['RETCB']
nm_feature['GDP'] = nm_feature2['GDPRX']
nm_feature['可再生生产比例'] = nm_feature['可再生生产'] / nm_feature['总能源生产']
nm_feature['可再生消费比例'] = nm_feature['可再生总消费'] / nm_feature['总能源消耗']
nm_feature['能源供需'] = nm_feature['总能源生产'] / nm_feature['总能源消耗']

tx_feature['可再生生产'] = tx_feature2['REPRB']
tx_feature['可再生总消费'] = tx_feature2['RETCB']
tx_feature['GDP'] = tx_feature2['GDPRX']
tx_feature['可再生生产比例'] = tx_feature['可再生生产'] / tx_feature['总能源生产']
tx_feature['可再生消费比例'] = tx_feature['可再生总消费'] / tx_feature['总能源消耗']
tx_feature['能源供需'] = tx_feature['总能源生产'] / tx_feature['总能源消耗']

#四洲能源消耗图

#总能源消耗
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['总能源消耗'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['总能源消耗'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['总能源消耗'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['总能源消耗'])

#可再生能源消耗
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['可再生能源总消费'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['可再生能源总消费'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['可再生能源总消费'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['可再生能源总消费'])


#总能源生产

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['总能源生产'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['总能源生产'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['总能源生产'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['总能源生产'])

#总平均价格

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['总能源平均价格'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['总能源平均价格'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['总能源平均价格'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['总能源平均价格'])

#总人口

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['常住人口'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['常住人口'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['常住人口'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['常住人口'])


#可再生能源生产
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['可再生能源生产'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['可再生能源生产'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['可再生能源生产'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['可再生能源生产'])

#原油生产
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature2['PAPRB'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature2['PAPRB'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature2['PAPRB'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature2['PAPRB'])

#天然气生产

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature2['NGMPB'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature2['NGMPB'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature2['NGMPB'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature2['NGMPB'])

#煤炭生产

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature2['CLPRB'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature2['CLPRB'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature2['CLPRB'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature2['CLPRB'])

#煤炭净进口  数据无
#电力进口

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature2['ELIMB'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature2['ELIMB'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature2['ELIMB'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature2['ELIMB'])

#能源消耗
#石油消耗
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['石油消耗量']) 
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['石油消耗量'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['石油消耗量'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['石油消耗量'])

#天然气消耗
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['天然气消耗量'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['天然气消耗量'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['天然气消耗量'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['天然气消耗量'])


#煤炭消耗
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['煤炭消耗量'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['煤炭消耗量'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['煤炭消耗量'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['煤炭消耗量'])

#太阳能消耗
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['太阳能消耗量'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['太阳能消耗量'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['太阳能消耗量'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['太阳能消耗量'])

#水能消耗
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['水能消耗量'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['水能消耗量'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['水能消耗量'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['水能消耗量'])

#风能消耗量
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['风能消耗量'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['风能消耗量'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['风能消耗量'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['风能消耗量'])

#地热能消耗量
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['地热能消耗量'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['地热能消耗量'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['地热能消耗量'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['地热能消耗量'])


#能源供需
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['能源供需'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['能源供需'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['能源供需'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['能源供需'])


#可再生能源比例

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['可再生生产比例'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['可再生生产比例'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['可再生生产比例'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['可再生生产比例'])

#可再生消费比例

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['可再生消费比例'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['可再生消费比例'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['可再生消费比例'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['可再生消费比例'])

#人均能源消费

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature2['TETPB'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature2['TETPB'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature2['TETPB'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature2['TETPB'])

#人均能源支出

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature2['TETPV'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature2['TETPV'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature2['TETPV'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature2['TETPV'])

#GDP
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feature['GDP'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feature['GDP'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feature['GDP'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feature['GDP'])


#能源消耗 增长模型
#可再生能源包括风能，太阳能，地热能，水能，生物能，
#清洁能源包括核能和可再生能源
#不可再生能源包括石油，天然气，煤炭


#石油的资源贡献率：
ca_feature['石油贡献率'] = ca_feature2['PATCB'].diff()
ca_feature['石油贡献率'].plot()

#天然气的资源贡献率：
ca_feature['天然气贡献率'] = ca_feature2['NNTCB'].diff()
ca_feature['天然气贡献率'].plot()

#煤炭的资源贡献率：
ca_feature['煤炭贡献率'] = ca_feature2['CLTXP'].diff()
ca_feature['煤炭贡献率'].plot()

#核能的资源贡献率：
ca_feature['核能贡献率'] = ca_feature2['NUETB'].diff()
ca_feature['核能贡献率'].plot()

#水能的资源贡献率：
ca_feature['水能贡献率'] = ca_feature2['HYTCB'].diff()
ca_feature['水能贡献率'].plot()

#风能的资源贡献率
ca_feature['风能贡献率'] = ca_feature2['WYTCB'].diff()
ca_feature['风能贡献率'].plot()

corrmat = ca_feature.corr()
f, ax = plt.subplots(figsize=(10, 7))

sns.heatmap(corrmat, vmax=.8, square=True)



#利用最小二乘，对四个州的资源消耗总量进行线性拟合
from sklearn.linear_model import LinearRegression
from sklearn import metrics
lr = LinearRegression()
x = ca_feature['year'].values.reshape(-1,1)
y = ca_feature['总能源消耗'].values
lr.fit(x,y )
ypred = lr.predict(x)
print(lr.coef_)
print(lr.intercept_)
np.sqrt(metrics.mean_squared_error(ypred, y))



ca_feature['部门总消耗'] = ca_feature['工业部门'] + ca_feature['商业部门'] + ca_feature['住宅部门'] + ca_feature['运输部门'] 
ca_feature['部门总消耗2'] = ca_feature2['TECCB'] + ca_feature2['TEICB'] + ca_feature2['TERCB'] + ca_feature2['TEACB']

#GDP

ca_feature['GDP'].ix[0:17] = a
az_feature['GDP'].ix[0:17] = b
nm_feature['GDP'].ix[0:17] = c
tx_feature['GDP'].ix[0:17] = d


#选取对应指标进行建模
ca_feat = pd.DataFrame()
az_feat = pd.DataFrame()
nm_feat = pd.DataFrame()
tx_feat = pd.DataFrame()

ca_feat['TETCB'] = ca_feature['总能源消耗']               #总能源消耗
ca_feat['TPOPP'] = ca_feature['常住人口']                  #人口
ca_feat['TEPRB'] = ca_feature['总能源生产']                #总能源生产
ca_feat['GDPRX'] = ca_feature['GDP']                     #GDP
ca_feat['REPRB'] = ca_feature['可再生能源生产']        #可再生能源生产
ca_feat['WYTCB'] = ca_feature2['WYTCB']             #风能
ca_feat['NUETB'] = ca_feature2['NUETB']             #核电
ca_feat['HYTCB'] = ca_feature2['HYTCB']             #水电
ca_feat['GEEGB'] = ca_feature2['GEEGB']             #地热能
ca_feat['SOEGB'] = ca_feature2['SOEGB']             #太阳能
ca_feat['PAPRB'] = ca_feature2['PAPRB']             #原油生产
ca_feat['NGMPB'] = ca_feature2['NGMPB']             #天然气生产
ca_feat['EMFDB'] = ca_feature2['EMFDB']             #生物质能

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error

predicotrs = [i for i in ca_feat.columns if i != 'TETCB']
x_train, x_test, y_train, y_test = train_test_split(ca_feat[predicotrs], ca_feat['TETCB'], test_size = 0.2)

gbr = GradientBoostingRegressor()

gbr.fit(x_train, y_train)
pred = gbr.predict(x_test)
print(np.sqrt(mean_squared_error(pred, y_test)))

feature_import=pd.DataFrame()
feature_import['res'] = predicotrs
feature_import['score'] = gbr.feature_importances_


#各种资源消耗量与总消耗量的分析

#选取对应指标进行建模
ca_feat = pd.DataFrame()
az_feat = pd.DataFrame()
nm_feat = pd.DataFrame()
tx_feat = pd.DataFrame()

def fun7(train, ca_feature):
#==============================================================================
#      train['TETCB'] = ca_feature['总能源消耗']               #总能源消耗
#      train['TPOPP'] = ca_feature['常住人口']                  #人口
#      train['TEPRB'] = ca_feature['总能源生产']                #总能源生产
#      train['GDPRX'] = ca_feature['GDP']                     #GDP
#      train['REPRB'] = ca_feature['可再生能源生产']        #可再生能源生产
#==============================================================================
     train['CLTXP'] = ca_feature['煤炭消耗量']
     train['PATCB'] = ca_feature['石油消耗量']
     train['NNTCB'] = ca_feature['天然气消耗量']
     train['NUETB'] = ca_feature['核能消耗量']
     train['WYTCB'] = ca_feature['风能消耗量']
     train['SOTCB'] = ca_feature['太阳能消耗量']
     train['GETCB'] = ca_feature['地热能消耗量']
     train['HYTCB'] = ca_feature['水能消耗量']
     train['BMTCB'] = ca_feature['生物质能']
     return train

ca_feat = fun7(ca_feat, ca_feature)
az_feat = fun7(az_feat, az_feature)
nm_feat = fun7(nm_feat, nm_feature)
tx_feat = fun7(tx_feat, tx_feature)

#ca的特征重要度排序
predicotrs = [i for i in az_feat.columns if i != 'TETCB']
x_train, x_test, y_train, y_test = train_test_split(ca_feat[predicotrs], ca_feat['TETCB'], test_size = 0.2)

gbr = GradientBoostingRegressor()

gbr.fit(x_train, y_train)
pred = gbr.predict(x_test)
print(np.sqrt(mean_squared_error(pred, y_test)))

feature_import=pd.DataFrame()
feature_import['res'] = predicotrs
feature_import['score'] = gbr.feature_importances_
feature_import = feature_import.sort_index(by='score')

#az的特征重要度排序

x_train, x_test, y_train, y_test = train_test_split(az_feat[predicotrs], az_feat['TETCB'], test_size = 0.2)

gbr = GradientBoostingRegressor()

gbr.fit(x_train, y_train)
pred = gbr.predict(x_test)
print(np.sqrt(mean_squared_error(pred, y_test)))

feature_import_az=pd.DataFrame()
feature_import_az['res'] = predicotrs
feature_import_az['score'] = gbr.feature_importances_
feature_import_az = feature_import_az.sort_index(by='score')


#选取对应指标进行建模 总能量建模
ca_feat = pd.DataFrame()
az_feat = pd.DataFrame()
nm_feat = pd.DataFrame()
tx_feat = pd.DataFrame()

def fun7(train, ca_feature):
     train['总能源消耗'] = ca_feature['TETCB']               #总能源消耗
     train['人口'] = ca_feature['TPOPP']                  #人口
     train['总能源生产'] = ca_feature['TEPRB']                #总能源生产
     train['GDP'] = ca_feature['GDPRX']                     #GDP
     train['可再生能源生产'] = ca_feature['REPRB']        #可再生能源生产
     train['工业占比'] = ca_feature['TEICB']/ca_feature['TETCB']   #工业占比
     train['能源强度'] = ca_feature['TETGR']
     return train

ca_feat = fun7(ca_feat, ca_feature2)
az_feat = fun7(az_feat, az_feature2)
nm_feat = fun7(nm_feat, nm_feature2)
tx_feat = fun7(tx_feat, tx_feature2)

#填充缺失值
ca_feat['GDP'].ix[0:17] = a
az_feat['GDP'].ix[0:17] = b
nm_feat['GDP'].ix[0:17] = c
tx_feat['GDP'].ix[0:17] = d

#对能源强度做预测
ca_feat['能源强度'].ix[0:16] = [14.0,13.8,13.6,13.4,13.2,13.0,12.8,12.6,12.4,12.2,12.0,11.8,11.6,11.4,11.2,11.0,10.8]
az_feat['能源强度'].ix[0:16] = [21.0,20.8,20.6,20.4,20.0,19.7,19.3,18.9,18.7,18.2,17.9,17.6,17.1,16.8,16.4,16.0,15.7]
nm_feat['能源强度'].ix[0:16] = [26.0,25.6,25.1,24.8,24.8,24.4,24.0,23.5,23.4,23.0,22.6,22.1,21.6,21.6,21.4,21.0,20.6]
tx_feat['能源强度'].ix[0:16] = [28.9,28.6,28.4,27.9,27.6,27.4,27.0,26.7,26.4,26.0,25.6,25.3,25.0,24.6,24.2,23.6,23.2]

#能源强度比例画图

plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feat['能源强度'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feat['能源强度'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feat['能源强度'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feat['能源强度'])

#工业占比预测画图
plt.figure()
plt.subplot(221)
plt.plot(ca_feature['year'], ca_feat['工业占比'])
plt.subplot(222)
plt.plot(az_feature['year'], az_feat['工业占比'])
plt.subplot(223)
plt.plot(nm_feature['year'], nm_feat['工业占比'])
plt.subplot(224)
plt.plot(tx_feature['year'], tx_feat['工业占比'])


ca_2025 = np.array([42500.302,3433415.956,2495876,676324.8087,0.171729603,3.50784])
ca_2050 = np.array([54381.23,3763659.456,3745876,697820.3088,0.142936,2.3258])

az_2025 = np.array([9109.866,690114.9798,421218,87119.08004,0.125725,4.95945])
az_2050 = np.array([11493.306,653736.2345,731093,81735.55497,0.10895,3.54789])

nm_2025 = np.array([2378.177,2728386.896,108098,75671.97129,0.285784086,6.63304])
nm_2050 = np.array([3020.63,2780060.767,170598,137551.5625,0.263813304,4.9916])

tx_2025 = np.array([31379.69,11699623.17,1125295,1211916.683,0.45907,6.5237])
tx_2050 = np.array([38722.302,11954765.45,1214520,2604862.262,0.3717,4.6897])

def fun8(train, test):
     predicotrs = [i for i in train.columns if i != '总能源消耗']
     x_train, x_test, y_train, y_test = train_test_split(train[predicotrs], train['总能源消耗'], test_size = 0.2)
     
     gbr = GradientBoostingRegressor()
     
     gbr.fit(x_train, y_train)
     pred = gbr.predict(x_test)
     print(np.sqrt(mean_squared_error(pred, y_test)))   
     
     feature_import=pd.DataFrame()
     feature_import['res'] = predicotrs
     feature_import['score'] = gbr.feature_importances_
     test_pred = gbr.predict(test)
     return test_pred

ca_2025_pred = fun8(ca_feat, ca_2025)   #136485.753877
ca_2050_pred = fun8(ca_feat, ca_2050)   #126488.026886

az_2025_pred = fun8(az_feat, az_2025)   #26059.4115358
az_2050_pred = fun8(az_feat, az_2050)   #32635.5053406

nm_2025_pred = fun8(nm_feat, nm_2025)   #14625.9064192
nm_2050_pred = fun8(nm_feat, nm_2050)   #28513.4654125

tx_2025_pred = fun8(tx_feat, tx_2025)  #365218.622063
tx_2050_pred = fun8(tx_feat, tx_2050)  #216942.657143


#选取对应指标进行建模：可再生建模
ca_feat = pd.DataFrame()
az_feat = pd.DataFrame()
nm_feat = pd.DataFrame()
tx_feat = pd.DataFrame()

def fun9(train, ca_feature):
     train['可再生能源消耗'] = ca_feature['RETCB']               #总能源消耗
     train['人口'] = ca_feature['TPOPP']                  #人口
     train['总能源生产'] = ca_feature['TEPRB']                #总能源生产
     train['GDP'] = ca_feature['GDPRX']                     #GDP
     train['可再生能源生产'] = ca_feature['REPRB']        #可再生能源生产
     train['工业占比'] = ca_feature['TEICB']/ca_feature['TETCB']   #工业占比
     train['能源强度'] = ca_feature['TETGR']
     return train

ca_feat = fun9(ca_feat, ca_feature2)
az_feat = fun9(az_feat, az_feature2)
nm_feat = fun9(nm_feat, nm_feature2)
tx_feat = fun9(tx_feat, tx_feature2)


#填充缺失值
ca_feat['GDP'].ix[0:17] = a
az_feat['GDP'].ix[0:17] = b
nm_feat['GDP'].ix[0:17] = c
tx_feat['GDP'].ix[0:17] = d

#对能源强度做预测
ca_feat['能源强度'].ix[0:16] = [14.0,13.8,13.6,13.4,13.2,13.0,12.8,12.6,12.4,12.2,12.0,11.8,11.6,11.4,11.2,11.0,10.8]
az_feat['能源强度'].ix[0:16] = [21.0,20.8,20.6,20.4,20.0,19.7,19.3,18.9,18.7,18.2,17.9,17.6,17.1,16.8,16.4,16.0,15.7]
nm_feat['能源强度'].ix[0:16] = [26.0,25.6,25.1,24.8,24.8,24.4,24.0,23.5,23.4,23.0,22.6,22.1,21.6,21.6,21.4,21.0,20.6]
tx_feat['能源强度'].ix[0:16] = [28.9,28.6,28.4,27.9,27.6,27.4,27.0,26.7,26.4,26.0,25.6,25.3,25.0,24.6,24.2,23.6,23.2]


ca_2025 = np.array([42500.302,3433415.956,2495876,676324.8087,0.171729603,3.50784])
ca_2050 = np.array([54381.23,3763659.456,3745876,697820.3088,0.142936,2.3258])

az_2025 = np.array([9109.866,690114.9798,421218,87119.08004,0.125725,4.95945])
az_2050 = np.array([11493.306,653736.2345,731093,81735.55497,0.10895,3.54789])

nm_2025 = np.array([2378.177,2728386.896,108098,75671.97129,0.285784086,6.63304])
nm_2050 = np.array([3020.63,2780060.767,170598,137551.5625,0.263813304,4.9916])

tx_2025 = np.array([31379.69,11699623.17,1125295,1211916.683,0.45907,6.5237])
tx_2050 = np.array([38722.302,11954765.45,1214520,2604862.262,0.3717,4.6897])

def fun10(train, test):
     predicotrs = [i for i in train.columns if i != '可再生能源消耗']
     x_train, x_test, y_train, y_test = train_test_split(train[predicotrs], train['可再生能源消耗'], test_size = 0.2)
     
     gbr = GradientBoostingRegressor()
     
     gbr.fit(x_train, y_train)
     pred = gbr.predict(x_test)
     print(np.sqrt(mean_squared_error(pred, y_test)))   
     
     feature_import=pd.DataFrame()
     feature_import['res'] = predicotrs
     feature_import['score'] = gbr.feature_importances_
     test_pred = gbr.predict(test)
     return test_pred

ca_2025_pred = fun10(ca_feat, ca_2025)   #136485.753877    #22854.7159164
ca_2050_pred = fun10(ca_feat, ca_2050)   #126488.026886    #13917.4911294

az_2025_pred = fun10(az_feat, az_2025)   #26059.4115358     #5380.41207443
az_2050_pred = fun10(az_feat, az_2050)   #32635.5053406     #3291.19712351

nm_2025_pred = fun10(nm_feat, nm_2025)   #14625.9064192    #473.230052219
nm_2050_pred = fun10(nm_feat, nm_2050)   #28513.4654125    #1138.20844403

tx_2025_pred = fun10(tx_feat, tx_2025)  #365218.622063     #22773.5502662
tx_2050_pred = fun10(tx_feat, tx_2050)  #216942.657143     #14010.7033644

plt.figure()
plt.subplot(121)
x1 = np.array([1,2,3,4])
x2  = np.array(['CA','AZ','NM','TX'])
plt.xticks(x1,x2)
y1 = np.array([449956.82,114660.65 ,67541.20,233552.12])
y2 = np.array([203408.69,51010.95, 31784.10 ,109906.88])

plt.bar(x1,+y1,width=0.5,facecolor = 'blue',edgecolor="white")  
plt.bar(x1,-y2,width=0.5,facecolor = 'green',edgecolor="white") 

plt.subplot(122)
x1 = np.array([1,2,3,4])
x2  = np.array(['CA','AZ','NM','TX'])
plt.xticks(x1,x2)
y1 = np.array([490193.60,134660.65 ,78777.06,253552.12])
y2 = np.array([233408.69,54010.95, 43784.10 ,139906.88])

plt.bar(x1,+y1,width=0.5,facecolor = 'blue',edgecolor="white")  
plt.bar(x1,-y2,width=0.5,facecolor = 'green',edgecolor="white") 










