import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def create_graph(drivers):
    #create window
    fig, ax = plt.subplots(figsize=(12, 6))

    #set labels
    ax.set_xlabel("Driver") 
    ax.set_ylabel("Lap Time") 
    ax.set_title("Driver Lap Time Distribution")

    #format the lap times to show minutes rather than just seconds
    ax.yaxis.set_major_formatter( ticker.FuncFormatter(lambda x, pos: f"{int(x//60)}:{x%60:05.2f}") )

    #get driver laps
    driver_laps = [driver.laps for driver in drivers]


    # Create and show the graph also disable the overlay lines, bw method makes it less smooth
    violinplot = ax.violinplot(driver_laps, bw_method=0.2, widths=0.6, showmeans=False, showmedians=False, showextrema=False)
    
    #set the colour of each violin
    for i in range(len(violinplot["bodies"])): #iterate through each violin
        body = violinplot["bodies"][i]

        #modify body values
        body.set_facecolor(drivers[i].color)
        body.set_edgecolor("black")
        body.set_alpha(0.8)


    #Add driver names to grid
    ax.set_xticks(np.arange(1, len(drivers) + 1))
    ax.set_xticklabels([d.name for d in drivers])
    

    #display graph
    plt.show()