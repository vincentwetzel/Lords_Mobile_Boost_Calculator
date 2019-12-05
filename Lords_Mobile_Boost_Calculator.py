from datetime import datetime
import csv  # TODO: Remove this, make it XLSX
import os
import pandas  # Also requires xlrd to read xlsx files.


def main():
    print_section("Welcome to Vincent's Speed Up Calculator for Lord's Mobile!", '*')
    
    speed_up_3m = get_int_input("\nEnter the number of Speed Up (3 m) you have:")
    speed_up_5m = get_int_input("Enter the number of Speed Up (5 m) you have:")
    speed_up_10m = get_int_input("Enter the number of Speed Up (10 m) you have:")
    speed_up_15m = get_int_input("Enter the number of Speed Up (15 m) you have:")
    speed_up_30m = get_int_input("Enter the number of Speed Up (30 m) you have:")
    speed_up_60m = get_int_input("Enter the number of Speed Up (60 m) you have:")
    speed_up_3h = get_int_input("Enter the number of Speed Up (3 h) you have:")
    speed_up_8h = get_int_input("Enter the number of Speed Up (8 h) you have:")
    speed_up_15h = get_int_input("Enter the number of Speed Up (15 h) you have:")
    speed_up_24h = get_int_input("Enter the number of Speed Up (24 h) you have:")
    speed_up_3d = get_int_input("Enter the number of Speed Up (3 d) you have:")
    sum_speed_ups = (speed_up_3m * 3) + (speed_up_5m * 5) + (speed_up_10m * 10) + (speed_up_15m * 15) + (
            speed_up_30m * 30) + (speed_up_60m * 60) + (speed_up_3h * 180) + (speed_up_8h * 480) + (
                            speed_up_24h * 1440) + (speed_up_3d * 4320)

    speed_up_research_5m = get_int_input("\n\nEnter the number of Speed Up Research (5 m) you have:")
    speed_up_research_10m = get_int_input("Enter the number of Speed Up Research (10 m) you have:")
    speed_up_research_15m = get_int_input("Enter the number of Speed Up Research (15 m) you have:")
    speed_up_research_30m = get_int_input("Enter the number of Speed Up Research (30 m) you have:")
    speed_up_research_60m = get_int_input("Enter the number of Speed Up Research (60 m) you have:")
    speed_up_research_3h = get_int_input("Enter the number of Speed Up Research (3 h) you have:")
    speed_up_research_8h = get_int_input("Enter the number of Speed Up Research (8 h) you have:")
    speed_up_research_15h = get_int_input("Enter the number of Speed Up Research (15 h) you have:")
    speed_up_research_24h = get_int_input("Enter the number of Speed Up Research (24 h) you have:")
    sum_speed_up_research = (speed_up_research_5m * 5) + (speed_up_research_10m * 10) + (speed_up_research_15m * 15) + (
            speed_up_research_30m * 30) + (speed_up_research_60m * 60) + (speed_up_research_3h * 180) + (
                                    speed_up_research_8h * 480) + (speed_up_research_24h * 1440)

    speed_up_merging_15m = get_int_input("\n\nEnter the number of Speed Up Merging (15 m) you have:")
    speed_up_merging_60m = get_int_input("Enter the number of Speed Up Merging(60 m) you have:")
    speed_up_merging_3h = get_int_input("Enter the number of Speed Up Merging (3 h) you have:")
    speed_up_merging_8h = get_int_input("Enter the number of Speed Up Merging (8 h) you have:")
    speed_up_merging_15h = get_int_input("Enter the number of Speed Up Merging (15 h) you have:")
    sum_speed_up_merging = (speed_up_merging_15m * 15) + (speed_up_merging_60m * 60) + (speed_up_merging_3h * 180) + (
            speed_up_merging_8h * 480) + (speed_up_merging_15h * 900)

    print("\n\nTotal time from speed ups: " + format_minutes_to_time(sum_speed_ups))
    print("Total time from speed up research: " + format_minutes_to_time(sum_speed_up_research))
    print("Total time from speed up merging: " + format_minutes_to_time(sum_speed_up_merging))

    note = input("\n\nEnter a note for this data set: ")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

    with open("LM_boosts.csv", 'a', newline='') as outfile:  # output csv file
        writer = csv.DictWriter(outfile, fieldnames=fieldnames_for_csv)
        writer.writerow({"Date/Time": current_time,
                         "Notes": note,
                         "Speed_Up_Total": format_minutes_to_time(sum_speed_ups),
                         "Speed_Up_Research_Total": format_minutes_to_time(sum_speed_up_research),
                         "Speed_Up_Merging_Total": format_minutes_to_time(sum_speed_up_merging),
                         "Speed_Up_3m": format_minutes_to_time(speed_up_3m * 3),
                         "Speed_Up_5m": format_minutes_to_time(speed_up_5m * 5),
                         "Speed_Up_10m": format_minutes_to_time(speed_up_10m * 10),
                         "Speed_Up_15m": format_minutes_to_time(speed_up_15m * 15),
                         "Speed_Up_30m": format_minutes_to_time(speed_up_30m * 30),
                         "Speed_Up_60m": format_minutes_to_time(speed_up_60m * 60),
                         "Speed_Up_3h": format_minutes_to_time(speed_up_3h * 180),
                         "Speed_Up_8h": format_minutes_to_time(speed_up_8h * 480),
                         "Speed_Up_15h": format_minutes_to_time(speed_up_15h * 900),
                         "Speed_Up_24h": format_minutes_to_time(speed_up_24h * 1440),
                         "Speed_Up_3d": format_minutes_to_time(speed_up_3d * 4320),
                         "Speed_Up_Research_5m": format_minutes_to_time(speed_up_research_5m * 5),
                         "Speed_Up_Research_10m": format_minutes_to_time(speed_up_research_10m * 10),
                         "Speed_Up_Research_15m": format_minutes_to_time(speed_up_research_15m * 15),
                         "Speed_Up_Research_30m": format_minutes_to_time(speed_up_research_30m * 30),
                         "Speed_Up_Research_60m": format_minutes_to_time(speed_up_research_60m * 60),
                         "Speed_Up_Research_3h": format_minutes_to_time(speed_up_research_3h * 180),
                         "Speed_Up_Research_8h": format_minutes_to_time(speed_up_research_8h * 480),
                         "Speed_Up_Research_15h": format_minutes_to_time(speed_up_research_15h * 900),
                         "Speed_Up_Research_24h": format_minutes_to_time(speed_up_research_24h * 1440),
                         "Speed_Up_Merging_15m": format_minutes_to_time(speed_up_merging_15m * 15),
                         "Speed_Up_Merging_60m": format_minutes_to_time(speed_up_merging_60m * 60),
                         "Speed_Up_Merging_3h": format_minutes_to_time(speed_up_merging_3h * 180),
                         "Speed_Up_Merging_8h": format_minutes_to_time(speed_up_merging_8h * 480),
                         "Speed_Up_Merging_15h": format_minutes_to_time(speed_up_merging_15h * 900)
                         })

    os.startfile("LM_boosts.csv")

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


if __name__ == "__main__":
    main()
