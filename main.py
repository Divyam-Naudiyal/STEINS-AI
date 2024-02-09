import os
import openai
import speech_recognition as sr
import pyttsx3                 #for text to speech conversion
from pyttsx3 import init          #for text to speech conversion
import webbrowser
#import openaitest            #for interacting with gbt models and services
import datetime              #for real time date and time
import time
import pyautogui
import webbrowser
import subprocess
import random


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def chat(query):
    from configtest import apikey

    openai.api_key = apikey

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response and response['choices']:

        if 'text' in response['choices'][0]:
            print(response['choices'][0]['text'])
            text += response['choices'][0]['text']
        else:
            print("Response does not contain 'text' key in choices.")
    else:
        print("Response does not contain 'choices' key.")

    text += response["choices"][0]["message"]["content"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt-{random.randint(1,23456789)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)

def ai(prompt):
    from configtest import apikey

    openai.api_key = apikey

    messages = [
        {"role": "user", "content": prompt}
    ]
    text = f"Open AI response for prompt{prompt} \n *************************************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response and response['choices']:

        if 'text' in response['choices'][0]:
            print(response['choices'][0]['text'])
            text += response['choices'][0]['text']
        else:
            print("Response does not contain 'text' key in choices.")
    else:
        print("Response does not contain 'choices' key.")

    text +=response["choices"][0]["message"]["content"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #with open(f"Openai/prompt-{random.randint(1,23456789)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing.......")
            query = r.recognize_google(audio , language="en-in" )
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "sorry some error occured from Steins AI side "

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Steins  AI")
    while True:

        print("listening")
        query = takeCommand()
        # todo: Add more sites
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"],["twitch","https://twitch.com"],["chatgbt","https://chatgbt.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir....")
                webbrowser.open(site[1])

        #todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "C:\\Users\\lenovo\\Downloads\\Baby You - Yuka ! Japanese Song.mp3"
            os.startfile(musicPath)
        try:
            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir, the time is {strfTime}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        else:
            chat(query)




