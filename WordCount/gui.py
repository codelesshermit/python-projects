import PySimpleGUI as sg
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

def generate_wordcount(text):
    
    x,y = np.ogrid[:300, :300]
    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)

    wc = WordCloud(background_color="White", repeat=True, mask=mask)
    wc.generate(text)

    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()

sg.theme('LightGreen')
layout = [
            [sg.VPush()],
            [sg.Text('Create a WordCount by filling in \nthe form Below')],
            [sg.Input(key='-TEXT-')],
            [sg.Button('Create WordCount', key='-CREATE-')],
            [sg.VPush()]
         ] 

window = sg.Window('WordCount', layout, size=(300, 200))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CREATE-':
        generate_wordcount(values['-TEXT-'])


window.close()