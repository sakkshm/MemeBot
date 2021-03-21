# MemeBot 🤖
 A Python script that collects memes from reddit and complie them into a video.This bot uses a unofficial Reddit API (https://github.com/R3l3ntl3ss/Meme_Api/) and get a random meme from Reddit and use moviepy (https://github.com/Zulko/moviepy) to make the video.
 
 # Example
An example of the output is given in the output.mp4 file, and can also be found on Youtube. (https://www.youtube.com/watch?v=K3wpiGGY5og)
This is basically a compilation of memes that the bot scrapes from reddit and compile into a video.

# Requirements

The modules used in this project are:
- moviepy
- PIL
- requests

You have to install all these libraries to run this project.

# Running the Script

First install all the modules and Python 3.7+ in order to run the script, then create two folders by name `processVids` and `processed` in the home directory, then just type
`python process.py`

The script will automatically start running and scrape memes from reddit then moviepy will curate the video file and you will get the output as `output.mp4` in the home directory.

# Customization
- You can change subreddits by changing the subreddits list in `process.py` , currently the subreddits are: `["memes","dankmemes","cursedcomments","me_irl","HistoryMemes","BlackPeopleTwitter","ihadastroke","technicallythetruth"]`
