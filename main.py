import praw
import dotenv
import os

from dotenv import load_dotenv

load_dotenv()

print(os.getenv("CLIENT_ID"))

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='1guiwevlfo00esyy',
                     user_agent='testscript by /u/fakebot3',
                     username='fakebot3')