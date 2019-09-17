import datetime
import pyglet

datetime.datetime.now()

print("bay gio la ( )".format(datetime.datetime.now().strftime("%H:%M")))

alarmclock = input("gio ban muon hen: ")

while True:
    currentTime = datetime.datetime.now().strftime("%H:%M")

    if alarmclock == currentTime:
        print("bao thuc")
        music = pyglet.resource.media('crowd-cheering (4).wav')
        music.play()

        pyglet.app.run()
