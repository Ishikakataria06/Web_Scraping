#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import requests
from bs4 import BeautifulSoup


# In[2]:


# Function to extract title 
def get_title(soup):
    
    try:
        title = soup.find("span",attrs={'class':'VU-ZEz'}).text.strip()
        
    except AttributeError:
        title = ""
        
    return title
        
# Function to extract price 
def get_price(soup):
    
    try:
        price = soup.find("div",attrs={'class':'Nx9bqj CxhGGd'}).text
    
    except AttributeError:
        price = ""
    
    return price

# Function to extract ratings
def get_rating(soup):
    
    try:
        ratings = soup.find("div",attrs={'class':'XQDdHH'}).text
    
    except AttributeError:
        rating = ""
        
    return ratings


# In[5]:


if __name__=='__main__':
    
    # The webpage url 
    url = 'https://www.flipkart.com/search?q=skincare+products&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_8_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_8_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=skincare+products&requestId=d80f8b65-bec1-48f5-92e4-5860eda99c00&as-backfill=on'
    
    # Header 
    Header = ({'User_Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
           'Accept-Language': 'en-US,en;q=0.5'})
    
    # HTTP request
    webpage = requests.get(url,headers=Header)
    
    # Soup Object containing all data 
    soup = BeautifulSoup(webpage.content,'html.parser')
    
    # Fetch links 
    links = soup.find_all('a',{'class':'wjcEIp'})
    
    # Store links
    links_list = []
    
    # for loop for extracting all the links 
    for link in links:
        links_list.append(link.get('href'))
    
    d = {'Title':[],'Price':[],'Ratings':[]}
    
    # for loop for extracting product details
    for link in links_list:
        new_webpage = requests.get("https://flipkart.com"+link,headers=Header)
        
        new_soup = BeautifulSoup(new_webpage.content,'html.parser')
        # Calling functions to display product details
        d['Title'].append(get_title(new_soup))
        d['Price'].append(get_price(new_soup))
        d['Ratings'].append(get_rating(new_soup))
    
    #Creating DataFrame
    
    flipkart_df = pd.DataFrame(d)
    flipkart_df['Title'].replace("",np.nan,inplace=True)
    flipkart_df = flipkart_df.dropna(subset=['Title'])
    flipkart_df.to_csv("flipkart_data_skin_care.csv",header=True,index=False)


# In[6]:


flipkart_df

