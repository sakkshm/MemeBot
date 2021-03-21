'''
This function just takes response from main script and format the whole response into a list with useful data.
'''

def makeMemeList(response):
    memes = response['memes']
    respList = []

    for i in range(0,len(memes)):
        if memes[i]["nsfw"] == False and memes[i]["url"].split(".")[3]in ["jpg","png"]:

            tempDict = {}
            
            tempDict["url"] = memes[i]["url"] 
            tempDict["sub"] = memes[i]["subreddit"] 
            tempDict["imgID"] = memes[i]["url"].split("/")[3]

            respList.append(tempDict)
        else:
            continue

    return respList




