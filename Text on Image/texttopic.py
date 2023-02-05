from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg


def add_text(im, msg, saveas):
    img = Image.open(im)
    draw =ImageDraw.Draw(img)
    fnt= ImageFont.truetype('arial.ttf', 25)
    draw.text((100,60), msg, font=fnt, fill=(255,255,255))
    save_it = saveas + '.png'
    img.save(save_it)


def clear_input():
    for key in values:
        # window['-IMAGEPATH-'].update('')
        window['-TEXT-'].update('')
        window['-SAVEAS-'].update('')



layout = [
            [sg.Text('Upload Image to Write Over:' )],
            [sg.FilesBrowse(key='-IMAGEPATH-')],
            [sg.Text("Add the Text to write on image:")],
            [sg.Input(key='-TEXT-')],
            [sg.Text("Save New Image as:")],
            [sg.Input(key='-SAVEAS-')],
            [sg.Button("Add Text to Image", key='-ADD-'), sg.Button("Close", key='-EXIT-')]
         ]

window = sg.Window("Image to Text", layout)


while True:
    event, values = window.read()

    if event == (sg.WIN_CLOSED or '-EXIT-'):
        break

    if event == '-ADD-':
        im = values['-IMAGEPATH-']
        msg = values['-TEXT-']
        saveas = values['-SAVEAS-']

        add_text(im, msg, saveas)
        clear_input()

window.close()