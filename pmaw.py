# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:41:06 2021

@author: marco
"""

from pmaw import PushshiftAPI
import pandas as pd
import datetime as dt

api = PushshiftAPI()

# Set scraping parameters
before = int(dt.datetime(2021,9,1,0,0).timestamp()) 
after = int(dt.datetime(2015,1,1,0,0).timestamp())
subreddit = "0xPolygon"
sub_limit = 200000 # number of posts to scrape
com_limit = 100000 # num of comments to scrape

# Scrape submissions and comments
submissions = api.search_submissions(
    subreddit = subreddit, before = before, after = after, mem_safe = True) # no limit needed as before and after used
comments = api.search_comments(
    subreddit = subreddit, before = before, after = after, mem_safe = True) # no limit needed as before and after used

print(f'{len(submissions)} submissions retrieved from Pushshift')
print(f'{len(comments)} comments retrieved from Pushshift')

# Get all responses
sub_list = [sub for sub in submissions]
com_list = [comment for comment in comments]

# Make dataframe for posts and comments
sub_df = pd.DataFrame(sub_list)
com_df = pd.DataFrame(com_list)

# Preview the data. Remember to run in terminal
sub_df.head(5)
com_df.head(5)

# Convert to csv - make sure the file name and destination are correct
sub_df.to_csv(
     r'C:\Users\marco\OneDrive - Imperial College London\Trabajo\Ethereum\WebScraping\0xPolygon_submissions.csv',
     index = None)

com_df.to_csv(
     r'C:\Users\marco\OneDrive - Imperial College London\Trabajo\Ethereum\WebScraping\0xPolygon_comments.csv',
     index = None)