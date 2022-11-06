import math
start = "15:00"
# start = [int(i) for i in input().split(":")]
start = [int(i) for i in start.split(":")]
end = "23:59"
# end = [int(i) for i in input().split(":")]
end = [int(i) for i in end.split(":")]
idcard = "N"
def get_minutes(start, end):
    start_hour, start_minute = start
    end_hour, end_minute = end
    minutes = 0
    if end_minute - start_minute < 0:
        end_hour -= 1
        minutes = 60 - start_minute + end_minute
    else:
        minutes = end_minute - start_minute
    return minutes + (end_hour - start_hour) * 60
minutes = get_minutes(start, end)
if minutes <= 1:
    pay = 0
elif idcard == "Y":
    if minutes < 30:
        pay = 0
    else:
        pay = math.ceil(minutes/30) * 20 / 2
else:
    pay = math.ceil(minutes/30) * 20
print(int(pay))