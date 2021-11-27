from  asyncio import run as async_run
import schedule
from os import chdir as chdir
from time import sleep as sleep 
from sys import path as path
path.append('.\modules')
from requests import get, ConnectionError, RequestException
from data_handling import update_data, store_today_prayer_times
from notifications import create_notification
from media_controller import pause_current_session_240_seconds
from global_variables import today_prayer_times as today_prayer_times
from global_variables import current_date as current_date


def run():
    async_run(pause_current_session_240_seconds())


if __name__ == '__main__':
    chdir("[YOUR DIRECTORY HERE]") #eg. "E:\Work\PythonScripts\StopAudioWhenItsPrayerTime"  
    try:
        get("https://api.aladhan.com/v1/calendarByCity?city=Cairo&country=Egypt&method=5&month=" + current_date[4:7] + "&year=" + current_date[7:11]).json()
        update_data()
        create_notification("Prayer Time Application Started!", " ")
    except ConnectionError:
        print("PLEASE CHECK YOUR INTERNET CONNECTION" )
        create_notification("CONNECTION ERROR!", "WE WILL NOT BE ABLE TO UPDATE AZAN TIME, PLEASE REOPEN THE PROGRAM WHEN YOU HAVE INTERNET ACCESS.")
    except RequestException:
        print("UNKNOWN ERROR" )
        create_notification("UNKNOWN ERROR!", "SOMETHING HAPPENED, PLEASE REOPEN THE PROGRAM AFTER A WHILE.")
        
    store_today_prayer_times()
    schedule.every().day.at(today_prayer_times[0]).do(run)
    schedule.every().day.at(today_prayer_times[1]).do(run)
    schedule.every().day.at(today_prayer_times[2]).do(run)
    schedule.every().day.at(today_prayer_times[3]).do(run)
    schedule.every().day.at(today_prayer_times[4]).do(run)

    while 1:
        schedule.run_pending()
        sleep(1)
    


