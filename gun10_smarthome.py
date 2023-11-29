word = input().lower().capitalize()
supported = ["Lights off", "Lock the door",
    "Open the door", "Make coffee", "Shut down"]
if word in supported:
    print('OK')
else:
    print('unknown')