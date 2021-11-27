from api_calls import current_month_prayer_times_api_request as current_month_prayer_times_api_request
from global_variables import current_date as current_date
from global_variables import today_prayer_times as today_prayer_times

def update_data():
    response = current_month_prayer_times_api_request()
    data = []
    for item in response['data']:
        data.append(item['date']['gregorian']['date'])
        data.append(item['timings']['Fajr'][0:6])
        data.append(item['timings']['Dhuhr'][0:6])
        data.append(item['timings']['Asr'][0:6])
        data.append(item['timings']['Maghrib'][0:6])
        data.append(item['timings']['Isha'][0:6])
    f = open (".\Prayer times.txt", "r+")
    f.seek(0)
    f.truncate()
    for element in data:
         f.write(element + '\n')
    f.close()

def store_today_prayer_times():
    global today_prayer_times
    f = open (".\Prayer times.txt", "r")
    lines = f.readlines()
    for idx,line in enumerate(lines):
        if line == current_date+'\n': 
            for x in range(5):
                today_prayer_times.append(lines[idx + x + 1].replace('\n','').replace(' ',''))
    f.close()
