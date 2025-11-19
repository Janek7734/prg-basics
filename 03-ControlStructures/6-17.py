time = input("Enter time (24-hour format): ")
hour, minute = time.split(":")

hour = int(hour)

if hour == 0:
    new_hour = 12
    suffix = "am"
elif 1 <= hour <= 11:
    new_hour = hour
    suffix = "am"
elif hour == 12:
    new_hour = 12
    suffix = "pm"
elif 13 <= hour <= 23:
    new_hour = hour - 12
    suffix = "pm"

print(f"Time in 12-hour format: {new_hour}:{minute}{suffix}")

