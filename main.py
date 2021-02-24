import PySimpleGUI as sg

# Define the window's contents

sg.theme('GreenTan')   # Add a touch of color

val=0
start = False

layout = [[sg.Text('How long would you like to study?', size=(34, 1), font=("Helvetica", 20), auto_size_text=True, justification='right')],
          [sg.Text('0:00', size=(30,1), font=("Helvetica", 20), auto_size_text=True, justification='right', key='timer')],
          [sg.Slider(range=(0, 120), resolution=5, border_width=2, default_value=val, size=(20,15), orientation='horizontal', font=('Helvetica', 12), tick_interval=30, enable_events=True, key='Slider')],
          [sg.Button('Start', key='Start', enable_events=True)], 
          [sg.Button('Pause', key='Pause')],
          [sg.Button('Reset',key='Reset')],
          [sg.Image(r'/Users/talloncoxe/.spyder-py3/studytimer/study.png', tooltip='test')],

        ]

# Create the window
window = sg.Window('Study Timer 0.5', layout)

slider = window['Slider']


# Display and interact with the Window using an Event Loop
while True:
    # This is the code that reads and updates your window
    event, values = window.read(timeout=10)
    
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
            window.read(timeout=1000)
            window.refresh()

    
    #print(event)
    if event in (sg.Button, 'Pause'):
        window['Pause'].update('lol this doesnt work yet') # reference key value from 'time goes here' sg.Text line
        pass
    
    if event == "Slider":
        slider_val = values['Slider']
        print(int(slider_val))
        pass


    if event in (sg.Button, 'Start'):
        window['Slider'].Update(disabled=True)
        window['timer'].update(countdown)
        countdown(int(slider_val), 0)
        window.refresh()
        pass

        
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break  

# Finish up by removing from the screen
window.close()   #- Close the Window

# this is not an exit
