from datetime import datetime
# TIME LOOP: Mission 1 - Time Lab
# Run the program before changing anything.
now = datetime.now()
print("RAW TIME OBJECT:")
print(now)
# TODO 1: Print only the current time as HH:MM:SS using strftime().
print(now.strftime("%H:%M:%S"))
# TODO 2: Print the date as DD/MM/YYYY.
print(now.strftime("%d/%m/%Y"))
# TODO 3: Print a mission timestamp like: 02/11/2026 09:14
print(now.strftime("%d/%m/%Y %H:%M"))
# Extension: create three different formats and explain which is clearest for alog.





from datetime import datetime
# TIME LOOP: Mission 2 - Midnight Protocol Incident Recorder
# Build a recorder that timestamps incidents and appends them to incident_log.txt.
print("MIDNIGHT PROTOCOL - INCIDENT RECORDER")
#  TODO 5: Reject a blank incident instead of saving it.
while True:
  incident = input("Describe the incident: ").strip()
  # Challenge: repeat until the user enters QUIT.
  if incident.upper() == "QUIT":
    break
  elif incident == "":
    print("Error!, please enter the incident.")
    continue
# TODO 1: Capture the current date/time.
  incident_date_time = datetime.now()
# TODO 2: Format it as DD/MM/YYYY HH:MM:SS.
  timestamp = incident_date_time.strftime("%d/%m/%Y %H:%M:%S")
# Challenge: repeat until the user enters QUIT.
# TODO 4: Append: timestamp|incident to incident_log.txt
  file = open("incident_log.txt", "a")
  file.write(timestamp + "|" + incident + "\n")
  file.close()
# TODO 3: Display a useful confirmation message.
  print("Incident recorded successfully")
  print("Incident Description: ", incident)
  print("Time: ", timestamp)





from datetime import datetime
# TIME LOOP: Mission 3 - Parse a reported time
# Reuse what you learned in CRASH TEST.
reported = input("Enter reported time (HH:MM): ").strip()
# TODO 1: Use datetime.strptime() to convert the text into a datetime object.

# TODO 2: Handle ValueError so bad formats do not crash the program.
try:
  reported_time = datetime.strptime(reported, "%H:%M")
except ValueError:
  print("Invalid input!")
else:
  print(reported_time.strftime("%H:%M"))
  print(reported_time.strftime("%I:%M %p"))

# TODO 3: If valid, display the time in 12-hour AND 24-hour formats.
# Test with: 23:45, 09:07, 9:07, 25:00, banana, blank input.



from datetime import datetime
# TIME LOOP: Mission 4 - Timeline Analyzer
# events.txt contains timestamp|event records.
print("TEMPORAL TIMELINE ANALYZER")
with open("events.txt", "r") as file:
  lines = file.readlines()
events = []
malformed_records = 0
for line in lines:
  line = line.strip()
  if line == "":
    continue

  parts = line.split("|")
# TODO 1: Reject lines that do not have exactly two parts.
  if len(parts) != 2:
    malformed_records += 1
    continue
# TODO 2: Convert parts[0] using strptime("%d/%m/%Y %H:%M").
  try:
    event_time = datetime.strptime(parts[0], "%d/%m/%Y %H:%M")
  except ValueError:
    malformed_records += 1
    print("Error")
    continue
# TODO 3: Store valid events in a dictionary with keys time and event
  event = {"time": event_time,
              "event": parts[1]}
  events.append(event)
# TODO 4: Count malformed records rather than crashing.
print("Malformed records: ", malformed_records)
# TODO 5: Print every valid event in a clear format.
for event in events:
  print(event["time"])
  print(event["event"])
  
# TODO 6: Find the earliest and latest events without assuming the file is ordered.
if events:
    earliest = min(events, key=lambda event: event["time"])
    latest = max(events, key=lambda event: event["time"])
    print("Earliest event:", earliest["time"].strftime("%d/%m/%Y %H:%M"))
    print("Latest event:", latest["time"].strftime("%d/%m/%Y %H:%M"))
else:
    print("No valid events found")

# Challenge: detect a repeated timestamp - evidence of a TIME LOOP.
seen_times = set()
for event in events:
  timestamp = event["time"]
  if timestamp in seen_times:
    print("TIME LOOP WARNING ", timestamp)
  seen_times.add(timestamp)