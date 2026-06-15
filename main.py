import os
import eel
import subprocess  # device.bat chalane ke liye zaroori hai

from engine.features import *
from engine.command import *
from engine.auth import recoganize

# 1. Eel ko global level par initialize karna zaroori hai
eel.init("www")

# 2. Python functions ko JavaScript ke liye expose karna
@eel.expose
def init():
    # Aapki device batch file ko run karega
    subprocess.call(['device.bat'])
    
    eel.hideLoader()
    speak("Ready for Face Authentication") 
    
    # Face authentication check
    flag = 1
    
    if flag == 1:
        eel.hideFaceAuth()
        speak("Face Authentication Successful")
        eel.hideFaceAuthSuccess()
        speak("Hello, Welcome bhavesh, How can i Help You")
        eel.hideStart()
        
        playAssistantSound()
    else:
        speak("Face Authentication Fail")

# 3. Jarvis start karne ka main function
def start():
    playAssistantSound()
    
    # mode='edge' dene se Eel apne aap Microsoft Edge ko app mode me kholega.
    # Alag se os.system('start msedge.exe...') likhne ki zarurat nahi hai.
    eel.start('index.html', mode='edge', host='localhost', block=True)

# 4. Program ko sahi tarike se execute karne ke liye
if __name__ == '__main__':
    start()