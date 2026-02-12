import requests
import datetime


#define api link as constant global
global OPENF1
OPENF1 = "https://api.openf1.org/v1/"


def get_recent_session():
    #get current time
    current_date = datetime.datetime.now().isoformat()
    parameters = f"?date_end<{current_date}"
    sessions = requests.get(OPENF1 + "sessions" + parameters).json() #get all completed sessions

    #return the most recent session key
    return sessions[-1]["session_key"]


def get_session_laps(session_key):
    #get all laps from session
    parameters = f"?session_key={session_key}"
    laps = requests.get(OPENF1 + "laps" + parameters).json()

    return laps