import requests
import datetime


#define api link as constant global
global OPENF1
OPENF1 = "https://api.openf1.org/v1/"


#get session key of recent session
def get_recent_session():
    #get current time
    current_date = datetime.datetime.now().isoformat()
    parameters = f"?date_end<{current_date}"
    sessions = requests.get(OPENF1 + "sessions" + parameters).json() #get all completed sessions

    #return the most recent session key
    return sessions[-1]["session_key"]


#get all lap times from a session
def get_session_laps(session_key):
    #get all laps from session
    parameters = f"?session_key={session_key}"
    laps = requests.get(OPENF1 + "laps" + parameters).json()

    return laps


#get all driver info from a session
def get_drivers(session_key):
    parameters = f"?session_key={session_key}"
    drivers = requests.get(OPENF1 + "drivers" + parameters).json()

    #if the session returns null values try the previous session
    if drivers[0]["team_colour"] is None:
        parameters = f"?session_key={session_key-1}"
        drivers2 = requests.get(OPENF1 + "drivers" + parameters).json()

        #if this session has valid data return it, otherwise return the original data
        if drivers2[0]["team_colour"] is not None:
            return drivers2

    return drivers