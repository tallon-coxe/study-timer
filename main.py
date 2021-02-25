import PySimpleGUI as sg
import pygame as pg
from pygame import mixer

# --------------------
# CURRENT BUGS
#
# FIXED... starting the timer at 0 will crash the app ... FIXED
# FIXED.... you're unable to move the slider even after the timer runs out
# cant play lofi music after timer has started
# the window doesn't properly close until the timer runs out
# pressing any buttons while the timer is working will accelerate the timer
# cant play lofi after starting the timer; cant do anything after playing lofi
# --------------------

# Define the window's contents

sg.theme('GreenTan')   # Add a touch of color

val=0
start = False
pg.mixer.init()
pg.mixer.music.load('burnmarks.wav')

global layout

layout = [[sg.Text('How long would you like to study?', size=(34, 1), font=("Helvetica", 20), auto_size_text=True, justification='right')],
          [sg.Text('0:00', size=(30,1), font=("Helvetica", 20), auto_size_text=True, justification='right', key='timer')],
          [sg.Slider(resolution=5, range=(0, 120), border_width=2, default_value=val, size=(20,15), orientation='horizontal', font=('Helvetica', 12), tick_interval=30, enable_events=True, key='Slider')],
          [sg.Button('Start', key='Start', enable_events=True), 
          sg.Button('Reset',key='Reset'),
          sg.Button('pause music', key='pause')],
          [sg.Image(r'/Users/talloncoxe/.spyder-py3/studytimer/study.png', tooltip='test')],

        ]


# Create the window

global window
window = sg.Window('lofi study timer', layout)

slider = window['Slider']


# Display and interact with the Window using an Event Loop
while True:
    # This is the code that reads and updates your window
    event, values = window.read()
    slider_val = values['Slider']
    
    
    # ---- Countdown timer ----
    def countdown(p,q):
        i=p
        j=q
        k=0
        while True:
            if(j==-1):
                j=59
                i -=1
            if(j > 9):  
                window['timer'].update(str(i)+":"+str(j))
            else:
                window['timer'].update(str(i)+":"+str(k)+str(j))
            window.read(timeout=1000)
            window.refresh()
            #time.sleep(1) <--- using time.sleep is bad, using timeout(milliseconds) instead
            j -= 1
            if(i==0 and j==-1):
                break
        if(i==0 and j==-1):
            window['timer'].update("Goodbye!")
            window['Slider'].Update(disabled=False)
            window.read(timeout=1000)
            window.refresh()
            pass
    
    
    if event == "Slider":
        slider_val = values['Slider']
        #resolution = window['Slider']
        print(int(slider_val))
        window.refresh()
        #if int(slider_val) > 30:
         #   window['Slider'].Update(sg.Slider(resolution + 5))       
        pass
        #elif 30 <= int(slider_val) <=120:
         #   window['Slider'].Update(slider_val - 10)
        
    #if slider_val >= int(30):
       # window['Slider'].Update(resolution)
            
    if event in (sg.Button, 'Start'):
        if pg.mixer.music.get_busy() == False:
            pg.mixer.music.play()
            pass
        elif pg.mixer.music.get_busy() == True:
            if event in (sg.Button, 'pause'):
                pg.mixer.pause
                window.refresh()
        pass
        if countdown == int(0):
            window['Start'].Update(disabled=True)
        else:
            window['Slider'].Update(disabled=True)
            window['timer'].update(countdown)
            countdown(int(slider_val), 0)
            window.refresh()
            pass


    if event == sg.WIN_CLOSED or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()   # Close the Window

# this is not an exit
