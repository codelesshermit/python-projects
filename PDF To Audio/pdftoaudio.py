import PySimpleGUI as sg
import pyttsx3
import PyPDF2


def listen(pdf_to_convert):

    pdfReader = PyPDF2.PdfFileReader(pdf_to_convert)
    sg.Popup('Reading PDF out Loud')
    

    speak = pyttsx3.init()

    for pages in range(pdfReader.numPages):
        text = pdfReader.getPage(pages).extractText()
        speak.say(text)
        speak.runAndWait()
    speak.stop()

def generate_audio(pdf_to_convert, filename):
     pdfReader = PyPDF2.PdfFileReader(pdf_to_convert)
     save_as = filename + '.mp3'
     all_text = ''
     
     engine = pyttsx3.init()

     for pages in range(pdfReader.numPages):
        text = pdfReader.getPage(pages).extractText()

        all_text += text

        engine.save_to_file(all_text, save_as)
        engine.runAndWait()
        
     engine.stop()


sg.theme('Dark')
layout = [
            [sg.Text('PDF to Audio Convertor')],
            [sg.Text('PDF File', size=(10,1)), sg.Input(key='-PDF-'), sg.FileBrowse()],
            [sg.Text('Save Audio as', size=(10,1)), sg.Input( key='-FILENAME-')],
            [sg.Text("",key='-ACTION-')],
            [sg.Push(), sg.Button('Listen To PDF', key='-LISTEN-'), sg.Button('Generate Audio File', key='-GENERATEAUDIO-'), sg.Button('Close', key='-EXIT-')]

         ]

window = sg.Window('PDF to Audio Convertor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-LISTEN-':
        
        listen(values['-PDF-'])

    
    if event == '-GENERATEAUDIO-':
        generate_audio(values['-PDF-'], values['-FILENAME-'])


    if event == '-EXIT-':
        window.close()

window.close()



