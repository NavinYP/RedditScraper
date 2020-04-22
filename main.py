import praw
import dotenv
import os
from dotenv import load_dotenv
import sys

load_dotenv()

# TempestBot v0.1
# Made by Navin Pemarathne (Storm)
bot_version = "v0.1"

# Getting credentials from the .env file.
# todo:Might have to change this later.
reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))


# print(reddit.user.me())


def intro():
    print(f"""Welcome to TempestBot {bot_version}.\n""")
    user_input = input("Please enter the desired subreddit name: ")
    return user_input


def subreddit_intro():
    print(f"""You are currently in this subreddit:
    {subreddit.display_name}
    {subreddit.title}""")


def get_subreddit():
    user_input = reddit.subreddit(subreddit_name)
    return user_input


def choose_sort():
    print("""Select the sorting method you want:
    1. controversial
    2. gilded
    3. hot
    4. new
    5. rising
    6. top \n""")
    user_input = int(input("Please enter the number of your chosen sorting method: "))
    return user_input


def get_submission_count():
    user_input = int(input("How many submission links do you want?: "))
    return user_input


subreddit_name = intro()
subreddit = get_subreddit()
subreddit_intro()
method_number = choose_sort()
number_of_submissions = get_submission_count()

# print(subreddit_name)

# Sort methods in a dictionary to access by index key.
sort_methods = {1: subreddit.controversial, 2: subreddit.gilded, 3: subreddit.hot, 4: subreddit.new, 5: subreddit.rising
                , 6: subreddit.top}

for submission in sort_methods[method_number](limit=number_of_submissions):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)  # Output: the submission's ID
    print(submission.url)  # Output: the URL the submission points to
