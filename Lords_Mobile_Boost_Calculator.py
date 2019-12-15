from tkinter import *
from tkinter import ttk
from datetime import datetime
import csv
import os
import pandas  # Also requires xlrd to read xlsx files.

speed_up_string_vars = [None] * 11
"""
[0] = 3m,
[1] = 5m,
[2] = 10m,
[3] = 15m,
[4] = 30m,
[5] = 60m,
[6] = 3h,
[7] = 8h,
[8] = 15h,
[9] = 24h,
[10] = 3d
"""

speed_up_research_string_vars = [None] * 9
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
"""

speed_up_merging_string_vars = [None] * 5
"""
[0] = 15m,
[1] = 60m,
[2] = 3h,
[3] = 8h,
[4] = 15h,
"""

results_string_vars = [None] * 3
"""
[0] = speed up
[1] = research
[2] = merging
"""

data_set_notes_entry_string_var = None


def main():
    # Init Tkinter GUI
    root_tk = Tk()  # constructor for TK object
    root_tk.title("Lords Mobile Boost Calculator by Vincent Wetzel")
    main_frame = ttk.Frame(root_tk, padding="3 3 12 12")
    main_frame.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
    root_tk.columnconfigure(0, weight=1)
    root_tk.rowconfigure(0, weight=1)

    # Init globals
    global speed_up_string_vars
    for i in range(len(speed_up_string_vars)):
        speed_up_string_vars[i] = StringVar(value=0)

    global speed_up_research_string_vars
    for i in range(len(speed_up_research_string_vars)):
        speed_up_research_string_vars[i] = StringVar(value=0)

    global speed_up_merging_string_vars
    for i in range(len(speed_up_merging_string_vars)):
        speed_up_merging_string_vars[i] = StringVar(value=0)

    global results_string_vars
    for i in range(len(results_string_vars)):
        results_string_vars[i] = StringVar(value="0 minutes")

    global data_set_notes_entry_string_var
    data_set_notes_entry_string_var = StringVar()

    # Init Normal Speedups GUI
    ttk.Label(main_frame, text="3 minute speedups").grid(column=0, row=0, sticky=W)
    ttk.Label(main_frame, text="5 minute speedups").grid(column=0, row=1, sticky=W)
    ttk.Label(main_frame, text="10 minute speedups").grid(column=0, row=2, sticky=W)
    ttk.Label(main_frame, text="15 minute speedups").grid(column=0, row=3, sticky=W)
    ttk.Label(main_frame, text="30 minute speedups").grid(column=0, row=4, sticky=W)
    ttk.Label(main_frame, text="60 minute speedups").grid(column=0, row=5, sticky=W)
    ttk.Label(main_frame, text="3 hour speedups").grid(column=0, row=6, sticky=W)
    ttk.Label(main_frame, text="8 hour speedups").grid(column=0, row=7, sticky=W)
    ttk.Label(main_frame, text="15 hour speedups").grid(column=0, row=8, sticky=W)
    ttk.Label(main_frame, text="24 hour speedups").grid(column=0, row=9, sticky=W)
    ttk.Label(main_frame, text="3 day speedups").grid(column=0, row=10, sticky=W)
    speed_up_3m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[0])
    speed_up_3m_entry.grid(column=1, row=0)
    speed_up_3m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[0]))
    speed_up_3m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[0]))
    speed_up_5m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[1])
    speed_up_5m_entry.grid(column=1, row=1)
    speed_up_5m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[1]))
    speed_up_5m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[1]))
    speed_up_10m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[2])
    speed_up_10m_entry.grid(column=1, row=2)
    speed_up_10m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[2]))
    speed_up_10m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[2]))
    speed_up_15m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[3])
    speed_up_15m_entry.grid(column=1, row=3)
    speed_up_15m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[3]))
    speed_up_15m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[3]))
    speed_up_30m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[4])
    speed_up_30m_entry.grid(column=1, row=4)
    speed_up_30m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[4]))
    speed_up_30m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[4]))
    speed_up_60m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[5])
    speed_up_60m_entry.grid(column=1, row=5)
    speed_up_60m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[5]))
    speed_up_60m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[5]))
    speed_up_3h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[6])
    speed_up_3h_entry.grid(column=1, row=6)
    speed_up_3h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[6]))
    speed_up_3h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[6]))
    speed_up_8h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[7])
    speed_up_8h_entry.grid(column=1, row=7)
    speed_up_8h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[7]))
    speed_up_8h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[7]))
    speed_up_15h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[8])
    speed_up_15h_entry.grid(column=1, row=8)
    speed_up_15h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[8]))
    speed_up_15h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[8]))
    speed_up_24h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[9])
    speed_up_24h_entry.grid(column=1, row=9)
    speed_up_24h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[9]))
    speed_up_24h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[9]))
    speed_up_3d_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_string_vars[10])
    speed_up_3d_entry.grid(column=1, row=10)
    speed_up_3d_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_string_vars[10]))
    speed_up_3d_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_string_vars[10]))

    # Init Research Speedups GUI
    ttk.Label(main_frame, text="5 minute research").grid(column=2, row=0, sticky=W)
    ttk.Label(main_frame, text="10 minute research").grid(column=2, row=1, sticky=W)
    ttk.Label(main_frame, text="15 minute research").grid(column=2, row=2, sticky=W)
    ttk.Label(main_frame, text="30 minute research").grid(column=2, row=3, sticky=W)
    ttk.Label(main_frame, text="60 minute research").grid(column=2, row=4, sticky=W)
    ttk.Label(main_frame, text="3 hour research").grid(column=2, row=5, sticky=W)
    ttk.Label(main_frame, text="8 hour research").grid(column=2, row=6, sticky=W)
    ttk.Label(main_frame, text="15 hour research").grid(column=2, row=7, sticky=W)
    ttk.Label(main_frame, text="24 hour research").grid(column=2, row=8, sticky=W)
    speed_up_research_5m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[0])
    speed_up_research_5m_entry.grid(column=3, row=0)
    speed_up_research_5m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_research_string_vars[0]))
    speed_up_research_5m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[0]))
    speed_up_research_10m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[1])
    speed_up_research_10m_entry.grid(column=3, row=1)
    speed_up_research_10m_entry.bind('<FocusIn>',
                                     lambda e: entry_selected(speed_up_research_string_vars[1]))
    speed_up_research_10m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[1]))
    speed_up_research_15m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[2])
    speed_up_research_15m_entry.grid(column=3, row=2)
    speed_up_research_15m_entry.bind('<FocusIn>',
                                     lambda e: entry_selected(speed_up_research_string_vars[2]))
    speed_up_research_15m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[2]))
    speed_up_research_30m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[3])
    speed_up_research_30m_entry.grid(column=3, row=3)
    speed_up_research_30m_entry.bind('<FocusIn>',
                                     lambda e: entry_selected(speed_up_research_string_vars[3]))
    speed_up_research_30m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[3]))
    speed_up_research_60m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[4])
    speed_up_research_60m_entry.grid(column=3, row=4)
    speed_up_research_60m_entry.bind('<FocusIn>',
                                     lambda e: entry_selected(speed_up_research_string_vars[4]))
    speed_up_research_60m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[4]))
    speed_up_research_3h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[5])
    speed_up_research_3h_entry.grid(column=3, row=5)
    speed_up_research_3h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_research_string_vars[5]))
    speed_up_research_3h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[5]))
    speed_up_research_8h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[6])
    speed_up_research_8h_entry.grid(column=3, row=6)
    speed_up_research_8h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_research_string_vars[6]))
    speed_up_research_8h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[6]))
    speed_up_research_15h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[7])
    speed_up_research_15h_entry.grid(column=3, row=7)
    speed_up_research_15h_entry.bind('<FocusIn>',
                                     lambda e: entry_selected(speed_up_research_string_vars[7]))
    speed_up_research_15h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[7]))
    speed_up_research_24h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_research_string_vars[8])
    speed_up_research_24h_entry.grid(column=3, row=8)
    speed_up_research_24h_entry.bind('<FocusIn>',
                                     lambda e: entry_selected(speed_up_research_string_vars[8]))
    speed_up_research_24h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_research_string_vars[8]))

    # Init Merging GUI
    ttk.Label(main_frame, text="15 minute merging").grid(column=4, row=0, sticky=W)
    ttk.Label(main_frame, text="60 minute merging").grid(column=4, row=1, sticky=W)
    ttk.Label(main_frame, text="3 hour merging").grid(column=4, row=2, sticky=W)
    ttk.Label(main_frame, text="8 hour merging").grid(column=4, row=3, sticky=W)
    ttk.Label(main_frame, text="15 hour merging").grid(column=4, row=4, sticky=W)
    speed_up_merging_15m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_merging_string_vars[0])
    speed_up_merging_15m_entry.grid(column=5, row=0)
    speed_up_merging_15m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_merging_string_vars[0]))
    speed_up_merging_15m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_merging_string_vars[0]))
    speed_up_merging_60m_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_merging_string_vars[1])
    speed_up_merging_60m_entry.grid(column=5, row=1)
    speed_up_merging_60m_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_merging_string_vars[1]))
    speed_up_merging_60m_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_merging_string_vars[1]))
    speed_up_merging_3h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_merging_string_vars[2])
    speed_up_merging_3h_entry.grid(column=5, row=2)
    speed_up_merging_3h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_merging_string_vars[2]))
    speed_up_merging_3h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_merging_string_vars[2]))
    speed_up_merging_8h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_merging_string_vars[3])
    speed_up_merging_8h_entry.grid(column=5, row=3)
    speed_up_merging_8h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_merging_string_vars[3]))
    speed_up_merging_8h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_merging_string_vars[3]))
    speed_up_merging_15h_entry = ttk.Entry(main_frame, width=4, textvariable=speed_up_merging_string_vars[4])
    speed_up_merging_15h_entry.grid(column=5, row=4)
    speed_up_merging_15h_entry.bind('<FocusIn>', lambda e: entry_selected(speed_up_merging_string_vars[4]))
    speed_up_merging_15h_entry.bind('<FocusOut>', lambda e: entry_deselected(speed_up_merging_string_vars[4]))

    # Init Results GUI
    ttk.Label(main_frame, text="Speed Up Total:").grid(column=0, row=100, sticky=W)
    ttk.Label(main_frame, text="Speed Up Research Total:").grid(column=0, row=101, sticky=W)
    ttk.Label(main_frame, text="Speed Up Merging Total:").grid(column=0, row=102, sticky=W)
    ttk.Label(main_frame, textvariable=results_string_vars[0]).grid(column=1, row=100, sticky=(W, E), columnspan=3)
    ttk.Label(main_frame, textvariable=results_string_vars[1]).grid(column=1, row=101, sticky=(W, E), columnspan=3)
    ttk.Label(main_frame, textvariable=results_string_vars[2]).grid(column=1, row=102, sticky=(W, E), columnspan=3)

    # Enter notes for this dataset
    notes_entry = ttk.Entry(main_frame, width=75, textvariable=data_set_notes_entry_string_var)
    notes_entry.grid(column=0, row=200, columnspan=5, sticky=W)

    # Set Save button
    ttk.Button(main_frame, text="Save to file", command=lambda: save_to_file()).grid(column=5, row=200, sticky=W)

    # Init hotkeys
    root_tk.bind('<Control-s>', lambda x: save_to_file())
    root_tk.bind('<Return>', lambda x: update_totals())

    # Pad everything in the grid
    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    # Set the starting location of the typing cursor
    speed_up_3m_entry.focus()

    # Start the main program loop
    root_tk.mainloop()

    # Done!


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
            print("That didn't work. Try again.")


def format_minutes_to_time(minutes):
    """
    Put in minutes, get back formatted hours + minutes
    :param minutes: The number of minutes to break down
    :return: A string of the hours and minutes in the original value
    """

    hours = minutes // 60
    minutes = minutes % 60
    if hours == 0:
        return str(minutes) + " Minutes"
    if hours < 24:
        return str(hours) + " Hour, " + str(minutes) + " Minutes"
    else:
        days = hours // 24
        hours = hours % 24
        return str(days) + " Days, " + str(hours) + " Hours, " + str(minutes) + " Minutes"


def print_section(section_title, symbol):
    """
    A helper method to print our output to the console in a pretty fashion
    :param section_title:   The name of the section we are printing.
    :param symbol:      The symbol to repetetively print to box in our output. This will usually be a '*'.
    :return:    None
    """
    print("\n" + (symbol * 50) + "\n" + section_title + "\n" + (symbol * 50) + "\n")


def update_totals():
    global results_string_vars
    speed_up_total = 0
    speed_up_total += 3 * int(speed_up_string_vars[0].get())
    speed_up_total += 5 * int(speed_up_string_vars[1].get())
    speed_up_total += 10 * int(speed_up_string_vars[2].get())
    speed_up_total += 15 * int(speed_up_string_vars[3].get())
    speed_up_total += 30 * int(speed_up_string_vars[4].get())
    speed_up_total += 60 * int(speed_up_string_vars[5].get())
    speed_up_total += 180 * int(speed_up_string_vars[6].get())
    speed_up_total += 480 * int(speed_up_string_vars[7].get())
    speed_up_total += 900 * int(speed_up_string_vars[8].get())
    speed_up_total += 1440 * int(speed_up_string_vars[9].get())
    speed_up_total += 4320 * int(speed_up_string_vars[10].get())
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
    results_string_vars[1].set(format_minutes_to_time(speed_up_research_total))

    global speed_up_merging_string_vars
    speed_up_merging_total = 0
    speed_up_merging_total += 15 * int(speed_up_merging_string_vars[0].get())
    speed_up_merging_total += 60 * int(speed_up_merging_string_vars[1].get())
    speed_up_merging_total += 180 * int(speed_up_merging_string_vars[2].get())
    speed_up_merging_total += 480 * int(speed_up_merging_string_vars[3].get())
    speed_up_merging_total += 900 * int(speed_up_merging_string_vars[4].get())
    results_string_vars[2].set(format_minutes_to_time(speed_up_merging_total))


def save_to_file():
    # TODO: Doc this

    fieldnames_for_csv = [
        "Date/Time",
        "Notes",
        "Speed_Up_Total",
        "Speed_Up_Research_Total",
        "Speed_Up_Merging_Total",
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
        "Speed_Up_Research_5m",
        "Speed_Up_Research_10m",
        "Speed_Up_Research_15m",
        "Speed_Up_Research_30m",
        "Speed_Up_Research_60m",
        "Speed_Up_Research_3h",
        "Speed_Up_Research_8h",
        "Speed_Up_Research_15h",
        "Speed_Up_Research_24h",
        "Speed_Up_Merging_15m",
        "Speed_Up_Merging_60m",
        "Speed_Up_Merging_3h",
        "Speed_Up_Merging_8h",
        "Speed_Up_Merging_15h"
    ]

    global speed_up_string_vars
    global speed_up_research_string_vars
    global speed_up_merging_string_vars
    global results_string_vars
    global data_set_notes_entry_string_var

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("LM_boosts.csv", 'a', newline='') as outfile:  # output csv file
        writer = csv.DictWriter(outfile, fieldnames=fieldnames_for_csv)
        writer.writerow({"Date/Time": current_time,
                         "Notes": data_set_notes_entry_string_var.get(),
                         "Speed_Up_Total": results_string_vars[0].get(),
                         "Speed_Up_Research_Total": results_string_vars[1].get(),
                         "Speed_Up_Merging_Total": results_string_vars[2].get(),
                         "Speed_Up_3m": format_minutes_to_time(int(speed_up_string_vars[0].get()) * 3),
                         "Speed_Up_5m": format_minutes_to_time(int(speed_up_string_vars[1].get()) * 5),
                         "Speed_Up_10m": format_minutes_to_time(int(speed_up_string_vars[2].get()) * 10),
                         "Speed_Up_15m": format_minutes_to_time(int(speed_up_string_vars[3].get()) * 15),
                         "Speed_Up_30m": format_minutes_to_time(int(speed_up_string_vars[4].get()) * 30),
                         "Speed_Up_60m": format_minutes_to_time(int(speed_up_string_vars[5].get()) * 60),
                         "Speed_Up_3h": format_minutes_to_time(int(speed_up_string_vars[6].get()) * 180),
                         "Speed_Up_8h": format_minutes_to_time(int(speed_up_string_vars[7].get()) * 480),
                         "Speed_Up_15h": format_minutes_to_time(int(speed_up_string_vars[8].get()) * 900),
                         "Speed_Up_24h": format_minutes_to_time(int(speed_up_string_vars[9].get()) * 1440),
                         "Speed_Up_3d": format_minutes_to_time(int(speed_up_string_vars[10].get()) * 4320),
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
                         "Speed_Up_Merging_15m": format_minutes_to_time(
                             int(speed_up_merging_string_vars[0].get()) * 15),
                         "Speed_Up_Merging_60m": format_minutes_to_time(
                             int(speed_up_merging_string_vars[1].get()) * 60),
                         "Speed_Up_Merging_3h": format_minutes_to_time(
                             int(speed_up_merging_string_vars[2].get()) * 180),
                         "Speed_Up_Merging_8h": format_minutes_to_time(
                             int(speed_up_merging_string_vars[3].get()) * 480),
                         "Speed_Up_Merging_15h": format_minutes_to_time(
                             int(speed_up_merging_string_vars[4].get()) * 900)
                         })

    os.startfile("LM_boosts.csv")


def entry_selected(string_var):
    # TODO: Doc this
    if string_var.get() == '0':
        string_var.set('')


def entry_deselected(string_var):
    # TODO: Doc this
    try:
        i = int(string_var.get())
    except:
        string_var.set(0)

    update_totals()


if __name__ == "__main__":
    main()
