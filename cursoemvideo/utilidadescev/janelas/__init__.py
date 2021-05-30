import PySimpleGUI as sg


def JanelaPython(titulo, msg):
    sg.theme('DarkAmber')   # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [[sg.Text('Quebrando a Maldição', font='Courier 14', text_color='yellow'),
               sg.InputText(msg, font='Courier 12', text_color='blue')], [sg.OK(), sg.Cancel()]]

    # Create the Window
    window = sg.Window(titulo, layout)
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()


def popup(msg):
    sg.popup(msg)
