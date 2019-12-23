import logging
import sys
import tkinter
import tkinter.ttk
import tkinter.messagebox
from datetime import datetime
import csv
import os

# NOTE TO USER: use logging.DEBUG for testing, logging.CRITICAL for runtime
logging.basicConfig(stream=sys.stderr,
                    level=logging.CRITICAL)

speed_up_items_count = 14
speed_up_research_items_count = 10
speed_up_merging_items_count = 8

speed_up_string_vars = [None] * speed_up_items_count
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

speed_up_research_string_vars = [None] * speed_up_research_items_count
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

speed_up_merging_string_vars = [None] * speed_up_merging_items_count
"""
[0] = 15m,
[1] = 60m,
[2] = 3h,
[3] = 8h,
[4] = 15h,
[5] = 24h,
[6] = 3d,
[7] = 7d
"""

speed_up_entries = [None] * speed_up_items_count
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

speed_up_research_entries = [None] * speed_up_research_items_count
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

speed_up_merging_entries = [None] * speed_up_merging_items_count
"""
[0] = 15m,
[1] = 60m,
[2] = 3h,
[3] = 8h,
[4] = 15h,
[5] = 24h,
[6] = 3d,
[7] = 7d
"""

frame_1_results_string_vars = [None] * 3
"""
[0] = speed up
[1] = research
[2] = merging
"""

data_set_notes_entry_string_var = None
root_tk = None
notebook = None
frame_1 = None
frame_2 = None

frame_1_file = "LM_boosts.csv"


def init_frame_2():
    pass


def main():
    # Init Tkinter GUI
    global root_tk
    global notebook
    global frame_1
    global frame_2

    root_tk = tkinter.Tk()  # constructor for TK object
    root_tk.title("Lords Mobile Boost Calculator by Vincent Wetzel")

    notebook = tkinter.ttk.Notebook(root_tk)

    frame_1 = tkinter.ttk.Frame(notebook, padding="3 3 12 12")
    frame_1.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
    frame_1.columnconfigure(0, weight=1)
    frame_1.rowconfigure(0, weight=1)

    init_frame_1()

    frame_2 = tkinter.ttk.Frame(notebook, padding="3 3 12 12")
    frame_2.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
    frame_2.columnconfigure(0, weight=1)
    frame_2.rowconfigure(0, weight=1)

    init_frame_2()

    notebook.add(frame_1, text="Page 1")
    notebook.add(frame_2, text="Page 2")
    notebook.grid()

    # Init hotkeys
    root_tk.bind('<Control-s>', lambda x: save_to_file())
    root_tk.bind('<Return>', lambda x: update_frame_1_totals())

    # Start the main program loop
    root_tk.mainloop()
    exit()

    # Done!


def init_frame_1():
    global root_tk
    global frame_1
    # Init Normal Speedups GUI
    tkinter.ttk.Label(frame_1, text="1 minute speedups").grid(column=0, row=0, sticky='W')
    tkinter.ttk.Label(frame_1, text="3 minute speedups").grid(column=0, row=1, sticky='W')
    tkinter.ttk.Label(frame_1, text="5 minute speedups").grid(column=0, row=2, sticky='W')
    tkinter.ttk.Label(frame_1, text="10 minute speedups").grid(column=0, row=3, sticky='W')
    tkinter.ttk.Label(frame_1, text="15 minute speedups").grid(column=0, row=4, sticky='W')
    tkinter.ttk.Label(frame_1, text="30 minute speedups").grid(column=0, row=5, sticky='W')
    tkinter.ttk.Label(frame_1, text="60 minute speedups").grid(column=0, row=6, sticky='W')
    tkinter.ttk.Label(frame_1, text="3 hour speedups").grid(column=0, row=7, sticky='W')
    tkinter.ttk.Label(frame_1, text="8 hour speedups").grid(column=0, row=8, sticky='W')
    tkinter.ttk.Label(frame_1, text="15 hour speedups").grid(column=0, row=9, sticky='W')
    tkinter.ttk.Label(frame_1, text="24 hour speedups").grid(column=0, row=10, sticky='W')
    tkinter.ttk.Label(frame_1, text="3 day speedups").grid(column=0, row=11, sticky='W')
    tkinter.ttk.Label(frame_1, text="7 day speedups").grid(column=0, row=12, sticky='W')
    tkinter.ttk.Label(frame_1, text="30 day speedups").grid(column=0, row=13, sticky='W')

    # Init Research Speedups GUI
    tkinter.ttk.Label(frame_1, text="5 minute research").grid(column=2, row=0, sticky='W')
    tkinter.ttk.Label(frame_1, text="10 minute research").grid(column=2, row=1, sticky='W')
    tkinter.ttk.Label(frame_1, text="15 minute research").grid(column=2, row=2, sticky='W')
    tkinter.ttk.Label(frame_1, text="30 minute research").grid(column=2, row=3, sticky='W')
    tkinter.ttk.Label(frame_1, text="60 minute research").grid(column=2, row=4, sticky='W')
    tkinter.ttk.Label(frame_1, text="3 hour research").grid(column=2, row=5, sticky='W')
    tkinter.ttk.Label(frame_1, text="8 hour research").grid(column=2, row=6, sticky='W')
    tkinter.ttk.Label(frame_1, text="15 hour research").grid(column=2, row=7, sticky='W')
    tkinter.ttk.Label(frame_1, text="24 hour research").grid(column=2, row=8, sticky='W')
    tkinter.ttk.Label(frame_1, text="3 day research").grid(column=2, row=9, sticky='W')

    # Init Merging GUI
    tkinter.ttk.Label(frame_1, text="15 minute merging").grid(column=4, row=0, sticky='W')
    tkinter.ttk.Label(frame_1, text="60 minute merging").grid(column=4, row=1, sticky='W')
    tkinter.ttk.Label(frame_1, text="3 hour merging").grid(column=4, row=2, sticky='W')
    tkinter.ttk.Label(frame_1, text="8 hour merging").grid(column=4, row=3, sticky='W')
    tkinter.ttk.Label(frame_1, text="15 hour merging").grid(column=4, row=4, sticky='W')
    tkinter.ttk.Label(frame_1, text="24 hour merging").grid(column=4, row=5, sticky='W')
    tkinter.ttk.Label(frame_1, text="3 day merging").grid(column=4, row=6, sticky='W')
    tkinter.ttk.Label(frame_1, text="7 day merging").grid(column=4, row=7, sticky='W')

    for i in range(len(frame_1_results_string_vars)):
        frame_1_results_string_vars[i] = tkinter.StringVar(value="0 minutes")

    # Init Main Frame Results GUI
    tkinter.ttk.Label(frame_1, text="Speed Up Total:").grid(column=0, row=100, sticky='W')
    tkinter.ttk.Label(frame_1, text="Speed Up Research Total:").grid(column=0, row=101, sticky='W')
    tkinter.ttk.Label(frame_1, text="Speed Up Merging Total:").grid(column=0, row=102, sticky='W')
    tkinter.ttk.Label(frame_1, textvariable=frame_1_results_string_vars[0]).grid(column=1, row=100,
                                                                                 sticky=('W', 'E'),
                                                                                 columnspan=3)
    tkinter.ttk.Label(frame_1, textvariable=frame_1_results_string_vars[1]).grid(column=1, row=101,
                                                                                 sticky=('W', 'E'),
                                                                                 columnspan=3)
    tkinter.ttk.Label(frame_1, textvariable=frame_1_results_string_vars[2]).grid(column=1, row=102,
                                                                                 sticky=('W', 'E'),
                                                                                 columnspan=3)

    # Init Entries and StringVars for Speed Up, Research Speed Up, and Merging Speed Up
    global speed_up_string_vars
    global speed_up_entries
    for i in range(len(speed_up_string_vars)):
        speed_up_string_vars[i] = tkinter.StringVar(value=0)
        speed_up_entries[i] = tkinter.ttk.Entry(frame_1, width=4, textvariable=speed_up_string_vars[i])
        speed_up_entries[i].grid(column=1, row=i)
        speed_up_entries[i].bind('<FocusIn>', lambda_to_bind_string_var_to_entry_selected(speed_up_string_vars[i]))
        speed_up_entries[i].bind('<FocusOut>', lambda_to_bind_string_var_to_entry_deselected(speed_up_string_vars[i]))
    global speed_up_research_string_vars
    global speed_up_research_entries
    for i in range(len(speed_up_research_string_vars)):
        speed_up_research_string_vars[i] = tkinter.StringVar(value=0)
        speed_up_research_entries[i] = tkinter.ttk.Entry(frame_1, width=4,
                                                         textvariable=speed_up_research_string_vars[i])
        speed_up_research_entries[i].grid(column=3, row=i)
        speed_up_research_entries[i].bind('<FocusIn>',
                                          lambda_to_bind_string_var_to_entry_selected(speed_up_research_string_vars[i]))
        speed_up_research_entries[i].bind('<FocusOut>',
                                          lambda_to_bind_string_var_to_entry_deselected(
                                              speed_up_research_string_vars[i]))
    global speed_up_merging_string_vars
    global speed_up_merging_entries
    for i in range(len(speed_up_merging_string_vars)):
        speed_up_merging_string_vars[i] = tkinter.StringVar(value=0)
        speed_up_merging_entries[i] = tkinter.ttk.Entry(frame_1, width=4,
                                                        textvariable=speed_up_merging_string_vars[i])
        speed_up_merging_entries[i].grid(column=5, row=i)
        speed_up_merging_entries[i].bind('<FocusIn>',
                                         lambda_to_bind_string_var_to_entry_selected(speed_up_merging_string_vars[i]))
        speed_up_merging_entries[i].bind('<FocusOut>',
                                         lambda_to_bind_string_var_to_entry_deselected(speed_up_merging_string_vars[i]))

    global data_set_notes_entry_string_var
    data_set_notes_entry_string_var = tkinter.StringVar()

    # Reset button
    tkinter.ttk.Button(frame_1, text="Reset", command=lambda: reset_all_values()).grid(column=0, row=200,
                                                                                       sticky='W')

    # Enter notes for this dataset
    tkinter.ttk.Label(frame_1, text="Notes:").grid(column=0, row=201, sticky='W', )
    notes_entry = tkinter.ttk.Entry(frame_1, width=75, textvariable=data_set_notes_entry_string_var)
    notes_entry.grid(column=1, row=201, columnspan=4, sticky='W')

    # Set Save button
    tkinter.ttk.Button(frame_1, text="Save to file", command=lambda: save_to_file()).grid(column=5, row=201,
                                                                                          sticky='W')

    # Pad everything in the grid
    for child in frame_1.winfo_children():
        child.grid_configure(padx=5, pady=5)

    # Set the starting location of the typing cursor
    speed_up_entries[0].focus()


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


def update_frame_1_totals():
    """
    This method updates all the running totals and then updates the GUI
    :return:    None
    """
    try:
        global frame_1_results_string_vars
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
        frame_1_results_string_vars[0].set(format_minutes_to_time(speed_up_total))

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
        frame_1_results_string_vars[1].set(format_minutes_to_time(speed_up_research_total))

        global speed_up_merging_string_vars
        speed_up_merging_total = 0
        speed_up_merging_total += 15 * int(speed_up_merging_string_vars[0].get())
        speed_up_merging_total += 60 * int(speed_up_merging_string_vars[1].get())
        speed_up_merging_total += 180 * int(speed_up_merging_string_vars[2].get())
        speed_up_merging_total += 480 * int(speed_up_merging_string_vars[3].get())
        speed_up_merging_total += 900 * int(speed_up_merging_string_vars[4].get())
        speed_up_merging_total += 1440 * int(speed_up_merging_string_vars[5].get())
        speed_up_merging_total += 4320 * int(speed_up_merging_string_vars[6].get())
        speed_up_merging_total += 10080 * int(speed_up_merging_string_vars[7].get())
        frame_1_results_string_vars[2].set(format_minutes_to_time(speed_up_merging_total))
    except ValueError:
        # Do not update, there was an error
        return


def save_to_file(confirm_save=False):
    """
    Saves the data to an output file.
    :return:    None
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    global notebook
    if notebook.index(notebook.select()) == 0:
        if confirm_save or tkinter.messagebox.askyesno(title="Save to File", message="Do you want to save this data?"):

            fieldnames_for_csv = [
                "Date/Time",
                "Notes",
                "Speed_Up_Total",
                "Speed_Up_Research_Total",
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
            global speed_up_merging_string_vars
            global frame_1_results_string_vars
            global data_set_notes_entry_string_var
            global frame_1_file

            try:
                # If the file doesn't exist, create it
                if not os.path.exists(frame_1_file):
                    with open(frame_1_file, 'w', newline='') as fnew:
                        writer = csv.DictWriter(fnew, fieldnames=fieldnames_for_csv)
                        writer.writeheader()

                # Append the current set of data to the file
                with open(frame_1_file, 'a', newline='') as outfile:  # output csv file
                    # Make sure there are no blank strings (focused Entry) that will cause errors
                    for count, x in enumerate(speed_up_string_vars):
                        if speed_up_string_vars[count].get() == "":
                            speed_up_string_vars[count].set(0)
                    for count, x in enumerate(speed_up_research_string_vars):
                        if speed_up_research_string_vars[count].get() == "":
                            speed_up_research_string_vars[count].set(0)
                    for count, x in enumerate(speed_up_merging_string_vars):
                        if speed_up_merging_string_vars[count].get() == "":
                            speed_up_merging_string_vars[count].set(0)
                    # Open outfile
                    writer = csv.DictWriter(outfile, fieldnames=fieldnames_for_csv)

                    # Write to outfile
                    writer.writerow({"Date/Time": current_time,
                                     "Notes": data_set_notes_entry_string_var.get(),
                                     "Speed_Up_Total": frame_1_results_string_vars[0].get(),
                                     "Speed_Up_Research_Total": frame_1_results_string_vars[1].get(),
                                     "Speed_Up_Merging_Total": frame_1_results_string_vars[2].get(),
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
                                     "Speed_Up_Merging_15m": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[0].get()) * 15),
                                     "Speed_Up_Merging_60m": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[1].get()) * 60),
                                     "Speed_Up_Merging_3h": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[2].get()) * 180),
                                     "Speed_Up_Merging_8h": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[3].get()) * 480),
                                     "Speed_Up_Merging_15h": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[4].get()) * 900),
                                     "Speed_Up_Merging_24h": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[5].get()) * 1440),
                                     "Speed_Up_Merging_3d": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[6].get()) * 4320),
                                     "Speed_Up_Merging_7d": format_minutes_to_time(
                                         int(speed_up_merging_string_vars[4].get()) * 10080)
                                     })
                if tkinter.messagebox.askyesno(title="Would you like to open the file?",
                                               message="The file has been saved. Would you like to open it?"):
                    os.startfile(frame_1_file)
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

    update_frame_1_totals()


def reset_all_values():
    """
    Resets all values back to 0.
    """
    global speed_up_string_vars
    global speed_up_research_string_vars
    global speed_up_merging_string_vars

    for i in range(len(speed_up_string_vars)):
        speed_up_string_vars[i].set(0)

    for i in range(len(speed_up_research_string_vars)):
        speed_up_research_string_vars[i].set(0)

    for i in range(len(speed_up_merging_string_vars)):
        speed_up_merging_string_vars[i].set(0)

    update_frame_1_totals()


if __name__ == "__main__":
    main()
