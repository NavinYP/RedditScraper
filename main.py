#TempestBot v0.1
#Made by Navin Pemarathne (Storm)
bot_version = "v0.1"

#Importing libraries.
import praw
import dotenv
import os

from dotenv import load_dotenv

load_dotenv()

#Getting credentials from the .env file.
#todo:Might have to change this later.
reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))

# print(reddit.user.me())


def intro():
    print(f"""Welcome to TempestBot {bot_version}.\n\n""")
    user_input = input("Please enter the desired subreddit name: ")
    return user_input


def subreddit_intro():
    print(f"""You are currently in this subreddit:
    {subreddit.display_name}
    {subreddit.title}""")


def get_subreddit():
    user_input = reddit.subreddit(subreddit_name)
    return user_input


subreddit_name = intro()
subreddit = get_subreddit()
subreddit_intro()

# print(subreddit_name)


