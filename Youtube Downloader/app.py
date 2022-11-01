import PySimpleGUI as sg
from pytube import YouTube
from pytube import Search
import os
from pathlib import Path
from PIL import Image
import requests




def download_audio(link):
    # download path
    folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads/Youtube Download/Music')
    yt = YouTube(link)
    yt.streams.get_audio_only().download(output_path=folder)

def download_video(link):
    #download path
    path_to_download_folder = str(os.path.join(Path.home(), "Downloads/Youtube Download/Videos"))
    yt = YouTube(link,)
    yt.streams.get_highest_resolution().download(output_path=path_to_download_folder)

def query_search(query):
    s = Search(query)
    print(len(s.results))

    for result in s.results:
        print(f'{result.title} and the url {result.watch_url} and thumbnail path{result.thumbnail_url}')

def create_window():
    sg.theme('GreenTan')
    layout = [
                [sg.Text('Paste the youtube Link below ', key='-TEXT-')],
                #[sg.Button('Search'), sg.Button('Paste Link')],
                [sg.Input(key='-LINK-'), sg.Button('Preview', key='-PREVIEW-')],
                #[sg.Input(key='-QUERY-'), sg.Button('Search', key='-SEARCH-')],
                [sg.Text('', key='-TITLE-')],
                [sg.Image('', key='-THUMBNAIL-', size=(240,240), visible=False)],
                [sg.Button('Download Audio', key='-AUDIO-', visible=False), sg.Button('Download Video', key='-VIDEO-', visible=False),sg.Push(), sg.Button('Close', key='-CLOSE-', visible=False)]
            ]

    return sg.Window('Youtube Video/Audio Downloader', layout, resizable=True, keep_on_top=True, location=(400,20)).Finalize()

window = create_window()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-PREVIEW-':
        if values['-LINK-'] == '':
            sg.Popup("Paste a link. The field can't be empty")
            create_window()
            
        else:
            yt = YouTube(values['-LINK-'])
            print(yt.title)
            window['-TITLE-'].update(yt.title)
            im = Image.open(requests.get(yt.thumbnail_url, stream=True).raw)
            im = im.save('image.png')
            #sg.Image('image.png', size=(300,300))
            window['-THUMBNAIL-'].update(visible=True)
            window['-THUMBNAIL-'].update('image.png')
            window['-AUDIO-'].update(visible=True)
            window['-VIDEO-'].update(visible=True)
            window['-CLOSE-'].update(visible=True)
            
    
    if event == '-SEARCH-':
        if values['-QUERY-'] == '':
            sg.Popup("Enter a search Query, the link can't be empty")
            create_window()
        else:
            query_search(values['-QUERY-'])
        
    
    if event == '-AUDIO-': 
        download_audio(values['-LINK-'])
        sg.Popup("Your Audio has been downloaded.\n Check Downloads\\Youtube Download ")
    window.refresh()

    if event == '-VIDEO-':
        download_video(values['-LINK-'])
        sg.Popup("Your Video has been downloaded.\n Check Downloads\\Youtube Download ")
    window.refresh()

    if event == '-CLOSE-':
        window.close()



window.close()