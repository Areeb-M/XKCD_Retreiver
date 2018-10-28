from pygame import *
from pygame.locals import *
from urllib import request
from random import randint
import os

"""
    Check whether folder containing XKCD comics exists

    If it doesn't, create it
"""
if not os.path.exists("C:/xkcd/"):
    os.makedirs("C:/xkcd/")

#get_new_comic()
comic = None #image.load("C:/xkcd/360.png")
init()
screen = display.set_mode((800, 800))
comic_num = 0


def get_new_comic():
    global comic, screen, comic_num

    comic_num = str(randint(1, 1710))
    #comic_num = "360"
    im_lazy = not os.path.exists("C:/xkcd/" + comic_num + ".png")
    if im_lazy:
        request.urlretrieve("http://www.xkcd.com/" + comic_num + "/", "C:/xkcd/page.html")

        stringusedtogetacomicsfilenameanddownloaditinanobscureway = """<div id="comic">
<img src="//"""
        stringusedtogetacomicstitletextinanobscureway = '''{{'''
        data = open("C:/xkcd/page.html").read()
        place = data.find(stringusedtogetacomicsfilenameanddownloaditinanobscureway) + len(stringusedtogetacomicsfilenameanddownloaditinanobscureway)
        url = ""
        while data[place] != '"':
            url += data[place]
            place += 1
        request.urlretrieve("https://" + url, "C:/xkcd/"+str(comic_num)+".png")
        # place = data.find(stringusedtogetacomicstitletextinanobscureway) +
        # len(stringusedtogetacomicstitletextinanobscureway)

        titletext = ""
        place += 1
        while data[place] != '"':
            place += 1
        place += 1
        while data[place] != '"':
            titletext += data[place]
            place += 1
        #titletext = "XKCD uses inconsistent coding :/"
        titletext = titletext.replace("Title text:", "")
        titletext = titletext.replace("title text:", "")
        titletext = titletext.replace("Title Text:", "")
        titletext = titletext.replace("&#39;", "'")
        titletext = titletext.replace("&quot;", '"')

        comic = image.load("C:/xkcd/"+str(comic_num)+".png").convert()
        '''
        if len(titletext) * 10 > comic.get_width() - 40:
            comic = transform.scale(comic, (int(comic.get_width() * (len(titletext) * 10 / comic.get_width())), int(comic.get_height() * (len(titletext) * 10 / comic.get_width()))))
            '''
        screen = display.set_mode((comic.get_width(), comic.get_height()))
        display.set_caption(titletext)
        data = open("C:/xkcd/"+comic_num+".txt", 'w')
        data.write(titletext)
        print(titletext)
    else:
        comic = image.load("C:/xkcd/"+comic_num+".png").convert()
        screen = display.set_mode((comic.get_width(), comic.get_height()))
        try:
            display.set_caption(open("C:/xkcd/"+comic_num+".txt").read())
            print(open("C:/xkcd/"+comic_num+".txt").read())
        except:
            pass
            #os.removedirs("C:/xkcd/"+comic_num+".png")


get_new_comic()
alive = 1
plz_no_scroll = 0
while alive:
    for e in event.get():
        if e.type == QUIT:
            alive = 0
        elif mouse.get_pressed()[0] == 1:
            while True:
                try:
                    plz_no_scroll = 1
                    get_new_comic()
                    break;
                except:
                    pass
        else:
            plz_no_scroll = 0
    screen.blit(comic, (0, 0))
    display.flip()
