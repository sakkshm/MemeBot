import requests
import random
import formatResponse
import editImage
import videoMaker
import os
import glob


# Getting memes from API and formatting it into a list

url = "https://meme-api.herokuapp.com/gimme/"

count = 10
subreddits = ["memes","dankmemes","cursedcomments","me_irl","HistoryMemes","BlackPeopleTwitter","ihadastroke","technicallythetruth"]

def make(j):
  try:
      # Getting response from API
    memeList = []
    rand = random.randrange(0,len(subreddits))
    resp = requests.get(url+subreddits[rand]+"/"+str(count)).json()
    memeList = formatResponse.makeMemeList(resp)
  except:
    resp.status_code == 200
  finally:
    # Calling formatResponse 
    print("Raw Data:\n")
    print(memeList)
    print("\n")


    #Clearing all the old photos in the process folder

  files = glob.glob('processed/*')
  for f in files:
      os.remove(f)


    #Reformat Image using editImage

  try:
    editImage.Reformat_Image(memeList)
  finally:
    print("Done!")

    #Making a video out of the Images
  try:
    videoMaker.makeVidFromImgSequence(memeList,j)
  finally:
    print("Video is done!")


for j in range(0,12):
  print("\n Video #",j)
  make(j)


#Export Video
print("Combining all the clips")
videoMaker.combineVideos()
print("Video Completed!")