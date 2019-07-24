def main():
    sum_speed_ups = 0
    sum_speed_ups += (get_int_input("\n\nEnter the number of Speed Up (3 m) you have:") * 3)
    sum_speed_ups += (get_int_input("Enter the number of Speed Up (5 m) you have:") * 5)
    sum_speed_ups += (get_int_input("Enter the number of Speed Up (10 m) you have:") * 10)
    sum_speed_ups += (get_int_input("Enter the number of Speed Up (15 m) you have:") * 15)
    sum_speed_ups += (get_int_input("Enter the number of Speed Up (30 m) you have:") * 30)
    sum_speed_ups += (get_int_input("Enter the number of Speed Up (60 m) you have:") * 60)
    sum_speed_ups += (get_int_input("Enter the number of Speed Up (3 h) you have:") * 180)
    sum_speed_ups += (get_int_input("Enter the number of Speed Up (8 h) you have:") * 480)
    sum_speed_ups += (get_int_input("Enter the number of Speed Up (24 h) you have:") * 1440)

    sum_speed_up_research = 0
    sum_speed_up_research += (get_int_input("\n\nEnter the number of Speed Up (5 m) you have:") * 5)
    sum_speed_up_research += (get_int_input("Enter the number of Speed Up (10 m) you have:") * 10)
    sum_speed_up_research += (get_int_input("Enter the number of Speed Up (15 m) you have:") * 15)
    sum_speed_up_research += (get_int_input("Enter the number of Speed Up (30 m) you have:") * 30)
    sum_speed_up_research += (get_int_input("Enter the number of Speed Up (60 m) you have:") * 60)
    sum_speed_up_research += (get_int_input("Enter the number of Speed Up (3 h) you have:") * 180)
    sum_speed_up_research += (get_int_input("Enter the number of Speed Up (8 h) you have:") * 480)
    sum_speed_up_research += (get_int_input("Enter the number of Speed Up (24 h) you have:") * 1440)

    sum_speed_up_merging = 0
    sum_speed_up_merging += (get_int_input("\n\nEnter the number of Speed Up (15 m) you have:") * 15)
    sum_speed_up_merging += (get_int_input("Enter the number of Speed Up (60 m) you have:") * 60)
    sum_speed_up_merging += (get_int_input("Enter the number of Speed Up (3 h) you have:") * 180)
    sum_speed_up_merging += (get_int_input("Enter the number of Speed Up (8 h) you have:") * 480)

    print("\n\nTotal time from speed ups: " + format_minutes_to_time(sum_speed_ups))
    print("Total time from speed up research: " + format_minutes_to_time(sum_speed_up_research))
    print("Total time from speed up merging: " + format_minutes_to_time(sum_speed_up_merging))


def get_int_input(query_str):
    while True:
        try:
            return int(input(query_str))
        except ValueError:
            print("That didn't work. Try again.")


def format_minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return str(hours) + " Hour, " + str(minutes) + " Minutes"


if __name__ == "__main__":
    main()
