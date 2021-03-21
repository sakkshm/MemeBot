from moviepy.editor import ImageSequenceClip,AudioFileClip
import moviepy
from moviepy.audio.fx.audio_loop import audio_loop
from PIL import Image
import glob
import os

def makeVidFromImgSequence(memes,j):
    ids = []
    for i in range(0,len(memes)):
        ids.append("processed\\"+memes[i]["imgID"])

    #Save Video
    clip = ImageSequenceClip(ids, fps=0.2)
    clip.write_videofile("processVids/output"+str(j)+".mp4")

def combineVideos():
    vids = []
    for file in glob.glob("processVids/*.mp4"):
        vids.append(moviepy.editor.VideoFileClip(file))

    final = moviepy.editor.concatenate_videoclips(vids)
    audio = AudioFileClip("src/music.mp3")
    song = audio_loop( audio, duration=final.duration)
    final.audio = song
    final.write_videofile("combined.mp4")

    intro = moviepy.editor.VideoFileClip("src/intro.mp4")
    combined = moviepy.editor.VideoFileClip("combined.mp4")
    last = moviepy.editor.concatenate_videoclips([intro,combined])
    last.write_videofile("final.mp4")
