import PySimpleGUI as sg

# Define the window's contents

sg.theme('GreenTan')   # Add a touch of color

layout = [[sg.Text('How long would you like to study?', size=(25, 1), auto_size_text=False, justification='right')],
          [sg.Slider(range=(0, 120), resolution=10, border_width=2, default_value=0, size=(20,15), orientation='horizontal', font=('Helvetica', 12), tick_interval=30, enable_events=True)],
          [sg.Button('Start'), sg.Button('Pause'), sg.Button('Reset')],
          [sg.Image(r'C:\Users\Tallon\PycharmProjects\pythonProject1\study.png', tooltip='test')],


        ]


# Create the window
window = sg.Window('Study Timer', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window


# Finish up by removing from the screen
window.close()                # Part 5 - Close the Window
