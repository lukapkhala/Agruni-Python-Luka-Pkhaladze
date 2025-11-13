time_input = input("Input time: ")
time_input_split = time_input
for sep in "-T+:":
    time_input_split = time_input_split.replace(sep, " ")

l = time_input_split.split()

year = l[0]
month = l[1]
day = l[2]
hour = l[3]
minute = l[4]
second = l[5]
zone_hour = l[6]
zone_minute = l[7]
sign = time_input[-6]

output = day + "-" + month + "-" + year + " " + str(int(hour) % 12) + ":" + minute + ":" + second.split(".")[0] + " " + sign + str(int(zone_hour))



if zone_minute != "00":
    output += ":" + zone_minute

print(output)