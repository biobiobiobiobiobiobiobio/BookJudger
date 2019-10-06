# import the library
from appJar import gui
import glob

def get(btn):
    print(app.getOptionBox("Images"))

app=gui()
app.setFont(20)
app.addLabelOptionBox("Images", [''] + glob.glob('./*.png') + glob.glob('./*.jpg'))
app.addButton("GET", get)
app.go()