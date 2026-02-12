#get all drivers that set a kao
def get_drivers(laps):
    drivers = list({lap["driver_number"] for lap in laps})

    return drivers

#get all lap times for that driver
def get_driver_laps(laps, driver_number):
    #get list of all none null lap times for that driver
    driver_laps = [float(lap["lap_duration"]) for lap in laps if lap["driver_number"] == driver_number and lap["lap_duration"] is not None]

    #get lowest lap time
    avg = min(driver_laps)

    #remove outliers
    driver_laps = [lap for lap in driver_laps if lap <= avg*1.1 and lap < 200]

    return driver_laps