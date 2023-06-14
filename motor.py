import limmy
import time

# How to use limmy, by Adrian Ornelas

# First, create a motor object. This will automatically start the heartbeat thread that keeps the motor alive.

serial_port = 'COM15' # Change this to the serial port of your VESC, on Linux (Raspberry Pi) it will be something like '/dev/ttyUSB0'

motor = limmy.VESC(serial_port=serial_port)

print("Firmware: ", motor.get_firmware_version())
time.sleep(1)

# Traditional motors can be started via motor.set_speed_mph command:
# The utilization for the command is: motor.set_speed_mph(speed)

print('Setting speed to 2 mph')
motor.set_speed_mph(2)

time.sleep(15)

# You can also poll relevent data from the motor:

print('Motor runtime data:')
print(motor.get_v_in()) # Input voltage to the Flipsky VESC, should match Orion BMS 2 Pack Voltage, roughly 44~48V
print(motor.get_motor_current()) # Current being drawn by the motor, informs force output
print(motor.get_incoming_current()) # Current being drawn from the battery, should match Orion BMS 2 Pack Current
time.sleep(0.5)

# Similarly, the motor can be stopped via the motor.halt command:
motor.halt()
time.sleep(1)

# Lastly, remember to stop the heartbeat thread before the object goes out of scope:
    # Failing to do so will mean the thread will continue to run in the background, 
    # even if the program has ended, and the motor will not be able to be controlled
    # until the python runtime is fully restarted.
motor.stop_heartbeat()