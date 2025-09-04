"""
You're building a smart thermostat alert system:
    If the `device_status` is "active"
        And `temperature` > 35 --> Warn: "High Temperature Alert!"
        Else: "Temperature Normal."
    If device is off --> "Device is Offline."
"""

device_status = "active"
temperature = 36  

if (device_status == "active"):
    if (temperature > 35):
        print("High Temperature Alert!")
    else:
        print("Temperature Normal.")
else:
    print("Device is Offline.")