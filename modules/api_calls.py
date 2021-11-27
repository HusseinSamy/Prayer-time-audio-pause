from requests import get as get
from global_variables import current_date as current_date
def current_month_prayer_times_api_request():
    response = get("https://api.aladhan.com/v1/calendarByCity?city=Cairo&country=Egypt&method=5&month=" + current_date[4:7] + "&year=" + current_date[7:11]).json()
    return response