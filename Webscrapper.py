'''
Created on 19Aug.,2017

@author: MYVIKOK

'''
import requests
from urllib import request
import time
from bs4 import BeautifulSoup as bs
import json,requests,pprint,xlsxwriter
#import re
#from datetime import datetime as dt
#import pandas as pd




class SCRAPPER:   
     
    
    def __init__(self,name,stockCode):
         self.name=name
         self.stockCode = stockCode
    
    #def __convertToPD(fq_date,rev,pbt,np,eps,div,nta,percent):
      
    def getQuarterResult(self):
      

        # Dow Jones
        
        rows = None
        table = None
        
        response = requests.get("https://www.malaysiastock.biz/Corporate-Infomation.aspx?securityCode=" + self.stockCode)

        if (response.status_code == 200):
           html = response.content         
           bsObj = bs(html,'lxml')
           table = bsObj.find("table",id='MainContent_gvReport')
           rows = table.findAll('tr')

        return rows        
         
#        data= {
#                "SAMLRequest": "PHNhbWwycDpBdXRoblJlcXVlc3QgeG1sbnM6c2FtbDJwPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FN\r\nTDoyLjA6cHJvdG9jb2wiIERlc3RpbmF0aW9uPSJodHRwczovL3N0c2ludC5hYmIuY29tL2FkZnMv\r\nbHMvIiBJRD0iX2Y4ODg4YjBkZmY4NDdlZjY0ZmNhMzczYWJhZGVhN2ZkODVhMzY5YmIiIElzc3Vl\r\nSW5zdGFudD0iMjAxNy0xMS0wNFQwOTo1Nzo0OC40MThaIiBWZXJzaW9uPSIyLjAiPjxzYW1sMjpJ\r\nc3N1ZXIgeG1sbnM6c2FtbDI9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphc3NlcnRpb24i\r\nPnNhbWwuY2lzY29jbG91ZHdlYnNlY3VyaXR5LmNvbTwvc2FtbDI6SXNzdWVyPjxkczpTaWduYXR1\r\ncmUgeG1sbnM6ZHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiPjxkczpTaWdu\r\nZWRJbmZvPjxkczpDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53\r\nMy5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIi8+PGRzOlNpZ25hdHVyZU1ldGhvZCBBbGdvcml0\r\naG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZHNpZy1tb3JlI3JzYS1zaGEyNTYiLz48\r\nZHM6UmVmZXJlbmNlIFVSST0iI19mODg4OGIwZGZmODQ3ZWY2NGZjYTM3M2FiYWRlYTdmZDg1YTM2\r\nOWJiIj48ZHM6VHJhbnNmb3Jtcz48ZHM6VHJhbnNmb3JtIEFsZ29yaXRobT0iaHR0cDovL3d3dy53\r\nMy5vcmcvMjAwMC8wOS94bWxkc2lnI2VudmVsb3BlZC1zaWduYXR1cmUiLz48ZHM6VHJhbnNmb3Jt\r\nIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIi8+PC9k\r\nczpUcmFuc2Zvcm1zPjxkczpEaWdlc3RNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9y\r\nZy8yMDAwLzA5L3htbGRzaWcjc2hhMSIvPjxkczpEaWdlc3RWYWx1ZT5TdFg0a3pCck1oYjFha0Qv\r\naUlyT3pjT05Tbms9PC9kczpEaWdlc3RWYWx1ZT48L2RzOlJlZmVyZW5jZT48L2RzOlNpZ25lZElu\r\nZm8+PGRzOlNpZ25hdHVyZVZhbHVlPkJVMjNvd20wWlA4Ym0wVjhlRVZoUEt0VjhpaHNOYUk5ckoy\r\ndDM2QUlKQ1NXYmpmdlVsQ2dmZnpQUmhKMGxtN0ZFVXVaREM3aG9IZ2t2TEYzMlBZR2hlcWJUMHBU\r\nMVlWd2JSbXUrMk9BVXNWSFpFOGVqZDMvR0xvWjhFdjBwaEd1L0dJMERCK25lNkFteDc0RFE5OVhN\r\nOXk1dDhkb0xXUk42QmNidzNQZm9HMnBsenp0Sms0T2NLM0JJM2ZqUVRqT0FPWXpYSDFOU25CVE1u\r\nR1A1UGdlVWk5Z3gzbktHK1Y5cGNFb1VCYi80N2FiaUZlTUtGMDAxYmZ0MEZkU0RFdnR2U3orQkYy\r\nNW1vemRQWW9meDVHNHM1YVFEN1lWemFqMExKVjVnNVE5dFQ2UEU0VG5WZStJeHFkbkk4ZTNabk5o\r\nSkt6ZDdDTyttQmxtai93QkRtY1AzUT09PC9kczpTaWduYXR1cmVWYWx1ZT48L2RzOlNpZ25hdHVy\r\nZT48L3NhbWwycDpBdXRoblJlcXVlc3Q+\r\n",
#                "RelayState" : "1IQv31P4KIyxBVOQVePR0u63ZwFLNrSy8BjHkHsN--EjI6DVN9zmDdOzMgCoB7ucnriVK5V5pl8iWpW14VwFKY_doghD5UeyB4g6OcDuNv1i1ZAflI0AH2SW-0sbqhhgo4KelJ7jEVjP8fPN0sE-LHfcHUTvLnYa4kimbOlnDMgHyjTROixty_NRPYjz4ZRyNjnQAhc5m5nd2Fb1dygN2N72LpUuHABQW1mHcKW4N7fQI2qJYVHDCsvp9tmFJdoiJHpaTiPYb0gSnnHw1iiAZNjGLY1L0KIDI9mjp3ZVWWX8"
#            }
#        r = requests.post('https://stsint.abb.com/adfs/ls/', data=data)

       
#==============================================================================
#          rows = table.find_all('tr')
#          for tr in rows:
#              cols = tr.find_all('td')
#              if len(cols) == 11:
#                  date, fy,no, fq, rev, pbt, np, eps, div, nta, percent = [c.text for c in cols]
#                  print("##")
# #                 print(fy, fq,rev,pbt,np,eps,div)
#                  print(cols)
#                  #convert fq to datetime object                        
#                  fq_date =  dt.strptime(fq,'%d %b %Y')
#==============================================================================
                 
         

sc = SCRAPPER("CYPARK","8567")
rows = sc.getQuarterResult()