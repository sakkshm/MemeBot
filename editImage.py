from PIL import Image
import urllib.request

#This Code formats and resizes the image and add a black background to the image

def Reformat_Image(lst):

    for i in range(0,len(lst)):
        image = Image.open(urllib.request.urlopen(lst[i]["url"]))
        image.save("ocrImg/"+lst[i]["imgID"])
        image_size = image.size
        width = image_size[0]
        height = image_size[1]

        if(width != height):
            bigside = width if width > height else height

            #Resize
            background = Image.new('RGBA', (bigside, bigside), (0, 0, 0, 255))
            offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))
            baseheight = 1000
            background.paste(image, offset)
            wpercent = (baseheight/float(background.size[0]))
            hsize = int((float(background.size[1])*float(wpercent)))
            background = background.resize((hsize,baseheight), Image.ANTIALIAS)
            image = background

        else:
            print("Image is not resized due to some error!")


        #Add Black Background
        im1 = Image.open(r'src/background.png')
        im2 = image
        bg_w, bg_h = im1.size
        img_w, img_h = im2.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        back_im = im1.copy()
        back_im.paste(im2 , offset)

        #Save Image 
        imgID = lst[i]["imgID"]
        back_im.save("processed/"+imgID)
        image = Image.open("processed/"+imgID)
        back = back_im.resize((1920,1080))
        back.save("processed/"+imgID)
        print("Image " + imgID + " has been edited and saved!")



