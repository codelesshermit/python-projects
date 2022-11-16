import PySimpleGUI as sg
from pytube import YouTube
from pytube import Search
import os
from pathlib import Path
from PIL import Image
import requests
import webbrowser




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


    
main_menu = [
                ['Paste Link',['Paste Link', 'Exit']],
                ['Search Youtube', ['Search Youtube']],
            ]


def create_window():
    sg.theme('GreenTan')
    layout = [
               [sg.Menu(main_menu)],
               [sg.Image('icon.png', size=(None, None))],
               [sg.Text('Enter Search Query Below\n(T functionality is under development and only returns search results for now)', key='-STEXT-', visible=False)],
               [sg.Input(key='-QUERY-', visible=False), sg.Button('Search', key='-SEARCH-', visible=False)],
               [sg.Column([[]], key='-RESULTS-', visible=False)],
               [sg.Text('Paste your Link below', key='-PLTEXT-')],
               [sg.Input(key='-LINK-'), sg.Button('Preview', key='-PREVIEW-')],
               [sg.Text(key='-TITLE-')],
               [sg.Image(key='-THUMBNAIL-', size=(240,240), visible=False)],
               [sg.Button('Download Audio', key='-AUDIO-', visible=False), sg.Button('Download Video', key='-VIDEO-', visible=False), sg.Push(), sg.Button('Close', key='-CLOSE-', visible=False)],
               [sg.Text('YouTubedownloader (YtDwn)', pad=(10,10), justification='center')],
             ]

    return sg.Window('Youtube Video/Audio Downloader', layout, resizable=True, icon='icon.png', location=(400,20)).Finalize()

window = create_window()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    #paste link functionality--------------------------------------------------
    if event == 'Paste Link':
        create_window() 
    
    if event == 'Exit':
        window.close()

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
                 
    if event == '-AUDIO-': 
        download_audio(values['-LINK-'])
        sg.Popup("Your Audio has been downloaded.\n Check Downloads\\Youtube Download ")
        webbrowser.open('codelesshermit.github.io')
        window.Refresh()

    if event == '-VIDEO-':
        download_video(values['-LINK-'])
        sg.Popup("Your Video has been downloaded.\n Check Downloads\\Youtube Download ")
        webbrowser.open('codelesshermit.github.io')
        window.Refresh()

    if event == '-CLOSE-':
        window.close()

    #search functionality
    if event == 'Search Youtube':
        window['-QUERY-'].update(visible=True)
        window['-STEXT-'].update(visible=True)
        window['-SEARCH-'].update(visible=True)
        window['-RESULTS-'].update(visible=True)
        window['-PLTEXT-'].update(visible=False)
        window['-LINK-'].update(visible=False)
        window['-PREVIEW-'].update(visible=False)

    def query_search(query):
        s = Search(query)
        #print(len(s.results))
       

        for index, result in enumerate(s.results):
            top_searches = 10
            if index < top_searches:
                #Sprint(index, result)
                img = Image.open(requests.get(result.thumbnail_url, stream=True).raw)
                img = img.save('result_image.png')
                window.extend_layout(window['-RESULTS-'], [[sg.Text(result.title, key="-RESULTTEXT-", enable_events=True)]])
                #sg.Image('result_image.png', size=(50,50))
                #print(f'{result.title} and the url {result.watch_url} and thumbnail path{result.thumbnail_url}')
    
    if event == '-RESULTTEXT-':
        sg.Popup('Adding Download Capabilities soon')
                


    if event == '-SEARCH-':
        if values['-QUERY-'] == '':
            sg.Popup("Enter a search Query, the link can't be empty")
            create_window()
        else:
            query_search(values['-QUERY-'])



window.close()