try:
    hour_in , minute_in , hour_out , minute_out = [int(e) for e in input("Enter your input : ").split()]
except ValueError:
    print("Invalid Input")
    exit()
if(hour_out < hour_in or hour_in < 0 or hour_out < 0 or minute_in < 0 or minute_out < 0 or minute_in >= 60 or minute_out >= 60):
    print("Invalid Input")
    exit()
if(hour_out < 7 or hour_out > 23 or (hour_out == 23 and minute_out > 0) or hour_in < 7 or hour_in > 23 or (hour_in == 23 and minute_in > 0)):
    print("Invalid Input")
    exit()
