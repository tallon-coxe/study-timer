import PySimpleGUI as sg
import pygame as pg
from pygame import mixer
import sys
import os

# --------------------
# CURRENT BUGS
# FIXED... starting the timer at 0 will crash the app ... FIXED
# FIXED.... you're unable to move the slider even after the timer runs out
# the window doesn't properly close until the timer runs out
# pressing any buttons while the timer is working will accelerate the timer
# cant play lofi after starting the timer; cant do anything after playing lofi
# pause button doesn't work
# --------------------

# Define the window's contents
sg.theme('GreenTan')
val=0
start = False
pg.mixer.init()
#pg.mixer.music.load('burnmarks.wav')

layout = [[sg.Text('How long would you like to study?', size=(34, 1), font=("Helvetica", 20), auto_size_text=True, justification='right')],
          [sg.Text('0:00', size=(30,1), font=("Helvetica", 20), auto_size_text=True, justification='right', key='timer')],
          [sg.Slider(resolution=5, range=(0, 120), border_width=2, default_value=val, size=(20,15), orientation='horizontal', font=('Helvetica', 12), tick_interval=30, enable_events=True, key='Slider')],
          [sg.Button('Start', key='Start', enable_events=True), 
          sg.Button('Reset',key='Reset', enable_events=True),
          sg.Button('pause music', key='Pause')],
          [sg.Image(r'~/Documents/study_timer/study-timer/assets/study.png', tooltip='test')],
        ]


# Create the window

window = sg.Window('lofi study timer', layout)
running = False
time_format = "00:00"

# Display and interact with the Window using an Event Loop
while True:

    # This is the code that reads and updates your window
    event, values = window.read(timeout=1000)
    slider_val = values['Slider']

    # Define the countdown timer components
    if event == "Start":
        minutes = slider_val
        sec = int(minutes * 60)
        minn, secc = divmod(sec, 60)
        time_format = "{:02d}:{:02d}".format(minn, secc)

    if event in (sg.Button, 'Reset'):
        running = False
        sec = int(minutes * 60)
        minn, secc = divmod(sec, 60)
        time_format = "{:02d}:{:02d}".format(minn, secc)
        window["timer"].update(time_format)
        window["Start"].update("Start")
        window["Reset"].update(disabled=True)
        window['Slider'].Update(disabled=False)



    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    
    # ---- Countdown timer ----

    if event in 'Slider':
        print(int(slider_val))
        window.refresh()
        pass


    if time_format == "00:00":
        running = False


    #def reset_button():
     #   window['Slider'].Update(disabled=False) # Reenable the slider after reset has been pressed.
      #  window['Start'].Update(disabled=False) # Reenable the start button.
       ##window.refresh()


    if running is True:
        minutes = int(slider_val)
        minn, secc = divmod(sec, 60)
        time_format = "{:02d}:{:02d}".format(minn, secc)
        window["timer"].update(time_format)
        window["Reset"].update(disabled=False)
        sec -= 1


    if event in (sg.Button, 'Start'):

        minutes = int(slider_val)
        
        if running:             
            running = False
            minutes = int(slider_val)
            window["Start"].update("Start")

        else:
            running = True
            window['Start'].update("Pause") # Change the 'Start' button to say 'Pause'
            window['Slider'].Update(disabled=True) # Disable the slider after start has been pressed.
        
        window.refresh()


window.close()         
