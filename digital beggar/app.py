import PySimpleGUI as sg
import qrcode

layout = [
    [sg.Text('E-Beg Platform', key='-HEADING-')],
    [sg.Button('Contribute', key='-CONTRIBUTE-'), sg. Button('Offer Job or Other Help', key='-OTHER-')],
    [sg.HSeparator()],
    [sg.Text('Property of DigitaL Beggar. Ts & Cs Apply')]
]
window = sg.Window("Digital Beggar", layout)

while True:
    event, values = window. read()

    if event == '-CONTRIBUTE-':
        qr = qrcode.make("We are working on the payment systems")
        qr.save('PAYMENT.PNG')

    if event == sg.WIN_CLOSED:
        break

window.close()


