# Twillioke
An incredibly impractical Twillio-Based karaoke service built as a part of a hackathon.
## Inspiration

I didn't really have any inspiration for this project, I just heard that Twilio was able to make phone calls and send SMS messages, and the fully formed idea popped straight into my head.

## What it does
My project allows a user to perform kareoke versions of 3 different songs.
However, there is a twist! 
The songs, instead of being played through your computer's speakers, are played through a phone call made to your number, and the lyrics, instead of showing up on your screen, are delivered through SMS messages!

## Bodge Job

This project was a bit of a messy one and had a couple of bodges and "hacky" parts to it.
Some things include:
- Having to Manually sync lyrics to each song instrumental.
- Having to set my Phone's Ringtone to be a countdown to "standardize" the amount of time it'd take for me to answer (since my code would start counting the offset for the lyrics from when the call was placed, not when the end user picks up).
- Having the GUI Freeze every time call is placed (for some reason, i think ```time.sleep()``` was the issue!)
- Having every lyric start with "Sent from your Twilio trial account - " because the upgrade keys we were given didn't work.
- Having to wait 10 seconds at the start of every phone call to wait through a "This is a trail, please Dial a number to execute your code" message.
- Only being able to call my number as Twilio doesn't allow free accounts to call/message "unauthorized" numbers.

And many more things!

The code itsself is BARELY holding together. but it does work! So I'm counting that as a personal Win


## How I built it
A Whole lot of trial and error.
I used python to interface with Twilio's Call & SMS API to send lyrics in an order that are synced to an instrumental version of a Song.

I selected 3 popular songs with manually-coded word timings due to a lack of online resources for free timestamped lyrics, and seperated their lyrics into "lines" which are sent with the beforementioned timings.

## Challenges I ran into

Halfway through the Hackathon My Twilio account ran out of credit and I had to pause the "backend" of  my project, and instead taught myself how to make a questionable UI in python.
I was eventually able to create a second Twilio account with a second phone number.

This meant that I wasn't able to test my project as much as I would've liked to.

I've never coded in python outside of guided jupyter notebooks, so it was a nice change to use a full IDE to develop an app.

## Accomplishments that I'm proud of

I'm honestly just happy that I was able to bring something I thought of into reality!
This is my first hackathon project and I done it solo, it's been quite fun.

## What we learned

I've learned that Twilio has an incredibly weird API and that TwiML is horrendous to look at and 'code'.
Also, PySimpleGUI is indeed, a simpe GUI library.

Plus, I've also learned that Pycharm is a lot better at autocompleting than google colab.

## What's next for SMS Karaoke

Absolutely nothing, i'm not dealing with the upkeep costs of this, about 4 hours of testing cost me 12 quid!



#Running SMS Karaoke on your own

Don't. 

if you actually want to, you'll have to create a twilio account and put your own auth keys and phone numbers and stuff, it's really not worth it and i'd recommend just looking
up a lyric video on youtube...

