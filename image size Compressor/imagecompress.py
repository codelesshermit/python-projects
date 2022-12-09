import PySimpleGUI as sg
from PIL import Image
import os
from pathlib import Path


def Compress(imagetocompress, filename):
    path_to_download_folder = str(os.path.join(Path.home(), "Pictures/"))
    img = Image.open(imagetocompress)
    save_as = path_to_download_folder + filename + '.jpg'
    img.save(save_as, "JPEG", optimize = True, quality = 10)
    sg.PopupAutoClose('Photo in your Pictures Folder')

def clear_input():
    for key in values:
        window['-IMAGE-'].update('')
        window['-FILENAME-'].update('')

layout = [
            [sg.Text('Image Compressor')],
            [sg.Text('Image to Upload', size=(14,1)), sg.Input(key='-IMAGE-'), sg.FilesBrowse()],
            [sg.Text('New Image Name:', size=(14,1)), sg.Input(key='-FILENAME-')],
            [sg.Button('Compress', key='-COMPRESS-'), sg.Button('Close', key='-EXIT-')],
         ]

window = sg.Window('Image Compressor', layout)


while True:
    event, values = window.read()

    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break

    if event == '-COMPRESS-':
        Compress(values['-IMAGE-'], values['-FILENAME-'])
        clear_input()

window.close()

