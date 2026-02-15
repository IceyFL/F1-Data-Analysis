from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from tkinter import ttk
import numpy as np
import tkinter as tk

from functions import get_graph_data

#create the GUI window
def create_gui():
    #create window
    window = tk.Tk()
    window.title("F1 Lap Time Distribution")

    #set window size
    window.geometry("1200x600")

    #return the window
    return window


#populate GUI with graph and controls
def populate_gui(gui, graph, recent_name, sessions):
    #add left margin for the menu
    graph.subplots_adjust(left=0.2)

    #put the graph on the GUI
    canvas = FigureCanvasTkAgg(graph, master=gui) 
    canvas.draw() 
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


    #add label
    Label = tk.Label(gui, text="Session")
    Label.place(x=10, y=35)


    #add the dropdown
    opt = tk.StringVar(gui)
    opt.set(recent_name)  #default value
    dropdown = ttk.Combobox(gui, textvariable=opt, values=[s[1] for s in sessions])
    dropdown.place(x=10, y=60)



    #function to filter the dropdown list as the user types
    def filter_list(event):
        typed = opt.get().lower() 
        filtered = [d for d in sessions if typed in d[1].lower()] 
        dropdown['values'] = [d[1] for d in filtered]

    
    #update graph
    def update_graph(event):
        #get selected session key
        selected_session = event.widget.get()
        session_key = next(s[0] for s in sessions if s[1] == selected_session)

        #get new graph data
        drivers = get_graph_data(session_key)

        #create new graph
        graph = create_graph(drivers)

        #add left margin for the new graph
        graph.subplots_adjust(left=0.2)

        #update the graph on the GUI
        canvas.figure = graph
        canvas.draw()

    #filter the options when key is typed
    dropdown.bind("<KeyRelease>", filter_list)

    #update graph when new option is selected
    dropdown.bind("<<ComboboxSelected>>", update_graph)

    return gui


#create the graph
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
    

    #return graph
    return fig