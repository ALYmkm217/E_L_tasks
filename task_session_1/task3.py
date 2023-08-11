import calendar
year = int(input("Enter the Year : "))
mnth = int(input("Enter the Mounth : "))
dy = int(input("Enter the Day : "))
print(calendar.month(year, mnth, dy))



# import calendar

# def mark_selected_day(cal_str, day):
#     # Find the starting position of the selected day in the calendar
#     start_pos = cal_str.find(str(day))

#     if start_pos != -1:
#         # Create a new string with the selected day highlighted
#         marked_cal_str = cal_str[:start_pos] + f"[{day}]" + cal_str[start_pos + len(str(day)):]

#         return marked_cal_str
#     else:
#         return cal_str

# year = int(input("Enter the Year: "))
# month = int(input("Enter the Month: "))
# day = int(input("Enter the Day: "))

# cal_str = calendar.month(year, month)
# marked_cal_str = mark_selected_day(cal_str, day)

# print(marked_cal_str)
