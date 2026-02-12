#get all drivers that set a kao
def get_drivers(laps):
    drivers = list({lap["driver_number"] for lap in laps})

    return drivers

#get all lap times for that driver
def get_driver_laps(laps, driver_number):
    #get list of all none null lap times for that driver
    driver_laps = [lap["lap_duration"] for lap in laps if lap["driver_number"] == driver_number and lap["lap_duration"] is not None]

    return driver_laps