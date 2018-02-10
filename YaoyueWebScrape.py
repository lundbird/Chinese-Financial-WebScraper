# -*- coding: utf-8 -*-
'''
Created on Jun 18, 2017

@author: alex
'''
from bs4 import BeautifulSoup
import requests
import csv

filename='yaoyuescrapeexcel.csv'
f=open(filename,'rb')
reader=csv.reader(filename)
for row in reader:
    print(row)
headers="1,2,3,4,5,6,7,8\n"
f.write(headers)

stock_url='000700'
base_url='http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=sz'
r=requests.get(base_url+stock_url)
soup=BeautifulSoup(r.content,'html.parser')
#selects the entrire table
data=soup.find_all('table',{"class":"needScroll"})
#selects each row from the table
entries=data[0].find_all('tr')

answer_1=entries[9].find_all('td')[1].text
answer_2=entries[13].find_all('td')[1].text
answer_3=entries[23].find_all('td')[1].text
print(answer_1 + "," + answer_2+","+answer_3 +"\n")
#for i in range(len(entries)):
    #selects only row 9,13,23
 #   if i==9|13|23:
        #for that row returns all cells
 #       rows=entries[i].contents.find_all('td')[1]
        #returns cell one text
 #       for row in rows:
  #          answer_1=row[1].text

f.write(answer_1 + "," + answer_2+","+answer_3 +"\n")
f.close()        



if __name__ == '__main__':
    pass