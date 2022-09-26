import PySimpleGUI as sg

sg.theme('TanBlue')
sg.set_options(font='Calibri, 16')
button_size = (6,2)
button_size_alt = (4,1)
layout =[
            [sg.Push(), sg.Text("|", key='-SCREEN-', font='Helvetica, 28', pad=(10,15))],
            [sg.Button(1, size=button_size), sg.Button(2, size=button_size), sg.Button(3,size=button_size)],
            [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(6, size=button_size)],
            [sg.Button(7, size=button_size), sg.Button(8, size=button_size), sg.Button(9, size=button_size)],
            [sg.Button('*',size=button_size_alt), sg.Button('+', size=button_size_alt), sg.Button(0, size=button_size_alt), sg.Button('#',size=button_size_alt)],
            [sg.Button('CALL', expand_x=True), sg.Button("CLEAR",  expand_x=True)]
        ]

window = sg.Window("Dail Pad", layout)

phone_digits = []
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','*', '#', '+']:
        phone_digits.append(event)
        phone_number = ''.join(phone_digits)
        window['-SCREEN-'].update(phone_number)
    
    if event in ['CALL']:
        print(event)
        window['CLEAR'].update('REJECT')
    
    if event in ['CLEAR']:
        print(event)


window.close()
