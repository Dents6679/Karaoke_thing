from twilio.rest import Client

from twilio.twiml.voice_response import Gather, VoiceResponse, Say, Play, Dial
import time
import PySimpleGUI as sg
import re

"""RickRoll Stuff"""
rickroll_link = "https://dl.sndup.net/n7y6/RickRoll%20Inst.mp3"
rickroll_lyrics = """We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy to say it 
Inside, we both know what's been going on 
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
[break it down, babe]
We've known each other for so long
Your heart's been aching, but you're too shy to say it 
Inside, we both know what's been going on 
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""
rickroll_lines = rickroll_lyrics.split("\n")  # splits lyrics into individual lines

rickroll_timings = [43.5, 3.98, 4.23, 4.22, 3.99, 5.31, 2.63, 2.11, 2.09, 4.33, 1.99, 2.16, 5.11, 4.18, 4.15, 4.28,
                    4.06, 5.22, 2.67, 2.15, 2.10, 4.28, 2.13, 1.97, 4.35, 2.07, 2.11, 4.23, 2.16, 2.11, 4.76, 17.19,
                    4.24, 4.23, 4.23, 4, 5.3, 2.65, 2.1, 2.19, 4.24, 2.09, 2.07, 4.29, 2.05, 2.13, 4.31, 2.01, 2.19,
                    4.24, 2.13, 2.09, 4.24, 2.01, 2.17]

"""Tequila Stuff"""
tequila_link = "https://dl.sndup.net/nt4q/tequila.mp3"
tequila_lines = ["Tequila!", "Tequila!", "Tequila!"]

tequila_timings = [22 + 52, 43, 32]

"""All Star Stuff"""
allstar_link = "https://dl.sndup.net/c3rt/AllStar_inst.mp3"
allstar_lyrics = """Somebody once told me
The world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb
With her finger and her thumb
In the shape of an L on her forehead
Well the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars, break the mold
It's a cool place and they say it gets colder
You're bundled up now, wait till you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture
The ice we skate is getting pretty thin
The water's getting warm so you might as well swim
My world's on fire, how about yours?
That's the way I like it and I never get bored
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
All that glitters is gold
Only shooting stars break the mold
[Break it down, darling]
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars
Somebody once asked could I spare some change for gas?
I need to get myself away from this place
I said yep what a concept
I could use a little fuel myself
And we could all use a little change
Well, the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
And all that glitters is gold
Only shooting stars break the mold



"""
allstar_lines = allstar_lyrics.split("\n")

allstar_timings = [27, 2.53, 2.44, 4.43, 2.03, 2.26, 5.01, 2.89, 2.29, 2.31, 2.3, 1.75, 2.68, 2.23, 2.54, 2.46, 4.41,
                   3.74, 5.46, 2.45, 2.12, 1.93, 2.24, 2.35, 2.26, 2.28, 3.06, 4.63,
                   4.39, 3.73, 5.17, 19.07, 5.47, 4.55, 3.53, 2.92, 4.29, 4.90, 2.38, 1.97, 4.9, 2.86, 2.31, 2.25, 2.4,
                   1.71, 2.73, 2.17, 2.61, 4.61, 4.33, 3.73, 5.51, 3.74]

"""Auth Token Stuff"""

account_sid = 'AC2fab780b5a0545eb3fb74fbe4efecd40'
auth_token = '[REDACTED]'
client = Client(account_sid, auth_token)


target_number = "[REDACTED]"
from_number = "+442033227901"

"""Call Stuff"""


def play_rickroll():
    response = VoiceResponse()
    response.say("I'll never give you up")
    response.play(rickroll_link)

    call = client.calls.create(
        twiml=str(response),
        to=target_number,
        from_=from_number
    )


def play_tequila():
    response = VoiceResponse()
    response.play(tequila_link)

    call = client.calls.create(
        twiml=str(response),
        to=target_number,
        from_=from_number
    )


def play_allstar():
    response = VoiceResponse()
    response.say("Ogres are like onions, they've got layers.")
    response.play(allstar_link)

    call = client.calls.create(
        twiml=str(response),
        to=target_number,
        from_=from_number
    )


"""Message Stuff"""


def send_message(input_str):
    client.messages.create(
        messaging_service_sid='MG528ea37a00d6b206d0bde77f6fb19120',
        body=input_str,
        to=target_number
    )


def send_tequila_lyrics():
    for i in range(3):
        time.sleep(tequila_timings[i])
        window.refresh()
        send_message(tequila_lines[i])



def send_rickroll_lyrics():
    for i in range(55):
        time.sleep(rickroll_timings[i])
        window.refresh()
        send_message(rickroll_lines[i])



def send_allstar_lyrics():
    for i in range(len(allstar_timings)):
        window.refresh()
        time.sleep(allstar_timings[i])
        send_message(allstar_lines[i])



""" UI STUFF """

number_checker_re = re.compile(r'(\+447)\d{9}$')

otherlayout = [[sg.Button("OK")]]

layout = [
    [sg.Text("Welcome to Tom's shitty karaoke!")],
    [sg.Text("Mobile Number:"), sg.Input(key="-IN-")],
    [sg.Button("Submit & Send test message", key="submit_button")],
    [sg.Button("Never Gonna Give You Up", key="rickroll_button"),
     sg.Button("All Star", key="all_star_button"),
     sg.Button("Tequila", key="tequila_button")],
    [sg.Text("", size=(1, 2))],
    [sg.Button("Exit")]

]

window = sg.Window("Test Window", layout)

while True:
    window.refresh()
    event, values = window.read()

    if event == "submit_button":
        number_input = values.get("-IN-")
        # check number validity
        if not number_checker_re.match(number_input):
            print("This number is invalid!")
            continue
        target_number = number_input

        send_message("Ready to go, Please select a song!")

    if event == "all_star_button":
        play_allstar()
        send_allstar_lyrics()
        continue
    if event == "tequila_button":
        play_tequila()
        # send_tequila_lyrics()
        continue
    if event == "rickroll_button":
        play_rickroll()
        send_rickroll_lyrics()
        continue

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()
