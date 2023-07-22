import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re
import os
# from nsetools import Nse

# nse = Nse()

# q = nse.get_quote('INFY')

def fetch_stock_price(stock_code):
    
    stock_url  = 'https://www.nseindia.com/get-quotes/equity?symbol='+str(stock_code)
    #print(stock_url)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    span_element = soup.find('span', id='quoteLtp')
    content = span_element.text
    print("Content:", content)

nifty50_url = 'https://archives.nseindia.com/content/indices/ind_nifty50list.csv'
fetch_NSE_stock_price('INFY')
    
 