# Athena
Schedule reader and information assistant

I really needed an adult to tell me what to do and when to do it, and since I can't afford a PA & I'm also a grown man so can't rely on my parents & teachers to nag me like when I was six, I decided to create a digital version. Essentially, that bit of most people's brains which spurs them on to do whatever? It doesn't work so great for me; I'm an expert procrastinator, so I'm replicating that functionality in code instead.

I'm working on Linux, so I edited crontab to call the .sh file once a minute. This script then calls all the Python files. I've not yet tried running this under any other OS, so although I'm sure it can be done, I don't know the details of how just yet.

Oh, and the text to speech (TTS) engine I'm using is Google's, so you need to be online. The speech01.sh script isn't mine (I copied it off stackoverflow I think - I'll add credit once I find it again), but I wanted to include it for the sake of completeness.

You're going to need Python installed (I meant to use v3 for this but it turns out I was using v2.7 by mistake - whoops! At least it's backwards compatible XD ), and you'll notice the speech script pushes its output to mplayer, so you'll need that installed as well.

The schedule is just a .csv with 3 columns - 24hr time in the form HH.MM,thing you want to do,alarm(optional)

Alarms are currently as follows:
- alarm01 = full schedule read out, news update, weather forecast, river level monitoring. You'll need to update the various files with your location and preferences.
- alarm02 = news update
- alarm03 = weather forecast
- alarm04 = river level monitoring

Updates to follow, at some point, when I have time:
- trigger an automatic alarm if the river starts to flood
- weight/bmi/sleep/fat% info if I can pull the data from FitBit's API
- allow user control via command line
- ooooohhhhhh so much error checking if a website changes its design
- a more natural interface. voice control would be perfect, though I currently have no idea how to do that
