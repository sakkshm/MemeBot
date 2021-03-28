# MemeBot 🤖
 A Python script that collects memes from Reddit and compiles them into a video. This bot uses an unofficial Reddit API (https://github.com/R3l3ntl3ss/Meme_Api/) and get a random meme from Reddit and use moviepy (https://github.com/Zulko/moviepy) to make the video. Then these videos are automatically uploaded to Youtube. 
 
 # Example
An example of the output is given in the output.mp4 file, and can also be found on Youtube. (https://www.youtube.com/watch?v=K3wpiGGY5og)
This is basically a compilation of memes that the bot scrapes from Reddit and compile into a video.

# Requirements

The modules used in this project are:
- moviepy
- PIL
- requests
- telegram
- Youtube Data API v3

You have to install all these libraries to run this project.

# Running the Script

First, install all the modules and Python 3.7+ in order to run the script, then create two folders by name `processVids` and `processed` in the home directory, then just type
`python process.py`

The script will automatically start running and scrape memes from Reddit then moviepy will curate the video file and you will get the output as `output.mp4` in the home directory.

# Customization
- You can change subreddits by changing the subreddits list in `process.py` , currently the subreddits are: `["memes","dankmemes","cursedcomments","me_irl","HistoryMemes","BlackPeopleTwitter","ihadastroke","technicallythetruth"]`
- Add Your Telegram API key and chat ID to the `notifBot.py` file
- Go to Google Cloud Platform and generate a config.json file for the Youtube Data API v3 and add it to the `src` folder

Feel free to ask questions by raising an issue.

# Contribution
Contributions are most welcome!
