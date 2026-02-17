from API import *

#create driver object
class Driver:
    #initialize
    def __init__(self, number, laps, team, color):
        self.number = number
        self.laps = laps
        self.name = team
        self.color = color

#get graph data
def get_graph_data(session_keys):
    #initialize drivers list
    drivers = []

    #iterate through all session keys and combine the graph data for each session
    for session_key in session_keys:
        #get the session laps
        laps = get_session_laps(session_key)
        
        #get info on all drivers
        driver_info = get_drivers(session_key)

        #get all drivers from session
        tempDrivers = get_driver_nums(laps)

        #iterate through drivers and get their lap times
        for driverNum in tempDrivers:
            #check if driver is already stored in drivers list
            if driverNum in [d.number for d in drivers]:
                #find the driver in the list
                driver = next(d for d in drivers if d.number == driverNum)
                driver.laps.extend(get_driver_laps(laps, driverNum)) #add the new lap times to the existing driver

            else: #driver not already in list
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

    return drivers



#get all drivers that set a lap
def get_driver_nums(laps):
    drivers = list({lap["driver_number"] for lap in laps})

    return drivers


#get all lap times for that driver
def get_driver_laps(laps, driver_number):
    #get list of all none null lap times for that driver
    driver_laps = [float(lap["lap_duration"]) for lap in laps if lap["driver_number"] == driver_number and lap["lap_duration"] is not None]

    if len(driver_laps) == 0: return [] #avoid error due to empty list
    #get lowest lap time
    fastest = min(driver_laps)

    #remove outliers
    driver_laps = [lap for lap in driver_laps if lap <= fastest*1.1 and lap < 200]

    return driver_laps


#get color for driver
def get_driver_info(driver_number, driver_info):
    #find selected drivers info
    cur_driver_info = [d for d in driver_info if d["driver_number"] == driver_number][0]

    #return the found team color
    return cur_driver_info["name_acronym"], "#" + cur_driver_info["team_colour"]

