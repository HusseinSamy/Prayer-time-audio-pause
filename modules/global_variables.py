from datetime import datetime as datetime

now = datetime.now()
today_prayer_times = []
current_date = now.strftime("%d-") + now.strftime("%m") +  now.strftime("-%Y")
session_title = "Prayer Time!"
session_message= "We have paused your current audio, it will be played back after the Azan."

