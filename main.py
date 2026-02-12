from functions import *
from API import *
import GUI

#main function
def main():
    #get the most recent session key
    session_key = get_recent_session()
    
    #get the session laps
    laps = get_session_laps(session_key)

    #get all drivers from session
    drivers = get_drivers(laps)

    #iterate through drivers and get their lap times
    for driver in drivers:
        driver_laps = get_driver_laps(laps, driver)
        print(driver_laps)

#only run main function if this file is run directly
if __name__ == "__main__":
    main()