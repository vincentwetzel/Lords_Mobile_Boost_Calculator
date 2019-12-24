""" Pad everything in the grid
for frame_number in tk_frames:
    for child in tk_frames[frame_number].winfo_children():
        child.grid_configure(padx=5, pady=5)
"""

import logging
import sys
import tkinter
import tkinter.ttk
import tkinter.messagebox
from datetime import datetime
import csv
import os
from PIL import ImageTk, Image

# NOTE TO USER: use logging.DEBUG for testing, logging.CRITICAL for runtime
logging.basicConfig(stream=sys.stderr,
                    level=logging.CRITICAL)

SPEED_UP_ITEMS_COUNT = 14
SPEED_UP_RESEARCH_ITEMS_COUNT = 10
SPEED_UP_WALL_REPAIR_COUNT = 5
SPEED_UP_HEALING_COUNT = 4
SPEED_UP_TRAINING_COUNT = 7
SPEED_UP_MERGING_ITEMS_COUNT = 9

TABS_COUNT = 6
IMG_SCALE = 50

results_string_vars = list()
"""
[0] = speed up
[1] = research
[2] = wall repair
[3] = healing
[4] = training
[5] = merging
"""

speed_up_string_vars = list()
"""
[0] = 1m
[1] = 3m,
[2] = 5m,
[3] = 10m,
[4] = 15m,
[5] = 30m,
[6] = 60m,
[7] = 3h,
[8] = 8h,
[9] = 15h,
[10] = 24h,
[11] = 3d
[12] = 7d
[13] = 30d
"""

speed_up_research_string_vars = list()
"""
[0] = 5m,
[1] = 10m,
[2] = 15m,
[3] = 30m,
[4] = 60m,
[5] = 3h,
[6] = 8h,
[7] = 15h,
[8] = 24h,
[9] = 3d
"""

speed_up_merging_string_vars = list()
"""
[0] = 1m
[1] = 15m,
[2] = 60m,
[3] = 3h,
[4] = 8h,
[5] = 15h,
[6] = 24h,
[7] = 3d,
[8] = 7d
"""

speed_up_wall_repair_string_vars = list()
"""
[0] = 15m
[1] = 60m,
[2] = 3h,
[3] = 8h,
[4] = 24h
"""

speed_up_healing_string_vars = list()
"""
[0] = 15m
[1] = 60m,
[2] = 3h,
[3] = 8h,
"""

speed_up_training_string_vars = list()
"""
[0] = 10m
[1] = 30m,
[2] = 60m,
[3] = 3h,
[4] = 8h,
[5] = 24h,
[6] = 3d
"""

speed_up_entries = list()
"""
[0] = 1m
[1] = 3m,
[2] = 5m,
[3] = 10m,
[4] = 15m,
[5] = 30m,
[6] = 60m,
[7] = 3h,
[8] = 8h,
[9] = 15h,
[10] = 24h,
[11] = 3d
[12] = 7d
[13] = 30d
"""

speed_up_research_entries = list()
"""
[0] = 5m,
[1] = 10m,
[2] = 15m,
[3] = 30m,
[4] = 60m,
[5] = 3h,
[6] = 8h,
[7] = 15h,
[8] = 24h,
[9] = 3d
"""

speed_up_merging_entries = list()
"""
[0] = 1m
[1] = 15m,
[2] = 60m,
[3] = 3h,
[4] = 8h,
[5] = 15h,
[6] = 24h,
[7] = 3d,
[8] = 7d
"""

speed_up_wall_repair_entries = list()
"""
[0] = 15m
[1] = 60m,
[2] = 3h,
[3] = 8h,
[4] = 24h
"""

speed_up_healing_entries = list()
"""
[0] = 15m
[1] = 60m,
[2] = 3h,
[3] = 8h,
"""

speed_up_training_entries = list()
"""
[0] = 10m
[1] = 30m,
[2] = 60m,
[3] = 3h,
[4] = 8h,
[5] = 24h,
[6] = 3d
"""

speed_up_labels = list()
"""
[0] = 1m
[1] = 3m,
[2] = 5m,
[3] = 10m,
[4] = 15m,
[5] = 30m,
[6] = 60m,
[7] = 3h,
[8] = 8h,
[9] = 15h,
[10] = 24h,
[11] = 3d
[12] = 7d
[13] = 30d
"""

speed_up_research_labels = list()
"""
[0] = 5m,
[1] = 10m,
[2] = 15m,
[3] = 30m,
[4] = 60m,
[5] = 3h,
[6] = 8h,
[7] = 15h,
[8] = 24h,
[9] = 3d
"""

speed_up_merging_labels = list()
"""
[0] = 1m
[1] = 15m,
[2] = 60m,
[3] = 3h,
[4] = 8h,
[5] = 15h,
[6] = 24h,
[7] = 3d,
[8] = 7d
"""

speed_up_wall_repair_labels = list()
"""
[0] = 15m
[1] = 60m,
[2] = 3h,
[3] = 8h,
[4] = 24h
"""

speed_up_healing_labels = list()
"""
[0] = 15m
[1] = 60m,
[2] = 3h,
[3] = 8h,
"""

speed_up_training_labels = list()
"""
[0] = 10m
[1] = 30m,
[2] = 60m,
[3] = 3h,
[4] = 8h,
[5] = 24h,
[6] = 3d
"""

speed_up_tk_images = list()
"""
[0] = 1m
[1] = 3m,
[2] = 5m,
[3] = 10m,
[4] = 15m,
[5] = 30m,
[6] = 60m,
[7] = 3h,
[8] = 8h,
[9] = 15h,
[10] = 24h,
[11] = 3d
[12] = 7d
[13] = 30d
"""

speed_up_research_tk_images = list()
"""
[0] = 5m,
[1] = 10m,
[2] = 15m,
[3] = 30m,
[4] = 60m,
[5] = 3h,
[6] = 8h,
[7] = 15h,
[8] = 24h,
[9] = 3d
"""

speed_up_merging_tk_images = list()
"""
[0] = 1m
[1] = 15m,
[2] = 60m,
[3] = 3h,
[4] = 8h,
[5] = 15h,
[6] = 24h,
[7] = 3d,
[8] = 7d
"""

speed_up_wall_repair_tk_images = list()
"""
[0] = 1m
[1] = 60m,
[2] = 3h,
[3] = 8h,
[4] = 24h
"""

speed_up_healing_tk_images = list()
"""
[0] = 15m
[1] = 60m,
[2] = 3h,
[3] = 8h,
"""

speed_up_training_tk_images = list()
"""
[0] = 10m
[1] = 30m,
[2] = 60m,
[3] = 3h,
[4] = 8h,
[5] = 24h,
[6] = 3d
"""

speed_up_image_locations = [
    "assets/speed_up/speed_up_1m.png",
    "assets/speed_up/speed_up_3m.png",
    "assets/speed_up/speed_up_5m.png",
    "assets/speed_up/speed_up_10m.png",
    "assets/speed_up/speed_up_15m.png",
    "assets/speed_up/speed_up_30m.png",
    "assets/speed_up/speed_up_60m.png",
    "assets/speed_up/speed_up_3h.png",
    "assets/speed_up/speed_up_8h.png",
    "assets/speed_up/speed_up_15h.png",
    "assets/speed_up/speed_up_24h.png",
    "assets/speed_up/speed_up_3d.png",
    "assets/speed_up/speed_up_7d.png",
    "assets/speed_up/speed_up_30d.png"
]

speed_up_research_image_locations = [
    "assets/speed_up_research/speed_up_research_5m.png",
    "assets/speed_up_research/speed_up_research_10m.png",
    "assets/speed_up_research/speed_up_research_15m.png",
    "assets/speed_up_research/speed_up_research_30m.png",
    "assets/speed_up_research/speed_up_research_60m.png",
    "assets/speed_up_research/speed_up_research_3h.png",
    "assets/speed_up_research/speed_up_research_8h.png",
    "assets/speed_up_research/speed_up_research_15h.png",
    "assets/speed_up_research/speed_up_research_24h.png",
    "assets/speed_up_research/speed_up_research_3d.png"
]

speed_up_merging_image_locations = [
    "assets/speed_up_merging/speed_up_merging_1m.png",
    "assets/speed_up_merging/speed_up_merging_15m.png",
    "assets/speed_up_merging/speed_up_merging_60m.png",
    "assets/speed_up_merging/speed_up_merging_3h.png",
    "assets/speed_up_merging/speed_up_merging_8h.png",
    "assets/speed_up_merging/speed_up_merging_15h.png",
    "assets/speed_up_merging/speed_up_merging_24h.png",
    "assets/speed_up_merging/speed_up_merging_3d.png",
    "assets/speed_up_merging/speed_up_merging_7d.png"
]

speed_up_wall_repair_image_locations = [
    "assets/speed_up_wall_repair/speed_up_wall_repair_15m.png",
    "assets/speed_up_wall_repair/speed_up_wall_repair_60m.png",
    "assets/speed_up_wall_repair/speed_up_wall_repair_3h.png",
    "assets/speed_up_wall_repair/speed_up_wall_repair_8h.png",
    "assets/speed_up_wall_repair/speed_up_wall_repair_24h.png"
]

speed_up_healing_image_locations = [
    "assets/speed_up_healing/speed_up_healing_15m.png",
    "assets/speed_up_healing/speed_up_healing_60m.png",
    "assets/speed_up_healing/speed_up_healing_3h.png",
    "assets/speed_up_healing/speed_up_healing_8h.png"
]

speed_up_training_image_locations = [
    "assets/speed_up_training/speed_up_training_10m.png",
    "assets/speed_up_training/speed_up_training_30m.png",
    "assets/speed_up_training/speed_up_training_60m.png",
    "assets/speed_up_training/speed_up_training_3h.png",
    "assets/speed_up_training/speed_up_training_8h.png",
    "assets/speed_up_training/speed_up_training_24h.png",
    "assets/speed_up_training/speed_up_training_3d.png",
]

labels = [speed_up_labels, speed_up_research_labels, speed_up_wall_repair_labels,
          speed_up_healing_labels, speed_up_training_labels, speed_up_merging_labels]
tk_images = [speed_up_tk_images, speed_up_research_tk_images, speed_up_wall_repair_tk_images,
             speed_up_healing_tk_images, speed_up_training_tk_images, speed_up_merging_tk_images]
image_locations = [speed_up_image_locations, speed_up_research_image_locations, speed_up_wall_repair_image_locations,
                   speed_up_healing_image_locations, speed_up_training_image_locations,
                   speed_up_merging_image_locations]
string_vars = [speed_up_string_vars, speed_up_research_string_vars, speed_up_wall_repair_string_vars,
               speed_up_healing_string_vars, speed_up_training_string_vars, speed_up_merging_string_vars]
entries = [speed_up_entries, speed_up_research_entries, speed_up_wall_repair_entries,
           speed_up_healing_entries, speed_up_training_entries, speed_up_merging_entries]
counters = [SPEED_UP_ITEMS_COUNT, SPEED_UP_RESEARCH_ITEMS_COUNT, SPEED_UP_WALL_REPAIR_COUNT, SPEED_UP_HEALING_COUNT,
            SPEED_UP_TRAINING_COUNT, SPEED_UP_MERGING_ITEMS_COUNT]

data_set_notes_entry_string_var = None
root_tk = None
notebook = None
tk_frames = list()

save_file = "LM_boosts.csv"


def main():
    # Init Tkinter GUI
    global root_tk
    global notebook
    global tk_frames
    global TABS_COUNT
    global results_string_vars
    global data_set_notes_entry_string_var

    root_tk = tkinter.Tk()  # constructor for TK object
    root_tk.title("Lords Mobile Boost Calculator by Vincent Wetzel")

    data_set_notes_entry_string_var = tkinter.StringVar()

    notebook = tkinter.ttk.Notebook(root_tk)

    for i in range(TABS_COUNT):
        tk_frames.append(tkinter.ttk.Frame(notebook, padding="3 3 12 12"))

    notebook.add(tk_frames[0], text="Speed Up")
    notebook.add(tk_frames[1], text="Research")
    notebook.add(tk_frames[2], text="Wall Repair")
    notebook.add(tk_frames[3], text="Healing")
    notebook.add(tk_frames[4], text="Training")
    notebook.add(tk_frames[5], text="Merging")

    notebook.grid()

    for i in range(TABS_COUNT):
        results_string_vars.append(tkinter.StringVar(value="0 minutes"))

    global labels
    global tk_images
    global image_locations
    global string_vars
    global entries

    for c in range(TABS_COUNT):
        init_frame(c, counters[c], labels[c], tk_images[c], image_locations[c], string_vars[c], entries[c])

    # Init hotkeys
    root_tk.bind('<Control-s>', lambda x: save_to_file())
    root_tk.bind('<Return>', lambda x: update_totals())

    # Start the main program loop
    root_tk.mainloop()
    exit()

    # Done!


def init_frame(frame_number, counters_param, labels_list, tk_images_list, image_locations_list, string_vars_list,
               entries_list):
    global tk_frames
    global IMG_SCALE
    global data_set_notes_entry_string_var

    # Init Labels and put Images on them
    for label_counter in range(counters_param):
        # Open then resize the image object
        image = Image.open(image_locations_list[label_counter])
        image = image.resize((IMG_SCALE, IMG_SCALE), Image.ANTIALIAS)
        tk_images_list.append(ImageTk.PhotoImage(image))

        # Create a Label and display the image in the grid
        labels_list.append(tkinter.ttk.Label(tk_frames[frame_number], image=tk_images_list[label_counter]))
        labels_list[label_counter].grid(column=0, row=label_counter, sticky='W')

    # Init Entries
    for entry_counter in range(counters_param):
        string_vars_list.append(tkinter.StringVar(value=0))
        entries_list.append(
            tkinter.ttk.Entry(tk_frames[frame_number], width=4, textvariable=string_vars_list[entry_counter]))
        entries_list[entry_counter].grid(column=1, row=entry_counter)
        entries_list[entry_counter].bind('<FocusIn>',
                                         lambda_to_bind_string_var_to_entry_selected(string_vars_list[entry_counter]))
        entries_list[entry_counter].bind('<FocusOut>',
                                         lambda_to_bind_string_var_to_entry_deselected(string_vars_list[entry_counter]))

    # Init Main Frame Results GUI
    tkinter.ttk.Label(tk_frames[frame_number], text="Speed Up Total:").grid(column=0, row=100, sticky='W',
                                                                            columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], text="Speed Up Research Total:").grid(column=0, row=101,
                                                                                     sticky='W', columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], text="Speed Up Wall Repair Total:").grid(column=0, row=102, sticky='W',
                                                                                        columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], text="Speed Up Healing Total:").grid(column=0, row=103, sticky='W',
                                                                                    columnspan=2)

    tkinter.ttk.Label(tk_frames[frame_number], text="Speed Up Training Total:").grid(column=0, row=104, sticky='W',
                                                                                     columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], text="Speed Up Merging Total:").grid(column=0, row=105, sticky='W',
                                                                                    columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], textvariable=results_string_vars[0]).grid(column=2, row=100,
                                                                                         sticky=('W', 'E'),
                                                                                         columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], textvariable=results_string_vars[1]).grid(column=2, row=101,
                                                                                         sticky=('W', 'E'),
                                                                                         columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], textvariable=results_string_vars[2]).grid(column=2, row=102,
                                                                                         sticky=('W', 'E'),
                                                                                         columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], textvariable=results_string_vars[3]).grid(column=2, row=103,
                                                                                         sticky=('W', 'E'),
                                                                                         columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], textvariable=results_string_vars[4]).grid(column=2, row=104,
                                                                                         sticky=('W', 'E'),
                                                                                         columnspan=2)
    tkinter.ttk.Label(tk_frames[frame_number], textvariable=results_string_vars[5]).grid(column=2, row=105,
                                                                                         sticky=('W', 'E'),
                                                                                         columnspan=2)

    # Reset buttons
    tkinter.ttk.Button(tk_frames[frame_number], text="Reset",
                       command=lambda: reset_all_values_in_frame(frame_number)).grid(column=0, row=200,
                                                                                     sticky='W')
    tkinter.ttk.Button(tk_frames[frame_number], text="Reset All",
                       command=lambda: reset_all_values()).grid(column=1, row=200, sticky='W')
    # Enter notes for this dataset
    tkinter.ttk.Label(tk_frames[frame_number], text="Notes:").grid(column=0, row=201, sticky='W', )
    notes_entry = tkinter.ttk.Entry(tk_frames[frame_number], width=75,
                                    textvariable=data_set_notes_entry_string_var)
    notes_entry.grid(column=1, row=201, columnspan=4, sticky='W')

    # Set Save button
    tkinter.ttk.Button(tk_frames[frame_number], text="Save to file", command=lambda: save_to_file()).grid(
        column=5, row=201,
        sticky='W')

    # Set the starting location of the typing cursor
    entries_list[0].focus()


def get_int_input(query_str):
    """
    Prompt the user for an integer input and only continue once they've given a valid input.
    :param query_str:   The prompt to the user.
    :return:    An integer type that the user has entered.
    """
    while True:
        try:
            return int(input(query_str))
        except ValueError:
            logging.debug("That didn't work. Try again.")


def format_minutes_to_time(minutes):
    """
    Put in minutes, get back formatted hours + minutes
    :param minutes: The number of minutes to break down
    :return: A string of the hours and minutes in the original value
    """
    days = minutes // 1440
    minutes = minutes % 1440
    hours = minutes // 60
    minutes = minutes % 60

    output = ""
    if days > 0:
        if hours > 0 or minutes > 0:
            if days == 1:
                output += str(days) + " Day, "
            else:
                output += str(days) + " Days, "
        else:
            if days == 1:
                return str(days) + " Day"
            else:
                return str(days) + " Days"
    if hours > 0:
        if minutes > 0:
            if hours == 1:
                output += str(hours) + " Hour, "
            else:
                output += str(hours) + " Hours, "
        else:
            if hours == 1:
                return output + str(hours) + " Hour"
            else:
                return output + str(hours) + " Hours"

    if minutes == 1:
        return output + str(minutes) + " Minute"
    else:
        return output + str(minutes) + " Minutes"


def update_totals():
    """
    This method updates all the running totals and then updates the GUI
    :return:    None
    """
    try:
        global results_string_vars
        speed_up_total = 0
        speed_up_total += 1 * int(speed_up_string_vars[0].get())
        speed_up_total += 3 * int(speed_up_string_vars[1].get())
        speed_up_total += 5 * int(speed_up_string_vars[2].get())
        speed_up_total += 10 * int(speed_up_string_vars[3].get())
        speed_up_total += 15 * int(speed_up_string_vars[4].get())
        speed_up_total += 30 * int(speed_up_string_vars[5].get())
        speed_up_total += 60 * int(speed_up_string_vars[6].get())
        speed_up_total += 180 * int(speed_up_string_vars[7].get())
        speed_up_total += 480 * int(speed_up_string_vars[8].get())
        speed_up_total += 900 * int(speed_up_string_vars[9].get())
        speed_up_total += 1440 * int(speed_up_string_vars[10].get())
        speed_up_total += 4320 * int(speed_up_string_vars[11].get())
        speed_up_total += 10080 * int(speed_up_string_vars[12].get())
        speed_up_total += 43200 * int(speed_up_string_vars[13].get())
        results_string_vars[0].set(format_minutes_to_time(speed_up_total))

        global speed_up_research_string_vars
        speed_up_research_total = 0
        speed_up_research_total += 5 * int(speed_up_research_string_vars[0].get())
        speed_up_research_total += 10 * int(speed_up_research_string_vars[1].get())
        speed_up_research_total += 15 * int(speed_up_research_string_vars[2].get())
        speed_up_research_total += 30 * int(speed_up_research_string_vars[3].get())
        speed_up_research_total += 60 * int(speed_up_research_string_vars[4].get())
        speed_up_research_total += 180 * int(speed_up_research_string_vars[5].get())
        speed_up_research_total += 480 * int(speed_up_research_string_vars[6].get())
        speed_up_research_total += 900 * int(speed_up_research_string_vars[7].get())
        speed_up_research_total += 1440 * int(speed_up_research_string_vars[8].get())
        speed_up_research_total += 4320 * int(speed_up_research_string_vars[9].get())
        results_string_vars[1].set(format_minutes_to_time(speed_up_research_total))

        global speed_up_wall_repair_string_vars
        speed_up_wall_repair_total = 0
        speed_up_wall_repair_total += 15 * int(speed_up_wall_repair_string_vars[0].get())
        speed_up_wall_repair_total += 60 * int(speed_up_wall_repair_string_vars[1].get())
        speed_up_wall_repair_total += 180 * int(speed_up_wall_repair_string_vars[2].get())
        speed_up_wall_repair_total += 480 * int(speed_up_wall_repair_string_vars[3].get())
        speed_up_wall_repair_total += 1440 * int(speed_up_wall_repair_string_vars[4].get())
        results_string_vars[2].set(format_minutes_to_time(speed_up_wall_repair_total))

        global speed_up_healing_string_vars
        speed_up_healing_total = 0
        speed_up_healing_total += 15 * int(speed_up_healing_string_vars[0].get())
        speed_up_healing_total += 60 * int(speed_up_healing_string_vars[1].get())
        speed_up_healing_total += 180 * int(speed_up_healing_string_vars[2].get())
        speed_up_healing_total += 480 * int(speed_up_healing_string_vars[3].get())
        results_string_vars[3].set(format_minutes_to_time(speed_up_healing_total))

        global speed_up_training_string_vars
        speed_up_training_total = 0
        speed_up_training_total += 10 * int(speed_up_training_string_vars[0].get())
        speed_up_training_total += 30 * int(speed_up_training_string_vars[1].get())
        speed_up_training_total += 60 * int(speed_up_training_string_vars[2].get())
        speed_up_training_total += 180 * int(speed_up_training_string_vars[3].get())
        speed_up_training_total += 480 * int(speed_up_training_string_vars[4].get())
        speed_up_training_total += 1440 * int(speed_up_training_string_vars[5].get())
        speed_up_training_total += 4320 * int(speed_up_training_string_vars[6].get())
        results_string_vars[4].set(format_minutes_to_time(speed_up_training_total))

        global speed_up_merging_string_vars
        speed_up_merging_total = 0
        speed_up_merging_total += 1 * int(speed_up_merging_string_vars[0].get())
        speed_up_merging_total += 15 * int(speed_up_merging_string_vars[1].get())
        speed_up_merging_total += 60 * int(speed_up_merging_string_vars[2].get())
        speed_up_merging_total += 180 * int(speed_up_merging_string_vars[3].get())
        speed_up_merging_total += 480 * int(speed_up_merging_string_vars[4].get())
        speed_up_merging_total += 900 * int(speed_up_merging_string_vars[5].get())
        speed_up_merging_total += 1440 * int(speed_up_merging_string_vars[6].get())
        speed_up_merging_total += 4320 * int(speed_up_merging_string_vars[7].get())
        speed_up_merging_total += 10080 * int(speed_up_merging_string_vars[8].get())
        results_string_vars[5].set(format_minutes_to_time(speed_up_merging_total))

    except ValueError:
        # Do not update, there was an error
        return


def save_to_file(confirm_save=False):
    """
    Saves the data to an output file.
    :return:    None
    """
    print("STF called")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    global notebook
    if notebook.index(notebook.select()) == 0:
        if confirm_save or tkinter.messagebox.askyesno(title="Save to File", message="Do you want to save this data?"):

            fieldnames_for_csv = [
                "Date/Time",
                "Notes",

                "Speed_Up_Total",
                "Speed_Up_Research_Total",
                "Speed_Up_Wall_Repair_Total",
                "Speed_Up_Healing_Total",
                "Speed_Up_Training_Total",
                "Speed_Up_Merging_Total",

                "Speed_Up_1m",
                "Speed_Up_3m",
                "Speed_Up_5m",
                "Speed_Up_10m",
                "Speed_Up_15m",
                "Speed_Up_30m",
                "Speed_Up_60m",
                "Speed_Up_3h",
                "Speed_Up_8h",
                "Speed_Up_15h",
                "Speed_Up_24h",
                "Speed_Up_3d",
                "Speed_Up_7d",
                "Speed_Up_30d",

                "Speed_Up_Research_5m",
                "Speed_Up_Research_10m",
                "Speed_Up_Research_15m",
                "Speed_Up_Research_30m",
                "Speed_Up_Research_60m",
                "Speed_Up_Research_3h",
                "Speed_Up_Research_8h",
                "Speed_Up_Research_15h",
                "Speed_Up_Research_24h",
                "Speed_Up_Research_3d",

                "Speed_Up_Wall_Repair_15m",
                "Speed_Up_Wall_Repair_60m",
                "Speed_Up_Wall_Repair_3h",
                "Speed_Up_Wall_Repair_8h",
                "Speed_Up_Wall_Repair_24h",

                "Speed_Up_Healing_15m",
                "Speed_Up_Healing_60m",
                "Speed_Up_Healing_3h",
                "Speed_Up_Healing_8h",

                "Speed_Up_Training_10m",
                "Speed_Up_Training_30m",
                "Speed_Up_Training_60m",
                "Speed_Up_Training_3h",
                "Speed_Up_Training_8h",
                "Speed_Up_Training_24h",
                "Speed_Up_Training_3d",

                "Speed_Up_Merging_1m",
                "Speed_Up_Merging_15m",
                "Speed_Up_Merging_15m",
                "Speed_Up_Merging_60m",
                "Speed_Up_Merging_3h",
                "Speed_Up_Merging_8h",
                "Speed_Up_Merging_15h",
                "Speed_Up_Merging_24h",
                "Speed_Up_Merging_3d",
                "Speed_Up_Merging_7d"
            ]

            global speed_up_string_vars
            global speed_up_research_string_vars
            global speed_up_wall_repair_string_vars
            global speed_up_healing_string_vars
            global speed_up_training_string_vars
            global speed_up_merging_string_vars

            global results_string_vars
            global data_set_notes_entry_string_var
            global save_file

            try:
                # If the file doesn't exist, create it
                if not os.path.exists(save_file):
                    with open(save_file, 'w', newline='') as fnew:
                        writer = csv.DictWriter(fnew, fieldnames=fieldnames_for_csv)
                        writer.writeheader()

                # Append the current set of data to the file
                with open(save_file, 'a', newline='') as outfile:  # output csv file
                    # Make sure there are no blank strings (focused Entry) that will cause errors
                    for count, x in enumerate(speed_up_string_vars):
                        if speed_up_string_vars[count].get() == "":
                            speed_up_string_vars[count].set(0)
                    for count, x in enumerate(speed_up_research_string_vars):
                        if speed_up_research_string_vars[count].get() == "":
                            speed_up_research_string_vars[count].set(0)
                    for count, x in enumerate(speed_up_wall_repair_string_vars):
                        if speed_up_wall_repair_string_vars[count].get() == "":
                            speed_up_wall_repair_string_vars[count].set(0)
                    for count, x in enumerate(speed_up_healing_string_vars):
                        if speed_up_healing_string_vars[count].get() == "":
                            speed_up_healing_string_vars[count].set(0)
                    for count, x in enumerate(speed_up_training_string_vars):
                        if speed_up_training_string_vars[count].get() == "":
                            speed_up_training_string_vars[count].set(0)
                    for count, x in enumerate(speed_up_merging_string_vars):
                        if speed_up_merging_string_vars[count].get() == "":
                            speed_up_merging_string_vars[count].set(0)
                    # Open outfile
                    writer = csv.DictWriter(outfile, fieldnames=fieldnames_for_csv)

                    # Write to outfile
                    writer.writerow({"Date/Time": current_time,
                                     "Notes": data_set_notes_entry_string_var.get(),
                                     "Speed_Up_Total": results_string_vars[0].get(),
                                     "Speed_Up_Research_Total": results_string_vars[1].get(),
                                     "Speed_Up_Wall_Repair_Total": results_string_vars[2].get(),
                                     "Speed_Up_Healing_Total": results_string_vars[3].get(),
                                     "Speed_Up_Training_Total": results_string_vars[4].get(),
                                     "Speed_Up_Merging_Total": results_string_vars[5].get(),

                                     "Speed_Up_1m": format_minutes_to_time(int(speed_up_string_vars[0].get()) * 1),
                                     "Speed_Up_3m": format_minutes_to_time(int(speed_up_string_vars[1].get()) * 3),
                                     "Speed_Up_5m": format_minutes_to_time(int(speed_up_string_vars[2].get()) * 5),
                                     "Speed_Up_10m": format_minutes_to_time(
                                         int(speed_up_string_vars[3].get()) * 10),
                                     "Speed_Up_15m": format_minutes_to_time(
                                         int(speed_up_string_vars[4].get()) * 15),
                                     "Speed_Up_30m": format_minutes_to_time(
                                         int(speed_up_string_vars[5].get()) * 30),
                                     "Speed_Up_60m": format_minutes_to_time(
                                         int(speed_up_string_vars[6].get()) * 60),
                                     "Speed_Up_3h": format_minutes_to_time(
                                         int(speed_up_string_vars[7].get()) * 180),
                                     "Speed_Up_8h": format_minutes_to_time(
                                         int(speed_up_string_vars[8].get()) * 480),
                                     "Speed_Up_15h": format_minutes_to_time(
                                         int(speed_up_string_vars[9].get()) * 900),
                                     "Speed_Up_24h": format_minutes_to_time(
                                         int(speed_up_string_vars[10].get()) * 1440),
                                     "Speed_Up_3d": format_minutes_to_time(
                                         int(speed_up_string_vars[11].get()) * 4320),
                                     "Speed_Up_7d": format_minutes_to_time(
                                         int(speed_up_string_vars[12].get()) * 10080),
                                     "Speed_Up_30d": format_minutes_to_time(
                                         int(speed_up_string_vars[13].get()) * 43200),

                                     "Speed_Up_Research_5m": format_minutes_to_time(
                                         int(speed_up_research_string_vars[0].get()) * 5),
                                     "Speed_Up_Research_10m": format_minutes_to_time(
                                         int(speed_up_research_string_vars[1].get()) * 10),
                                     "Speed_Up_Research_15m": format_minutes_to_time(
                                         int(speed_up_research_string_vars[2].get()) * 15),
                                     "Speed_Up_Research_30m": format_minutes_to_time(
                                         int(speed_up_research_string_vars[3].get()) * 30),
                                     "Speed_Up_Research_60m": format_minutes_to_time(
                                         int(speed_up_research_string_vars[4].get()) * 60),
                                     "Speed_Up_Research_3h": format_minutes_to_time(
                                         int(speed_up_research_string_vars[5].get()) * 180),
                                     "Speed_Up_Research_8h": format_minutes_to_time(
                                         int(speed_up_research_string_vars[6].get()) * 480),
                                     "Speed_Up_Research_15h": format_minutes_to_time(
                                         int(speed_up_research_string_vars[7].get()) * 900),
                                     "Speed_Up_Research_24h": format_minutes_to_time(
                                         int(speed_up_research_string_vars[8].get()) * 1440),
                                     "Speed_Up_Research_3d": format_minutes_to_time(
                                         int(speed_up_research_string_vars[9].get()) * 4320),

                                     "Speed_Up_Wall_Repair_15m": format_minutes_to_time(
                                         int(speed_up_wall_repair_string_vars[0].get()) * 15),
                                     "Speed_Up_Wall_Repair_60m": format_minutes_to_time(
                                         int(speed_up_wall_repair_string_vars[1].get()) * 60),
                                     "Speed_Up_Wall_Repair_3h": format_minutes_to_time(
                                         int(speed_up_wall_repair_string_vars[2].get()) * 180),
                                     "Speed_Up_Wall_Repair_8h": format_minutes_to_time(
                                         int(speed_up_wall_repair_string_vars[3].get()) * 480),
                                     "Speed_Up_Wall_Repair_24h": format_minutes_to_time(
                                         int(speed_up_wall_repair_string_vars[4].get()) * 1440),

                                     "Speed_Up_Healing_15m": format_minutes_to_time(
                                         int(speed_up_healing_string_vars[0].get()) * 15),
                                     "Speed_Up_Healing_60m": format_minutes_to_time(
                                         int(speed_up_healing_string_vars[1].get()) * 60),
                                     "Speed_Up_Healing_3h": format_minutes_to_time(
                                         int(speed_up_healing_string_vars[2].get()) * 180),
                                     "Speed_Up_Healing_8h": format_minutes_to_time(
                                         int(speed_up_healing_string_vars[3].get()) * 480),

                                     "Speed_Up_Training_10m": format_minutes_to_time(
                                         int(speed_up_training_string_vars[0].get()) * 10),
                                     "Speed_Up_Training_30m": format_minutes_to_time(
                                         int(speed_up_training_string_vars[1].get()) * 30),
                                     "Speed_Up_Training_60m": format_minutes_to_time(
                                         int(speed_up_training_string_vars[2].get()) * 60),
                                     "Speed_Up_Training_3h": format_minutes_to_time(
                                         int(speed_up_training_string_vars[3].get()) * 180),
                                     "Speed_Up_Training_8h": format_minutes_to_time(
                                         int(speed_up_training_string_vars[4].get()) * 480),
                                     "Speed_Up_Training_24h": format_minutes_to_time(
                                         int(speed_up_training_string_vars[5].get()) * 1440),
                                     "Speed_Up_Training_3d": format_minutes_to_time(
                                         int(speed_up_training_string_vars[6].get()) * 4320),

                                     "Speed_Up_Merging_1m": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[0].get()) * 1),
                                     "Speed_Up_Merging_15m": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[1].get()) * 15),
                                     "Speed_Up_Merging_60m": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[2].get()) * 60),
                                     "Speed_Up_Merging_3h": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[3].get()) * 180),
                                     "Speed_Up_Merging_8h": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[4].get()) * 480),
                                     "Speed_Up_Merging_15h": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[5].get()) * 900),
                                     "Speed_Up_Merging_24h": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[6].get()) * 1440),
                                     "Speed_Up_Merging_3d": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[7].get()) * 4320),
                                     "Speed_Up_Merging_7d": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[8].get()) * 10080)
                                     })
                if tkinter.messagebox.askyesno(title="Would you like to open the file?",
                                               message="The file has been saved. Would you like to open it?"):
                    os.startfile(save_file)
            except PermissionError:
                if tkinter.messagebox.askretrycancel("Error opening CSV file",
                                                     "The CSV file you are trying to save to is already open. "
                                                     "Close the file then retry."):
                    save_to_file(confirm_save=True)


def lambda_to_bind_string_var_to_entry_selected(string_var_to_bind_to_entry):
    return lambda x: entry_selected(string_var_to_bind_to_entry)


def lambda_to_bind_string_var_to_entry_deselected(string_var_to_bind_to_entry):
    return lambda x: entry_deselected(string_var_to_bind_to_entry)


def entry_selected(string_var):
    """
    If an entry box is clicked and the current StringVar value of the box is 0, clear the box.
    """
    if string_var.get() == '0':
        string_var.set('')


def entry_deselected(string_var):
    """
    If an entry box is deselected without a value being entered in it, set the StringVar to 0.
    """
    try:
        # Make sure the value entered is an int
        int(string_var.get())
    except ValueError:
        string_var.set(0)

    update_totals()


def reset_all_values_in_frame(frame_number):
    """
    Resets all values back to 0.
    """

    global string_vars
    global counters

    for i in range(counters[frame_number]):
        string_vars[frame_number][i].set(0)

    """for i in range(len(speed_up_string_vars)):
        speed_up_string_vars[i].set(0)

    for i in range(len(speed_up_research_string_vars)):
        speed_up_research_string_vars[i].set(0)

    for i in range(len(speed_up_merging_string_vars)):
        speed_up_merging_string_vars[i].set(0)"""

    update_totals()


def reset_all_values():
    global speed_up_string_vars
    global speed_up_research_string_vars
    global speed_up_wall_repair_string_vars
    global speed_up_healing_string_vars
    global speed_up_training_string_vars
    global speed_up_merging_string_vars

    for i in range(len(speed_up_string_vars)):
        speed_up_string_vars[i].set(0)

    for i in range(len(speed_up_research_string_vars)):
        speed_up_research_string_vars[i].set(0)

    for i in range(len(speed_up_wall_repair_string_vars)):
        speed_up_wall_repair_string_vars[i].set(0)

    for i in range(len(speed_up_healing_string_vars)):
        speed_up_healing_string_vars[i].set(0)

    for i in range(len(speed_up_training_string_vars)):
        speed_up_training_string_vars[i].set(0)

    for i in range(len(speed_up_merging_string_vars)):
        speed_up_merging_string_vars[i].set(0)

    update_totals()


if __name__ == "__main__":
    main()
