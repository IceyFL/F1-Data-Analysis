from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from tkinter import ttk
import numpy as np
import tkinter as tk

from functions import get_graph_data

plt.style.use("grayscale")

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
    graph.subplots_adjust(left=0.25)

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

    #Create a frame to display what is being displayed currently
    list_frame = tk.Frame(gui)
    list_frame.place(x=10, y=100)


    #create empty list to store what to display
    added_items = []


    #function to filter the dropdown list as the user types
    def filter_list(event):
        typed = opt.get().lower() 
        filtered = [d for d in sessions if typed in d[1].lower()] 
        dropdown['values'] = [d[1] for d in filtered]

    #function to add item to list of displayed items
    def add_to_list(item):
        #check it is not already in the list
        for row in added_items: #iterate through already added items
            if row.winfo_children()[0].cget("text") == item: #check if the label of the row matches the item
                return #skip rest of function

        #create item to store the label and button
        row_frame = tk.Frame(list_frame)

        #add label to row
        lbl = tk.Label(row_frame, text=item)
        lbl.pack(side="left")

        #function to remove item from lsit
        def remove_item():
            row_frame.destroy()
            added_items.remove(row_frame)

        #add a button to the row to remove it
        btn = tk.Button(row_frame, text="Remove", command=remove_item)
        btn.pack(side="left", padx=5)

        #add the frame
        row_frame.pack(anchor="w")
        added_items.append(row_frame)

    #update graph
    def update_graph(event):
        #get selected session key
        selected_session = event.widget.get()

        #add the session to the list of displayed items
        add_to_list(selected_session)

        #get a list of all selected sessions
        selected_sessions = [row.winfo_children()[0].cget("text") for row in added_items]

        #list to store session keys
        session_keys = []

        #get all session keys
        for session in selected_sessions:
            #get the session key for the selected session
            session_keys.append(next(s[0] for s in sessions if s[1] == session)) 

        #get graph data for all selected sessions
        drivers = get_graph_data(session_keys)
        
        #create new graph
        graph = create_graph(drivers)

        #add left margin for the new graph
        graph.subplots_adjust(left=0.25)

        #update the graph on the GUI
        canvas.figure = graph
        canvas.draw()



    #filter the options when key is typed
    dropdown.bind("<KeyRelease>", filter_list)

    #update graph when new option is selected
    dropdown.bind("<<ComboboxSelected>>", update_graph)

    #add recent session to list of displayed items
    add_to_list(recent_name)

    return gui


#create the graph
def create_graph(drivers):
    #create window
    fig, ax = plt.subplots(figsize=(12, 6))

    #make the background dark

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
        body.set_linewidth(0.8)
        body.set_alpha(0.6)


    #Add driver names to grid
    ax.set_xticks(np.arange(1, len(drivers) + 1))
    ax.set_xticklabels([d.name for d in drivers])
    

    #return graph
    return fig