#create driver object
class Driver:
    #initialize
    def __init__(self, number, laps, team, color):
        self.number = number
        self.laps = laps
        self.name = team
        self.color = color



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

