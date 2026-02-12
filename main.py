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
    tempDrivers = get_drivers(laps)
    driver_laps = []
    drivers = []

    #iterate through drivers and get their lap times
    for driver in tempDrivers:
        #get laps of that driver
        temp = get_driver_laps(laps, driver)

        #only add driver if they have laps
        if len(temp) > 0:
            driver_laps.append(temp)
            drivers.append(driver)

    graph = GUI.create_graph(drivers, driver_laps)


#only run main function if this file is run directly
if __name__ == "__main__":
    main()