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

time_in = hour_in * 60 + minute_in
time_out = hour_out * 60 + minute_out
total_time = time_out - time_in
total_hours = total_time // 60
total_minutes = total_time % 60

if(total_time > 15 and total_minutes > 0):
    total_hours += 1
if(total_time <= 15):
    fee = 0;
if(total_hours <= 3):
    fee = total_hours * 10;
elif(total_hours > 3 and total_hours <= 6):
    fee = 30 + (total_hours - 3) * 20;
else:
    fee = 200;
print(fee)