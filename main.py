from functions import *
from API import *
import GUI

#main function
def main():
    #get most recent session key
    recent_key, recent_name, sessions = get_sessions()

    #get graph data
    drivers = get_graph_data([recent_key])

    #create graph
    graph = GUI.create_graph(drivers)

    #create GUI window
    gui = GUI.create_gui()

    #populate GUI with graph and controls
    gui = GUI.populate_gui(gui, graph, recent_name, sessions)

    #loop GUI
    gui.mainloop()


#only run main function if this file is run directly
if __name__ == "__main__":
    main()