import PySimpleGUI as sg
from fpdf import FPDF
import os


def convert_to_pdf(images, pdf_title):
    folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/')

    fpdf = FPDF()

    imagelist = [ ]
    imagelist.extend(images)

    save_as = folder + pdf_title + '.pdf'

    for img in imagelist:
        fpdf.add_page()
        fpdf.image(img, x=10,y=10,w=192, h=267)

    fpdf.output(save_as, 'F')
    sg.popup('PDF Generated ' + save_as + '\n You can Pick new Images and create another PDF')


layout = [
            [sg.Text('Image to PDF Convertor')],
            [sg.Text('Select Image(s)', size=(12,1)), sg.Input(key='-IMAGES-'), sg.FilesBrowse()],
            [sg.Text('Save PDF as:', size=(12,1)), sg.Input(key='-PDFTITLE-')],
            [sg.Button('Convert', key='-CONVERT-'), sg.Button('Close', key='-CLOSE-')],
         ]

window = sg.Window('Image To PDF', layout)

def clear_input():
    for key in values:
        window['-IMAGES-'].update('')
        window['-PDFTITLE-'].update('')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        selected_images = values['-IMAGES-'].split(';')
        convert_to_pdf(selected_images, values['-PDFTITLE-'])
        clear_input()
        

    if event == '-CLOSE-':
        window.close()

window.close()
