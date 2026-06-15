import pyttsx3
import speech_recognition as sr
import eel
import time
import os
import webbrowser  # Websites ko bina error ke direct browser me kholne ke liye

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)  # Siri jaisi crisp and smart speed
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        eel.DisplayMessage('Listening....')
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source, 10, 6)

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(1)
       
    except Exception:
        return ""
    
    return query.lower().strip()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
        
    if not query:
        return

    try:
        # =============================================================
        # 🚀 SMART PREMIUM APPLICATION & WEBSITE AUTOMATION
        # =============================================================
        if "open" in query or "kholo" in query:
            app_name = query.replace("open", "").replace("kholo", "").strip()
            clean_name = app_name.replace(" ", "")
            
            if not clean_name:
                return

            # Saari mashhoor websites aur apps ki list
            web_services = ["youtube", "google", "whatsapp", "github", "facebook", "instagram", "chatgpt", "linkedin", "gmail", "twitter"]
            
            # Check: Agar bolne me koi website ka naam hai ya direct URL bola hai
            if clean_name in web_services or ".com" in clean_name or ".in" in clean_name:
                speak(f"Sure, opening {app_name}")
                
                # Special bypass for YouTube and Google URLs
                if "youtube" in clean_name:
                    web_url = "https://www.youtube.com"
                elif "google" in clean_name:
                    web_url = "https://www.google.com"
                elif ".com" in clean_name or ".in" in clean_name:
                    web_url = clean_name if "http" in clean_name else f"https://{clean_name}"
                else:
                    web_url = f"https://{clean_name}.com"
                
                # Yeh browser ko force karke naye tab me front par kholega
                webbrowser.open_new_tab(web_url)
                eel.ShowHood()
                return

            # 2. Agar koi internal Windows App hai (Notepad, Calc, mspaint)
            else:
                speak(f"Opening {app_name}")
                # Pehle direct system se open karne ki koshish karenge
                exit_code = os.system(f"start {clean_name}")
                
                # Agar windows me software nahi milta, toh automatic error popup se bachakar browser me search kar dega
                if exit_code != 0:
                    webbrowser.open_new_tab(f"https://{clean_name}.com")
                
                eel.ShowHood()
                return
        # =============================================================

        # 🎵 YOUTUBE MUSIC CONTROLLER
        elif "on youtube" in query or "youtube pe" in query:
            from engine.features import PlayYoutube
            speak("Playing that on YouTube.")
            PlayYoutube(query)
            time.sleep(1.5)
            os.system("start chrome")  # Chrome window ko aage push karne ke liye
            eel.ShowHood()
            return

        # 📞 WHATSAPP / MOBILE CALLS
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("WhatsApp or Mobile Network?")
                preferance = takecommand()

                if "mobile" in preferance or "network" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("What is the message?")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                elif "whatsapp" in preferance:
                    if "send message" in query:
                        speak("What would you like to send?")
                        query = takecommand()
                        whatsApp(contact_no, query, 'message', name)
                    elif "phone call" in query:
                        whatsApp(contact_no, query, 'call', name)
                    else:
                        whatsApp(contact_no, query, 'video call', name)
            return

        # 🧠 CORE AI INTEL (GEMINI)
        else:
            from engine.features import geminai
            geminai(query)
            
    except Exception as e:
        print("Backend Error:", e)
        try:
            from engine.features import geminai
            geminai(query)
        except:
            pass
    
    eel.ShowHood()