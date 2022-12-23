import pyttsx3
import speech_recognition as sr
import webbrowser as web
import pyjokes
import os


def sp_to_text():
    recognize = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listing.....")
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)
        try:
            print("Recognizing....")
            data = recognize.recognize_google(audio)
            # text_to_sp(data)
            return data
        except:
            print('Try Again')


def text_to_sp(dt):
    ptt = pyttsx3.init()
    voices = ptt.getProperty('voices')
    ptt.setProperty('voice', voices[1].id)
    rate = ptt.getProperty('rate')
    ptt.setProperty('rate', 150)
    ptt.say(dt)
    ptt.runAndWait()


if __name__ == '__main__':

    data1 = sp_to_text().lower()
    print(data1)
    if "open youtube" in data1:
        text_to_sp(data1)
        web.open('www.youtube.com')
    elif "joke" in data1:
        text_to_sp(data1)
        jk = pyjokes.get_joke(language='en', category='all')
        text_to_sp(jk)
        print(jk)
    # elif "music" in data1:
    #     text_to_sp(data1)
    #     add = "D:\SONG"
    #     listsong = os.listdir(add)
    #     os.startfile(os.path.join(add, listsong[180]))
