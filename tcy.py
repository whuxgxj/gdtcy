#!/usr/bin/python
#-*-coding:utf-8-*-
import os
import re
from pandas import DataFrame
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

DIR = "/app/tcygd/data/"
files = os.listdir(DIR)
print files
# files = ["PlayerDespoitData20170129.log"]







def read_log_file(file):
    with open("/app/tcygd/data/"+file,"rb") as fi:
        data = []
        data_rows=fi.readlines()
        # headers =filter(lambda x: x, data_rows[0].replace('\r',"").replace('\t'," ").replace('\n',"").split(' '))
        for dr in data_rows[1:]:
            if dr=="": continue
            data_row = ','.join(filter(lambda x: x, dr.replace('\r\r\n',"").split(' '))).split(",")
            data_row.append(re.findall("\d+",file)[0])
            data.append(data_row)
            print data_row
        if len(data_row)==17:
            headers = ["time","houseID","userID","TotalNo","firstHouseID","Money","TeaFea","class","winorlose","S&D","tonghuashunshu","liuzha","siwangzha","zuduichengyuan","duihuanquan","shifouzuopai","Date"]
        else:
            headers = ["time","houseID","userID","TotalNo","firstHouseID","Money","TeaFea","class","winorlose","S&D","tonghuashunshu","liuzha","siwangzha","zuduichengyuan","Date"]
        data = DataFrame(data,index=None,columns=headers,dtype=int)
        # AverageNew = data[data["TotalNo"]<5].groupby("userID")["time"].count().mean()
    return data

for f in files:
    file = read_log_file(f).to_csv(f.replace(".log",".csv"),encoding="utf-8", index=False)



# # 生成时间序列来计算留存与流失用户
# date_range = pd.date_range("28/12/2016",periods=41,freq='D')
# # 玩家总括数据
# wanjia = []
# # 按循环计算
# for i in range(len(date_range)):
#     today_data = read_log_file("/app/tcygd/data/PlayerDespoitData"+str(date_range[i].date()).replace("-","")+".log")
#     AverageNew = today_data[today_data["TotalNo"]<5]["userID"].value_count().mean()
#     AverageLost = None
#     AverageRemain = None
#     if i != 0:
#         today_users = today_data["userID"].unique()
#         lastday_users = lastday_data["userID"].unique()


#     day_row = []
#     if i ==  0:
#         today_file = "/app/tcygd/data/PlayerDespoitData"+str(date_range[i].date()).replace("-","")+".log"
#         today_data = read_log_file(today_file)

#         wanjia.append([date_range[i].date(),AverageNew,None,None])
#         lastday_data = today_data
#         continue




    



