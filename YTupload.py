from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
import glob
import os
import random
import notifBot

# loggin into the channel
channel = Channel()
channel.login("src/client_id.json", "src/credentials.storage")

def upload():
    myfile = "src/vidnum.txt"
    with open(myfile, "r") as f:
        num = int(f.read())

    with open(myfile, "w") as f:
        f.write(str(num)

    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path="final.mp4")

    # setting snippet
    video.set_title("Top memes I found on Reddit #" + str(num + 1))
    video.set_description('''Top memes I found on Reddit #

        Like, Share and Subscribe for daily videos


        Music used in the Video:
        Kevin MacLeod - Fluffing A Duck

        Memes from subreddits:

        r/memes,r/dankmemes,r/me_irl,r/HistoryMemes,r/BlackPeopleTwitter,r/facepalm,r/ihadastroke,r/woosh,r/technicallythetruth

        Disclaimer:
        I do not own any of the images shown in this video and I am not the creator of these memes.
''')

    video.set_tags(["memes", "reddit","reddit memes","reddit compilation","meme compilation","funny","dank memes","funny memes","top memes","top reddit","top"])
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)

    img = []
    for file in glob.glob("processed/*.jpg"):
        img.append(file)

    rand = random.randrange(0,len(img))

    # setting thumbnail
    video.set_thumbnail_path(img[rand])

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.id)
    print(video)

    return [video.id , video , img[rand]]

