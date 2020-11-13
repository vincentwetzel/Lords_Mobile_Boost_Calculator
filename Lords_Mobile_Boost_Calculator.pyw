#! /usr/bin/env python3

import logging
import sys
import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.filedialog
from PIL import ImageTk, Image
import os
import pandas
from datetime import datetime
from typing import List
from collections import OrderedDict

# NOTE TO USER: use logging.DEBUG for testing, logging.CRITICAL for runtime
from sys import platform

if platform == "win32":
    from win32com.client import Dispatch

logging.basicConfig(stream=sys.stderr,
                    level=logging.CRITICAL)


class LordsMobileCalculator:

    def __init__(self):

        # Init Tkinter GUI
        self.root_tk = tkinter.Tk()  # constructor for TK object
        self.root_tk.title("Lords Mobile Boost Calculator by Vincent Wetzel")
        self.root_tk.geometry("700x800")
        self.inputs_frame = tkinter.ttk.Frame(self.root_tk).grid(row=0, column=0)
        self.results_frame = tkinter.ttk.Frame(self.root_tk).grid(row=1, column=0)

        self.results_string_vars: List[tkinter.StringVar] = list()
        """[0] = speed up
        [1] = research
        [2] = wall repair
        [3] = healing
        [4] = training
        [5] = merging
        """

        self.speed_up_string_vars: List[tkinter.StringVar] = list()
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

        self.speed_up_research_string_vars: List[tkinter.StringVar] = list()
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

        self.speed_up_merging_string_vars: List[tkinter.StringVar] = list()
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

        self.speed_up_wall_repair_string_vars: List[tkinter.StringVar] = list()
        """
        [0] = 15m
        [1] = 60m,
        [2] = 3h,
        [3] = 8h,
        [4] = 24h
        """

        self.speed_up_healing_string_vars: List[tkinter.StringVar] = list()
        """
        [0] = 5m,
        [1] = 15m
        [2] = 60m,
        [3] = 3h,
        [4] = 8h,
        """

        self.speed_up_training_string_vars: List[tkinter.StringVar] = list()
        """
        [0] = 10m
        [1] = 30m,
        [2] = 60m,
        [3] = 3h,
        [4] = 8h,
        [5] = 15h,
        [6] = 24h,
        [7] = 3d
        """

        self.speed_up_entries: List[tkinter.Entry] = list()
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

        self.speed_up_research_entries: List[tkinter.Entry] = list()
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

        self.speed_up_merging_entries: List[tkinter.Entry] = list()
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

        self.speed_up_wall_repair_entries: List[tkinter.Entry] = list()
        """
        [0] = 15m
        [1] = 60m,
        [2] = 3h,
        [3] = 8h,
        [4] = 24h
        """

        self.speed_up_healing_entries: List[tkinter.Entry] = list()
        """
        [0] = 5m,
        [1] = 15m
        [2] = 60m,
        [3] = 3h,
        [4] = 8h,
        """

        self.speed_up_training_entries: List[tkinter.Entry] = list()
        """
        [0] = 10m
        [1] = 30m,
        [2] = 60m,
        [3] = 3h,
        [4] = 8h,
        [5] = 15h,
        [6] = 24h,
        [7] = 3d
        """

        self.speed_up_labels: List[tkinter.Label] = list()
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

        self.speed_up_research_labels: List[tkinter.Label] = list()
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

        self.speed_up_merging_labels: List[tkinter.Label] = list()
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

        self.speed_up_wall_repair_labels: List[tkinter.Label] = list()
        """
        [0] = 15m
        [1] = 60m,
        [2] = 3h,
        [3] = 8h,
        [4] = 24h
        """

        self.speed_up_healing_labels: List[tkinter.Label] = list()
        """
        [0] = 5m,
        [1] = 15m
        [2] = 60m,
        [3] = 3h,
        [4] = 8h,
        """

        self.speed_up_training_labels: List[tkinter.Label] = list()
        """
        [0] = 10m
        [1] = 30m,
        [2] = 60m,
        [3] = 3h,
        [4] = 8h,
        [5] = 15h,
        [6] = 24h,
        [7] = 3d
        """

        self.speed_up_tk_images: List[tkinter.PhotoImage] = list()
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

        self.speed_up_research_tk_images: List[tkinter.PhotoImage] = list()
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

        self.speed_up_merging_tk_images: List[tkinter.PhotoImage] = list()
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

        self.speed_up_wall_repair_tk_images: List[tkinter.PhotoImage] = list()
        """
        [0] = 1m
        [1] = 60m,
        [2] = 3h,
        [3] = 8h,
        [4] = 24h
        """

        self.speed_up_healing_tk_images: List[tkinter.PhotoImage] = list()
        """
        [0] = 5m,
        [1] = 15m
        [2] = 60m,
        [3] = 3h,
        [4] = 8h,
        """

        self.speed_up_training_tk_images: List[tkinter.PhotoImage] = list()
        """
        [0] = 10m
        [1] = 30m,
        [2] = 60m,
        [3] = 3h,
        [4] = 8h,
        [5] = 15h,
        [6] = 24h,
        [7] = 3d
        """

        self.speed_up_image_locations: List[str] = [
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

        self.speed_up_research_image_locations: List[str] = [
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

        self.speed_up_merging_image_locations: List[str] = [
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

        self.speed_up_wall_repair_image_locations: List[str] = [
            "assets/speed_up_wall_repair/speed_up_wall_repair_15m.png",
            "assets/speed_up_wall_repair/speed_up_wall_repair_60m.png",
            "assets/speed_up_wall_repair/speed_up_wall_repair_3h.png",
            "assets/speed_up_wall_repair/speed_up_wall_repair_8h.png",
            "assets/speed_up_wall_repair/speed_up_wall_repair_24h.png"
        ]

        self.speed_up_healing_image_locations: List[str] = [
            "assets/speed_up_healing/speed_up_healing_5m.png",
            "assets/speed_up_healing/speed_up_healing_15m.png",
            "assets/speed_up_healing/speed_up_healing_60m.png",
            "assets/speed_up_healing/speed_up_healing_3h.png",
            "assets/speed_up_healing/speed_up_healing_8h.png"
        ]

        self.speed_up_training_image_locations: List[str] = [
            "assets/speed_up_training/speed_up_training_10m.png",
            "assets/speed_up_training/speed_up_training_30m.png",
            "assets/speed_up_training/speed_up_training_60m.png",
            "assets/speed_up_training/speed_up_training_3h.png",
            "assets/speed_up_training/speed_up_training_8h.png",
            "assets/speed_up_training/speed_up_training_15h.png",
            "assets/speed_up_training/speed_up_training_24h.png",
            "assets/speed_up_training/speed_up_training_3d.png",
        ]

        self.SPEED_UP_ITEMS_COUNT: int = 14
        self.SPEED_UP_RESEARCH_ITEMS_COUNT: int = 10
        self.SPEED_UP_WALL_REPAIR_COUNT: int = 5
        self.SPEED_UP_HEALING_COUNT: int = 5
        self.SPEED_UP_TRAINING_COUNT: int = 8
        self.SPEED_UP_MERGING_ITEMS_COUNT: int = 9

        self.TABS_COUNT: int = 6
        self.IMG_SCALE: int = 50

        self.labels: List[List[tkinter.Label]] = [self.speed_up_labels, self.speed_up_research_labels,
                                                  self.speed_up_wall_repair_labels,
                                                  self.speed_up_healing_labels, self.speed_up_training_labels,
                                                  self.speed_up_merging_labels]
        self.tk_images: List[List[tkinter.PhotoImage]] = [self.speed_up_tk_images, self.speed_up_research_tk_images,
                                                          self.speed_up_wall_repair_tk_images,
                                                          self.speed_up_healing_tk_images,
                                                          self.speed_up_training_tk_images,
                                                          self.speed_up_merging_tk_images]
        self.image_locations: List[List[str]] = [self.speed_up_image_locations, self.speed_up_research_image_locations,
                                                 self.speed_up_wall_repair_image_locations,
                                                 self.speed_up_healing_image_locations,
                                                 self.speed_up_training_image_locations,
                                                 self.speed_up_merging_image_locations]
        self.string_vars: List[List[tkinter.StringVar]] = [self.speed_up_string_vars,
                                                           self.speed_up_research_string_vars,
                                                           self.speed_up_wall_repair_string_vars,
                                                           self.speed_up_healing_string_vars,
                                                           self.speed_up_training_string_vars,
                                                           self.speed_up_merging_string_vars]
        self.entries: List[List[tkinter.Entry]] = [self.speed_up_entries, self.speed_up_research_entries,
                                                   self.speed_up_wall_repair_entries,
                                                   self.speed_up_healing_entries, self.speed_up_training_entries,
                                                   self.speed_up_merging_entries]
        self.counter_constants_list: List[int] = [self.SPEED_UP_ITEMS_COUNT, self.SPEED_UP_RESEARCH_ITEMS_COUNT,
                                                  self.SPEED_UP_WALL_REPAIR_COUNT,
                                                  self.SPEED_UP_HEALING_COUNT, self.SPEED_UP_TRAINING_COUNT,
                                                  self.SPEED_UP_MERGING_ITEMS_COUNT]

        self.notebook: tkinter.ttk.Notebook = tkinter.ttk.Notebook(master=self.inputs_frame)
        self.tk_frames: List[tkinter.Frame] = list()

        self.save_notes_entry_string_var: tkinter.StringVar = tkinter.StringVar()

        for tab in range(self.TABS_COUNT):
            self.tk_frames.append(tkinter.ttk.Frame(self.notebook, padding="3 3 12 12"))

        self.notebook.add(self.tk_frames[0], text="Speed Up")
        self.notebook.add(self.tk_frames[1], text="Research")
        self.notebook.add(self.tk_frames[2], text="Wall Repair")
        self.notebook.add(self.tk_frames[3], text="Healing")
        self.notebook.add(self.tk_frames[4], text="Training")
        self.notebook.add(self.tk_frames[5], text="Merging")

        self.notebook.grid(row=0, column=0, sticky=tkinter.W, columnspan=5)
        self.notebook.enable_traversal()  # Allows CTRL + Tab

        for result_str in range(self.TABS_COUNT):
            self.results_string_vars.append(tkinter.StringVar(value="0 minutes"))

        # Init Frames
        for curr_tab_counter in range(self.TABS_COUNT):
            self.init_frame(curr_tab_counter, self.tk_frames[curr_tab_counter],
                            self.counter_constants_list[curr_tab_counter],
                            self.labels[curr_tab_counter], self.tk_images[curr_tab_counter],
                            self.image_locations[curr_tab_counter],
                            self.string_vars[curr_tab_counter], self.entries[curr_tab_counter])

        # Button to reset all Calculator Entries
        tkinter.ttk.Button(self.results_frame, text="Reset All",
                           command=lambda: self.reset_all_values()).grid(column=0, row=99,
                                                                         sticky='W')

        # Init Main Frame Results GUI
        tkinter.ttk.Label(self.results_frame, text="Speed Up Total:").grid(column=0, row=100, sticky='W',
                                                                           columnspan=1)
        tkinter.ttk.Label(self.results_frame, text="Speed Up Research Total:").grid(column=0, row=101,
                                                                                    sticky='W', columnspan=1)
        tkinter.ttk.Label(self.results_frame, text="Speed Up Wall Repair Total:").grid(column=0, row=102, sticky='W',
                                                                                       columnspan=1)
        tkinter.ttk.Label(self.results_frame, text="Speed Up Healing Total:").grid(column=0, row=103, sticky='W',
                                                                                   columnspan=1)

        tkinter.ttk.Label(self.results_frame, text="Speed Up Training Total:").grid(column=0, row=104, sticky='W',
                                                                                    columnspan=1)
        tkinter.ttk.Label(self.results_frame, text="Speed Up Merging Total:").grid(column=0, row=105, sticky='W',
                                                                                   columnspan=1)
        tkinter.ttk.Label(self.results_frame, textvariable=self.results_string_vars[0]).grid(column=1, row=100,
                                                                                             sticky=('W', 'E'),
                                                                                             columnspan=1)
        tkinter.ttk.Label(self.results_frame, textvariable=self.results_string_vars[1]).grid(column=1, row=101,
                                                                                             sticky=('W', 'E'),
                                                                                             columnspan=1)
        tkinter.ttk.Label(self.results_frame, textvariable=self.results_string_vars[2]).grid(column=1, row=102,
                                                                                             sticky=('W', 'E'),
                                                                                             columnspan=1)
        tkinter.ttk.Label(self.results_frame, textvariable=self.results_string_vars[3]).grid(column=1, row=103,
                                                                                             sticky=('W', 'E'),
                                                                                             columnspan=1)
        tkinter.ttk.Label(self.results_frame, textvariable=self.results_string_vars[4]).grid(column=1, row=104,
                                                                                             sticky=('W', 'E'),
                                                                                             columnspan=1)
        tkinter.ttk.Label(self.results_frame, textvariable=self.results_string_vars[5]).grid(column=1, row=105,
                                                                                             sticky=('W', 'E'),
                                                                                             columnspan=1)

        # Enter notes for this dataset
        tkinter.ttk.Label(self.results_frame, text="Notes:").grid(column=0, row=201, sticky='W', )
        notes_entry = tkinter.ttk.Entry(self.results_frame, width=45,
                                        textvariable=self.save_notes_entry_string_var)
        notes_entry.grid(column=1, row=201, columnspan=1, sticky='W')

        # Set Save button
        tkinter.ttk.Button(self.results_frame, text="Save to file", command=lambda: self.save_to_file()).grid(
            column=4, row=201,
            sticky='W')

        # Set the starting location of the typing cursor
        self.speed_up_entries[0].focus()

        # Init hotkeys
        self.root_tk.bind_all('<Control-s>', lambda x: self.save_to_file())
        self.root_tk.bind_all('<Return>', lambda x: self.update_totals())

        # Start the main program loop
        self.root_tk.mainloop()
        exit()

        # End Script!

    def init_frame(self, frame_idx: int, current_frame: tkinter.Frame, counters_param: int,
                   labels_list: List[tkinter.Label],
                   tk_images_list: List[tkinter.PhotoImage], image_locations_list,
                   string_vars_list: List[tkinter.StringVar],
                   entries_list: List[tkinter.Entry]):
        """
        Initializes a tkinter Frame object for the calculator.
        :param frame_idx: The index of the frame being created. All frames are stored in a list.
        :param current_frame: The Frame Object we are currently initializing.
        :param counters_param: Controls how many calculator fields exist in this frame.
        :param labels_list: A list to hold Labels will ultimately hold pictures.
        :param tk_images_list: A list to hold ImageTK Objects. These are then put onto Labels.
        :param image_locations_list: A list image files that will be used to create ImageTK objects.
        :param string_vars_list: A list to hold StringVar Objects associated with Entry fields in this calculator.
        :param entries_list: A list to hold Entry Objects for the user to interact with the calculator.
        :return:
        """

        # Init Labels and put Images on them
        for label_counter in range(counters_param):
            # Open then resize the image object
            image = Image.open(image_locations_list[label_counter])
            image = image.resize((self.IMG_SCALE, self.IMG_SCALE), Image.ANTIALIAS)
            tk_images_list.append(ImageTk.PhotoImage(image))

            # Create a Label and display the image in the grid
            labels_list.append(
                tkinter.ttk.Label(current_frame, image=tk_images_list[label_counter], padding="3 3 12 12"))
            labels_list[label_counter].grid(column=0 if (label_counter < counters_param / 2) else 2,
                                            row=label_counter if (
                                                    label_counter < counters_param / 2) else label_counter - (
                                                    counters_param // 2) - (0 if counters_param % 2 == 0 else 1),
                                            sticky='W')

        # Init Entries
        for entry_counter in range(counters_param):
            string_vars_list.append(tkinter.StringVar(value=0))
            entries_list.append(
                tkinter.ttk.Entry(current_frame, width=4, textvariable=string_vars_list[entry_counter]))
            entries_list[entry_counter].grid(column=1 if (entry_counter < counters_param / 2) else 3,
                                             row=entry_counter if (
                                                     entry_counter < counters_param / 2) else entry_counter - (
                                                     counters_param // 2) - (0 if counters_param % 2 == 0 else 1),
                                             sticky='W')
            entries_list[entry_counter].bind('<FocusIn>',
                                             self.lambda_to_bind_string_var_to_entry_selected(
                                                 string_vars_list[entry_counter]))
            entries_list[entry_counter].bind('<FocusOut>',
                                             self.lambda_to_bind_string_var_to_entry_deselected(
                                                 string_vars_list[entry_counter]))

        # Reset buttons
        tkinter.ttk.Button(current_frame, text="Reset",
                           command=lambda: self.reset_all_values_in_frame(frame_idx)).grid(column=0, row=200,
                                                                                           sticky='W')

    @staticmethod
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

    def update_totals(self):
        """
        This method updates all the running totals and then updates the GUI
        :return:    None
        """
        try:
            speed_up_total = 0
            speed_up_total += 1 * int(self.speed_up_string_vars[0].get())
            speed_up_total += 3 * int(self.speed_up_string_vars[1].get())
            speed_up_total += 5 * int(self.speed_up_string_vars[2].get())
            speed_up_total += 10 * int(self.speed_up_string_vars[3].get())
            speed_up_total += 15 * int(self.speed_up_string_vars[4].get())
            speed_up_total += 30 * int(self.speed_up_string_vars[5].get())
            speed_up_total += 60 * int(self.speed_up_string_vars[6].get())
            speed_up_total += 180 * int(self.speed_up_string_vars[7].get())
            speed_up_total += 480 * int(self.speed_up_string_vars[8].get())
            speed_up_total += 900 * int(self.speed_up_string_vars[9].get())
            speed_up_total += 1440 * int(self.speed_up_string_vars[10].get())
            speed_up_total += 4320 * int(self.speed_up_string_vars[11].get())
            speed_up_total += 10080 * int(self.speed_up_string_vars[12].get())
            speed_up_total += 43200 * int(self.speed_up_string_vars[13].get())
            self.results_string_vars[0].set(self.format_minutes_to_time(speed_up_total))

            speed_up_research_total = 0
            speed_up_research_total += 5 * int(self.speed_up_research_string_vars[0].get())
            speed_up_research_total += 10 * int(self.speed_up_research_string_vars[1].get())
            speed_up_research_total += 15 * int(self.speed_up_research_string_vars[2].get())
            speed_up_research_total += 30 * int(self.speed_up_research_string_vars[3].get())
            speed_up_research_total += 60 * int(self.speed_up_research_string_vars[4].get())
            speed_up_research_total += 180 * int(self.speed_up_research_string_vars[5].get())
            speed_up_research_total += 480 * int(self.speed_up_research_string_vars[6].get())
            speed_up_research_total += 900 * int(self.speed_up_research_string_vars[7].get())
            speed_up_research_total += 1440 * int(self.speed_up_research_string_vars[8].get())
            speed_up_research_total += 4320 * int(self.speed_up_research_string_vars[9].get())
            self.results_string_vars[1].set(self.format_minutes_to_time(speed_up_research_total))

            speed_up_wall_repair_total = 0
            speed_up_wall_repair_total += 15 * int(self.speed_up_wall_repair_string_vars[0].get())
            speed_up_wall_repair_total += 60 * int(self.speed_up_wall_repair_string_vars[1].get())
            speed_up_wall_repair_total += 180 * int(self.speed_up_wall_repair_string_vars[2].get())
            speed_up_wall_repair_total += 480 * int(self.speed_up_wall_repair_string_vars[3].get())
            speed_up_wall_repair_total += 1440 * int(self.speed_up_wall_repair_string_vars[4].get())
            self.results_string_vars[2].set(self.format_minutes_to_time(speed_up_wall_repair_total))

            speed_up_healing_total = 0
            speed_up_healing_total += 5 * int(self.speed_up_healing_string_vars[0].get())
            speed_up_healing_total += 15 * int(self.speed_up_healing_string_vars[0].get())
            speed_up_healing_total += 60 * int(self.speed_up_healing_string_vars[1].get())
            speed_up_healing_total += 180 * int(self.speed_up_healing_string_vars[2].get())
            speed_up_healing_total += 480 * int(self.speed_up_healing_string_vars[3].get())
            self.results_string_vars[3].set(self.format_minutes_to_time(speed_up_healing_total))

            speed_up_training_total = 0
            speed_up_training_total += 10 * int(self.speed_up_training_string_vars[0].get())
            speed_up_training_total += 30 * int(self.speed_up_training_string_vars[1].get())
            speed_up_training_total += 60 * int(self.speed_up_training_string_vars[2].get())
            speed_up_training_total += 180 * int(self.speed_up_training_string_vars[3].get())
            speed_up_training_total += 480 * int(self.speed_up_training_string_vars[4].get())
            speed_up_training_total += 900 * int(self.speed_up_training_string_vars[5].get())
            speed_up_training_total += 1440 * int(self.speed_up_training_string_vars[6].get())
            speed_up_training_total += 4320 * int(self.speed_up_training_string_vars[7].get())
            self.results_string_vars[4].set(self.format_minutes_to_time(speed_up_training_total))

            speed_up_merging_total = 0
            speed_up_merging_total += 1 * int(self.speed_up_merging_string_vars[0].get())
            speed_up_merging_total += 15 * int(self.speed_up_merging_string_vars[1].get())
            speed_up_merging_total += 60 * int(self.speed_up_merging_string_vars[2].get())
            speed_up_merging_total += 180 * int(self.speed_up_merging_string_vars[3].get())
            speed_up_merging_total += 480 * int(self.speed_up_merging_string_vars[4].get())
            speed_up_merging_total += 900 * int(self.speed_up_merging_string_vars[5].get())
            speed_up_merging_total += 1440 * int(self.speed_up_merging_string_vars[6].get())
            speed_up_merging_total += 4320 * int(self.speed_up_merging_string_vars[7].get())
            speed_up_merging_total += 10080 * int(self.speed_up_merging_string_vars[8].get())
            self.results_string_vars[5].set(self.format_minutes_to_time(speed_up_merging_total))

        except ValueError:
            # Do not update, an error was probably caused by an empty Entry field.
            return

    def lambda_to_bind_string_var_to_entry_selected(self, string_var_to_bind_to_entry):
        return lambda x: self.entry_selected(string_var_to_bind_to_entry)

    def lambda_to_bind_string_var_to_entry_deselected(self, string_var_to_bind_to_entry):
        return lambda x: self.entry_deselected(string_var_to_bind_to_entry)

    # noinspection PyMethodMayBeStatic
    def entry_selected(self, string_var: tkinter.StringVar) -> None:
        """
        If an entry box is clicked and the current StringVar value of the box is 0, clear the box.
        :rtype: None
        :param string_var: The string to evaluate
        """
        if string_var.get() == '0':
            string_var.set('')

    def entry_deselected(self, string_var) -> None:
        """
        If an entry box is deselected without a value being entered in it, set the StringVar to 0.
        :rtype: None
        """
        try:
            # Make sure the value entered is an int
            int(string_var.get())
        except ValueError:
            string_var.set(0)

        self.update_totals()

    def reset_all_values_in_frame(self, frame_number):
        """
        Resets all values back to 0.
        """

        for i in range(self.counter_constants_list[frame_number]):
            self.string_vars[frame_number][i].set(0)

        self.update_totals()

    def reset_all_values(self):
        for i in range(len(self.speed_up_string_vars)):
            self.speed_up_string_vars[i].set(0)

        for i in range(len(self.speed_up_research_string_vars)):
            self.speed_up_research_string_vars[i].set(0)

        for i in range(len(self.speed_up_wall_repair_string_vars)):
            self.speed_up_wall_repair_string_vars[i].set(0)

        for i in range(len(self.speed_up_healing_string_vars)):
            self.speed_up_healing_string_vars[i].set(0)

        for i in range(len(self.speed_up_training_string_vars)):
            self.speed_up_training_string_vars[i].set(0)

        for i in range(len(self.speed_up_merging_string_vars)):
            self.speed_up_merging_string_vars[i].set(0)

        self.update_totals()

    def save_to_file(self):
        """
        Saves the data to an output file.
        :return:    None
        """
        save_file = None
        try:
            save_file = open("settings.ini", 'r').readline().strip().split("save_file=")[1]
        except (FileNotFoundError, IndexError):
            save_file = tkinter.filedialog.asksaveasfilename(title="Save File", defaultextension='xlsx',
                                                             filetypes=[("Excel Workbook", ".xlsx")])
            if save_file == "":
                return
            else:
                print("save_file=" + str(save_file))
                with open('settings.ini', 'w') as settings_file:
                    settings_file.write("save_file=" + save_file)

        # Confirm the save file name
        while True:
            save_confirm = tkinter.messagebox.askyesnocancel(title="Save File",
                                                             message="Would you like to save this file as: "
                                                                     + save_file + "?")
            if save_confirm:
                # "Yes" response, save the file to default value
                break
            elif not save_confirm:
                # "No" response, rename file
                save_file = tkinter.filedialog.asksaveasfilename(title="Save File", defaultextension='xslx',
                                                                 filetypes=[
                                                                     ("Excel Workbook", ".xlsx")])
                with open('settings.ini', 'w') as settings_file:
                    settings_file.write("save_file=" + save_file)
            elif save_confirm is None:
                # Cancelled or dialogue window closed
                return

        main_df = None
        if os.path.exists(os.path.realpath(save_file)):
            main_df = pandas.read_excel(save_file)
        else:
            main_df = pandas.DataFrame()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        output_df = pandas.DataFrame(OrderedDict((("Date/Time", pandas.Series(current_time)),
                                                  ("Notes", pandas.Series(self.save_notes_entry_string_var.get())),
                                                  ("Speed_Up_Total",
                                                   pandas.Series(self.results_string_vars[0].get())),
                                                  ("Speed_Up_Research_Total",
                                                   pandas.Series(self.results_string_vars[1].get())),
                                                  ("Speed_Up_Wall_Repair_Total",
                                                   pandas.Series(self.results_string_vars[2].get())),
                                                  ("Speed_Up_Healing_Total",
                                                   pandas.Series(self.results_string_vars[3].get())),
                                                  ("Speed_Up_Training_Total",
                                                   pandas.Series(self.results_string_vars[4].get())),
                                                  ("Speed_Up_Merging_Total",
                                                   pandas.Series(self.results_string_vars[5].get())),

                                                  ("Speed_Up_1m", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[0].get()) * 1))),
                                                  ("Speed_Up_3m", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[1].get()) * 3))),
                                                  ("Speed_Up_5m", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[2].get()) * 5))),
                                                  ("Speed_Up_10m", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[3].get()) * 10))),
                                                  ("Speed_Up_15m", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[4].get()) * 15))),
                                                  ("Speed_Up_30m", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[5].get()) * 30))),
                                                  ("Speed_Up_60m", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[6].get()) * 60))),
                                                  ("Speed_Up_3h", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[7].get()) * 180))),
                                                  ("Speed_Up_8h", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[8].get()) * 480))),
                                                  ("Speed_Up_15h", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[9].get()) * 900))),
                                                  ("Speed_Up_24h", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[10].get()) * 1440))),
                                                  ("Speed_Up_3d", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[11].get()) * 4320))),
                                                  ("Speed_Up_7d", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[12].get()) * 10080))),
                                                  ("Speed_Up_30d", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_string_vars[13].get()) * 43200))),

                                                  (
                                                      "Speed_Up_Research_5m",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_research_string_vars[0].get()) * 5))),
                                                  ("Speed_Up_Research_10m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_research_string_vars[1].get()) * 10))),
                                                  ("Speed_Up_Research_15m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_research_string_vars[2].get()) * 15))),
                                                  ("Speed_Up_Research_30m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_research_string_vars[3].get()) * 30))),
                                                  ("Speed_Up_Research_60m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_research_string_vars[4].get()) * 60))),
                                                  (
                                                      "Speed_Up_Research_3h",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_research_string_vars[5].get()) * 180))),
                                                  (
                                                      "Speed_Up_Research_8h",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_research_string_vars[6].get()) * 480))),
                                                  ("Speed_Up_Research_15h",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_research_string_vars[7].get()) * 900))),
                                                  ("Speed_Up_Research_24h",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_research_string_vars[8].get()) * 1440))),
                                                  (
                                                      "Speed_Up_Research_3d",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_research_string_vars[
                                                                  9].get()) * 4320))),

                                                  ("Speed_Up_Wall_Repair_15m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_wall_repair_string_vars[0].get()) * 15))),
                                                  ("Speed_Up_Wall_Repair_60m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_wall_repair_string_vars[1].get()) * 60))),
                                                  ("Speed_Up_Wall_Repair_3h",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_wall_repair_string_vars[2].get()) * 180))),
                                                  ("Speed_Up_Wall_Repair_8h",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_wall_repair_string_vars[3].get()) * 480))),
                                                  ("Speed_Up_Wall_Repair_24h",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_wall_repair_string_vars[
                                                               4].get()) * 1440))),
                                                  (
                                                      "Speed_Up_Healing_5m",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_healing_string_vars[0].get()) * 15))),

                                                  (
                                                      "Speed_Up_Healing_15m",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_healing_string_vars[0].get()) * 15))),
                                                  (
                                                      "Speed_Up_Healing_60m",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_healing_string_vars[1].get()) * 60))),
                                                  ("Speed_Up_Healing_3h", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_healing_string_vars[2].get()) * 180))),
                                                  ("Speed_Up_Healing_8h", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_healing_string_vars[3].get()) * 480))),

                                                  ("Speed_Up_Training_10m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_training_string_vars[0].get()) * 10))),
                                                  ("Speed_Up_Training_30m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_training_string_vars[1].get()) * 30))),
                                                  ("Speed_Up_Training_60m",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_training_string_vars[2].get()) * 60))),
                                                  (
                                                      "Speed_Up_Training_3h",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_training_string_vars[3].get()) * 180))),
                                                  (
                                                      "Speed_Up_Training_8h",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_training_string_vars[4].get()) * 480))),
                                                  ("Speed_Up_Training_15h",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_training_string_vars[5].get()) * 900))),
                                                  ("Speed_Up_Training_24h",
                                                   pandas.Series(self.format_minutes_to_time(
                                                       int(self.speed_up_training_string_vars[6].get()) * 1440))),
                                                  (
                                                      "Speed_Up_Training_3d",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_training_string_vars[
                                                                  7].get()) * 4320))),

                                                  ("Speed_Up_Merging_1m", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_merging_string_vars[0].get()) * 1))),
                                                  (
                                                      "Speed_Up_Merging_15m",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_merging_string_vars[1].get()) * 15))),
                                                  (
                                                      "Speed_Up_Merging_60m",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_merging_string_vars[2].get()) * 60))),
                                                  ("Speed_Up_Merging_3h", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_merging_string_vars[3].get()) * 180))),
                                                  ("Speed_Up_Merging_8h", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_merging_string_vars[4].get()) * 480))),
                                                  (
                                                      "Speed_Up_Merging_15h",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_merging_string_vars[5].get()) * 900))),
                                                  (
                                                      "Speed_Up_Merging_24h",
                                                      pandas.Series(self.format_minutes_to_time(
                                                          int(self.speed_up_merging_string_vars[6].get()) * 1440))),
                                                  ("Speed_Up_Merging_3d", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_merging_string_vars[7].get()) * 4320))),
                                                  ("Speed_Up_Merging_7d", pandas.Series(self.format_minutes_to_time(
                                                      int(self.speed_up_merging_string_vars[8].get()) * 10080)))
                                                  )))

        # Merge the new data into the existing dataframe that olds all my old data
        main_df = main_df.append(output_df, sort=False)
        while True:
            try:
                main_df.to_excel(save_file, encoding="utf-8", header=True, index=False, freeze_panes=(1, 0))
                break
            except PermissionError:
                if not tkinter.messagebox.askretrycancel("Error writing to Excel file", str(
                        save_file) + " is already open. Close the file then retry."):
                    return

        # Autosize the columns of the output file
        if platform == "win32":
            excel = Dispatch('Excel.Application')
            wb = excel.Workbooks.Open(save_file)
            excel.Worksheets(1).Activate()
            excel.ActiveSheet.Columns.AutoFit()
            wb.Save()
            wb.Close()

        # Open the output file
        os.startfile(save_file)


if __name__ == "__main__":
    LordsMobileCalculator()
