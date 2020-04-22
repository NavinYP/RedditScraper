import praw
import dotenv
import os
import urllib
import datetime
from datetime import datetime
from dotenv import load_dotenv
import sys

load_dotenv()

# TempestBot v0.3
# Made by Navin Pemarathne (Storm)
bot_version = "v0.3"

# Getting credentials from the .env file.
# todo:Might have to change this later.
reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))

current_directory = os.getcwd()

# print(reddit.user.me())


def intro():
    print("""What would you like to do?
    1. Change current subreddit.
    2. Display full submission info.
    3. Download images from subreddit.
    4. Quit""")
    user_input = int(input("\nPlease enter the option number: "))
    return user_input


def get_subreddit_name():
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


def print_submissions_full():
    for submission in sort_methods[method_number](limit=number_of_submissions):
        print(submission.title)  # Output: the submission's title
        print(submission.score)  # Output: the submission's score
        print(submission.id)  # Output: the submission's ID
        print(submission.url)  # Output: the URL the submission points to


def download_images():
    time_now = datetime.now()
    current_timestamp = time_now.strftime(f"%y_%m_%d_%H_%M_%S")
    folder_name = f"{subreddit_name}_{current_timestamp}"
    os.mkdir(f"{current_directory}/downloads/{folder_name}")
    for submission in sort_methods[method_number](limit=number_of_submissions):
        if any(ext in submission.url for ext in image_formats):
            filename = submission.url.split('/')[-1]
            print(filename)
            urllib.request.urlretrieve(submission.url, f"{current_directory}/downloads/{folder_name}/{filename}")
            print("Download complete.\n")

        elif "reddituploads" in submission.url:
            filename = submission.url.split("/")[-1].split("?")[0]
            print(filename)
            urllib.request.urlretrieve(submission.url, f"{current_directory}/downloads/{folder_name}/{filename}.jpg")
            print("Download complete.\n")

image_formats = [".jpeg", ".png", ".jpg", ".gif", "img",]


print(f"""Welcome to TempestBot {bot_version}.\n""")

while True:
    option_number = intro()

    if option_number == 1:
        subreddit_name = get_subreddit_name()
        subreddit = get_subreddit()

        # Sort methods in a dictionary to access by index key.
        sort_methods = {1: subreddit.controversial, 2: subreddit.gilded, 3: subreddit.hot, 4: subreddit.new,
                        5: subreddit.rising
            , 6: subreddit.top}

        subreddit_intro()

    elif option_number == 2:
        method_number = choose_sort()
        number_of_submissions = get_submission_count()
        print_submissions_full()

    elif option_number == 3:
        method_number = choose_sort()
        number_of_submissions = get_submission_count()
        download_images()

    elif option_number == 4:
        print("\nThank you for using TempestBot. Have a good day!")
        break










