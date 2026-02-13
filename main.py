from functions import *
from API import *
import GUI

#main function
def main():
    #get the most recent session key
    session_key = get_recent_session()
    
    #get the session laps
    laps = get_session_laps(session_key)
    
    #get info on all drivers
    driver_info = get_drivers(session_key)

    #get all drivers from session
    tempDrivers = get_driver_nums(laps)

    #initialize drivers list
    drivers = []

    #iterate through drivers and get their lap times
    for driverNum in tempDrivers:
        #get laps of that driver
        temp = get_driver_laps(laps, driverNum)

        #only add driver if they have laps
        if len(temp) > 0:
            #get driver info
            name, color = get_driver_info(driverNum, driver_info)

            #add driver to driver list
            drivers.append(Driver(driverNum, temp, name, color))

    #sort drivers list by fastest lap time
    drivers.sort(key=lambda d: min(d.laps))

    #create graph
    graph = GUI.create_graph(drivers)


#only run main function if this file is run directly
if __name__ == "__main__":
    main()