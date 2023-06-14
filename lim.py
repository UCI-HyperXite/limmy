import limmy
import time

# How to use limmy, by Adrian Ornelas

# First, create motor objects. This will automatically start the heartbeat thread that keeps the motor alive.

serial_port_1 = 'COM15' # Change this to the serial port of your VESC, on Linux (Raspberry Pi) it will be something like '/dev/ttyUSB0'
serial_port_2 = 'COM8'

print('[INFO] Initializing motor 1 on port: ', serial_port_1)
motor_1 = limmy.VESC(serial_port=serial_port_1)
print('[INFO] Initializing motor 2 on port: ', serial_port_2)
motor_2 = limmy.VESC(serial_port=serial_port_2)

print("Firmware 1: ", motor_1.get_firmware_version())
print("Firmware 2: ", motor_2.get_firmware_version())
time.sleep(1) # Wait for the motor controller to respond and set up Comms

# Motor can be started via motor.engage command:
    # The utilization for the command is: motor.engage(current, frequency)
    # Where current, I, is in Amps and is a float above 0.0
    # And frequency, f, is in Hz and is an float above 0.0

f = 30
I = 30

val = True
run = True
direction = True

input('[INFO] Wait for input to start')

while run:
    if direction:
        motor_2.halt()
        motor_1.engage(I, f)
        direction = False
    else:
        motor_1.halt()
        motor_2.engage(I, f)
        direction = True
    val = input("Enter: Change directions, Space: Change parameters, Any other key: Abort")
    if val == ' ':
        motor_1.halt()
        motor_2.halt()
        I = float(input("Enter current: "))
        val = ''
    run = val == ''

motor_1.halt()
motor_2.halt()

time.sleep(1)

motor_1.stop_heartbeat()
motor_2.stop_heartbeat()