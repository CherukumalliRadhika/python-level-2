from datetime import datetime

now = datetime.now()
print("Current date & time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted:", formatted)
