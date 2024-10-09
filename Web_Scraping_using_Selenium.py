#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries 
import time 
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
driver = webdriver.Chrome()     # Start a new Chrome browser instance

# Navigate to the Flipkart website
driver.get("http://www.flipkart.com")
driver.maximize_window()     # Maximize the browser window

# Locate the search input field and search button
input_search = driver.find_element(By.CLASS_NAME,"Pke_EE")     # Adjust class name as necessary
search_buttom = driver.find_element(By.CLASS_NAME,"_2iLD__")   # Adjust class name as necessary

# Input the search term and click the search button
input_search.send_keys("Body and Face skincare ")
search_buttom.click()

# Lists to hold product names, prices, and ratings
Products = []
Prices = []
Ratings = []

# Loop through multiple pages to scrape products
for i in range(20):                 # Adjust the range for the desired number of pages
    print("Scarping Page",i+1)      # Indicate which page is being scraped
    sleep(1)                        # Wait for the page to load

    
     # Find all product, price, and rating elements on the current page
    product_element = driver.find_elements(By.CLASS_NAME,"wjcEIp")    # Adjust class name as necessary
    price_element = driver.find_elements(By.CLASS_NAME,"Nx9bqj")      # Adjust class name as necessary
    rating_element = driver.find_elements(By.CLASS_NAME,"XQDdHH")     # Adjust class name as necessary
    
    try:
        current_page_count = 0      # Counter for products on the current page

        # Iterate through products, prices, and ratings simultaneously
        for product,price,rating in zip(product_element,price_element,rating_element):
            # Check for duplicates before adding to the lists
            if product.text not in Products:
                Products.append(product.text)      # Add product name
                Prices.append(price.text)          # Add product price
                Ratings.append(rating.text)        # Add product rating
            current_page_count += 1                # Increment the page counter

        # Get the total number of unique products scraped
        total_count = len(Products)
        print(f"Products scraped from Page {i + 1}: {current_page_count}")       # Show count for the current page
        print(f"Total length of products: {total_count}")                        # Show cumulative count of products
        
    except:                              # Catch any exceptions during the scraping process
        print(f"Error occurred: {e}")    # Print the error message
        Products.append("N/A")           # Add "N/A" for missing data
        Prices.append("N/A")

    # Find and click the "Next" button to go to the next page
    next_button = driver.find_element(By.XPATH,"//span[text()='Next']")        # Adjust XPath as necessary
    next_button.click()                                                        # Click the "Next" button
    sleep(5)                                                                   # Wait for the next page to load
    
# Quit the browser after scraping the data 
driver.quit()


# In[2]:


# Converting the List to Dictionary 
data = {"Product_Title":Products,
       "Price": Prices,
       "Ratings":Ratings}


# In[3]:


# Create a DataFrame using Dictionary 
df = pd.DataFrame(data)
df


# In[4]:


# Check if the data has any duplicated value
df.duplicated().sum()


# In[5]:


# Check for the null values
df.isnull().sum()

