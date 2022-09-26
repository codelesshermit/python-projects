import PySimpleGUI as sg

layout = [
    [sg.Text("Request For Blood Donation")],
    [sg.Text("Patient Name", key='-PATIENTNAME-'), sg.Input(key='-NAMEINPUT-')],
    [sg.Text("Blood Type"), sg.Spin(['A+', 'A-', 'B+', 'B-', 'O+','O-','AB+', 'AB-'], key='-BLOODTYPE-')],
    [sg.Text("Pints Required"), sg.Input(key='-PINTS-')],
    [sg.Text("Hospital/Location"), sg.Input(key='-LOCATION-')],
    [sg.Text("Contact Person"), sg.Input(key='-CONTACTPERSON-')],
    [sg.Text("Contact Phonenumber"), sg.Input(key='-PHONENUMBER-')],
    [sg.Button("Submit", key='-SUBMIT-')]
]
window = sg.Window("Pint4Life", layout)

while True:
    event, values = window.read()

    if event == '-SUBMIT-':
        print("Good Start, Project Under construction")

    if event == sg.WIN_CLOSED:
        break


window.close()