# -*- coding: utf-8 -*-

"""
Code to scrape comments and posts from a subreddit. Remember to change
the destination for each new scrape.

Parameters: 

before: date before which data must be scraped
after: date after which data must be scraped
subreddit: name of subreddit to be scraped
sub_limit: number of submissions we want to scrape
com_limit: number of comments we want to scrape
"""

from pmaw import PushshiftAPI
import pandas as pd
import datetime as dt

api = PushshiftAPI()

# Set scraping parameters
before = int(dt.datetime(2022,9,1,0,0).timestamp()) 
after = int(dt.datetime(2000,1,1,0,0).timestamp())
subreddit = "Name of subreddit here (without r/)"
sub_limit = 1234 # number of posts to scrape
com_limit = 1234 # num of comments to scrape

# Submission and comment destinations. Change with each scrape
sub_dest = r'submission destination here'
com_dest = r'comment destination here'

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

# Convert to csv
sub_df.to_csv(sub_dest, index = None)
com_df.to_csv(com_dest, index = None)
